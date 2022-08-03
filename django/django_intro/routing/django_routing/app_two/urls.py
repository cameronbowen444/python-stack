from django.urls import path 
from . import views

urlpatterns = [
    path('', views.next),
    path('second/', views.second),
]