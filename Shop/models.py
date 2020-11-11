from django.db import models

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
