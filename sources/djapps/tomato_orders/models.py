from django.contrib.auth.models import User
from django.db import models

from tomato_products.models import Product


class Additional(models.Model):
    title = models.CharField(max_length=255)


# Create your models here.
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    test = models.OneToOneField(Additional, on_delete=models.CASCADE, null=True)


