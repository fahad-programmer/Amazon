from django.contrib import admin
from .models import Product, Order
from actstream import registry

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)

# Django-Activity-Stream
registry.register(Product)
