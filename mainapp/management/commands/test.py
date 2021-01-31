import json
import os

from django.core.management import BaseCommand

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        product = Basket.objects.all()
        print(product)


