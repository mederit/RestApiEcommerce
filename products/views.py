from rest_framework import generics
from .serializers import *



class BikeView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

