from flask import Flask, current_app, request, redirect, render_template
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, ValidationError

from wardrobe.domain import commands
from wardrobe.entrypoints.flask_app import message_bus
from wardrobe.entrypoints.flask_app.utils import get_safe_next_url, make_safe_url


class StripedStringField(StringField):
    def _value(self):
        return super()._value().strip()

    def process_data(self, value):
        try:
            value = value.strip()
        except:
            pass

        self.data = value

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0].strip()


class EqualTo(object):  # --> Change to 'LessThan'
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """

    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(
                field.gettext("Invalid field name '%s'.") % self.fieldname
            )
        if field.data != other.data:  # --> Change to >= from !=
            d = {
                "other_label": hasattr(other, "label")
                and other.label.text
                or self.fieldname,
                "other_name": self.fieldname,
            }
            message = self.message
            if message is None:
                message = field.gettext("Field must be equal to %(other_name)s.")

            raise ValidationError(message % d)


class LoginForm(FlaskForm):
    username = StripedStringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StripedStringField("username", validators=[DataRequired()])
    name = StripedStringField("name", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    password_confirm = PasswordField(
        "password_confirm", validators=[DataRequired(), EqualTo("password")]
    )


def register_view():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            name = form.name.data
            password = form.password.data
            cmd = commands.RegisterUser.factory(username, name, password)
            resp = message_bus.bus.handle(cmd)
            if not resp:
                return resp.message

            login_user(resp.value)
            return redirect("/")

    return render_template(
        "users/register.html",
        form=form,
    )


def login_view():
    safe_next_url = get_safe_next_url(
        "next", current_app.config.get("USER_AFTER_LOGIN_ENDPOINT", "")
    )
    safe_reg_next_url = get_safe_next_url(
        "reg_next", current_app.config.get("USER_AFTER_REGISTER_ENDPOINT", "")
    )
    service_url = current_app.config.get("SERVICE_URL")
    error = ""
    username = ""

    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():

        username = request.form.get("username")
        password = request.form.get("password")

        cmd = commands.UserLogin(username=username, password=password)
        resp = message_bus.bus.handle(cmd)
        if not resp:
            error = resp.message
            return render_template(
                "users/login.html",
                safe_next_url=safe_next_url,
                safe_reg_next_url=safe_reg_next_url,
                service_url=service_url,
                error=error,
                username=username,
                form=form,
            )

        user = resp.value
        login_user(user)
        safe_next_url = make_safe_url(request.args.get("next", ""))

        return redirect(safe_next_url)

    return render_template(
        "users/login.html",
        safe_next_url=safe_next_url,
        safe_reg_next_url=safe_reg_next_url,
        service_url=service_url,
        error=error,
        username=username,
        form=form,
    )


def logout_view():
    logout_user()
    return redirect("/")


def profile_view():
    return "Not Implemented"


def update_user_profile_view():
    return "Not Implemented"


def change_user_password_view():
    return "Not Implemented"


def reset_user_password_view():
    return "Not Implemented"


def find_user_email_view():
    return "Not Implemented"


def reset_user_email_view():
    return "Not Implemented"


def apply_user_routes(app: Flask, url_prefix="/users"):
    app.add_url_rule(
        f"{url_prefix}/register",
        "user.register",
        view_func=register_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/login",
        "user.login",
        view_func=login_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/logout",
        "user.logout",
        view_func=logout_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/profile",
        "user.profile",
        view_func=profile_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/update-user-profile",
        "user.update_user_profile",
        view_func=update_user_profile_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/change-user-password",
        "user.change_user_password",
        view_func=change_user_password_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/reset-user-password",
        "user.reset_user_password",
        view_func=reset_user_password_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/find-user-email",
        "user.find_user_email",
        view_func=find_user_email_view,
        methods=[
            "GET",
            "POST",
        ],
    )

    app.add_url_rule(
        f"{url_prefix}/reset-user-email",
        "user.reset_user_email",
        view_func=reset_user_email_view,
        methods=[
            "GET",
            "POST",
        ],
    )
