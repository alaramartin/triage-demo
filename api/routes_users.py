"""HTTP routes for user profile and account pages."""
from services.users import signup, request_password_reset


def post_signup(request):
    return signup(request["email"], request["name"])


def get_profile(request):
    # Decoy: this route is fine. It's where a loud, vague complaint happens to resolve —
    # there's no actual bug here, which is the point.
    user_data = services.users.get_user_data(request["user_id"])
    return {"user_id": request["user_id"], "profile_loaded": True, **user_data}


def post_password_reset(request):
    return {"sent": request_password_reset(request["user_id"])}