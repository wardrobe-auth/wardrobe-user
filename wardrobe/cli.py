import click

from wardrobe.repositories.interface import IUserRepository
from wardrobe.request_objects.register_user import RegisterUserRequestObject
from wardrobe.use_cases.user.register_user import RegisterUserUseCase
from wardrobe.config.user import UserConfig


@click.group('cli')
def main():
    pass


class FakeUserRepository(IUserRepository):
    def register_user(self, email=None, name=None, hashed_password=None):
        pass


def get_session():
    return 'fake session'


class EmailService:
    pass


class PasswordService:
    def hash_password(self, password):
        return f'hashed-{password}'


def get_user_settings():
    user_config = UserConfig()
    user_config.init({})

    return user_config


@main.add_command
@click.command()
def register_user():
    session = get_session()
    user_repository = FakeUserRepository(session)
    user_settings = get_user_settings()
    request_object = RegisterUserRequestObject.factory(
        email='email',
        name='',
        password='',
    )
    email_service = EmailService()
    password_service = PasswordService()
    uc = RegisterUserUseCase(
        user_repository,
        user_settings,
        email_service=email_service,
        password_service=password_service
    )
    resp = uc.execute(request_object)
    if not resp:
        click.echo('some error')

    click.echo('ok')


if __name__ == '__main__':
    main()
