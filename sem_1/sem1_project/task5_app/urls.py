from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coinflip/', views.coinflip, name='coinflip'),
    path('dice/', views.dice, name='dice'),
    path('random_num/',views.random_num, name='random_num'),
]