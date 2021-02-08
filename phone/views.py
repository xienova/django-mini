from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse,HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from django.forms.models import model_to_dict

from phone.models import Phone  # 引入样机类
from phone.forms import SearchForm


# Create your views here.


# class SearchView(View):
#     '''
#     查询有什么书
#     '''
#     def get(self,request):
#         pass


class PhoneListView(View):
    '''
    # model = Phone   # 得到Phone表的所有内容，相当于执行 Phone.objects.all()
    # context_object_name = "phones"  # 传入模板中的变量名称，若不写此名，默认为 object
    # template_name = 'phone/phone_borrow.html'       # 使用的html文件
    '''
    def get(self, request):
        search_form = SearchForm()
        phones = Phone.objects.all()
        return render(request, "phone/phone_borrow.html", {"phones": phones, "form": search_form})

    def post(self, request):
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_data = search_form.cleaned_data
            IMEI = search_data['IMEI']
            name = search_data['name']  # 获得的是一个phone对象
            stage = search_data['stage']
            num = search_data['num']
            is_borrow = search_data['is_borrow']
            phone_dep = search_data['phone_dep']    # 获得的是一个phonedep对象

            phones = Phone.objects.all()
            if IMEI != "":
                phones = phones.filter(IMEI__icontains = IMEI)
            if name != "":
                phones = phones.filter(name__icontains = name)
            if stage != "":
                phones = phones.filter(stage__icontains = stage)
            if num != "":
                phones = phones.filter(num__icontains = num)
            if is_borrow != '2':    # 为2的时候没有选择；
                phones = phones.filter(is_borrow = is_borrow)
            if phone_dep != None:
                phones = phones.filter(phone_dep = phone_dep)

            return render(request, "phone/phone_borrow.html", {"phones": phones,"form":search_form})
        else:
            print(search_form.errors)


class PhoneInputView(View):
    '''

    '''
    def get(self, request):
        return render(request, "phone/phone_input.html")


def data_phone_input(request):
    '''
    尝试JSON数据
    '''
    if request.method == 'GET':
        phones = Phone.objects.all().values_list()
        return JsonResponse(list(phones),safe=False)
