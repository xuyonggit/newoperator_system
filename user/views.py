# -*- coding: utf-8 -*-
import uuid

from django.shortcuts import render, render_to_response, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from user.user_email import SendMultiEmail
from user.myFunctions import *


@csrf_exempt
def Login(request):
    """
    登录模块
    :param request:
    :errcode    2 ： 密码好像错咯
                3 ：账号被禁用，请联系系统管理员
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('userpwd')
        issavecookies = request.POST.get('issavecookies')
        # 密码加密
        res_passwd = to_md5(passwd)
        # get data from database
        userdata = tb_user.objects.get(username=username)
        # 初始化返回数据
        response_data = {'state': 0, 'info': 'success'}
        # 密码比对
        if res_passwd != userdata.passwd:
            response_data = {'state': 2, 'info': '密码好像错咯'}
        else:
            # 密码正确
            # 检测账号是否可用
            if userdata.status == 1:
                response_data = {'state': 3, 'info': '账号被禁用，请联系系统管理员'}
            else:
                print("login success, userid: {}".format(userdata.id))
        return HttpResponse(json.dumps(response_data))
    else:
        return render_to_response("login.html")


@csrf_exempt
def Checkis(request):
    """

    :param request:
    :typex  5 - 重置密码
    :return:
        错误码：
        state:  0: 邮件已发送
                1:邮箱地址重复
                2:邮箱地址错误
                1000:未知错误
    """
    if request.method == 'POST':
        typex = request.POST.get('typex')
        response_data = {"state": 0}
        # typex 5 重置密码
        if int(typex) == 5:
            usermail = request.POST.get("usermail")
            database_data = tb_user.objects.filter(email_address=usermail)
            if len(database_data) == 1:
                onlyid = makeResetLink(email_address=usermail)
                if onlyid:
                    link = "http://{0}/user/reset_password/{1}".format(request.get_host(), onlyid)
                SendMultiEmail('重置密码', tolist=[usermail], template='Email.html', link=link, user=usermail)
                response_data['info'] = "邮件已发送"
            elif len(database_data) > 1:
                response_data['state'] = 1
                response_data['info'] = "邮箱地址重复"
            else:
                response_data['state'] = 2
                response_data['info'] = "邮箱地址错误"
        else:
            response_data['state'] = 1000
            response_data['info'] = "未知错误"
        return HttpResponse(json.dumps(response_data))


@csrf_exempt
def ResetPassword(request, onlyid=''):
    oid = onlyid
    response_data = {"state": 0}

    d = tb_resetpwd.objects.filter(onlyId=oid, status=0).values()
    if len(d) > 0:
        userdata = tb_user.objects.get(id=d[0]['userId'])
        userdata.passwd = 'e10adc3949ba59abbe56e057f20f883e'
        userdata.save()
        # 失效重置ID
        outUseOnlyId(onlyid)
    else:
        raise Http404("哎呀~~~ 页面走丢啦！")

    return render(request, 'passwdResetResult.html', {'state': response_data['state'], 'info': response_data.get('info')})
