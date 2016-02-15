# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


class User(models.Model):
    """
    用户验证信息：
    nickname:名称
    mail:邮箱
    password:账号
    change_password:修改密码的验证码
    create_time:创建时间
    """
    nickname = models.CharField(max_length=50, verbose_name=u'昵称')  # 名字
    mail = models.CharField(max_length=120, verbose_name=u'登陆邮箱')   # 登陆邮箱
    password = models.CharField(max_length=50, verbose_name=u'密码')  # 40位sha1加密后的密码
    change_password = models.CharField(max_length=10, blank=True, default='none')  # 修改密码时候的验证码
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    action_time = models.DateTimeField(auto_now_add=True)  # 用户最近一次登陆时间

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = u'用户验证信息'


class Info(models.Model):
    """
    用户相关信息保存,
    """
    user = models.ForeignKey(User)

