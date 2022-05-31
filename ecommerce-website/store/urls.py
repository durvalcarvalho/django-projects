from django.urls import path

from store import views

app_name = 'store'

urlpatterns = [
    path('', views.store_view, name='store-view'),
    path('product/<int:pk>/', views.product_detail_view, name='product-detail-view'),
    path('cart/', views.cart_view, name='cart-view'),
    path('checkout/', views.checkout_view, name='checkout-view'),
    path(
        'add-remove-one-to-cart/<int:pk>/<str:action>/',
        views.add_remove_one_to_cart_endpoint,
        name='add-to-cart-endpoint'
    ),
]
