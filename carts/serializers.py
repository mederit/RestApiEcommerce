from rest_framework import serializers
from .models import *
from products.serializers import *


class CartSerializer(serializers.ModelSerializer):

    client = serializers.ReadOnlyField(source='client.username')

    class Meta:
        model = Cart
        fields = ['client', 'ordered', 'total_price', 'cart_items']





class CartItemSerializer(serializers.ModelSerializer):
    # cart = CartSerializer(read_only=True)
    product = serializers.ReadOnlyField(source='product.bike_name')
    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'price']


