from rest_framework import viewsets

from product.models import Category, Product
from product.serializers.front import ProductFrontSerializer, CategoryFrontSerializer


class CategoryFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryFrontSerializer


class ProductFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFrontSerializer
