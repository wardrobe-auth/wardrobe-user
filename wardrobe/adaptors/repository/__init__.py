import abc
from dataclasses import dataclass
from typing import Callable


class InvalidInput:
    def __nonzero__(self):
        return False

    __bool__ = __nonzero__


@dataclass
class UserInput:
    email: str
    name: str
    password: str

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__

    @classmethod
    def factory(
        cls,
        email=None,
        name=None,
        password=None,
        validator: Callable = lambda **_kwargs: True,
        raise_exception=False,
    ):
        if not validator(email=email, name=name, password=password):
            if raise_exception:
                raise ValueError
            else:
                return InvalidInput("error-message")

        return cls(email=email, name=name, password=password)


class AbstractUserRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    @abc.abstractmethod
    def register(self, user: UserInput):
        pass

    @abc.abstractmethod
    def get(self, id_):
        pass

    @abc.abstractmethod
    def get_by_email(self, email):
        pass
