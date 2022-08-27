from rest_framework import serializers

from .models import Category, Crop

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "quantity",
            "discount",
            "delivery_type",
            "get_date",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    crops = CropSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "get_absolute_url",
            'crops'
        )