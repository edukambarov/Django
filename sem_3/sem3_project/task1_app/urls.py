from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('games/', views.games, name='games'),
    path('coinflip/<int:attempts>', views.coinflip, name='coinflip'),
    path('dice/<int:attempts>', views.dice, name='dice'),
    path('random_num/<int:attempts>', views.random_num, name='random_num'),
    path('articles/<int:id_author>', views.articles, name='articles'),
]
