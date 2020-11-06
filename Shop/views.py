from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from Shop.models import Product

# Create your views here.


def cart(request):
    return render(request, 'home/cart.html')

# Cart Views


@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    # product = Product.objects.get(id=id)
    # cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    # product = Product.objects.get(id=id)
    # cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    # product = Product.objects.get(id=id)
    # cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
