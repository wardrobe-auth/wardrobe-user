from sqlalchemy import Column, Integer, Boolean, DateTime, String
from sqlalchemy.orm import relationship

from wardrobe.adaptors.repository.sqla import Base
from wardrobe.domain.models import User as UserEntity


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    active = Column("is_active", Boolean(), nullable=False, server_default="1")

    # User authentication information. The  is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = Column(
        String(
            255,
        ),
        nullable=True,
        unique=False,
    )
    email_confirmed_at = Column(DateTime())
    password = Column(String(255), nullable=False, server_default="")

    # User information
    first_name = Column(
        String(
            100,
        ),
        nullable=False,
        server_default="",
    )
    last_name = Column(
        String(
            100,
        ),
        nullable=False,
        server_default="",
    )
    gender = Column(
        String(
            100,
        ),
        nullable=True,
        server_default=None,
    )
    language = Column(
        String(
            2,
        ),
        nullable=True,
        server_default=None,
    )
    country = Column(
        String(
            255,
        ),
        nullable=True,
        server_default=None,
    )

    # Define the relationship to Role via UserRoles
    roles = relationship("Role", secondary="user_roles")

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

    def get_user_id(self):
        return self.id

    def get_id(self):
        return self.id

    # @classmethod
    # def get_user_by_token(cls, token):
    #     return db.session.query(cls).get(token)

    def to_entity(self):
        return UserEntity.from_dict(
            id=self.id,
            username=self.email,
            email=self.email,
        )


# Define the Role data-model
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True)


# Define the UserRoles association table
class UserRoles(Base):
    __tablename__ = "user_roles"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), db.ForeignKey("users.id", ondelete="CASCADE"))
    role_id = Column(Integer(), db.ForeignKey("roles.id", ondelete="CASCADE"))
