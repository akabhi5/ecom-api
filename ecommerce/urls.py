
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings


def home(request):
    return JsonResponse({'message': 'Welcome to store!'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', home),
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')), ]
