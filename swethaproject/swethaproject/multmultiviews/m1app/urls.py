from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('m', views.message),
    path('m1', views.message1),
    path('m2', views.message2),
]
