import random

# from django.http import HttpResponse
from django.shortcuts import render
import logging
from .forms import RandomForm, AuthorForm, ArticleForm
from .models import Author, Article

logger = logging.getLogger(__name__)


# Create your views here.


# def index(request):
#     # logger.info('Main page was visited.')
#     context = {'hello': 'Всем привет!', 'title': 'Main page'}
#     return render(request, "hw_sem4_app/main.html", context=context)
#
#
# def about(request):
#     # logger.info('Main page was visited.')
#     context = {'title': 'About me'}
#     return render(request, "hw_sem4_app/about.html", context=context)


def games(request):
    context = {'title': 'games'}
    return render(request, "hw_sem4_app/shop_main.html", context=context)



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
        return render(request, "sem4_app/games_play.html", context)
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
        return render(request, "sem4_app//games_play.html", context)
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
        return render(request, "sem4_app/games_play.html", context)
    except Exception as e:
        logger.exception(f'Error in about page: {e}')


def perform_action(request):
    if request.method == 'POST':
        form = RandomForm(request.POST)
        if form.is_valid():
            event_type = form.cleaned_data['event_type']
            attempts = form.cleaned_data['attempts']
            if event_type == "coinflip":
                return coinflip(request, attempts)
            elif event_type == "dice":
                return dice(request, attempts)
            elif event_type == "random_num":
                return random_num(request, attempts)
            # logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = RandomForm()
    return render(request, 'sem4_app/games_form.html',
                  {'form': form})





def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            author = Author.objects.create(
                first_name=form_data['first_name'],
                last_name=form_data['last_name'],
                email=form_data['email'],
                bio=form_data['bio'],
                birthday=form_data['birthday']
            )
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {'authors': authors, 'form': form}
    return render(request, 'sem4_app/author.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            article = Article.objects.create(
                title=form_data['title'],
                text =form_data['text'],
                author=form_data['author'],
                category=form_data['category'],
                publication_date=form_data['publication_date'],
                is_published=form_data['is_published'],
                views=form_data['views'],
            )
    else:
        form = ArticleForm()
    context = {'title': 'Добавить статьи', 'form': form}
    return render(request, 'sem4_app/add_article.html', context)


def articles(request, id_author: int = None):
    if id_author:
        author = Author.objects.filter(id=id_author).first()
        articles_ = Article.objects.filter(author=author)
        title = f'Статьи автора {author.full_name()}'
    else:
        articles_ = Article.objects.all()
        title = f'Все статьи'
    context = {'title': title,
               'articles': articles_}
    return render(request, "sem4_app/articles.html", context)


