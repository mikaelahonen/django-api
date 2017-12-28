from django.db import models
from django.db.models import F, Count, Avg, Value, ExpressionWrapper
#from gym.models import *

#Pandas and NumPy
import numpy as np
import pandas as pd

class RoutineManager(models.Manager):

	#Default queryset
	def get_queryset(self):
		queryset = super(RoutineManager, self).get_queryset().order_by('-id')

		#Add orp field
		queryset = queryset.annotate(
			section_count=Count('section'),
		)

		return queryset

class SetManager(models.Manager):

	#Default queryset
	def get_queryset(self):
		#Initial queryset
		queryset = super(SetManager, self).get_queryset()

		#Add orp field
		queryset = queryset.annotate(
			orm=ExpressionWrapper(
				(36/(37-F('reps')))*F('weight'),
				#F('reps')+F('weight'),
				output_field=models.FloatField()
			)
		)
		return queryset

	def done_order(self, instance, serializer):

		workout_order = serializer.validated_data['workout_order']

		#If done and wasn't done
		if(not instance.done and serializer.validated_data['done']):

			sets = self.filter(workout=instance.workout).values()
			df = pd.DataFrame(list(sets))
			done_groups = df.groupby('done')
			#If at least one True
			if(True in list(done_groups.groups)):
				dones = done_groups.size()[True]
			else:
				dones = 0
			workout_order = dones + 1

		return workout_order

class WorkoutManager(models.Manager):

	#Default queryset
	def get_queryset(self):
		#Initial queryset
		queryset = super(WorkoutManager, self).get_queryset()

		#Add orp field
		queryset = queryset.annotate(
			sets_total=Count('set'),
		)
		return queryset

	#def get_queryset():
		#Date ordering for nulls
			#1.1.1970 or
			#nulls last
		#Add status column:
			#1: completed
			#0: in progress
			#-1: not started
		#Sets done
        #Duration
