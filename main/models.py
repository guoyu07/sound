# -*-coding:utf-8-*-
from django.db import models

# Create your models here.
##
# User表：用户信息
# Express表：表白信息保存
# Comments评论表：评论表
# Timeline表：历史
##

# 历史操作记录
TYPE = {
    0: u"浏览历史",
    1: u"收藏的",
    2: u"点赞的",
    3: u"分享的",
    4: u"回复的",
}


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
    mail = models.CharField(max_length=120, blank=True, verbose_name=u'登陆邮箱')   # 登陆邮箱
    password = models.CharField(max_length=50, verbose_name=u'密码')  # 40位sha1加密后的密码
    avatar = models.CharField(max_length=200, default='none', verbose_name=u'用户头像')
    change_password = models.CharField(max_length=10, blank=True, default='none')  # 修改密码时候的验证码
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    action_time = models.DateTimeField(auto_now_add=True)  # 用户最近一次登陆时间

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = u'用户信息'


class Express(models.Model):
    """
    用户发布的表白内容
    """
    user = models.ForeignKey(User)
    # 内容
    contain_text = models.CharField(blank=True, max_length=200, verbose_name=u'表白文字内容')
    contain_pic = models.CharField(blank=True, max_length=200, verbose_name=u'表白图片内容')
    contain_voice = models.CharField(blank=True, max_length=200, verbose_name=u'表白语音')

    like = models.IntegerField(default=0, verbose_name=u'点赞人数')
    collection = models.IntegerField(default=0, verbose_name=u'收藏人数')
    share = models.IntegerField(default=0, verbose_name=u'分享次数')
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        ordering = ['-like']
        verbose_name_plural = verbose_name = u'用户发布内容'


class Comments(models.Model):
    """
    用户发布的表白内容的评论
    """
    express = models.ForeignKey(Express)

    comments = models.CharField(default=u'什么都没有', max_length=500, verbose_name=u'评论内容')
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = u'用户发布内容'


class Timeline(models.Model):
    """
    历史事件时间线路
    """
    user = models.OneToOneField(User)
    express = models.ForeignKey(Express)

    type = models.IntegerField(choices=TYPE.items(), verbose_name=u'操作类型')

    class Meta:
        verbose_name_plural = verbose_name = u'用户操作记录'
