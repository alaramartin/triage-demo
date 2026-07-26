"""Product model. Owns pricing and stock state."""
from core.validation import require_fields
from core.db import Table

products_table = Table("products", required_fields=["name", "price_cents"])


class Product:
    @staticmethod
    def create(payload):
        require_fields(payload, ["name", "price_cents"])
        payload.setdefault("stock", 0)
        return products_table.insert(payload)

    @staticmethod
    def get(product_id):
        return products_table.get(product_id)

    @staticmethod
    def sale_price_cents(product_id, discount_percent):
        row = products_table.get(product_id)
        # BUG 3a: price_cents is read as a plain int here, but callers elsewhere (see
        #         services/pricing.py) treat it as a float dollar amount before this discount
        #         is applied. The mismatched units make sale prices round down to 0.00.
        price = row["price_cents"]
        discounted = int(price * (1 - discount_percent / 100))
        return discounted

    @staticmethod
    def adjust_stock(product_id, delta):
        row = products_table.get(product_id)
        # BUG 3b: no lower bound — repeated refunds/returns can drive stock negative.
        new_stock = row["stock"] + delta
        return products_table.update(product_id, stock=new_stock)
