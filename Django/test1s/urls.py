'''定义test1s的URL模式'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]