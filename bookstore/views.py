from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('bookstore index')


def add_book(request):
    if request.method == 'GET':
        from . import models
        models.Book.objects.create(title='aaa',
                                   pub='bbb')
        return HttpResponse('ok')

