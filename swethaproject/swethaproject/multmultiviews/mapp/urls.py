from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('g',views.greetings),
    path('g1', views.greetings1),
    path('g2', views.greetings2),
]
