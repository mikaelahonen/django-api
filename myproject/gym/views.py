#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from gym.serializers import *

#Python libraries
import datetime as dt
import json

# Import models and forms
from .models import *

#Viewsets http://www.django-rest-framework.org/api-guide/viewsets/

class WorkoutViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Workout.objects.all().order_by('-id')
	serializer_class = WorkoutSerializer
	
	def retrieve(self, request, pk=None):
		queryset = Workout.objects.all()
		workout = get_object_or_404(queryset, pk=pk)
		serializer = WorkoutSetsSerializer(workout)
		return Response(serializer.data)
	
class SetViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Set.objects.all().order_by('-id')
	serializer_class = SetSerializer
	
class ExcerciseViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Excercise.objects.all().order_by('-id')
	serializer_class = ExcerciseSerializer
	
class MuscleGroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = MuscleGroup.objects.all().order_by('-id')
	serializer_class = MuscleGroupSerializer