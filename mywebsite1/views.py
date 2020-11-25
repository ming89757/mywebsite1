from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


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
    html = '生日为：' + y + '年' + m + '月' + d + '日'
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
        year = request.GET.get('year', '0000')
        month = request.GET.get('month', '1')
        day = request.GET.get('day', '1')
        html = "生日是：%s年%s月%s日" % (year, month, day)
    return HttpResponse(html)


def test1(request):
    html = ''
    for k in request.GET:
        html += k + request.GET[k] + '  '
    return HttpResponse(html)


def search(request):
    html = """
    <!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form method="post" action="/search">
        <input name="sss" type="text">
        <input type="submit">
    </form>
</body>
</html>
    """
    if request.method == 'GET':
        return HttpResponse(html)
    elif request.method == 'POST':
        sss = request.POST['sss']
        return HttpResponse('正在POST提交 sss=' + sss)
    else:
        return HttpResponse('其他方式提交')


def shebao(request):
    html = """
    <!DOCTYPE html>
    <html lang="cn">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <form method="post" action="/shebao">
            <div>
                请输入基数<input type=input name="income">
            </div>
            <div>
                户口类型
                <select name="is_city">
                    <option value="1">城镇户口</option>
                    <option value="0">农村户口</option>
                </select>
            </div>
            <input type="submit">
        </form>
    """
    html_table = """
     <table>
        <thead>
            <tr>                
                <th>项目</th>
                <th>个人缴纳</th>
                <th>单位缴纳</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>养老保险</td>"""
    html_table_end = """</tr>
                </tbody>
            </table>"""
    html_end = """
                </body>
                </html>
                """
    if request.method == 'GET':
        return HttpResponse(html + html_end)
    elif request.method == 'POST':
        base = request.POST.get('income', '0')
        base = float(base)
        is_city = request.POST.get('is_city')
        html_table += '<td>%d元</td>' % (base * 0.08)
        html_table += '<td>%d元</td>' % (base * 0.12)
        return HttpResponse(html + html_table + html_table_end + html_end)


def page1_template(request):
    t = loader.get_template('page1.html')
    html = t.render()
    return HttpResponse(html)


def page5_template(request):
    return render(request, 'page1.html')


def page6_template(request):
    t = loader.get_template('page2.html')
    html = t.render({'name': '国老师',
                     'age': 18})
    return HttpResponse(html)


def page7_template(request):
    return render(request, 'page2.html', {'name': '国老师', 'age': 18})


def test_tag(request):
    dic = {
        'name': '老田',
        'has_car': False,
        'age': 35,
        'fav': ['乒乓球', '电影', '篮球', '写代码']
    }
    return render(request, 'page3.html', dic)
