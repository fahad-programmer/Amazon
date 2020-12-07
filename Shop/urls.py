from django.urls import path
from Shop.views import CategorySearch, cart_add, payout, payout2, payout3, cart_clear, cart_detail, item_clear, item_decrement, item_increment, search, main_product,  CategorySearch

urlpatterns = [
    # Cart Urls
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),

    # Search Urls
    path('product/search/<int:page_num>', search, name='search'),
    path('product/<str:slug>', main_product, name="main_product"),
    path('payout/', payout, name="payout"),
    path('payout2/', payout2, name="payout2"),
    path('payout3/', payout3, name="payout3"),


    # Product Urls
    path('product/<str:slug>', main_product, name="main_product"),


    # Category Search
    path('category', CategorySearch, name="cat"),

]
