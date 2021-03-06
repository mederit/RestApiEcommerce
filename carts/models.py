from django.db import models
from django.conf import settings
from products.models import Bike
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Cart(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.client.username) + " " + str(self.total_price)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Bike, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items =models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.client.username) + " " + str(self.product.bike_name)


@receiver(pre_save, sender=CartItem)
def correct_price(**kwargs):
    cart_items = kwargs['instance']
    price_of_product = Bike.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
