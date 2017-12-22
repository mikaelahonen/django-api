#Viewsets http://www.django-rest-framework.org/api-guide/viewsets/
#Import django libraries
from django.db.models import F
from django.core import serializers
from django.contrib.auth.models import User
#Import DRF libraries
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
#Import app specific libraries
from gym.serializers import *
from gym.functions import routine_start
from gym.models import *

class ExcerciseViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows excercises to be viewed or edited.
	"""
	queryset = Excercise.objects.all().order_by('excercise')
	serializer_class = ExcerciseSerializer

	#Filtering
	filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
	filter_fields = ('id','excercise')
	search_fields = ('excercise',)
	ordering_fields = ('id','excercise')

class MuscleGroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows muscle groups to be viewed or edited.
	"""
	queryset = MuscleGroup.objects.all().order_by('muscle_group')
	serializer_class = MuscleGroupSerializer

class RoutineViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows routines to be viewed or edited.
	"""
	queryset = Routine.manager.all()
	serializer_class = RoutineSerializer

	#Filtering
	filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
	filter_fields = ('id','name')
	search_fields = ('name',)
	ordering_fields = ('id','name')

	#Route to start a Routine
	@detail_route(methods=['post'])
	def start(self, request, pk=None):
		routine = Routine.objects.get(id=pk)
		user = self.request.user
		response = routine_start(routine, user)
		return Response(response)

class SectionViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows sections to be viewed or edited.
	"""
	queryset = Section.objects.all()
	serializer_class = SectionSerializer

	#Filtering
	filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
	filter_fields = ('id','routine')
	search_fields = ('comments',)
	ordering_fields = ('id','routine')

class SetViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows sets to be viewed or edited.
	"""

	serializer_class = SetSerializer
	queryset = Set.manager.all()

	#Filtering
	filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
	filter_fields = ('id','workout','excercise','workout_order','workout__start_time')
	search_fields = ('comments',)
	ordering_fields = ('id','orp','workout','excercise','workout_order','workout__start_time')


	def get_queryset(self):
		#Request shouldn't be passed to the manager
		queryset = self.queryset.filter(user=self.request.user)
		return queryset

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def perform_update(self, serializer):
		old_instance = self.get_object()
		workout_order = Set.manager.done_order(old_instance, serializer)
		new_instance = serializer.save(workout_order=workout_order)


class WorkoutViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows workouts to be viewed or edited.
	"""
	queryset = Workout.manager.all().order_by('-start_time')
	serializer_class = WorkoutSerializer

	#Filtering
	filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
	filter_fields = ('id',)
	search_fields = ('comments',)
	ordering_fields = ('id','start_time','end_time',)

	def get_queryset(self):
		#Request shouldn't be passed to the manager
		queryset = self.queryset.filter(user=self.request.user)
		return queryset

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
