from wardrobe.config.user import UserConfig
from wardrobe.repositories.interface import IUserRepository
from wardrobe.request_objects.register_user import RegisterUserRequestObject
from wardrobe.response_objects import ResponseSuccess
from wardrobe.use_cases import UseCase


class RegisterUserUseCase(UseCase):
    def __init__(self, user_repository: IUserRepository, user_settings, email_service, password_service=None):
        self.user_repository: IUserRepository = user_repository
        self.user_config: UserConfig = user_settings
        self.email_service = email_service
        self.password_service = password_service

    def hash_password(self, password):
        return self.password_service.hash_password(password)

    def process_request(self, request_object: RegisterUserRequestObject):
        user = self.user_repository.register_user(
            request_object.email,
            self.hash_password(request_object.password),
        )

        return ResponseSuccess(value=user)
