"""Shared exception types."""


class AppError(Exception):
    """Base class for all application errors."""


class NotFoundError(AppError):
    def __init__(self, entity, entity_id):
        super().__init__(f"{entity} {entity_id} not found")
        self.entity = entity
        self.entity_id = entity_id


class ValidationError(AppError):
    pass


class InsufficientStockError(AppError):
    def __init__(self, product_id, requested, available):
        super().__init__(
            f"cannot reserve {requested} of product {product_id}, only {available} available"
        )
