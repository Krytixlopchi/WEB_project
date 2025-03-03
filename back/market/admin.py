from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ShippingAddress, Category, Product, Cart, Wishlist, Order, OrderItem, Payment, Review

# Налаштування для кастомного користувача
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "phone", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("username", "email", "phone")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональна інформація", {"fields": ("first_name", "surname", "last_name", "email", "phone")}),
        ("Ролі та доступ", {"fields": ("role", "is_staff", "is_active", "groups", "user_permissions")}),
        ("Дати", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "phone", "password1", "password2", "role", "is_staff", "is_active"),
        }),
    )
    ordering = ("username",)

# Налаштування для моделі адреси доставки
@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("user", "country", "city", "street", "postal_code")
    search_fields = ("user__username", "city", "postal_code")

# Категорії товарів
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)
    list_filter = ("parent",)

# Продукти
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "seller", "price", "category", "stock_quantity", "image")
    search_fields = ("title", "description")
    list_filter = ("category", "seller")
    list_editable = ("price", "stock_quantity")

# Кошик
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity")
    search_fields = ("user__username", "product__title")

# Бажане (Wishlist)
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
    search_fields = ("user__username", "product__title")

# Замовлення
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_amount", "status", "created_at", "shipping_address")
    search_fields = ("user__username", "status")
    list_filter = ("status", "created_at")

# Позиції в замовленні
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    search_fields = ("order__user__username", "product__title")

# Оплати
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "payment_method", "status", "transaction_id")
    search_fields = ("order__user__username", "transaction_id")
    list_filter = ("payment_method", "status")

# Відгуки
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "rating", "created_at")
    search_fields = ("user__username", "product__title")
    list_filter = ("rating", "created_at")
