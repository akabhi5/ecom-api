from itertools import product
from store.models import Category, Product
from store import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ListCategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductsByCategory(ListCreateAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        queryset = Product.objects.filter(category__code=category)
        return queryset
