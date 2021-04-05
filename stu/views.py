# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#渲染登陆页面
def index_view(request):
    return render(request, 'login.html')

#处理登陆功能
def login_view(request):
    #接受登陆参数
    uname = request.GET.get('uname', '')
    pwd = request.GET.get('pwd', '')

    #判断
    if uname == 'zhangsan' and pwd == '123':
        return HttpResponse('登陆成功！')

    return HttpResponse('登陆失败！')

