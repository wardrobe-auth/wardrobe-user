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
    password: str

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__

    @classmethod
    def factory(cls, email=None, password=None, validator: Callable = lambda **_kwargs: True, raise_exception=False):
        if not validator(email=email, password=password):
            if raise_exception:
                raise ValueError
            else:
                return InvalidInput('error-message')

        return cls(email=email, password=password)


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def register(self, user: UserInput):
        pass

    @abc.abstractmethod
    def get(self, id_):
        pass


class SqlAlchemyUserRepository(AbstractUserRepository):
    def __init__(self, session):
        self.session = session

    def get(self, id_):
        pass

    def register(self, user):
        pass
