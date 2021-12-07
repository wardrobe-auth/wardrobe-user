from abc import ABCMeta, abstractmethod


class IUserRepository(metaclass=ABCMeta):
    def __init__(self, session):
        self._session = session

    @abstractmethod
    def register_user(self, email=None, name=None, hashed_password=None):
        pass
