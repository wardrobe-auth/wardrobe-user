import logging
from typing import Dict, Type, List, Callable, Union

from wardrobe.domain import events, commands
from wardrobe.service_layers import unit_of_work

Message = Union[commands.Command, events.Event]


class MessageBus:
    def __init__(
        self,
        uow: unit_of_work.AbstractUnitOfWork,
        event_handlers: Dict[Type[events.Event], List[Callable]],
        command_handlers: Dict[Type[commands.Command], Callable],
        logger=None,
    ):
        if logger is None:
            logger = logging.getLogger(__name__)

        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers
        self.logger = logger
        self.queue = []

    def handle(self, message: Message):
        self.queue = [message]
        response = None

        while self.queue:
            event_or_command = self.queue.pop(0)
            if isinstance(message, events.Event):
                self.handle_event(event_or_command)
            elif isinstance(event_or_command, commands.Command):
                response = self.handle_command(event_or_command)
            else:
                raise Exception(f"{event_or_command} was not an Event or Command")

        return response

    def handle_event(self, event: events.Event):
        for handler in self.event_handlers[type(event)]:
            try:
                handler(event)
                self.queue.extend(self.uow.collect_new_events())
            except Exception:
                self.logger.exception("Exception handling event %s", event)
                continue

    def handle_command(self, cmd: commands.Command):
        response = None
        try:
            handler = self.command_handlers[type(cmd)]
            response = handler(cmd)
            self.queue.extend(self.uow.collect_new_events())
        except Exception:
            self.logger.exception("Exception handling command %s", cmd)
            raise

        return response
