import random

from django.http import HttpResponse
from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world!")

def coinflip(request):
    _sides = ['averse','reverse']
    res1 = random.choice(_sides)
    try:
        logger.debug(f'\n{coinflip.__name__.title()} successfully completed task. Result is equal to: {res1}.')
        return HttpResponse(f'Your result is {res1}.')
    except Exception as e:
        logger.exception(f'Error in about page: {e}')

def dice(request):
    _dice = [1,2,3,4,5,6]
    res2 = random.choice(_dice)
    try:
        logger.debug(f'\n{dice.__name__.title()} successfully completed task. Result is equal to: {res2}.')
        return HttpResponse(f'Your result is {res2}.')
    except Exception as e:
        logger.exception(f'Error in about page: {e}')

def random_num(request):
    _lst = [x for x in range (1,101)]
    res3 = random.choice(_lst)
    try:
        logger.debug(f'\n{random_num.__name__.title()} successfully completed task. Result is equal to: {res3}.')
        return HttpResponse(f'Your result is {res3}.')
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
