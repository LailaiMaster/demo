import os

from steamSpider import scrapyPriceTimes
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from steamSpider.c5Spider import test123

from steamSpider.models import C5ItemModel


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        print("=====POST=====")
        list = scrapyPriceTimes.scrape()
        return render(request, 'index.html', {'dicts': list})
