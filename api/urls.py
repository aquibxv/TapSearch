from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name='search'),
    path('clear', views.clear, name='clear'),
    path('index', views.index, name='index'),
]