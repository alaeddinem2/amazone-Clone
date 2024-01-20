from rest_framework import serializers
from order.models import Order,OrderDetail,Cart,CartDetail
from product.api.serializers import ProductListSerializer

class CartDetailSerializer(serializers.ModelSerializer):
    #product = ProductListSerializer()
    product = serializers.StringRelatedField()
    coupon = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)

    class  Meta:
        model = Cart
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    products = OrderProductSerializer(many=True,source='order_detail')

    class Meta:
        model = Order
        fields = '__all__'

