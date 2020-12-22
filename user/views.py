from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import models, login, authenticate, logout
# Create your views here.


def mylogin2(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            user = models.User.objects.get(username=username, is_active=True)
            if user.check_password(password):
                login(request, user)
                return HttpResponse('success')
            else:
                return HttpResponse('password error')
        except:
            return HttpResponse('no user')
