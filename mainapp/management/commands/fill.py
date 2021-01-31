import json
import os

from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product


from authapp.models import ShopUser


def load_json(file_name):
    with open(os.path.join('mainapp/json', file_name + '.json')) as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        categories = load_json('categories')
        ProductCategory.objects.all().delete()
        for cat in categories:
            new_cat = ProductCategory(**cat)
            new_cat.save()

        products = load_json('products')
        Product.objects.all().delete()

        for product in products:
            category_name = product["category"]
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
