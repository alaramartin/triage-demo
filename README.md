# shipyard

A small internal e-commerce backend: checkout, orders, users, inventory, and admin tooling.

## Layout

- `core/` — validation, config, and shared error types
- `models/` — Order, User, Product, Cart
- `services/` — business logic per domain (orders, users, inventory, pricing, upload)
- `api/` — HTTP route handlers
- `utils/` — logging and CSV export helpers

## Running tests

```
pytest tests/
```
