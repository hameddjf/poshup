"""
URL configuration for online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from category.views import BaseView

from azbankgateways.urls import az_bank_gateways_urls

admin.autodiscover()

# app_name = 'online_shop'
urlpatterns = [
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path('securelogin/', admin.site.urls),
    path('admin/', admin.site.urls),

    path('', BaseView.as_view(), name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('account/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('connect/', include('connect.urls', namespace='connect')),
    path('discount/', include('discount.urls')),
    path('coupons/', include('coupons.urls')),
    path('like/', include('like.urls')),


    path("bankgateways/", az_bank_gateways_urls()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
