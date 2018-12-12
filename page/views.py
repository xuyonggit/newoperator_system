# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from user.myFunctions import needLogin


@needLogin
def index(request):
    contest = {}
    contest['index'] = '1'
    return render(request, 'index.html', contest)
