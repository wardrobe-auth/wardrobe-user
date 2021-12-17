from wardrobe.domain import commands


def handle_say_hello(
    cmd: commands.SayHelloCommand,
):
    return f"Hello, {cmd.name}!"


EVENT_HANDLERS = {}

COMMAND_HANDLERS = {commands.SayHelloCommand: handle_say_hello}
