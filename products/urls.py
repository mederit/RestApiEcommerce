from django.urls import path
from .views import *

urlpatterns = [
    path('bike/list/', BikeView.as_view(), name='bike_url'),
]