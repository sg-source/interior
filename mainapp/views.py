from django.shortcuts import render
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
import json
import os
from geekshop.settings import BASE_DIR
from django.shortcuts import get_object_or_404

def get_hot_product():
    products_list = Product.objects.all()

    return random.sample(list(products_list), 1)[0]

def get_related_products(hot_product):
    related_products = Product.objects.filter(category=hot_product.category).\
        exclude(pk=hot_product.pk)[:3]

    return related_products

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def main(request):
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:4]
    # products = Product.objects.all()[:4]#random.sample(list(productModel), 4)
    menu = []
    menu_main = os.path.join(BASE_DIR, 'main.json')
    submenu = ProductCategory.objects.all()
    if os.path.exists(menu_main):
        with open(menu_main) as menu_links:
          menu = json.loads(menu_links.read())
    context = {
        'title': 'главная',
        #'productModel': productModel,
        'products' : products,
        'menu': menu,
        'submenu': submenu
    }
    return render(request, 'mainapp/index.html', context)

def product(request, pk=None, page=1):

    # basket = get_basket(request.user)
    products_list = Product.objects.all()
    submenu = ProductCategory.objects.all()
    category = {'name': 'all'}
    hot_product = get_hot_product()
    related_products = get_related_products(hot_product)
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category = {'pk': 0, 'name': 'all'}

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products_list, 4)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': 'Продукты',
            'submenu': submenu,
            'category': category,
            'products_list': products_paginator, #products_list,
            # 'basket': basket,
            'hot_product': hot_product,
            'related_products': related_products
        }
        return render(request, 'mainapp/products_list.html', context)

    context = {
        'title': 'Продукты',
        'submenu': submenu,
        'products_list': products_list,
        'category': category,
        # 'basket': basket,
    }
    return render(request, 'mainapp/products_list.html', context)


def product_details(request, pk):
    submenu = ProductCategory.objects.all()
    if pk is not None:
        product_item = Product.objects.filter(pk=pk)
        submenu = ProductCategory.objects.all()
        context = {
            'title': 'Продукты',
            'submenu': submenu,
            'product_item': product_item
        }
        return render(request, 'mainapp/product-details.html', context)


    context = {
        'title': 'Продукты',
        'submenu': submenu,
    }
    return render(request, 'mainapp/product-details.html', context)
