from . import views
from django.urls import path, include

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.ItemCreate.as_view(), name='items_create'),
  path('<int:pk>/delete/', views.ItemDelete.as_view(), name='delete_items'),
]
