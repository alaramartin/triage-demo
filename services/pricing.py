"""Pricing service — cart totals and discount application."""
from models.cart import Cart
from models.product import Product


def cart_total(cart: Cart):
    return cart.total_cents()


def apply_discount(product_id, discount_percent):
    return Product.sale_price_cents(product_id, discount_percent)


def quote_for_cart(cart: Cart, discount_percent=0):
    subtotal = cart_total(cart)
    if discount_percent:
        subtotal = subtotal * (1 - discount_percent / 100)
    return subtotal
