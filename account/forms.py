__author__ = 'xiechunhui'
__date__ = '2021/1/21 13:58'

# 引入表单类
from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label="邮箱前缀", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
