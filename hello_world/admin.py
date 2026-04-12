from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import User, Product, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

    def save_model(self, request, obj, form, change):
        # Always hash the password when saving through admin
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'date_of_order', 'cost')