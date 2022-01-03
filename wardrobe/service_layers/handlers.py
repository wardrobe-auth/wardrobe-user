from dataclasses import dataclass

from wardrobe.adaptors.repository import UserInput
from wardrobe.domain import commands
from wardrobe.response_objects import ResponseSuccess, ResponseFailure
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
        if not user:
            return ResponseFailure.build_resource_error("user not found")

    return ResponseSuccess(value=user)


def handle_user_register(
    cmd: commands.RegisterUser,
    uow: unit_of_work.AbstractUnitOfWork = None,
):
    with uow:
        user_input = UserInput(cmd.username, cmd.name, cmd.password)
        print(f"user_input={user_input}")
        user = uow.users.register(user_input)
        if not user:
            return ResponseFailure.build_system_error("system error")

    return ResponseSuccess(value=user)


EVENT_HANDLERS = {}

COMMAND_HANDLERS = {
    commands.SayHelloCommand: handle_say_hello,
    commands.UserLogin: handle_user_login,
    commands.RegisterUser: handle_user_register,
}
