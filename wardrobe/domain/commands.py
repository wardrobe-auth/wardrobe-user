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


@dataclass
class UserLogin(Command):
    username: str
    password: str

    @classmethod
    def factory(cls, username: str, password: str):
        try:
            return cls(username=username.strip(), password=password.strip())
        except Exception as e:
            print(str(e))
            return cls(username=username, password=password)

    def is_valid(self):
        return bool(self.username and self.password)


@dataclass
class RegisterUser(Command):
    username: str
    name: str
    password: str

    @classmethod
    def factory(cls, username, name, password):
        return cls(username=username, name=name, password=password)

    def is_valid(self):
        return bool(self.username and self.password)
