from django.contrib import admin
from django.contrib.auth.models import User
from actstream import registry
from .models import Profile

# Register your models here.

registry.register(User)

# Main classes here


# Modal registry

admin.site.register(Profile)
