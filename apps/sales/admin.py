from django.contrib import admin
from .models import Customer, SaleOrder, SaleOrderLine


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'address', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'phone', 'address']
    ordering = ['first_name', 'last_name']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Customer Information', {
            'fields': ('first_name', 'last_name', 'phone', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class SaleOrderLineInline(admin.TabularInline):
    model = SaleOrderLine
    fields = ['product', 'quantity', 'price']
    extra = 1


@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'customer', 'cashier', 'note', 'created_at', 'updated_at']
    list_filter = ['customer', 'cashier', 'created_at', 'updated_at']
    search_fields = ['customer__first_name', 'customer__last_name', 'cashier__username', 'note']
    list_select_related = ['customer', 'cashier']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [SaleOrderLineInline]

    fieldsets = (
        ('Sale Order Information', {
            'fields': ('customer', 'cashier', 'note')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SaleOrderLine)
class SaleOrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'order__customer', 'order__cashier']
    list_filter = ['order__customer', 'order__cashier', 'product__category', 'order__created_at']
    search_fields = ['order__customer__first_name', 'order__customer__last_name', 'product__name', 'product__sku']
    list_select_related = ['order', 'product', 'order__customer', 'order__cashier']
    ordering = ['-order__created_at']

    fieldsets = (
        ('Order Line Information', {
            'fields': ('order', 'product', 'quantity', 'price')
        }),
    )