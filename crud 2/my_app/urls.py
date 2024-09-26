from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
    path('', views.index),
    path('add1', views.add1),
    path('save1/', views.save1),
    path('delete1/<int:id>/', views.delete1),
    path('edit1/<int:id>/', views.edit1),
    path('update1/<int:id>/', views.update1),
]

