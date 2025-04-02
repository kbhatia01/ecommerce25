from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products


# Create your views here.

def hello(request):
    data = Products.objects.all()
    print(data[0].name)
    data[0].name = "ABC"
    data[0].save()
    data = Products.objects.all()
    print(data[0].name)
    return HttpResponse('Hello World!')
