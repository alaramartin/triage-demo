"""Shopping cart aggregate."""
from models.product import Product
from core.validation import require_fields


class Cart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.line_items = []

    def add_item(self, product_id, quantity):
        require_fields({"product_id": product_id, "quantity": quantity}, ["product_id", "quantity"])
        self.line_items.append({"product_id": product_id, "quantity": quantity})

    def total_cents(self):
        total = 0
        for item in self.line_items:
            product = Product.get(item["product_id"])
            # Reads price_cents as a float dollar amount, which disagrees with the plain-int
            # unit used in Product.sale_price_cents — this is why totals don't match.
            total += float(product["price_cents"]) * item["quantity"]
        return total
