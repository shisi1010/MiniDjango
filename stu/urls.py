#coding=utf-8

from django.conf.urls import url

import views

urlpatterns=[
    url('^$', views.index_view),
    url('^login/', views.login_view),
    url('^register/', views.register_view),
]