from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('add/', views.record_create, name='record_create'),
    path('<int:pk>/edit/', views.record_edit, name='record_edit'),
    path('<int:pk>/delete/', views.record_delete, name='record_delete'),
]
