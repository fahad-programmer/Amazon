from django.urls import path, include
from Home.views import index, login


urlpatterns = [
    path('', index, name="Home"),
    path('account/login', login, name="login")
]
