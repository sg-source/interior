from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
# from django.urls import reverse
from django.template.loader import render_to_string

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory
#from mainapp.views import get_basket


def basket(request):
    submenu = ProductCategory.objects.all()
    title = 'Корзина'
    basket_items = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'submenu': submenu,
        'basket_items': basket_items
    }
    return render(request, 'basketapp/basket.html', context)


def basket_add(request, pk):
    # if 'login' in request.META.get('HTTP_REFERER'):
    #     return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(user=request.user, product=product).first()
    print(product)
    print(basket_item)
    if not basket_item:
        basket_item = Basket(user=request.user, product=product)

    basket_item.quantity += 1
    basket_item.save()
    # product.quantity -= 1
    # product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user). \
            order_by('product__category')

        content = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/include/inc_cart_list.html', content)

        return JsonResponse({'result': result})




