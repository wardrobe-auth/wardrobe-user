from dataclasses import dataclass

from wardrobe.domain import commands
from wardrobe.response_objects import ResponseSuccess
from wardrobe.service_layers import unit_of_work


def handle_say_hello(
    cmd: commands.SayHelloCommand,
):
    return f"Hello, {cmd.name}!"


def handle_user_login(
    cmd: commands.UserLogin,
    uow: unit_of_work.AbstractUnitOfWork = None,
):
    with uow:
        user = uow.users.get_by_email(cmd.username)

    return ResponseSuccess(value=user)


EVENT_HANDLERS = {}

COMMAND_HANDLERS = {
    commands.SayHelloCommand: handle_say_hello,
    commands.UserLogin: handle_user_login,
}
