from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from Shop.models import Product
from notifications.models import Notification

# import geoip2.database
# import socket


def index(request):
    # products = Product.objects.all()[:3]
    # main_products = {'products': products}

    # Getting The Ip Address
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)

    # # Fetching The Country
    # reader = geoip2.database.Reader('./GeoLite2-Country.mmdb')
    # response = reader.country(ip_address=ip_address)
    # print(response)
    return render(request, 'home/index.html')


def SignIn(request):
    return render(request, 'home/login.html')

def search_result(request):
    return render(request, 'home/search.html')

def product_view(request):
    return render(request, 'home/product.html')

def signup(request):
    return render(request, 'home/signup.html')


def handlelogin(request):
    if request.method == 'POST':
        # Here we will get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully Logged In')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Crenditials Please Try Again')

    return render(request, 'home/login.html')


# Handling The Login Using The Email, Username And Password
def handleSignup(request):
    if request.method == 'POST':

        # Here we will get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check for errorneous inputs

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            myusers = User.objects.create_user(username, email, password)
            # Create the user
            myusers.save()
            messages.success(
                request, 'Your Account Has Been Created Successfully')
            return redirect('login')

        elif (User.objects.filter(username=username).exists()):
            messages.error(request, 'The Username Is Already Registered')

        elif (User.objects.filter(email=email).exists()):
            messages.error(request, 'The Email Is Already Registered')

        else:
            messages.error(
                request, 'Something Else Occured! Please Try Again....')

    return render(request, 'home/signup.html')


def user_notification(request):
    user_notifications = request.user.notifications.unread()
    params = {'notifications': user_notifications}
    return render(request, 'home/activity.html', params)
