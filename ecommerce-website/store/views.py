import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from store import models


def get_order_items(request):
    items = []

    order = {
        'get_cart_items_total': 0,
        'get_cart_total_value': 'BRL 0.00',
    }

    if request.user.is_authenticated:
        customer, created = models.Customer.objects.get_or_create(user=request.user)
        order, created = models.Order.objects.get_or_create(customer=customer, is_completed=False)
        items = order.orderitems.all()

    elif 'cart' in request.COOKIES:
        cart = json.loads(request.COOKIES['cart'])
        for product_id in cart:
            product = models.Product.objects.get(pk=product_id)
            items.append(
                models.OrderItem(
                    product=product,
                    quantity=cart[product_id]['quantity'],
                )
            )

        order['get_cart_items_total'] = sum(item.quantity for item in items)
        order['get_cart_total_value'] = f'BRL {sum(item.total_cents for item in items) / 100}'

    return items, order

def store_view(request):
    items, order = get_order_items(request)
    context = {
        'products': models.Product.objects.all(),
        'order': order,
    }
    return render(request, 'store/store.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    context = { 'product': product }
    return render(request, 'store/product_detail.html', context)

def cart_view(request):
    items, order = get_order_items(request)
    context = { 'items': items, 'order': order }
    return render(request, 'store/cart.html', context)

def checkout_view(request):
    items, order = get_order_items(request)
    context = { 'items': items, 'order': order }
    return render(request, 'store/checkout.html', context)

def add_remove_one_to_cart_endpoint(request, pk: int, action: str):
    product = get_object_or_404(models.Product, pk=pk)

    _, order = get_order_items(request)
    item, created = order.orderitems.get_or_create(product=product)

    if not created:
        if action == 'add':
            item.quantity += 1

        elif action == 'remove':
            item.quantity -= 1

        item.save()

    if item.quantity <= 0:
        item.delete()
        JsonResponse({'quantity': 0})

    return JsonResponse(item.to_json())
