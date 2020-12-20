from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test_cookie(request):
    resp = HttpResponse("OK")
    resp.set_cookie('myschool','hahaha')
    return resp


def show_cookie(request):
    dic = request.COOKIES
    return HttpResponse(str(dic))

