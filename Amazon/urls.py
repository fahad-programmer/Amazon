"""Amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Amazon.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap


admin.site.site_header = "Amazon Control Panel"
admin.site.site_title = "Amazon Control Panel"
admin.site.index_title = "Welcome To Amazon Control Panel"


# Sitemap Integration
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),


    # Sending To Home Directory Where Ever The Link Is Empty
    path('', include('Home.urls')),

    # Including The Social Authentication
    path('accounts/', include('allauth.urls')),

    # Shop Urls
    path('shop/', include('Shop.urls')),

    # Sitemap
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}),

    # Activity Stream
    path('activity/', include('actstream.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
