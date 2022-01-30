from itertools import product
from store.models import Category, Product
from store import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class ListProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ListCategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductsByCategory(ListCreateAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        queryset = Product.objects.filter(category__code=category)
        return queryset
