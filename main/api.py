from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ClothingItemFilter
from . import serializers, models

class ClothingItemListApiView(ListAPIView):
    queryset = models.ClothingItem.objects.all()
    serializer_class = serializers.ClothingItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClothingItemFilter
