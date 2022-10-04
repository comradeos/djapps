from django.db import models
from datetime import datetime


# Create your models here.

class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)

