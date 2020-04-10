from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app_searcher', views.app_searcher, name='searcher'),
    path('keyword_finder', views.keyword_finder, name='finder'),
]