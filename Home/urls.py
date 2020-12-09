from django.urls import path, include
from Home.views import index, SignIn, signup, about, account, numverify, terms, privacy, forget, handleSignup, handlelogin, user_notification, product_view, profile


urlpatterns = [
    path('', index, name="Home"),
    path('account/login', SignIn, name="login"),
    path('account/signup', signup, name="signup"),
    path('account/signup/handle', handleSignup, name="handlesignup"),
    path('account/login/handle', handlelogin, name="handlelogin"),
    path('product/', product_view, name="Product View"),
    path('user', user_notification, name="activity"),
    path('account/number-verification', numverify, name="numverify"),
    path('account/forget-password', forget, name="forget"),
    path('terms-and-conditions', terms, name="terms"),
    path('privacy-policy', privacy, name="privacy"),
    path('about', about, name="about"),
    path('account', account, name="account"),
    path('account/profile', profile, name="profile"),
]
