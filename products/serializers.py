from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    bikes = serializers.HyperlinkedRelatedField(many=True, view_name='bike-detail', read_only=True)

    class Meta:
        model = Category
        fields = ['url', 'category_name', 'image', 'bikes']


class BikeSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(many=True, view_name='bikeimages-detail', read_only=True)
    category = serializers.ReadOnlyField(source='category.category_name')
    color = serializers.ReadOnlyField(source='color.color_name')

    class Meta:
        model = Bike
        fields = ['url', 'bike_name', 'category', 'color', 'images']



class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikeImages
        fields = ['image',]