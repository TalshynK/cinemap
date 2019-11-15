from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from article.models import *
from django.utils import timezone
# def index(request):
#     return HttpResponse("<h3>Hello world<h3>")

def test(request):
    return HttpResponse("<h3>Programm working<h3>")

def index(request):
    latest_movies = Block.objects.order_by('-article_date')
    return render(request, 'article/list.html',{'latest_movies':latest_movies})

def table(request):
    return render(request, 'article/scheduleoffilms.html')
# Create your views here.
