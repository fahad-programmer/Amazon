from django.urls import path, include
from Home.views import index, SignIn, signup, handleSignup, handlelogin, user_notification


urlpatterns = [
    path('', index, name="Home"),
    path('account/login', SignIn, name="login"),
    path('account/signup', signup, name="signup"),
    path('account/signup/handle', handleSignup, name="handlesignup"),
    path('account/login/handle', handlelogin, name="handlelogin"),
    path('user', user_notification, name="activity")


]
