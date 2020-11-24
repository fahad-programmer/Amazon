from django.contrib.auth.models import User
from django.test import TestCase
from Shop.models import Order
from Shop.models import Product

# Create your tests here.


class Ordertestcase(TestCase):
    Order.objects.create(items_json="This is the best", user=User.objects.get(username="fahad"),
                         address="Best", city="islamabad", state="dvav", zip_code=558)

    def Order_created(self):
        main_order = Order.objects.get(user="fahad")
        self.assertEqual(main_order.items_json(), 'This is the best')

# class ProductTestCase(TestCase):
#     def json_data(self):
#         main_order = Product.objects.all()[0]
#         for key,values in main_order.data:
#             print(key, values)
