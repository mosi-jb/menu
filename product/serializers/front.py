from rest_framework import serializers

from product.models import Category, Product


class ProductFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryFrontSerializer(serializers.ModelSerializer):
    product = ProductFrontSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'
