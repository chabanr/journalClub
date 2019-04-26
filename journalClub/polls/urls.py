# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:29:04 2019

@author: rachaban
"""

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        ]