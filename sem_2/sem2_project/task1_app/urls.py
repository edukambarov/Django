from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coinflip/', views.coinflip, name='coinflip')
]