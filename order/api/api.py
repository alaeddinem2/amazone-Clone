from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User
from .serializers import CartDetailSerializer,CartSerializer
from order.models import Cart,CartDetail
from product.models import Product

class CartDetailCreateApi(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart, create = Cart.objects.get_or_create(user=user,status = "InProgress")

        data = CartSerializer(cart).data

        return Response({'cart':data})
    
    def post(self, request, *args, **kwargs):
        pass
    
    def delete (self, request, *args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
        cart_detail.delete()

        cart= Cart.objects.get(user=user,status = "InProgress")
        data = CartSerializer(cart).data
        return Response({'message':f"{cart_detail.product} Deleted successfully",'data':data})