from django.contrib import admin
from django.contrib.auth.models import User
from actstream import registry
from .models import Profile, Address, Addresses

# Register your models here.

registry.register(User)

# Main classes here

class AddressInline(admin.TabularInline):
	model = Addresses
	extra = 1

class Address_Admin(admin.ModelAdmin):
	inlines = [AddressInline]
	fieldsets = [
		('Main Information',	{'fields':['profile', 'country', 'zip_code', 'building_details']}),
	]
	inlines = [AddressInline]

	# List Display Format

	list_display = ['profile', 'country', 'zip_code']

# Modal registry

admin.site.register(Profile)
admin.site.register(Address, Address_Admin)
