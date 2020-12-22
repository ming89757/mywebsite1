from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    return HttpResponse('bookstore index')


def homepage(request):
    return render(request, 'index.html')


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
        # models.Book.objects.create(title='aaa',
        #                            pub='bbb')
    elif request.method == 'POST':
        t = request.POST.get('book_name', '')
        pub = request.POST.get('pub', '')
        price = request.POST.get('price', '')
        m_price = request.POST.get('market_price', '')
        # abook = models.Book.objects.create(
        #     title=t,
        #     pub=pub,
        #     price=price,
        #     market_price=m_price
        # )
        abook = models.Book(price=price)
        abook.title = t
        abook.pub = pub
        abook.market_price = m_price
        abook.save()
        return HttpResponse('success')


def test_f(request, up):
    books = models.Book.objects.all()
    for book in books:
        book.market_price += up
        book.save()
    return HttpResponse("" % up)


from django.core.paginator import Paginator
