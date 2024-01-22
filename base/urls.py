"""
app

"""
from django.contrib import admin
from django.urls import path

from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home', views.home),
    path('home/<int:id>',views.home),
    path('about', views.about),
    path('contact', views.contact),
]
