from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.fun_home),
    path('plants', views.fun_plants),
    path('trees', views.fun_trees),

]