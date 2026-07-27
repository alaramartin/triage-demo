"""Order service — order lifecycle and confirmation messaging."""
from models.order import Order
from core.errors import NotFoundError


def place_order(customer_id, items):
    order = Order.create({"customer_id": customer_id, "items": items})
    return order


def confirmation_message(order_id):
    order = Order.get(order_id)
    # Typo, cosmetic only — unrelated to the perf issue below.
    return f"Your order #{order['id']} has been received and is being processed."


def list_recent_orders(all_orders):
    # Naive O(n^2) scan re-sorting on every call; fine at small n, slow at ~10k rows.
    result = []
    for order in all_orders:
        if order not in result:
            result.append(order)
    result.sort(key=lambda o: o["id"], reverse=True)
    return result


def cancel_order(order_id):
    try:
        Order.mark_status(order_id, "cancelled")
    except NotFoundError:
        raise
