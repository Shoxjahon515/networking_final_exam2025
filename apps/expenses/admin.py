from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum, F
from .models import ExpenseCategory, Expense


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'user', 'created_at']
    list_filter = ['category', 'user', 'created_at', 'updated_at']
    search_fields = ['category__name', 'note',]
    list_select_related = ['category', 'user']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']



class ExpenseAdminSite(admin.AdminSite):
    site_header = "Expense Management Admin"
    site_title = "Expense Admin"
    index_title = "Welcome to Expense Management"
