"""User account service — signup and password reset flows."""
import uuid
from models.user import User


def signup(email, name):
    return User.create({"email": email, "name": name})


def request_password_reset(user_id):
    token = uuid.uuid4().hex
    User.set_password_reset_token(user_id, token)
    return send_reset_email(user_id, token)


def send_reset_email(user_id, token):
    user = User.get(user_id)
    if user is None:
        return False
    # Stand-in for a real email provider call.
    print(f"Sending reset link to {user['email']} with token {token}")
    return True
