from django.contrib import admin
from .models import Product, OrderItem, ShippingAddress

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'owner', 'category', 'name', 'price', 'date_added']
    list_filter = ['category', 'date_added']
    search_fields = ['id', 'category', 'name', 'price', 'date_added']

@admin.register(ShippingAddress)
class AdminShippingAddress(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'address', 'city', 'state', 'zipcode', 'date_submit']
    list_filter = ['state', 'date_submit']
    search_fields = ['id', 'name', 'phone', 'address', 'city', 'state', 'zipcode', 'date_submit']

@admin.register(OrderItem)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'shippingaddress', 'product', 'quantity', 'getTotal', 'date_orderd']
    list_filter = ['date_orderd']
    search_fields = ['id', 'product', 'quantity', 'getTotal', 'date_orderd']
