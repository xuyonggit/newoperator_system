# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def index(request):
    contest = {}
    contest['index'] = '1'
    return render(request, 'index_new.html', contest)
