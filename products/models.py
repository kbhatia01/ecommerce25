from django.utils.timezone import datetime

from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)




