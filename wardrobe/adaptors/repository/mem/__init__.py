from wardrobe.adaptors.repository import AbstractUserRepository, UserInput


class MemUserRepository(AbstractUserRepository):
    def register(self, user: UserInput):
        pass

    def get(self, id_):
        pass
