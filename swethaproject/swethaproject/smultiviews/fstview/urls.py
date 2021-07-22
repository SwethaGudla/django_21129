
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.mutli),
    path('ms',views.mutlisec),
]

