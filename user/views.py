# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def Login(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        response_data = {'state': 2, 'info': '密码好像错咯'}
        return HttpResponse(json.dumps(response_data))
    else:
        return render_to_response("login.html")


def Checkis(request):
    if request.method == 'POST':
        print(request.POST.get('typex', 1))
    pass
