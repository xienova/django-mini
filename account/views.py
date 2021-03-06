from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

from account.models import Dep, User
from phone.models import Log    # 日志
from account.forms import LoginForm, RegisterForm


# Create your views here.

def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    if request.method == "GET":
        # return redirect(reverse('account:login'))  # 跳转到登录界面
        return render(request,'base_adminlte2.html')


def dep_list(request):
    # 取出所有小组名
    deps = Dep.objects.all()
    # 需要传递给模板 templates 的对象
    context = {'deps': deps}
    # render函数：载入模板，并返回context对象
    return render(request, 'account/account_list_bootstrap3.html', context)


def user_login(request):
    '''
    登录
    :param request:
    :return:
    '''
    if request.method == "GET":
        if request.session.get('is_login'):  # 如果is_login存在，说明已经登陆，直接跳转到主页
            return redirect(reverse('account:home'))
        login_form = LoginForm()
        return render(request, 'account/login_bootstrap3.html', locals())

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            name = login_form.cleaned_data['name']
            password = login_form.cleaned_data['password']
            user = User.objects.filter(name=name).first()  # 返回filter后的第一个
            if user and user.password == password:
                request.session['is_login'] = True
                request.session['id'] = user.id   # id 展示的是ID，主键
                request.session['display_name'] = user.display_name
                Log.objects.create(user_id = user.id, action='登录')
                return redirect(reverse('account:home'))
            else:
                message = '用户名或密码错误！'
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
        else:
            return HttpResponse("不合法")
        return render(request, 'account/login_bootstrap3.html', locals())


def user_logout(request):
    '''
    用户登出
    :param request:
    :return:
    '''
    if request.method == "GET":
        if request.session.get('is_login'):
            Log.objects.create(user_id = request.session['id'], action= '登出' )
            request.session.flush()
            messages.success(request, '登出成功！')
        return redirect(reverse('account:login'))


def user_register(request):
    '''
    注册
    :param request:
    :return:
    '''
    if request.method == "GET":
        register_form = RegisterForm()
        return render(request, 'account/register_bootstrap3.html', locals())

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = '请检查填写的内容！'
        if register_form.is_valid():
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 == password2:
                new_user = register_form.save(commit=False)
                new_user.password = password1
                new_user.save()
                return redirect(reverse("account:login"))
            else:
                message = "两次输入的密码不一致"
        return render(request, 'account/register_bootstrap3.html', locals())  # 当提交数据出错时，使用


def myphone(request):
    '''
    登录后首先展示的页面，我的样机
    :param request:
    :return:
    '''
    if request.method == "GET":
        if not request.session.get('is_login', None):
            messages.error(request, '请先登录！')
            return redirect(reverse('account:login'))
        user_name = request.session['display_name'] # 展示的中文名字
        return render(request, 'account/account_myphone.html', locals())  # 定义的所有变量
