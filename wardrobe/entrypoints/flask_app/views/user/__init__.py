from flask import Flask, current_app, request, redirect, render_template
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired

from wardrobe.domain import commands
from wardrobe.entrypoints.flask_app import message_bus
from wardrobe.entrypoints.flask_app.utils import get_safe_next_url, make_safe_url


def register_view():
    return "Not Implemented"


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

    class LoginForm(FlaskForm):
        username = StringField("username", validators=[DataRequired()])
        password = PasswordField("password", validators=[DataRequired()])

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
