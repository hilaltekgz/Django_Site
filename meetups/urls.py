# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:08:43 2023

@author: hilal
"""
from django.urls import path

from . import views

urlpatterns = [
    
    path('meetups',views.index) #domain/meetups
    
    ]
