from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'test_cookie', views.test_cookie),
    url(r'show_cookie', views.show_cookie),

]