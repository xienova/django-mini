__author__ = 'xiechunhui'
__date__ = '2021/1/20 9:56'

from django.urls import path

from account.views import *                 # 导入同目录下的views.py

app_name = 'account'

urlpatterns = [
    path('dep_list/', dep_list, name='dep_list'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('home/', myphone, name = 'home'),
    path('register/', user_register, name = 'register'),
]


