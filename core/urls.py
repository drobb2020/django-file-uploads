from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_dogs, name='list-dogs'),
    path('delete/<int:pk>/', views.delete_image, name='delete-image'),
]
