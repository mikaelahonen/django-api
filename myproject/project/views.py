#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

#Rest framework and jwt
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework_jwt.settings import api_settings

#Project
from project.serializers import UserSerializer, GroupSerializer
from project import settings

#Others
import os
import datetime as dt
import json
from pprint import pprint

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
	
	@list_route(methods=['get'])
	def current(self, request):
		token = "asd"
		user = {
			"id": request.user.id,
			"firstname": request.user.first_name,
			"lastname": request.user.last_name,
			"email": request.user.email,
			
		}
		return HttpResponse(json.dumps(user))


def test(request):
	return HttpResponse(request.META['JWT'])
		
class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
    
    