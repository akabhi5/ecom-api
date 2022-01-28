
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({'message': 'Welcome to store!'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('', home),
]
