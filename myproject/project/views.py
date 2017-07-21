#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Get base directory from settings
from project import settings
import os

#Python libraries
import datetime as dt
import json

# Create your views here.
def index(request):
    path = os.path.join(settings.FRONT_DIR,'index.html')
    return render(request, path)
    
def index_2(request):
    path = os.path.join(settings.FRONT_DIR,'index-2.html')
    return render(request, path)
    
def fetchTime(request):
    t = dt.datetime.now().strftime("%I:%M:%S %d.%m.%Y")
    jsonStr = {
        'time': t
    }
    jsonStr = json.dumps(jsonStr)
    return HttpResponse(jsonStr)
    