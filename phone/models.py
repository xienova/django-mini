from django.db import models

from account.models import User


# Create your models here.


class PhoneDep(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    dep = models.ForeignKey(PhoneDep, on_delete=models.SET_NULL, null=True)  # 样机所属小组
    creater = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # 创建人
    IMEI = models.CharField(max_length=150)  # IMEI号编码
    name = models.CharField(max_length=150)  # 名称
    stage = models.CharField(max_length=128, default=000)  # 样机阶段
    num = models.CharField(max_length=150)  # 样机编号
    note = models.CharField(max_length=200)  # 备注
    display = models.BooleanField(default=True)  # 是否显示
    birthday = models.CharField(max_length=50)  # 创建日期

    def __str__(self):
        return self.display_name
