from django.urls import path
from Shop.views import cart, cart_add, cart_clear, cart_detail, item_clear, item_decrement, item_increment

urlpatterns = [
    path('cart', cart, name="cart"),

    # Cart Urls
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
]
