# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def index(request):
    contest = {}
    contest['index'] = '1'
    return render(request, 'index.html', contest)


def index_new_2(request):
    contest = {}
    contest['index_new_2'] = '1'
    return render(request, 'index_new_2.html', contest)


def index_new_3(request):
    contest = {}
    contest['index_new_3'] = '1'
    return render(request, 'index_new_3.html', contest)


def index_new_4(request):
    contest = {}
    contest['index_new_4'] = '1'
    return render(request, 'index_new_4.html', contest)


def guanli(request):
    contest = {}
    contest['guanli'] = '1'
    return render(request, 'guanli.html', contest)