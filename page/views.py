# -*- coding: utf-8 -*-
import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from user.myFunctions import needLogin
from page.models import url_name
from django.views.decorators.csrf import csrf_exempt


def index(request):
    data = '头号玩家'
    return render(request, 'index_test.html', context={'data': data})


@csrf_exempt
def names(request):
    if request.method == 'POST':

        uname = request.POST.get('uname')
        links = request.POST.get('links')
        url_name.objects.create(
            username=uname,
            urls=links
        )
        return HttpResponse(json.dumps({"state": 0}))
    else:
        return render(request, 'index_test.html')

