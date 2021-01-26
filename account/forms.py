__author__ = 'xiechunhui'
__date__ = '2021/1/21 13:58'

# 引入表单类
from django import forms

# 在ModelForm中有插件名widgets，所以这里引入插件时要取别名，否则报错
from django.forms import widgets as Fwidgets

from .views import User

class LoginForm(forms.Form):
    name = forms.CharField(label="邮箱前缀", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("dep","name","display_name","email","is_hisense")
        labels = {
            'name': '邮箱前缀',
            'display_name':'姓名',
            'email': '邮箱',
            'dep': '小组',
            'is_hisense': '是否海信',
        }
        widgets = {
            'name': Fwidgets.TextInput(attrs={'class': 'form-control', }),
            'display_name': Fwidgets.TextInput(attrs={'class': 'form-control', }),
            'email': Fwidgets.EmailInput(attrs={'class': 'form-control', }),
            'dep': Fwidgets.Select(attrs={'class': 'form-control', }),
            'is_hisense': Fwidgets.CheckboxInput,

        }