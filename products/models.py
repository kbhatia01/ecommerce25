from django.utils.timezone import datetime

from django.db import models


# Create your models here.

class AuditData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Products(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,
                                 related_name='products')


class Category(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

#TODO: SELECT related `select_related` : I need x data in few seconds, get it right away.. 1xm , 1:1
#  FOR MxM : `prefetch_related`
#  Order.objects.prefetch_related('products').all()
