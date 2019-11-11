from django.shortcuts import render
from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("<h3>Hello world<h3>")

def test(request):
    return HttpResponse("<h3>Programm working<h3>")

def index(request):
    # return HttpResponse("HELLO WORLD")
    return render(request, 'article/list.html')
# Create your views here.
