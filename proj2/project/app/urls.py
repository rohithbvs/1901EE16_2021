from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home,name='home'),
    path('/generate_over_range', views.generate_over_range,name='generate_over_range'),
    path('/generate_all', views.generate_all,name='generate_all'),
]