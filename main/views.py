# -*-coding:utf-8-*-
from django.shortcuts import render, render_to_response, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from main.models import User, Info
import time
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
token = 'salt'


@csrf_exempt
def register(request):
    """
    注册处理事件
    :param request:注册请求
    :return:
        ①result: '0'表示成功， '1'表示用户名重名， '2'表示未知错误,可能昵称/邮箱/密码为空，可能传输出错
        ②
    """
    # 回复
    response = HttpResponse()
    response['Content-Type'] = 'application/json'

    if request.method == 'POST':
        # 获取客户端信息
        nickname = request.POST.get('nickname', '')
        mail = request.POST.get('mail', '')
        password = request.POST.get('password', '')
        if nickname and mail and password:
            try:
                user = User.objects.get(nickname=nickname)
                result = '1'
            except ObjectDoesNotExist:
                user = User(nickname=nickname, mail=mail, password=password+'salt', create_time=time.time(),
                            action_time=time.time())
                user.save()
                result = '0'
        else:
            result = '2'
    else:
        result = '2'

    response.write(result)
    return response


@csrf_exempt
def login(request):
    """
    用户登陆事件
    :param request:登陆请求
    :return:
        ①result: 返回码， '0'表示成功 '1'表示用户不存在 '2'表示用户密码错误 '3'表示未知错误
        ②info:dict数据，登陆成功返回的用户信息就保存在这个json里面了
    """
    response = HttpResponse()
    response['Content-Type'] = 'application/json'
    info_data = {}
    result = '3'

    if request.method == 'POST':
        # 获取客户端信息
        mail = request.POST.get('mail', '')
        password = request.POST.get('password', '')
        if mail and password:
            try:
                # 用户存在
                user = User.objects.get(mail=mail)
                if user.password == password:
                    # 用户密码正确
                    info_data['base_info'] = {'name': user.nickname,
                                              'action_time': user.action_time}
                    result = '0'
                else:
                    result = '2'
            except ObjectDoesNotExist:
                result = '1'
    info = json.dumps(info_data)
    response.write(info)
    response.write(result)
    return response


@csrf_exempt
def cg_password(requset):
    """
    修改密码
    :param requset:
    :return:
    """
    # 需要配置邮件服务器，这个先不做



