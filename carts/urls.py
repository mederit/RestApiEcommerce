from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart_url'),
    # path('order/', OrderView.as_view(), name='order_url'),
]