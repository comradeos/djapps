from django.db import models
from datetime import datetime


# Create your models here.

class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now())
    email = models.EmailField(default='test@email.com')
    bool = models.BooleanField(default=1)
    float = models.FloatField(default=0.0)
    time = models.TimeField(default=datetime.now())
    text = models.TextField(null=True)
