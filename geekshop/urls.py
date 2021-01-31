"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import  admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

import mainapp.views as mainapp

urlpatterns = [
    #path('admin/', admin.site.urls),
    # /
    path('',mainapp.main, name='main'),
    #path('admin/', admin.site.urls),
    path('admin/', include('adminapp.urls', namespace='admin')),

    path('', include('social_django.urls', namespace='social')),

    path('products_list/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),

    #path('product-details/', include('mainapp.urls', namespace='products'))

    #path( 'product-details/<int:pk>', mainapp.product_details, name='product-details')

    #path('product-details/all/', mainapp.product, name='products_all'),
    #path('product-details/home/', mainapp.product, name='products_home'),
    #path('product-details/office/', mainapp.product, name='products_office'),
    #path('product-details/furniture/', mainapp.product, name='products_furniture'),
    #path('product-details/modern/', mainapp.product, name='products_modern'),
    #path('product-details/classic/', mainapp.product, name='products_classic')



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   import debug_toolbar

   urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
