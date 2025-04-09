from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Products
from products.serializers import ProductSerializer


# Create your views here.

def hello(request):
    data = Products.objects.all()
    d = data[0]
    print(data[0].name)
    d.name = "lkj"
    d.save()
    data = Products.objects.all()
    print(data[0].name)
    return HttpResponse('Hello World!')


@api_view(['GET'])
def get_products(request):
    data = Products.objects.all()
    serializedProducts = ProductSerializer(data, many=True)
    return Response(serializedProducts.data)


@api_view(['GET'])
def get_product(request, id):
    try:
        data = Products.objects.get(id=id)
        print(data)
        serializedProducts = ProductSerializer(data)
        return Response(serializedProducts.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_product(request):
    try:
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
# GET:

# /product/1 -> return me data

# DELTE
# /product/1 -> delete data...


# TODO:  CREATE AN API FOR CREATING AND SAVING PRODUCT TO DATABASE...
