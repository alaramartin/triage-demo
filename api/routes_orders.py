"""HTTP routes for order placement and pricing."""
from services.orders import place_order, confirmation_message
from services.pricing import quote_for_cart


def post_order(request):
    order = place_order(request["customer_id"], request["items"])
    return {"order": order, "message": confirmation_message(order["id"])}


def get_quote(request):
    return {"total_cents": quote_for_cart(request["cart"], request.get("discount_percent", 0))}