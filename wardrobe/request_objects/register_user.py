from dataclasses import dataclass


@dataclass
class RegisterUserRequestObject:
    email: str
    name: str
    password: str

    @classmethod
    def factory(cls, **kwargs):
        return cls(**kwargs)
