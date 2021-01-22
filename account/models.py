from django.db import models


# Create your models here.


class Dep(models.Model):
    name = models.CharField(max_length=20, unique=True)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        return self.name

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name


class User(models.Model):
    dep = models.ForeignKey(Dep, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150, unique=True)  # 拼音
    display_name = models.CharField(max_length=150, unique=True)  # 汉字
    password = models.CharField(max_length=128, default=000)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)  # 是否仍在海信
    is_hisense = models.BooleanField()  # 是否是海信员工

    def __str__(self):
        return self.display_name