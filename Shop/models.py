from django.db import models
from django.contrib.auth.models import User
import jsonfield
# Create your models here.


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    description = models.TextField(default="")
    rating = models.IntegerField(default=1)
    delievery_Date = models.CharField(default="", max_length=100)
    number_of_ratings = models.IntegerField(default=0)
    price = models.FloatField()
    brand = models.CharField(max_length=200, default='Amazon')
    slug = models.SlugField(default="", max_length=100)
    image = models.ImageField(upload_to="Shop/images", default=None)
    image_two = models.ImageField(upload_to="Shop/images", default=None)
    image_three = models.ImageField(upload_to="Shop/images", default=None)
    image_four = models.ImageField(upload_to="Shop/images", default=None)
    main_description = models.TextField(default="")
    warrenty_support = models.TextField(default="")
    data = jsonfield.JSONField(default="")
    video_url = models.URLField(default=None)
    in_stock = models.BooleanField(default=True)
    main_banner = models.ImageField(upload_to="Shop/images", default=None)
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
    order_status = models.BooleanField()

    def __str__(self):
        return self.city


class WishList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class OrderTracker(models.Model):
    pass
