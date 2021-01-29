__author__ = 'xiechunhui'
__date__ = '2021/1/20 19:35'

from django.urls import path

from .views import PhoneListView

app_name = 'phone'

urlpatterns = [
    path('phone_borrow', PhoneListView.as_view(), name='phone_borrow'),
]