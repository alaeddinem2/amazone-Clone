from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductDetailSerializer,ProductListSerializer, BrandDetailSerializer,BrandListSerializer, ReviewSerializer
from ..models import Product, Brand, Review
from rest_framework import generics

@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:30]
    data = ProductListSerializer(products,many=True,context={'request':request}).data
    return Response({"product_list":data})

@api_view(['GET'])
def product_detail_api(request,pk):
    products = Product.objects.get(id=pk)
    data = ProductDetailSerializer(products,context={'request':request}).data
    return Response({"product":data})

class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer

class ReviewListApi(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailApi(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


