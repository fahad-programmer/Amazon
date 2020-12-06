from django.contrib import admin
from django.contrib.auth.models import User
from actstream import registry
from .models import Profile, Address

# Register your models here.
registry.register(User)
admin.site.register(Profile)
admin.site.register(Address)
