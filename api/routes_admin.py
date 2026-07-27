"""Admin-only routes for bulk inventory and asset management."""
from services.inventory import restock, refund_stock
from services.upload import handle_upload
import json


def post_bulk_edit(request):
    try:
        results = []
        data = json.loads(request.body)
        for change in data.get('changes', []):
            results.append(restock(change['product_id'], change['quantity']))
        return {'updated': results}
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        return {'error': str(e)}, 400


def post_bulk_refund(request):
    try:
        return [refund_stock(r['product_id'], r['quantity']) for r in request.get('refunds', [])]
    except (KeyError, TypeError) as e:
        return {'error': str(e)}, 400


def post_admin_upload(request):
    try:
        return handle_upload(request['file'], request['fields'])
    except KeyError as e:
        return {'error': str(e)}, 400