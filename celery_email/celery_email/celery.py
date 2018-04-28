# _*_ coding:utf-8 _*_

from __future__ import absolute_import
import os
import django

from celery import Celery
from django.conf import  settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_email.settings")
# django.setup()

app = Celery('celery_email')

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)



