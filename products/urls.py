from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =format_suffix_patterns([
    path('products/', api_root),
    path('category/list/', CategoryView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('bike/list/', BikeView.as_view(), name='bike-list'),
    path('bike/<int:pk>/',BikeDetailView.as_view(), name='bike-detail'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='bikeimages-detail'),
])
