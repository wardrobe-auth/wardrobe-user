from flask import request, redirect, url_for, flash
from flask_login import LoginManager

from wardrobe import views
from wardrobe.entrypoints.flask_app import message_bus

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    print(f"user_id={user_id}")
    return views.get_user(user_id, message_bus.bus.uow)


@login_manager.unauthorized_handler
def handle_needs_login():
    flash("You have to be logged in to access this page.")
    return redirect(url_for("user.login", next=request.endpoint))
