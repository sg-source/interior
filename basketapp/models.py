from django.db import models
from django.conf import settings
from authapp.models import ShopUser
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):

    def save(self, *args, **kwargs):
        for object in self:
            object.product.quantity -= object.quantity
            object.product.save()
        super(BasketQuerySet, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.is_authenticated = None

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        total__quantity = sum(list(map(lambda x: x.quantity, items)))
        return total__quantity

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        total__cost = sum(list(map(lambda x: x.product_cost, items)))
        return total__cost

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_product(user, product):
        return Basket.objects.filter(user=user, product=product)

    @staticmethod
    def get_products_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]

        return basket_items_dic

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()
