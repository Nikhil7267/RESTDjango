from django.contrib import admin
from .models import Employee, Product, Customer, Sale

# Register your models with the admin site

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'email', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone', 'address')
    ordering = ('name',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'employee', 'customer', 'quantity', 'total_price', 'timestamp')
    list_filter = ('product', 'employee', 'customer')
    search_fields = ('product__name', 'employee__username', 'customer__name')
    ordering = ('-timestamp',)


