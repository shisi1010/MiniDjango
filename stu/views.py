# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# 渲染登陆页面
from stu.models import Student


# Create your views here.


def index_view(request):
    return render(request, 'login.html')


# 处理登陆功能
def login_view(request):
    # 接受登陆参数
    uname = request.POST.get('uname', '')
    pwd = request.POST.get('pwd', '')

    # 判断
    if uname == 'zhangsan' and pwd == '123':
        return HttpResponse('登陆成功！')

    return HttpResponse('登陆失败！')


def register_view(request):
    # 处理不同请求
    r_method = request.method
    if r_method == 'GET':
        return render(request, 'register.html')
    elif r_method == 'POST':
        # 1.获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        # 2.非空判断
        if uname and pwd:
            # 3.创建模型对象
            stu = Student(sname=uname, spwd=pwd)
            # 4.插入数据库
            stu.save()
            # 5.页面响应
            return HttpResponse('注册成功！')

    return HttpResponse('注册失败！')


def show_view(request):
    # 1.查询stu_student表中的所有数据
    stus = Student.objects.all()

    return render(request, 'showdate.html', {'students': stus})
