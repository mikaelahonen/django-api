#Import django libraries
from django.db.models import F
from django.core import serializers
from django.contrib.auth.models import User
#Import DRF libraries
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.response import Response
#Import app specific libraries
from gym.serializers import *
from gym.functions import routine_start
#Import Python libraries
import datetime as dt
import json
# Import models and forms
from .models import *

#Viewsets http://www.django-rest-framework.org/api-guide/viewsets/

class WorkoutViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows workouts to be viewed or edited.
	"""
	queryset = Workout.objects.all().order_by('-id')
	serializer_class = WorkoutSerializer

	def list(self, request):
		#All objects
		queryset = Workout.objects.all()
		#Filter by current user
		queryset = queryset.filter(user=self.request.user)
		#Sort. F() allows setting nulls to last
		queryset = queryset.order_by('-id').order_by(F("start_time").desc(nulls_last=True))

		#many=True: get or post multiple items at once
		serializer = WorkoutSerializer(queryset, many=True)
		return Response(serializer.data)

	#def retrieve(self, request, pk=None):


class SetViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows sets to be viewed or edited.
	"""

	serializer_class = SetSerializer
	queryset = Set.objects.all().order_by('workout_order')

	#Override the list method
	def list(self, request):

		#All objects
		queryset = Set.objects.all()

		#Get workout parameter from URL
		workout = self.request.query_params.get('workout', None)
		excercise = self.request.query_params.get('excercise', None)

		#Filter by workout parameter
		if(workout is not None):
			queryset = queryset.filter(workout__id=workout)

		#Filter by excercise parameter
		if(excercise is not None):
			queryset = queryset.filter(excercise__id=excercise)

		#Filter by current user
		queryset = queryset.filter(user=self.request.user)

		#Sort
		queryset = queryset.order_by('-done', 'workout_order')

		#many=True: get or post multiple items at once
		serializer = SetSerializer(queryset, many=True)
		return Response(serializer.data)

class ExcerciseViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows excercises to be viewed or edited.
	"""
	queryset = Excercise.objects.all().order_by('-id')
	serializer_class = ExcerciseSerializer

class RoutineViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows routines to be viewed or edited.
	"""
	queryset = Routine.objects.all().order_by('-id')
	serializer_class = RoutineSerializer

	#Route to start a Routine
	@detail_route(methods=['post'])
	def start(self, request, pk=None):
		routine = Routine.objects.get(id=pk)
		user = self.request.user
		response = routine_start(routine, user)
		return Response(response)

class MuscleGroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows muscle groups to be viewed or edited.
	"""
	queryset = MuscleGroup.objects.all().order_by('-id')
	serializer_class = MuscleGroupSerializer
