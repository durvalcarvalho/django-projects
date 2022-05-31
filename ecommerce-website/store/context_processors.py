from store.views import get_order_items


def number_of_items_in_cart(request):
    items, _ = get_order_items(request)
    context = { 'number_of_items_in_cart': len(items) }
    return context