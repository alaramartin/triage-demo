"""Admin-only routes for bulk inventory and asset management."""
from services.inventory import restock, refund_stock
from services.upload import handle_upload


def post_bulk_edit(request):
    results = []
    for change in request["changes"]:
        results.append(restock(change["product_id"], change["quantity"]))
    return {"updated": results}


def post_bulk_refund(request):
    return [refund_stock(r["product_id"], r["quantity"]) for r in request["refunds"]]


def post_admin_upload(request):
    return handle_upload(request["file"], request["fields"])
