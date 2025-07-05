from . import models
from rest_framework import serializers

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'slug']

class ClothingItemSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = models.ClothingItem
        fields = '__all__'