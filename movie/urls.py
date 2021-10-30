from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(':<int:id>/', views.retrieve, name='retrieve'),
    path('create/', views.create, name='create'),
    path(':<pk>/delete/', views.delete, name='delete'),
    path(':<pk>/update/', views.update, name='update'), 
]