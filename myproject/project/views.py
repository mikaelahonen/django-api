#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from project.serializers import UserSerializer, GroupSerializer

#Get base directory from settings
from project import settings
import os

#Python libraries
import datetime as dt
import json

# Create your views here.
def index(request):
    x = 'Hello world!'
    return HttpResponse(x)
	
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    