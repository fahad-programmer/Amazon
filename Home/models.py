from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.user.username


class Address(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, default="Pakistan")
    zip_code = models.CharField(max_length=20, default=1)
    building_details = models.CharField(max_length=500)

class Addresses(models.Model):
    address = models.ForeignKey(
        'Address',
        on_delete=models.CASCADE,
        )
    address_line_1 = models.CharField(max_length=500)
    address_line_2 = models.CharField(max_length=500, blank=True)