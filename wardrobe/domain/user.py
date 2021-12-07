from dataclasses import dataclass


@dataclass
class UserEntity:
    id: int
    email: str
    name: str
    hashed_password: str

    @classmethod
    def factory(cls, id_=None, email=None, name=None):
        return cls(id=id_, email=email, name=name)
