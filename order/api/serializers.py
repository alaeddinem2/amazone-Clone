from rest_framework import serializers
from order.models import Order,OrderDetail,Cart,CartDetail
from product.api.serializers import ProductListSerializer

class CartDetailSerializer(serializers.ModelSerializer):
    #product = ProductListSerializer()
    product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)

    class  Meta:
        model = Cart
        fields = '__all__'
