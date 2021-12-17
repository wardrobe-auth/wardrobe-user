import inspect
import logging
from typing import Optional, Callable

from wardrobe.service_layers import message_bus, handlers
from wardrobe.service_layers.unit_of_work import AbstractUnitOfWork


def bootstrap(uow: AbstractUnitOfWork, logger: Optional[Callable] = None):
    if logger is None:
        logger = logging.getLogger(__name__)

    dependencies = {"logger": logger}
    injected_event_handlers = {}
    injected_command_handlers = {
        command_type: inject_dependencies(command_handler, dependencies)
        for command_type, command_handler in handlers.COMMAND_HANDLERS.items()
    }
    bus = message_bus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )

    return bus


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda message: handler(message, **deps)
