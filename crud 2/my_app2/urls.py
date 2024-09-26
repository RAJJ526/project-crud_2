from django.contrib import admin
from django.urls import path
from my_app2 import views
urlpatterns = [
    path('', views.delta),
    path('add2/', views.add2),
    path('save2/', views.save2),
    path('delete2/<int:id>/', views.delete2),
    path('edit2/<int:id>/', views.edit2),
    path('update2/<int:id>/', views.update2),
]

    