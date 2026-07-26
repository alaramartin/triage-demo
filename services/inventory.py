"""Inventory service — stock adjustments on order and refund events."""
from models.product import Product
from core.db import Table

reservations_table = Table("reservations")


def reserve_stock(product_id, quantity):
    return Product.adjust_stock(product_id, -quantity)


def restock(product_id, quantity):
    return Product.adjust_stock(product_id, quantity)


def refund_stock(product_id, quantity):
    # Refunds restock via the same unbounded adjust_stock — no floor check here either.
    return Product.adjust_stock(product_id, quantity)
