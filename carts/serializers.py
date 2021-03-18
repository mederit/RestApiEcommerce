from .models import *
from products.serializers import *


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['total_price',]





class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    client = serializers.ReadOnlyField(source='client.username')
    product = serializers.ReadOnlyField(source='product.bike_name')
    class Meta:
        model = CartItem
        fields = ['id', 'client', 'product', 'quantity', 'price', 'cart']


