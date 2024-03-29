from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models.product import Product
from .serializer import ProductSerializer


# Create your views here.


def index(request):
    return HttpResponse("Hello world!")

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    print("am facut un nou request")
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)

# tema - folosim si postman
api_view(['POST'])
def add_product(request):
    # get params from request
    # insert params in database
    # return success / or not use http codes for this
    pass


 
