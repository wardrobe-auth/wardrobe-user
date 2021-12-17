import abc

from wardrobe.adaptors.repository import AbstractUserRepository
from wardrobe.adaptors.repository.mem import MemUserRepository


class AbstractUnitOfWork(abc.ABC):
    users: AbstractUserRepository

    def __init__(
        self,
        users: AbstractUserRepository = None,
    ):
        self.users = users

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for user in self.users.seen:
            while user.events:
                yield user.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class MemUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        users: AbstractUserRepository = None,
    ):
        super().__init__(users)

    def __enter__(self):
        self.users = MemUserRepository()

        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        pass

    def rollback(self):
        pass
