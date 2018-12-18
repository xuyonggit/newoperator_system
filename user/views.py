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
        userdata = tb_user.objects.filter(username=username).get()
        # 初始化返回数据
        response_data = {'state': 0, 'info': 'success'}
        # 密码比对
        if res_passwd != userdata.passwd:
            response_data = {'state': 2, 'info': '密码好像错咯'}
        else:
            # 密码正确
            # 检测账号是否可用
            if userdata.status == 0 and userdata.id != 1:
                response_data = {'state': 3, 'info': '账号被禁用，请联系系统管理员'}
            else:
                sessionId = create_sessionId(userid=userdata.id)
                # request.session["sessionId"] = username
                # request.session.set_expiry(0)   # session 过期时间 0 : 关闭浏览器即失效
                # request.session['is_login'] = True
                response_data['sessionId'] = sessionId
                print("login success, userid: {}, sessionId: {}".format(userdata.id, response_data['sessionId']))
        return HttpResponse(json.dumps(response_data))
    else:
        return render_to_response("login.html")


@csrf_exempt
def Logout(request):
    # request.session.clear()
    try:
        sessionid = request.META['HTTP_SESSIONID']
    except:
        sessionid = request.COOKIES['sessionId'].replace("%3D", '=')
        clearSessionId(sessionid)
    return HttpResponseRedirect("/user/login/")


@csrf_exempt
def Registry(request):
    pass
    return render_to_response("registry.html")


@csrf_exempt
def Checkis(request):
    """

    :param request:
    :typex  5 - 重置密码 2 - 检查是否登录
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
        elif int(typex) == 1:
            if not request.session.get('is_login', False):
                return HttpResponse("NotLogin")
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


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('form-username')
        passwd = request.POST.get('form-password')
        passwd = to_md5(passwd)
        code = request.POST.get('form-code')
        useremail = request.POST.get('form-email')
        position = request.POST.get('form-position', None)
        # templates
        # 无效参数
        template_success = {'state': 0, 'info': '用户创建成功'}
        template_invalid = {'state': 1, 'info': '无效参数'}
        template_Exists = {'state': 2, 'info': '用户已存在'}
        template_incalidcode = {'state': 3, 'info': '邀请码无效'}
        template_error = {'state': 4, 'info': '未知错误'}

        if not username or \
            not passwd or \
            not useremail:
            return HttpResponse(json.dumps(template_invalid))
        # 判断用户是否存在
        if userExists(useremail):
            return HttpResponse(json.dumps(template_Exists))
        # 检查邀请码
        if checkRegistryCode(code):
            # 创建用户
            createUser(username=username, passwd=passwd, email_address=useremail, inviteId=code, position=position)
            # 失效邀请码
            invialdRegistryCode(code)
        else:
            return HttpResponse(json.dumps(template_incalidcode))
        return HttpResponse(json.dumps(template_success))


@csrf_exempt
@needLogin
def getUserInfo(request, uid):
    if request.method == 'POST':
        uid = uid
        try:
            sessionid = request.META['HTTP_SESSIONID']
        except:
            sessionid = request.COOKIES['sessionId'].replace("%3D", '=')

        #uid = getUserIdFromSessionId(sessionid)
        if uid:
            response_data = make_UserInfo(uid=uid)
            if response_data:
                return HttpResponse(json.dumps(response_data, cls=CJsonEncoder))
            else:
                return HttpResponse("Error")

@csrf_exempt
@needLogin
def updateUserInfo(request):
    if request.method == 'POST':
        try:
            sessionid = request.META['HTTP_SESSIONID']
        except:
            sessionid = request.COOKIES['sessionId'].replace("%3D", '=')
        response_data = {"state": 0, "info": "用户修改成功"}
        # old info data
        uid = getUserIdFromSessionId(sessionid)
        oldInfo = make_UserInfo(uid)
        # form
        username = request.POST.get('username', oldInfo['username'])
        sex = request.POST.get('sex', oldInfo['sex'])
        age = request.POST.get('age', oldInfo['age'])
        email_address = request.POST.get('email_address', oldInfo['email_address'])
        position = request.POST.get('position', oldInfo['position'])
        # update
        update_UserInfo(uid=uid, username=username, sex=sex, age=age, email_address=email_address, position=position)
        return HttpResponse(json.dumps(response_data))
