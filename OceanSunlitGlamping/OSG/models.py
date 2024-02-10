from django.db import models


class Admin(models.Model):
    """管理員表"""
    username = models.CharField(verbose_name='帳號', max_length=32)
    password = models.CharField(verbose_name='密碼', max_length=64)


class UserInfo(models.Model):
    """員工表"""
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密碼', max_length=64)
    age = models.IntegerField(verbose_name='年齡')
    salary = models.DecimalField(verbose_name='薪資', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入職時間', auto_now_add=True)

# TODO:  會員表
