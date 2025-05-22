from django.contrib import admin
from .models import Category, Warehouse, Product, StockMovement


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Category Information', {
            'fields': ('name',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'address']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Warehouse Information', {
            'fields': ('name', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'category', 'cost_price', 'sell_price', 'size', 'color', 'created_at']
    list_filter = ['category', 'size', 'color', 'created_at', 'updated_at']
    search_fields = ['sku', 'name', 'category__name']
    list_select_related = ['category']
    ordering = ['sku']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Product Information', {
            'fields': ('sku', 'name', 'category')
        }),
        ('Pricing', {
            'fields': ('cost_price', 'sell_price')
        }),
        ('Attributes', {
            'fields': ('size', 'color')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'warehouse', 'movement_type', 'quantity', 'user', 'created_at']
    list_filter = ['movement_type', 'warehouse', 'product__category', 'user', 'created_at', 'updated_at']
    search_fields = ['product__name', 'product__sku', 'warehouse__name', 'user__username']
    list_select_related = ['product', 'warehouse', 'user']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Movement Information', {
            'fields': ('product', 'warehouse', 'movement_type', 'quantity')
        }),
        ('User Information', {
            'fields': ('user',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
