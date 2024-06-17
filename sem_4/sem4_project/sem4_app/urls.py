from django.urls import path, include
from . import views

urlpatterns = [
    path('coinflip/<int:attempts>', views.coinflip, name='coinflip'),
    path('dice/<int:attempts>', views.dice, name='dice'),
    path('random_num/<int:attempts>', views.random_num, name='random_num'),
    path('games/', views.perform_action, name='form'),
    path('author/', views.add_author, name='author'),
    path('article/', views.add_article, name='article'),
    path('articles/', views.articles, name='articles'),
]
