from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from Shop.models import Product
from actstream import action


# Create your views here.

# Cart Views


@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    action.send(request.user, verb="Product Has Been Added",
                description=f"The User {request.user} has added the product {product} in his cart", action_object=product)
    return redirect("Home")


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    action.send(request.user, verb="Product Has Been Removed",
                description=f"The User {request.user} has removed the product {product} from his cart", action_object=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    action.send(request.user, verb="Product Value Has Been Added",
                description=f"The User {request.user} has incremented the product {product} in his cart", action_object=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    action.send(request.user, verb="Product Value Has Been Decreased",
                description=f"The User {request.user} has decremented the product {product} in his cart", action_object=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    action.send(request.user, verb="Cart Has Cleared",
                description=f"{request.user} has cleared the cart")
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_detail(request):
    return render(request, 'Shop/cart.html')


def search(request):

    if request.method == "POST":
        global query, category
        query = request.POST['query']
        category = request.POST['category']

    filtered_product = Product.objects.filter(
        name__icontains=query)

    if request.user.is__authenticated:
        action.send(request.user, verb="User Has Searched",
                    description=f"{request.user} has searched the term {query} in the category {category}")

    params = {'products': filtered_product}
    return render(request, 'Shop/search.html', params)
