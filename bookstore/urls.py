from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^index', views.index),
    url(r'^add_book', views.add_book),
    url(r'test_f/(\d)', views.test_f),
]
