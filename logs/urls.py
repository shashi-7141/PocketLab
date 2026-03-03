from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    path('', views.log_list, name='list'),
    path('add/', views.log_create, name='create'),
    path('<int:pk>/', views.log_detail, name='detail'),
    path('<int:pk>/edit/', views.log_update, name='update'),
    path('<int:pk>/delete/', views.log_delete, name='delete'),
]
