import random

from django.http import HttpResponse
from django.shortcuts import render

from .models import CoinFlip


def index(request):
    return HttpResponse("Hello, world!")


# def coinflip(request):
#     result = random.choice(['H','T'])
#     flip = CoinFlip.objects.create(result=result)
#     return render(request, 'coinflip.html', {'flip': flip})


# def coinflip(request):
#     flips = CoinFlip.objects.all()
#     return render(request, 'coinflip.html', {'flips': flips})

def coinflip(request):
    flip = CoinFlip.get_last_n_flips_stats(3)
    return render(request, 'coinflip.html', {'flip': flip})