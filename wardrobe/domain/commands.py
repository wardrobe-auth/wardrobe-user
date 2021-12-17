import abc
from dataclasses import dataclass


class Command(abc.ABC):
    @abc.abstractmethod
    def is_valid(self):
        raise NotImplementedError


@dataclass
class SayHelloCommand(Command):
    name: str

    def is_valid(self):
        try:
            return len(self.name.strip()) > 0
        except:
            pass
