# _*_ coding:utf-8 _*_

__author__ = "zhy"
__date__ = "2018/4/28 11:41"

from celery_email.celery import app

@app.task
def hello_world():
    print("Hello, World")



