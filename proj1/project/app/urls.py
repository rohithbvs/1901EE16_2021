from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('email_sent/', views.send_emails,name="email"),
    path('concise_sheet/', views.concise_sheet,name="concise-sheet"),
]
