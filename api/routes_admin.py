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
    except (KeyError, ValueError) as e:
        return {'error': str(e)}, 400


def post_bulk_refund(request):
    try:
        data = json.loads(request.body)
        return [refund_stock(r['product_id'], r['quantity']) for r in data.get('refunds', [])]
    except (KeyError, ValueError) as e:
        return {'error': str(e)}, 400


def post_admin_upload(request):
    try:
        data = json.loads(request.body)
        return handle_upload(data['file'], data['fields'])
    except (KeyError, ValueError) as e:
        return {'error': str(e)}, 400