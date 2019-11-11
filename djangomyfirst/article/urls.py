from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.index, name='index'),
    path('test/', views.test, name='test'),
]
