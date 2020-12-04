from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from Shop.models import Product
from actstream import action
from notifications.signals import notify
from django.core.paginator import Paginator
from actstream.models import Action

# Create your views here.

# Cart Views


@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    action.send(request.user, verb="Product Has Been Added",
                description=f"The User {request.user} has added the product {product} in his cart", action_object=product)
    notify.send(request.user, verb="Product Has Been Added In Your Cart",
                recipient=request.user, level="success", action_object=product, description=f"The User {request.user} has added the product {product} in his cart")
    print(request.user.notifications.unread())
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


@login_required(login_url="/account/login")
def cart_detail(request):
    return render(request, 'Shop/cart.html')

@login_required(login_url="/account/login")
def payout(request):
    return render(request, 'Shop/payout.html')

@login_required(login_url="/account/login")
def payout2(request):
    return render(request, 'Shop/payout2.html')

def search(request, page_num):

    if request.method == "POST":
        global query, category
        query = request.POST['query']
        category = request.POST['category']

    filtered_product = Product.objects.filter(
        name__icontains=query, category=category)

    # Pagination
    page_obj = Paginator(filtered_product, 1, allow_empty_first_page=False)
    main_page = page_obj.get_page(page_num)
    print(main_page.count)
    # Only Sending Action When User Is (Authenticated)
    if request.user.is_authenticated:
        action.send(request.user, verb="User Has Searched",
                    description=f"{request.user} has searched the term {query} in the category {category}")

    # Context Used In The Template
    params = {'products': main_page}
    return render(request, 'home/search.html', params)

# Main Function (Product- Page)


def main_product(request, slug):
    pass
    # product = Product.objects.filter(slug=slug).first()

    # Product_History = []

    # # Sponsered Products
    # sponsered_product = Product.objects.filter(
    #     category=product.category).exclude(slug=slug)[:2]

    # for items in sponsered_product:
    #     Product_History.append(items.id)

    # # Json Data Related To Product
    # json_data = product.data

    # # Products Related To The Same Sub-Categories
    # # Sub_Category_Product = Product.objects.filter(
    # #     sub_category=product.sub_category).exclude(id=Product_History[1])[:7]

    # # Products Related To The Same Category
    # # Category_Products = Product.objects.filter(
    # #     category=product.category).exclude(slug=slug)[:7]

    # # Products(User Viewed)
    # user_history = Action.objects.filter(
    #     actor_object_id=request.user.id, verb="User Has Viewed Product")[:7]

    # # Sending the action to the database
    # if request.user.is_authenticated:
    #     action.send(request.user, verb="User Has Viewed Product",
    #                 description=f"{request.user} has viewed the product {product} with the slug {slug} and id of {product.id}", action_object=product, slug=slug, product_histotry=Product_History, product_data=json_data)

    # # Context Used In The Template
    # params = {'products': product,
    #           'jsonData': json_data, 'user_history': user_history, }

    # return render(request, 'home/product.html', params)
