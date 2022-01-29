from django.urls import path
from store import views

urlpatterns = [
    path('products/', views.ListProductAPIView.as_view()),
    path('products/<int:pk>/', views.ProductAPIView.as_view()),
    path('categories/', views.ListCategoryAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryAPIView.as_view()),
    path('products/category/<str:category>/',
         views.ProductsByCategory.as_view()),
]
