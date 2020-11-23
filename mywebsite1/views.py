from django.http import HttpResponse


def page1(request):
    print('page1')
    return HttpResponse('this is page1')


def page2(request):
    html = """
    <html>
    <head><title>this is page2</title></head>
    <body>
        <h1>this is h1<h1>
        <h2 style="color:red;">this is red</h2>
    </body>
    </html>
    """
    return HttpResponse(html)


def page3(request):
    return HttpResponse('this is page3')


def homepage(request):
    return HttpResponse('this is homepage')


def page_year(request, y):
    html = "xxxx" + y
    return HttpResponse(html)


def birthday(request, y, m, d):
    html = '生日为：' + y + '年'+m+'月'+d+'日'
    return HttpResponse(html)


def person(request, name, age):
    html = '<h1>name: ' + name + '</h1>'
    html += '<h1>age: ' + age + '</h1>'
    return HttpResponse(html)


def add(request, n1, n2):
    res = int(n1) + int(n2)
    html = '<h1>result is : ' + str(res) + '</h1>'
    return HttpResponse(html)


def sub(request, n1, n2):
    res = int(n1) - int(n2)
    html = '<h1>result is : ' + str(res) + '</h1>'
    return HttpResponse(html)


def test_get(request):
    value_a = request.GET.get('a', 'none')
    return HttpResponse('request ok' + value_a)


def birthday1(request):
    if request.method == 'GET':
        year = request.GET.get('year','0000')
        month = request.GET.get('month','1')
        day = request.GET.get('day','1')
        html = "生日是：%s年%s月%s日"%(year,month,day)
    return HttpResponse(html)


def test1(request):
    html = ''
    for k in request.GET:
        html += k + request.GET[k] + '  '
    return HttpResponse(html)


