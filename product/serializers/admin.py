from rest_framework import serializers

from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'
