from django.contrib import admin
from store import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name']
    }
    list_display = ['name', 'slug', 'description',
                    'unit_price', 'count', 'category', 'gender']


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'user']


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
