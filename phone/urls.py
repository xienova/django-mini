__author__ = 'xiechunhui'
__date__ = '2021/1/20 19:35'

from django.urls import path

from .views import PhoneListView, PhoneInputView, data_phone_input

app_name = 'phone'

urlpatterns = [
    path('phone_borrow/', PhoneListView.as_view(), name='phone_borrow'),
    path('phone_input/',PhoneInputView.as_view(), name = 'phone_input'),
    path('data_phone_input/', data_phone_input, name = 'data_phone_input')
]