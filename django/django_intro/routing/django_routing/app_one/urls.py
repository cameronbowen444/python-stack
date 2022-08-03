from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('one/', views.one),
    path('bears', views.one_method),
    path('bears/<int:my_val>', views.another_method),
    path('bears/<str:name>/poke', views.yet_another), 
    path('<int:id>/<str:color>', views.one_more),
]
