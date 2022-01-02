from wardrobe.adaptors.repository import AbstractUserRepository, UserInput
from wardrobe.domain.user import UserEntity


class MemUserRepository(AbstractUserRepository):
    def register(self, user: UserInput):
        pass

    def get(self, id_):
        return UserEntity.factory(42, "user@example.com", "John")

    def get_by_email(self, email):
        return UserEntity.factory(42, "user@example.com", "John")
