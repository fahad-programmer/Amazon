from django.contrib import admin
from .models import Product, Order, WishList
from actstream import registry

# Register your models here.
admin.site.register(Order)
admin.site.register(WishList)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)


# Django-Activity-Stream
registry.register(Product)
