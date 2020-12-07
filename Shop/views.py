from django.shortcuts import render, redirect, HttpResponse
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from Shop.models import Product
from actstream import action
from notifications.signals import notify
from django.core.paginator import Paginator
from actstream.models import Action
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.

# Cart Views

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)

    # Getting The Values
    if request.method == 'POST':
        global product, color, size, quantity
        product = Product.objects.get(id=id)
        color = request.POST['color']
        size = request.POST['size']
        quantity = request.POST['quantity']

    # Adding the products in cart
    cart.add(product=product, color=color, size=size, quantity=int(quantity))

    # Sending Action and Notification To The User
    action.send(request.user, verb="Product Has Been Added",
                description=f"The User {request.user} has added the product {product} in his cart of the color {color} and size of {size} and quantity of {quantity}", action_object=product)
    notify.send(request.user, verb="Product Has Been Added In Your Cart",
                recipient=request.user, level="success", action_object=product, description=f"The User {request.user} has added the product {product} in his cart")

    return redirect("Home")


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    action.send(request.user, verb="Product Has Been Removed",
                description=f"The User {request.user} has removed the product {product} from the cart", action_object=product)
    notify.send(request.user, verb="Product Has Been Removed From Your Cart",
                recipient=request.user, level="success", action_object=product, description=f"The User {request.user} has added the product {product} in his cart")
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


@cache_page(CACHE_TTL)
@login_required(login_url="/account/login")
def cart_detail(request):

    # Getting The User History
    prods = set()
    filtering_history = Action.objects.filter(
        actor_object_id=request.user.id, verb="User Has Viewed Product").order_by('timestamp')[:3]
    for items in filtering_history:
        prods.add(items.action_object_object_id)
    user_history = Product.objects.filter(id__in=prods)[::-1]

    # Context Used In Template
    params = {'userHistory': user_history}

    return render(request, 'Shop/cart.html', params)


@login_required(login_url="/account/login")
def payout(request):
    return render(request, 'Shop/payout.html')


@login_required(login_url="/account/login")
def payout2(request):
    return render(request, 'Shop/payout2.html')


@login_required(login_url="/account/login")
def payout3(request):
    return render(request, 'Shop/payout3.html')


def search(request, page_num, **filters):

    if request.method == "POST":

        global query, category
        query = request.POST['query']
        category = request.POST['category']

    filtered_product = Product.objects.filter(
        name__icontains=query, category=category).order_by('id')

    # Pagination
    page_obj = Paginator(filtered_product, 16, allow_empty_first_page=True
                         )
    main_page = page_obj.get_page(page_num)

    # Only Sending Action When User Is (Authenticated)
    if request.user.is_authenticated:
        action.send(request.user, verb="User Has Searched",
                    description=f"{request.user} has searched the term {query} in the category {category}")

    # category-products
    category_products = Product.objects.filter(
        category=category)[:1]

    # Context Used In The Template
    params = {'products': main_page, 'cat_prod': category_products}
    return render(request, 'home/search.html', params)

# Main Function (Product- Page)


@cache_page(CACHE_TTL)
def main_product(request, slug):

    product = Product.objects.filter(slug=slug).first()

    Product_History = []

    # Sponsered Products
    sponsered_product = Product.objects.filter(
        category=product.category).exclude(slug=slug)[:2]

    for items in sponsered_product:
        Product_History.append(items.id)

    # Json Data Related To Product
    json_data = product.data

    # Products Related To The Same Sub-Categories
    Sub_Category_Product = Product.objects.filter(
        sub_category=product.sub_category).exclude(id__in=Product_History)[:7]

    # Products Related To The Same Category
    Category_Products = Product.objects.filter(
        category=product.category).exclude(slug=slug)[:7]

    # Products(User Viewed)
    prods = set()
    filtering_history = Action.objects.filter(
        actor_object_id=request.user.id, verb="User Has Viewed Product").order_by('timestamp')[:6]
    for items in filtering_history:
        prods.add(items.action_object_object_id)
    user_history = Product.objects.filter(id__in=prods)

    # Sending the action to the database
    if request.user.is_authenticated:
        action.send(request.user, verb="User Has Viewed Product",
                    description=f"{request.user} has viewed the product {product} with the slug {slug} and id of {product.id}", action_object=product, slug=slug, product_histotry=Product_History, product_data=json_data)

    # Context Used In The Template
    params = {'products': product,
              'jsonData': json_data, 'user_history': user_history, }

    return render(request, 'home/product.html', params)


def api_check(request):
    if HttpResponse == 200:
        print("Good The Number Is Valid")
    else:
        print('The number is invalid')
    return render(request, 'first.html')


def CategorySearch(request, category, page_num):
    product = Product.objects.filter(category=category)

    # Pagination
    page_obj = Paginator(product, 16, allow_empty_first_page=True
                         )
    main_page = page_obj.get_page(page_num)

    context = {}
    return render(request, 'home/category.html', context)
