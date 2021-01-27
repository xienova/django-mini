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
    note = models.CharField(max_length=200, blank = True, null= True)  # 备注 可空
    is_display = models.BooleanField(default=True)  # 是否显示
    birthday = models.CharField(max_length=50)  # 创建日期
    is_borrow = models.BooleanField(default=False)  # 是否借出到同事手中；默认为否

    def __str__(self):
        return self.name + self.stage + self.num  # 返回样机名称阶段编号


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # 使用人
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, null=True)  # 样机
    borrow_date = models.DateTimeField(auto_now_add=True)  # 借出日期
    return_date = models.DateTimeField(auto_now=True)  # 归还日期
    test = models.CharField(max_length=200)  # 进行的测试
    is_normal = models.BooleanField()  # 是否正常
    note = models.CharField(max_length=200, blank=True, null=True)  # 有问题时需要填写备注


class Log(models.Model):
    '''
    日志表
    '''
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=30)

    class Meta:
        verbose_name = '日志'  # 自定义一个易于理解的名字
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[{}] {} {} {}'.format(self.time, self.user, self.action, self.phone)
