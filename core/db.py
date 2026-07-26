"""Tiny in-memory table store standing in for a real database layer."""
from core.validation import require_fields


class Table:
    def __init__(self, name, required_fields=None):
        self.name = name
        self.required_fields = required_fields or []
        self._rows = {}
        self._next_id = 1

    def insert(self, payload):
        if self.required_fields:
            require_fields(payload, self.required_fields)
        row_id = self._next_id
        self._next_id += 1
        self._rows[row_id] = {"id": row_id, **payload}
        return self._rows[row_id]

    def get(self, row_id):
        return self._rows.get(row_id)

    def update(self, row_id, **changes):
        row = self._rows.get(row_id)
        if row is None:
            return None
        row.update(changes)
        return row

    def all(self):
        return list(self._rows.values())
