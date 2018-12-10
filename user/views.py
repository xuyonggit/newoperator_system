# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from user.models import tb_user
import hashlib

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
        print(issavecookies)
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


def Checkis(request):
    if request.method == 'POST':
        print(request.POST.get('typex', 1))
    pass


# md5
def to_md5(str):
    md = hashlib.md5()
    md.update(str.encode('utf-8'))
    return md.hexdigest()


if __name__ == '__main__':
    print(to_md5('1a'))
