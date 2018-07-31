# coding=utf-8
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include
from django.urls import path


urlpatterns = [
    path('', include('dj_sponsoring.urls', namespace='dj_sponsoring')),
]
