from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('logs:list')),
    path('admin/', admin.site.urls),
    path('logs/', include('logs.urls')),
]