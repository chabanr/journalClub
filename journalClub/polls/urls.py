# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:29:04 2019

@author: rachaban
"""

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
        # examples: /polls/
        path('', views.index, name='index'),
        # examples /polls/5/
        path('<int:question_id>/', views.detail, name='detail'),
        # examples /polls/5/results/
        path('<int:question_id>/results/', views.results, name='results'),
        # examples: /polls/5/vote
        path('<int:question_id>/vote/', views.vote, name='vote'),
        ]
