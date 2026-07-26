"""CSV export for order history. Symptom carrier for the validation.py bug."""
from models.order import Order


def export_orders_csv(order_ids):
    rows = ["order_id,customer_id,status"]
    for oid in order_ids:
        order = Order.get(oid)
        # If require_fields silently let a blank customer_id through upstream, this row
        # ends up blank/skipped downstream by whatever consumes the CSV.
        if not order.get("customer_id"):
            continue
        rows.append(f"{order['id']},{order['customer_id']},{order['status']}")
    return "\n".join(rows)
