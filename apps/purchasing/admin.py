from django.contrib import admin
from .models import Supplier, PurchaseOrder, PurchaseOrderLine


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'phone', 'address']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Supplier Information', {
            'fields': ('name', 'phone', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class PurchaseOrderLineInline(admin.TabularInline):
    model = PurchaseOrderLine
    fields = ['product', 'quantity', 'cost']
    extra = 1


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'supplier', 'warehouse', 'note', 'created_at', 'updated_at']
    list_filter = ['supplier', 'warehouse', 'created_at', 'updated_at']
    search_fields = ['supplier__name', 'warehouse__name', 'note']
    list_select_related = ['supplier', 'warehouse']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PurchaseOrderLineInline]

    fieldsets = (
        ('Purchase Order Information', {
            'fields': ('supplier', 'warehouse', 'note')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PurchaseOrderLine)
class PurchaseOrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'cost', 'order__supplier', 'order__warehouse']
    list_filter = ['order__supplier', 'order__warehouse', 'product__category', 'order__created_at']
    search_fields = ['order__supplier__name', 'product__name', 'product__sku']
    list_select_related = ['order', 'product', 'order__supplier', 'order__warehouse']
    ordering = ['-order__created_at']

    fieldsets = (
        ('Order Line Information', {
            'fields': ('order', 'product', 'quantity', 'cost')
        }),
    )