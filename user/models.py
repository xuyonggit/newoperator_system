from django.db import models
from datetime import datetime, date


# Create your models here.
class tb_user(models.Model):
    id = models.AutoField(primary_key=True)     # ID
    username = models.CharField('用户名', max_length=255, default=None)
    # 密码 默认：123456
    passwd = models.CharField('密码', max_length=255, default='e10adc3949ba59abbe56e057f20f883e')
    # 邮箱
    email_address = models.CharField('邮箱地址', max_length=255, default=None)
    # 职位
    position = models.CharField('职位', max_length=255, default=None)
    # 创建日期，默认now
    create_date = models.DateField(auto_now_add=True)
    # 最新修改日期，默认now
    modify_date = models.DateField(auto_now=True)
    # 用户状态 0 为禁用，1 为正常
    status = models.IntegerField(default=0)
