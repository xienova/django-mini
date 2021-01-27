__author__ = 'xiechunhui'
__date__ = '2021/1/20 9:56'

from django.urls import path

from . import views                 # 导入同目录下的views.py

app_name = 'account'

urlpatterns = [
    path('dep_list', views.dep_list, name='dep_list'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.user_logout, name = 'logout'),
    path('home', views.home, name = 'home'),
    path('register', views.user_register, name = 'register'),
]


