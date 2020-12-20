from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url('^login', views.mylogin),
    url(r'^reg$', views.myregister),
    url(r'logout', views.mylogout),
    url(r'reg_form', views.reg_form),
]
