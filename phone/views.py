from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Phone   # 引入样机类
# Create your views here.


# class SearchView(View):
#     '''
#     查询有什么书
#     '''
#     def get(self,request):
#         pass


class PhoneListView(ListView):
    model = Phone   # 得到Phone表的所有内容，相当于执行 Phone.objects.all()
    context_object_name = "phones"  # 传入模板中的变量名称，若不写此名，默认为 object
    template_name = 'phone/phone_borrow.html'       # 使用的html文件