"""User account model."""
from core.validation import require_fields, is_valid_email
from core.db import Table

users_table = Table("users", required_fields=["email", "name"])


class User:
    @staticmethod
    def create(payload):
        require_fields(payload, ["email", "name"])
        if not is_valid_email(payload["email"]):
            raise ValueError("invalid email address")
        return users_table.insert(payload)

    @staticmethod
    def get(user_id):
        return users_table.get(user_id)

    @staticmethod
    def set_password_reset_token(user_id, token):
        return users_table.update(user_id, reset_token=token)
