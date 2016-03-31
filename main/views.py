# -*-coding:utf-8-*-
from django.shortcuts import render, render_to_response, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from main.models import User, Express, Comments, Timeline
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
        nickname = request.POST.get('userName', '')
        password = request.POST.get('userCode', '')
        avatar = request.POST.get('avatar', '')

        if nickname and password:
            try:
                user = User.objects.get(nickname=nickname)
                result = '1'
            except ObjectDoesNotExist:
                user = User(nickname=nickname, mail='nomail', password=password, create_time=time.time(),
                            action_time=time.time())
                user.save()
                result = '0'
        else:
            result = '2'
    else:
        result = '-1'

    response.write(result)
    response.write(fetch_recommend())  # 返回首页信息
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
    result = '3'

    if request.method == 'POST':
        # 获取客户端信息
        nickname = request.POST.get('userName', '')
        password = request.POST.get('password', '')
        if nickname and password:
            try:
                # 用户存在
                user = User.objects.get(nickname=nickname)
                if user.password == password:
                    # 用户密码正确
                    result = '0'
                else:
                    result = '-1'
            except ObjectDoesNotExist:
                result = '-1'
    response.write(result)
    response.write(fetch_recommend())
    return response


@csrf_exempt
def cg_password(requset):
    """
    修改密码
    :param requset:
    :return:
    """
    # 需要配置邮件服务器，这个先不做


@csrf_exempt
def test(request):
    """
    测试api
    :param request:
    :return:
    """
    response = HttpResponse()

    response['Content-Type'] = 'text/javascript'
    if request.method == 'POST':
        req = json.loads(request.body)
        if req.get("success", ""):
            response.write('success in POST:'+req.get("success"))
        else:
            response.write(str(request.body)+'fetch')
    return response


@csrf_exempt
def depatch(request):
    """
    路由分发函数
    :param request:json数据中含有操作类型
    :return:
    """

    if request.method == 'GET':
        type = request.GET.get('type', '')
    else:
        type = request.POST.get('type', '')

    if type == 'register':
        return register(request)
    elif type == 'login':
        return login(request)
    else:
        response = HttpResponse()
        response['Content-Type'] = 'application/json'
        response.write('-1')
        return response


def fetch_recommend():
    """

    :return:返回首页显示的json数据
    """
    # 构造成json数据
    show_list = []
    try:
        show = Express.objects.all()[0: 10]  # 默认按照点赞人数排行
        for show_item in show:
            show_list.append({
                "nickname": show_item.user.nickname,  # 名字
                "avatar": show_item.user.avatar,  # 头像
                "text": show_item.contain_text,  # 发表的文字内容
                "picture": show_item.contain_pic,  # 发表的图片信息，暂时只能一张图片
                "voice": show_item.contain_voice,  # 发表的语音
                "like": show_item.like,  # 点赞人数
                "collection": show_item.collection,
                "share": show_item.share,
                "create_time": show_item.create_time
                # TODO:评论内容点进去再加载
            })
    except ObjectDoesNotExist:
        pass

    json_dict = json.dumps(show_list)
    return json_dict









