from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        client = request.user
        cart = Cart.objects.filter(client=client, ordered=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        client =request.user
        cart,_ = Cart.objects.get_or_create(client=client, ordered=False)
        product = Bike.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_items = CartItem(cart=cart,client=client,product=product,price=price,quantity=quantity)
        cart_items.save()

        total_price = 0
        cart_items = CartItem.objects.filter(client=client, cart=cart.id)
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()

        return Response({'success': 'Items added to  your cart'})


    def patch(self, request):
        data = request.data
        cart_item = CartItem.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity = quantity
        cart_item.save()
        return Response({'success': 'Items Edited'})

    def delete(self, request):
        client = request.user
        data = request.data

        cart_item = CartItem.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(client=client, ordered=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)


# class OrderView(APIView):
#
#     def get(self, request):
#         queryset = Order.objects.filter(client=request.user)
#         serializer = OrderSerializer(queryset, many=True)
#         return Response(serializer.data)