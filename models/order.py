"""Order model and order-level validation."""
from core.validation import require_fields
from core.db import Table
from core.errors import NotFoundError

orders_table = Table("orders", required_fields=["customer_id", "items"])


class Order:
    def __init__(self, customer_id, items, status="pending"):
        self.customer_id = customer_id
        self.items = items
        self.status = status

    @staticmethod
    def create(payload):
        require_fields(payload, ["customer_id", "items"])
        return orders_table.insert(payload)

    @staticmethod
    def get(order_id):
        row = orders_table.get(order_id)
        if row is None:
            raise NotFoundError("Order", order_id)
        return row

    @staticmethod
    def mark_status(order_id, status):
        return orders_table.update(order_id, status=status)
