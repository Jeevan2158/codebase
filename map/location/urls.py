from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.save_location, name='save_location'),
    path('loc/', views.mapping, name='mapping'),

]
