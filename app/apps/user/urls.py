# -*- encoding: utf-8 -*-
"""
@author: eddie.wang
@contact: eddie.wang@infinigo.cn
@software: PyCharm
@file: urls.py
@time: 2021/11/30 16:13
"""

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
]