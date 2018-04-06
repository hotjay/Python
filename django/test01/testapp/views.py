from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import xlrd
import time
import cx_Oracle
import pymssql
import _mssql
import uuid
import decimal

import re
# Create your views here.

def qz(request):
    return  render(request,'wj.html')

def post1(request):
    import os
    os.system('python <F:\Python\msg\Excel.py>')
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))