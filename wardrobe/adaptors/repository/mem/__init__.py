from wardrobe.adaptors.repository import AbstractUserRepository, UserInput
from wardrobe.domain.user import UserEntity


class MemUserRepository(AbstractUserRepository):
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []

        self.seen = []
        self.data = [
            UserEntity.factory(
                item.get("id"),
                item.get("email"),
                item.get("name"),
                item.get("password"),
            )
            for item in initial_data
        ]

    def register(self, user: UserInput):
        next_user_id = max(*[user.id for user in self.data]) + 1
        user_entity = UserEntity(next_user_id, user.email, user.name, user.password)
        self.data.append(user_entity)

        return user_entity

    def get(self, id_):
        try:
            return next(user for user in self.data if user.id == id_)
        except StopIteration:
            return None

    def get_by_email(self, email):
        try:
            return next(user for user in self.data if user.email == email)
        except StopIteration:
            return None
