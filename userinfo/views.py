from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import models, forms

# Create your views here.


def mylogin(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'userinfo/login.html', locals())
    elif request.method == 'POST':
        remember = request.POST.get('remember', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            user = models.User.objects.get(name=username, password=password)
            request.session['userinfo'] = {
                'username': user.name,
                'id': user.id
            }
        except:
            return HttpResponse("Failed")
        resp = HttpResponseRedirect('/userinfo')
        if remember:
            resp.set_cookie('username', username, max_age=7 * 24 * 60 * 60)
        else:
            resp.delete_cookie('username')
        return resp


def myregister(request):
    if request.method == 'GET':
        return render(request, 'userinfo/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if username == '':
            username_error = '用户名不能为空'
            return render(request, 'userinfo/register.html', locals())
        if password == '':
            return HttpResponse("")
        if password != password2:
            return HttpResponse("")

        try:
            from . import models
            user = models.User.objects.create(name=username, password=password)
            return HttpResponseRedirect('/userinfo')
        except:
            return HttpResponseRedirect('/userinfo/reg')


def mylogout(request):
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect('/userinfo')


def homepage(request):
    return render(request, 'userinfo/homepage.html', locals())


def reg_form(request):
    if request.method == 'GET':
        myform = forms.RegForm()
        return render(request, 'userinfo/reg_form.html', locals())
