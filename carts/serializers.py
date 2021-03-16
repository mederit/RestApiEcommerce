from rest_framework import serializers
from .models import *
from products.serializers import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    product = serializers.ReadOnlyField(source='product.bike_name')
    class Meta:
        model = CartItem
        exclude = ('total_items', 'cart')

#
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'