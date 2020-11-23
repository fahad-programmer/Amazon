from django.contrib import admin
from django.contrib.auth.models import User
from actstream import registry

# Register your models here.
registry.register(User)
