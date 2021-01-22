from django.db import models

from account.models import Dep
# Create your models here.


class Phone(models.Model):
    dep = models.ForeignKey(Dep, on_delete=models.SET_NULL, null=True)
    IMEI = models.CharField(max_length=150)  # IMEI号编码
    name = models.CharField(max_length=150, unique=True)  # 名称
    stage = models.CharField(max_length=128, default=000)

    def __str__(self):
        return self.display_name