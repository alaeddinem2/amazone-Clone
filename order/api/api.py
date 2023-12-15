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
        user = User.objects.get(username = self.kwargs['username'])
        cart= Cart.objects.get(user=user,status = "InProgress")
        product = Product.objects.get(id = request.data['product_id'])
        quantity = request.data['quantity']

        cart_detail,created= CartDetail.objects.get_or_create(cart=cart, product=product)

        cart_detail.quantity += int(quantity)
        cart_detail.total = round(cart_detail.quantity * product.price, 2)
        cart_detail.save()

        data = CartDetailSerializer(cart_detail).data
        return Response({'message':f"{cart_detail.product} Edited successfully",'data':data})

    
    def delete (self, request, *args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
        cart_detail.delete()

        cart= Cart.objects.get(user=user,status = "InProgress")
        data = CartSerializer(cart).data
        return Response({'message':f"{cart_detail.product} Deleted successfully",'data':data})