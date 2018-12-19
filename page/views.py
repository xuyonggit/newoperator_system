# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from user.myFunctions import needLogin
from page.models import url_name
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
@needLogin
def index(request):
    # data = '头号玩家'
    data = url_name.objects.filter()
    # print(data.values())
    for i in data.values():
        print(i)
    return render(request, 'index.html', context={'data': data.values()})


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
