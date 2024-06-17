import random

# from django.http import HttpResponse
from django.shortcuts import render
import logging
from .models import Author, Article

logger = logging.getLogger(__name__)


# Create your views here.


def index(request):
    # logger.info('Main page was visited.')
    context = {'hello': 'Всем привет!', 'title': 'Main page'}
    return render(request, "hw_sem3_app/main.html", context=context)


def about(request):
    # logger.info('Main page was visited.')
    context = {'title': 'About me'}
    return render(request, "hw_sem3_app/about.html", context=context)


def games(request):
    context = {'title': 'games'}
    return render(request, "hw_sem3_app/shop_main.html", context=context)



dice_attempts = {}
dice_count = 0
def dice(request, attempts: int):
    _dice = [1, 2, 3, 4, 5, 6]
    global dice_count, dice_attempts
    try:
        for i in range(1, attempts + 1):
            res2 = random.choice(_dice)
            dice_count = i
            logger.debug(f'\n{dice.__name__.title()} successfully completed task. Result is equal to: {res2}.')
            dice_attempts[f'Попытка {dice_count}: '] = res2
        context = {'title': 'dice',
                    'game': 'игральные кости',
                    'attempts': dice_attempts}
        return render(request, "hw_sem3_app/games_play.html", context)
    except Exception as e:
        logger.exception(f'Error in about page: {e}')


coinflip_count = 0
coinflip_attempts = {}


def coinflip(request, attempts: int):
    _sides = ['орёл', 'решка']
    global coinflip_count, coinflip_attempts
    try:
        for j in range(1, attempts + 1):
            res1 = random.choice(_sides)
            coinflip_count = j
            logger.debug(f'\n{coinflip.__name__.title()} successfully completed task. Result is equal to: {res1}.')
            coinflip_attempts[f'Попытка {coinflip_count}: '] = res1
        context = {'title': 'coinflip',
                   'game': 'подбрасывание монетки',
                   'attempts': coinflip_attempts}
        return render(request, "hw_sem3_app/games_play.html", context)
    except Exception as e:
        logger.exception(f'Error in about page: {e}')


random_num_count = 0
random_num_attempts = {}


def random_num(request, attempts: int):
    _lst = [x for x in range(1, 101)]
    global random_num_count, random_num_attempts
    try:
        for k in range(1, attempts + 1):
            res3 = random.choice(_lst)
            random_num_count = k
            logger.debug(f'\n{random_num.__name__.title()} successfully completed task. Result is equal to: {res3}.')
            random_num_attempts[f'Попытка {random_num_count}: '] = res3
        context = {'title': 'random_num',
                   'game': 'выпадение случайного числа от 1 до 100',
                   'attempts': random_num_attempts}
        return render(request, "hw_sem3_app/games_play.html", context)
    except Exception as e:
        logger.exception(f'Error in about page: {e}')


def articles(request, id_author: int):
    author = Author.objects.filter(id=id_author).first()
    articles_ = Article.objects.filter(author=author)
    context = {'title': f'Статьи автора {author.full_name()}',
               'articles': articles_}
    return render(request, "hw_sem3_app/articles.html", context)
