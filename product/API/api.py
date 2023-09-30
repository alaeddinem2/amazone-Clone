from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from ..models import Product
from rest_framework import generics

@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:30]
    data = ProductSerializer(products,many=True,context={'request':request}).data
    return Response({"product_list":data})

@api_view(['GET'])
def product_detail_api(request,pk):
    products = Product.objects.get(id=pk)
    data = ProductSerializer(products,context={'request':request}).data
    return Response({"product":data})

class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


