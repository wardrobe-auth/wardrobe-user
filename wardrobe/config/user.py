class UserConfig:
    #: | Allow users to login and register with an email address
    ENABLE_EMAIL = True

    #: | Allow users to associate multiple email addresses with one config account.
    #: | Depends on USER_ENABLE_EMAIL=True
    ENABLE_MULTIPLE_EMAILS = False

    #: | Allow users to login and register with a username
    ENABLE_USERNAME = True

    #: | Allow users to change their username.
    #: | Depends on USER_ENABLE_USERNAME=True.
    ENABLE_CHANGE_USERNAME = True

    #: | Allow users to change their password.
    ENABLE_CHANGE_PASSWORD = True

    #: | Enable email confirmation emails to be sent.
    #: | Depends on USER_ENABLE_EMAIL=True.
    ENABLE_CONFIRM_EMAIL = True

    #: | Allow users to reset their passwords.
    #: | Depends on USER_ENABLE_EMAIL=True.
    ENABLE_FORGOT_PASSWORD = True

    #: | Allow unregistered users to be invited.
    ENABLE_INVITE_USER = False

    #: | Allow unregistered users to register.
    ENABLE_REGISTER = True

    #: | Remember config sessions across browser restarts.
    #:
    #: .. This hack shows a header above the _next_ section
    #: .. code-block:: none
    #:
    #:     Generic settings and their defaults
    ENABLE_REMEMBER_ME = True

    ENABLE_AUTH0 = False

    #: The application name displayed in email templates and page template footers.
    APP_NAME = 'USER_APP_NAME'

    #: The application version displayed in page template footers.
    APP_VERSION = "v1.0"

    #: Corporation name displayed in page template footers.
    CORPORATION_NAME = 'MyCorp'

    #: Copyright year displayed in page template footers.
    COPYRIGHT_YEAR = 2019

    #: Automatic sign-in if the config session has not expired.
    AUTO_LOGIN = True

    #: Automatic sign-in after a config confirms their email address.
    AUTO_LOGIN_AFTER_CONFIRM = True

    #: Automatic sign-in after a config registers.
    AUTO_LOGIN_AFTER_REGISTER = True

    #: Automatic sign-in after a config resets their password.
    AUTO_LOGIN_AFTER_RESET_PASSWORD = True

    #: Automatic sign-in at the login form (if the config session has not expired).
    AUTO_LOGIN_AT_LOGIN = True

    #: | Sender's email address, used by the EmailAdapters.
    #: | Required for sending emails.
    #: | Derived from MAIL_DEFAULT_SENDER or DEFAULT_MAIL_SENDER when specified.
    EMAIL_SENDER_EMAIL = ''

    #: | Sender's name, config by the EmailAdapters.
    #: | Optional. Defaults to USER_APP_NAME setting.
    EMAIL_SENDER_NAME = ''

    #: | The way Flask-User handles case insensitive searches.
    #: | Valid options are:
    #: | - 'ifind' (default): Use the case insensitive ifind_first_object()
    #: | - 'nocase_collation': username and email fields must be configured
    #: |     with an case insensitve collation (collation='NOCASE' in SQLAlchemy)
    #: |     so that a regular find_first_object() can be performed.
    IFIND_MODE = 'ifind'

    #: | Send notification email after a password change.
    #: | Depends on USER_ENABLE_EMAIL=True.
    SEND_PASSWORD_CHANGED_EMAIL = True

    #: | Send notification email after a registration.
    #: | Depends on USER_ENABLE_EMAIL=True.
    SEND_REGISTERED_EMAIL = True

    #: | Send notification email after a username change.
    #: | Depends on USER_ENABLE_EMAIL=True.
    SEND_USERNAME_CHANGED_EMAIL = True

    #: | Only invited users may register.
    #: | Depends on USER_ENABLE_EMAIL=True.
    REQUIRE_INVITATION = False

    #: | Ensure that users can login only with a confirmed email address.
    #: | Depends on USER_ENABLE_EMAIL=True.
    #:
    #: This setting works in tandem with the ``@allow_unconfirmed_emails``
    #: view decorator to allow users without confirmed email addresses
    #: to access certain views.
    #:
    #: .. caution::
    #:
    #:     | Use ``USER_ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL=True`` and
    #:         ``@allow_unconfirmed_email`` with caution,
    #:         as they relax security requirements.
    #:     | Make sure that decorated views **never call other views directly**.
    #:         Allways se ``redirect()`` to ensure proper view protection.
    ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL = False

    #: | Require users to retype their password.
    #: | Affects registration, change password and reset password forms.
    REQUIRE_RETYPE_PASSWORD = True

    #: | Show 'Email does not exist' message instead of 'Incorrect Email or password'.
    #: | Depends on USER_ENABLE_EMAIL=True.
    SHOW_EMAIL_DOES_NOT_EXIST = False

    #: | Show 'Username does not exist' message instead of 'Incorrect Username or password'.
    #: | Depends on USER_ENABLE_USERNAME=True.
    SHOW_USERNAME_DOES_NOT_EXIST = False

    #: | Email confirmation token expiration in seconds.
    #: | Default is 2 days (2*24*3600 seconds).
    CONFIRM_EMAIL_EXPIRATION = 2 * 24 * 3600

    #: | Invitation token expiration in seconds.
    #: | Default is 90 days (90*24*3600 seconds).
    INVITE_EXPIRATION = 90 * 24 * 3600

    #: | Reset password token expiration in seconds.
    #: | Default is 2 days (2*24*3600 seconds).
    RESET_PASSWORD_EXPIRATION = 2 * 24 * 3600

    #: | User session token expiration in seconds.
    #: | Default is 1 hour (1*3600 seconds).
    #:
    #: .. This hack shows a header above the _next_ section
    #: .. code-block:: none
    #:
    #:     Password hash settings
    USER_SESSION_EXPIRATION = 1 * 3600

    #: | List of accepted password hashes.
    #: | See `Passlib CryptContext docs on Constructor Keyword ``'schemes'`` <http://passlib.readthedocs.io/en/stable/lib/passlib.context.html?highlight=cryptcontext#constructor-keywords>`_
    #: | Example: ``['bcrypt', 'argon2']``
    #: |   Creates new hashes with 'bcrypt' and verifies existing hashes with 'bcrypt' and 'argon2'.
    PASSLIB_CRYPTCONTEXT_SCHEMES = ['bcrypt']

    #: | Dictionary of CryptContext keywords and hash options.
    #: | See `Passlib CryptContext docs on Constructor Keywords <http://passlib.readthedocs.io/en/stable/lib/passlib.context.html?highlight=cryptcontext#constructor-keywords>`_
    #: | and `Passlib CryptContext docs on Algorithm Options <http://passlib.readthedocs.io/en/stable/lib/passlib.context.html?highlight=cryptcontext#algorithm-options>`_
    #: | Example: ``dict(bcrypt__rounds=12, argon2__time_cost=2, argon2__memory_cost=512)``
    #:
    #: .. This hack shows a header above the _next_ section
    #:     URL settings
    PASSLIB_CRYPTCONTEXT_KEYWORDS = dict()

    CHANGE_PASSWORD_URL = '/config/change-password'  #:
    CHANGE_USERNAME_URL = '/config/change-username'  #:
    CONFIRM_EMAIL_URL = '/config/confirm-email/<token>'  #:
    EDIT_USER_PROFILE_URL = '/config/edit_user_profile'  #:
    EMAIL_ACTION_URL = '/config/email/<id>/<action>'  #:
    FORGOT_PASSWORD_URL = '/config/forgot-password'  #:
    INVITE_USER_URL = '/config/invite'  #:
    LOGIN_URL = '/config/sign-in'  #:
    LOGOUT_URL = '/config/sign-out'  #:
    MANAGE_EMAILS_URL = '/config/manage-emails'  #:
    REGISTER_URL = '/config/register'  #:
    RESEND_EMAIL_CONFIRMATION_URL = '/config/resend-email-confirmation'  #:

    #: .. This hack shows a header above the _next_ section
    #: .. code-block:: none
    #:
    #:     Template file settings
    RESET_PASSWORD_URL = '/config/reset-password/<token>'

    CHANGE_PASSWORD_TEMPLATE = 'flask_user/change_password.html'  #:
    CHANGE_USERNAME_TEMPLATE = 'flask_user/change_username.html'  #:
    EDIT_USER_PROFILE_TEMPLATE = 'flask_user/edit_user_profile.html'  #:
    FORGOT_PASSWORD_TEMPLATE = 'flask_user/forgot_password.html'  #:
    INVITE_USER_TEMPLATE = 'flask_user/invite_user.html'  #:
    LOGIN_TEMPLATE = 'flask_user/login.html'  #:
    LOGIN_AUTH0_TEMPLATE = 'flask_user/login_auth0.html'  #:
    MANAGE_EMAILS_TEMPLATE = 'flask_user/manage_emails.html'  #:
    REGISTER_TEMPLATE = 'flask_user/register.html'  #:
    RESEND_CONFIRM_EMAIL_TEMPLATE = 'flask_user/resend_confirm_email.html'  #:

    #: .. This hack shows a header above the _next_ section
    #: .. code-block:: none
    #:
    #:     Email template file settings
    RESET_PASSWORD_TEMPLATE = 'flask_user/reset_password.html'

    CONFIRM_EMAIL_TEMPLATE = 'flask_user/emails/confirm_email'  #:
    INVITE_USER_EMAIL_TEMPLATE = 'flask_user/emails/invite_user'  #:
    PASSWORD_CHANGED_EMAIL_TEMPLATE = 'flask_user/emails/password_changed'  #:
    REGISTERED_EMAIL_TEMPLATE = 'flask_user/emails/registered'  #:
    RESET_PASSWORD_EMAIL_TEMPLATE = 'flask_user/emails/reset_password'  #:

    #: .. This hack shows a header above the _next_ section
    #: .. code-block:: none
    #:
    #:     Flask endpoint settings
    USERNAME_CHANGED_EMAIL_TEMPLATE = 'flask_user/emails/username_changed'

    AFTER_CHANGE_PASSWORD_ENDPOINT = ''  #:
    AFTER_CHANGE_USERNAME_ENDPOINT = ''  #:
    AFTER_CONFIRM_ENDPOINT = ''  #:
    AFTER_EDIT_USER_PROFILE_ENDPOINT = ''  #:
    AFTER_FORGOT_PASSWORD_ENDPOINT = ''  #:
    AFTER_LOGIN_ENDPOINT = ''  #:
    AFTER_LOGOUT_ENDPOINT = ''  #:
    AFTER_REGISTER_ENDPOINT = ''  #:
    AFTER_RESEND_EMAIL_CONFIRMATION_ENDPOINT = ''  #:
    AFTER_RESET_PASSWORD_ENDPOINT = ''  #:
    AFTER_INVITE_ENDPOINT = ''  #:
    UNAUTHENTICATED_ENDPOINT = 'config.login'  #:
    UNAUTHORIZED_ENDPOINT = ''  #:

    # USER_UNCONFIRMED_EMAIL_ENDPOINT = '' #:

    def init(self, config):
        for k, v in config.items():
            if k.startswith('USER_') and hasattr(self, k[5:]):
                setattr(self, k[5:], v)
