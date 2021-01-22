from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Dep, User
from .forms import LoginForm


# Create your views here.

def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    if request.method == "GET":
        return redirect('account:login')  # 跳转到登录界面


def dep_list(request):
    # 取出所有小组名
    deps = Dep.objects.all()
    # 需要传递给模板 templates 的对象
    context = {'deps': deps}
    # render函数：载入模板，并返回context对象
    return render(request, 'account/account_list.html', context)


def user_login(request):
    '''
    登录
    :param request:
    :return:
    '''
    if request.method == "GET":
        # if request.session.get('is_login', None):  # 如果没有获取到is_login的值，则默认为None
        #     return redirect('account:login')  # 跳转到登录界面
        login_form = LoginForm()
        return render(request, 'account/login.html', locals())

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            name = login_form.cleaned_data['name']
            password = login_form.cleaned_data['password']
            user = User.objects.filter(name=name).first()   # 返回filter后的第一个
            if user and user.password == password:
                request.session['is_login'] = True
                request.session['name'] = user.display_name
                return redirect('account:home')
            else:
                message = '用户名或密码错误！'
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
        else:
            return HttpResponse("不合法")
        return render(request, 'account/login.html',locals())


def home(request):
    if request.method == "GET":
        if not request.session.get('is_login', None):
            messages.error(request, '请先登录！')
            return redirect('account:login')
        user_name = request.session['name']
        return render(request, 'account/home.html',locals())    # 定义的所有变量