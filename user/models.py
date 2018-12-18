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
    # 邀请人ID
    inviteId = models.IntegerField('邀请人ID', default=0)


class tb_resetpwd(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    # uid
    userId = models.IntegerField('用户ID', default=None)
    # onlyId 用于动态生成临时重置密码链接
    onlyId = models.CharField('唯一标识', max_length=255)
    # status 0: 正常 1：过期 2： 失效
    status = models.IntegerField('状态', default=0)


class tb_registry_code(models.Model):
    """
    邀请码
    """
    # ID
    id = models.AutoField(primary_key=True)
    # uid
    userId = models.IntegerField('邀请者ID', default=None)
    # code
    registry_code = models.IntegerField('用户ID', default=None)
    # status 0: 正常 1：失效
    status = models.IntegerField('状态', default=0)


class session(models.Model):
    # uid
    userId = models.IntegerField('userId', default=None)
    sessionId = models.CharField("sessionId", max_length=255, default=None)
    # 过期时间
    expire_date = models.DateTimeField(default=None)
