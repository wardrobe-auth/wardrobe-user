from dataclasses import dataclass


@dataclass
class UserEntity:
    id: int
    email: str
    name: str
    hashed_password: str

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @classmethod
    def factory(cls, id_=None, email=None, name=None, hashed_password=None):
        return cls(id=id_, email=email, name=name, hashed_password=hashed_password)
