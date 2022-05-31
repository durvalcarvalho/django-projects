# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Customer, Product, Order, OrderItem, ShippingAddress


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email')
    list_filter = ('user',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'digital')
    list_filter = ('digital',)
    search_fields = ('name',)


# Add OrderIgem Tabular
class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'created_at',
        'is_completed',
        'transaction_id',
    )
    list_filter = ('customer', 'created_at', 'is_completed')
    date_hierarchy = 'created_at'
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity', 'added_at')
    list_filter = ('product', 'order', 'added_at')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'order',
        'address',
        'city',
        'state',
        'zip_code',
        'country',
        'created_at',
    )
    list_filter = ('customer', 'order', 'created_at')
    date_hierarchy = 'created_at'
