from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about/', views.about, name='about'),
    path('order/',views.order,name="all fruits"),
    path('condact/',views.condact,name="condact"),
    path('fruits/',views.order,name="all fruits"),

]