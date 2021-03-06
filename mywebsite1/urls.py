"""mywebsite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookstore/', include('bookstore.urls')),
    url(r'^mystore/', include('mystore.urls')),
    url(r'^user/', include('user.urls')),
    # url(r'^userinfo/', include('userinfo.urls')),
    url(r'^$', views.homepage),
    url(r'^page1$', views.page1, name="page1"),
    url(r'^page2$', views.page2),
    url(r'page3', views.page3),
    url(r'year/(\d{4})', views.page_year),
    url(r'birthday/(\d{4})/(\d{1,2})/(\d{1,2})', views.birthday),
    url(r'person/(?P<name>\w+)/(?P<age>\d+)', views.person),
    url(r'(?P<n1>\d+)/add/(?P<n2>\d+)', views.add),
    url(r'(?P<n1>\d+)/sub/(?P<n2>\d+)', views.sub),
    url(r'^test_get', views.test_get),
    url(r'birthday1/', views.birthday1),
    url(r'^test1', views.test1),
    url(r'^search', views.search),
    url(r'^shebao', views.shebao),
    url(r'^page4', views.page1_template),
    url(r'^page5', views.page5_template),
    url(r'^page6', views.page6_template),
    url(r'^page7', views.page7_template),
    url(r'^page8', views.test_tag),
    url(r'^pages', views.pages),
    url(r'^person/(\w+)', views.person, name='person'),
    url(r'^info/(\w+)', views.info, name="info"),
]
