from django.urls import path, include
from Home.views import index


urlpatterns = [
    path('', index, name="Home")
]
