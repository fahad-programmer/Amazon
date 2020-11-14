from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    rating = models.IntegerField(default=1)
    price = models.FloatField()
    image = models.ImageField(upload_to="Shop/images")
    pub_date = models.DateField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField(default=0)

    def __str__(self):
        return self.city


class OrderTracker(models.Model):
    pass
