# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

def Login(request):
    return render_to_response("login.html")
