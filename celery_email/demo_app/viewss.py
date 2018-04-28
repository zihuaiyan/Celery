# _*_ coding:utf-8 _*_

__author__ = "zhy"
__date__ = "2018/4/28 14:55"

from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from .tasks import hello_world

def index(request):
    hello_world.delay()
    return HttpResponse(u"what Fuck!!")

