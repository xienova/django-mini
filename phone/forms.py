from django import forms

from phone.models import Phone, PhoneDep


class SearchForm(forms.Form):
    IMEI = forms.CharField(label="IMEI号",
                           required=False
                           )  # IMEI号编码
    name = forms.CharField(label="样机名称",
                           required=False,
                           )
    stage = forms.CharField(label="样机阶段",
                            required=False
                            )  # 样机阶段
    num = forms.CharField(label="样机编号",
                          required=False
                          )  # 样机编号
    is_borrow = forms.ChoiceField(label="样机状态",
                                  required=False,
                                  choices=((0, "在库"), (1, "借出"), (2, "")),
                                  widget=forms.widgets.Select(),
                                  initial=2
                                  )
    note = forms.CharField(label="备注",
                           required=False)
    phone_dep = forms.ModelChoiceField(label="所在小组",
                                       required=False,
                                       queryset=PhoneDep.objects.all().distinct()
                                       )  # 是否借出到同事手中；默认为否
