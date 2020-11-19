from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from Shop.models import Product

# Create your views here.

# Cart Views


@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("Home")


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_detail(request):
    return render(request, 'home/cart.html')


def search(request):

    if request.method == "POST":
        global query
        query = request.POST['query']
        # category = request.POST['category']

    filtered_product = Product.objects.filter(
        name__icontains=query)
    print(filtered_product)
    params = {'products': filtered_product}
    return render(request, 'Shop/search.html', params)
