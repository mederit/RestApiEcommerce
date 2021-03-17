from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'categories': reverse('category-list', request=request, format=format),
        'bikes': reverse('bike-list', request=request, format=format),
    })

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class BikeView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        filter_ = self.request.query_params.get('filter')
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(category__category_name__icontains=filter_) | Q(color__color_name__icontains=filter_))
        return queryset

class BikeDetailView(generics.RetrieveAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = [permissions.AllowAny]


class ImageDetailView(generics.RetrieveAPIView):
    queryset = BikeImages.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]
