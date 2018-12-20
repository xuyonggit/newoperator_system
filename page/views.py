# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from user.myFunctions import needLogin
from page.models import url_name
from django.views.decorators.csrf import csrf_exempt
import json
from user.myFunctions import getUserIdFromSessionId


@csrf_exempt
@needLogin
def index(request):
    #try:
    #    sessionid = request.META['HTTP_SESSIONID']
    #except:
    #    sessionid = request.COOKIES['sessionId'].replace("%3D", '=')
    #uid = getUserIdFromSessionId(sessionid)
    # data = '头号玩家'
    data = url_name.objects.filter()
    response_data = data.values()
    return render(request, 'index.html', context={'data': response_data, 'userid': 3})


@csrf_exempt
def names(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        links = request.POST.get('links')
        userdata = url_name.objects.filter(username=uname)
        print(len(userdata.values()))
        if len(userdata.values()) == 0:
            url_name.objects.create(
                username=uname,
                urls=links
            )
            response_data = {'state': 0, 'info': '保存成功'}
        else:
            response_data = {'state': 1, 'info': '保存失败'}
        return HttpResponse(json.dumps(response_data))

    else:
        return render(request, 'index.html')

