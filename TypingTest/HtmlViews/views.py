'''
Created on Aug 2, 2019

@author: as404g
'''
from django.shortcuts import render

def htmlhello(request):
   return render(request, "index.html", {})