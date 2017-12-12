#__str__()
from django.utils.encoding import python_2_unicode_compatible
#Create forms
from django.forms import ModelForm
#In django 1.10 this would be from django.urls import reverse
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
import datetime
import random

# Muscle groups
class MuscleGroup(models.Model):
	muscle_group = models.CharField(
		max_length=50
	)
	description = models.TextField(
		default = "",
	)
	#Make single object to show "Chest" instead of "MuscleGroup object"
	def __str__(self):
		return self.muscle_group

# Excercises
class Excercise(models.Model):

	excercise = models.CharField(
		max_length=100
	)
	muscle_group = models.ForeignKey(
		MuscleGroup,
		on_delete = models.SET_NULL,
		blank = True,
		null = True,
	)
	#Distance from movement axis in meters
	lever = models.FloatField(
		null=True,
		blank=True,
	)
	#Portion of body mass moving in the excercise
	mass_share = models.FloatField(
		null=True,
		blank=True,
	)
	#Isolated, Compound
	type = models.CharField(
		max_length=50,
	)
	#Variations for example
	description = models.TextField(
		default = "",
		blank = True,
	)

	def __str__(self):
		return self.excercise

	def get_absolute_url(self):
		return reverse('excercise-detail', kwargs={'pk': self.pk})

# Plan is a template for program
class Plan(models.Model):
	name = models.CharField(
		max_length = 100
	)
	comments = models.TextField(
		default = "",
	)
	def __str__(self):
		return self.name

		return True
		# Create program
		# Create workout

#Routine is a template for workout
class Routine(models.Model):
	TYPE_CHOICES = (

		#Excercise First. Execute the first excercise before moving to next.
		#This is the natural order according to the index.
		('EF','Excercise first'),

		#Set First. Execute first set from each excercise first.
		('SF','Set first'),

		#Alternate Two. Switch between two exercises.
		#If the number of excercices is odd, one excercice will be done last.
		('AT','Alternate two'),

		#Random order. Generate all sets and make the order random.
		('RO','Random order'),

	)
	name = models.CharField(
		max_length = 100,
	)
	plan = models.ManyToManyField(
		Plan,
		blank=True,
	)
	type = models.CharField(
		choices=TYPE_CHOICES,
		default='AT',
		max_length=2,
	)
	comments = models.TextField(
		default="",
		blank=True,
	)
	def __str__(self):
		return self.name


# A Section of a Routine is a building block of an routine.
# It has to be a single excercise.
# A Section is pointed to a specific routine
class Section(models.Model):
	#Sort key for section in the routine
	index = models.IntegerField(
		default = 1,
	)
	#If random is false, use this
	#Because this is optional, on delete is SET_NULL
	excercise = models.ForeignKey(
		Excercise,
		on_delete = models.SET_NULL,
		default = None,
		null = True,
	)
	#If random is true, use this
	#Because this is optional, on delete is SET_NULL
	muscle_group = models.ForeignKey(
		MuscleGroup,
		on_delete = models.SET_NULL,
		null = True,
	)
	random_excercise = models.BooleanField(
		default = True
	)
	#How many sets to do
	sets = models.IntegerField(
		default = 4,
	)
	#Target repetitions
	target = models.IntegerField(
		default = 10,
	)
	random_target = models.BooleanField(
		default = True
	)
	routine = models.ForeignKey(
		Routine,
		on_delete = models.CASCADE
	)
	def __str__(self):
		if(self.random_excercise):
			if(self.muscle_group is not None):
				e = self.muscle_group.muscle_group
			else:
				e = ""
		else:
			if(self.muscle_group is not None):
				e = self.excercise.excercise
			else:
				e = ""

		return self.routine.name + " -- " + e


class Workout(models.Model):
	name = models.CharField(
		default = "Workout X",
		max_length = 50,
	)
	start_time = models.DateTimeField(
		null = True,
		blank = True,
	)
	end_time = models.DateTimeField(
		null = True,
		blank = True,
	)
	location = models.CharField(
		default = "Gym X",
		max_length = 50,
		null = True,
	)
	user = models.ForeignKey(
		User,
		null=True
	)
	name = models.CharField(
		max_length = 50,
	)
	comments = models.TextField(
		default = "",
		blank = True,
	)
	def __str__(self):
		return self.name

class Set(models.Model):
	excercise = models.ForeignKey(
		Excercise,
		on_delete = models.SET_NULL,
		null = True,
		blank = True,
	)
	workout = models.ForeignKey(
		Workout,
		on_delete = models.CASCADE, #CASCADE is good for automation
		related_name = 'sets',
		null = True,
	)
	reps = models.IntegerField(
		default = None,
		null = True,
		blank = True,
	)
	weight = models.FloatField(
		default = None,
		null = True,
		blank = True,
	)
	#The oreder index of the set inside the workout
	workout_order = models.IntegerField(
		default = None,
		null = True,
	)
	done = models.BooleanField(
		default = 0,
	)
	user = models.ForeignKey(
		User,
		null = True,
	)
	comments = models.TextField(
		default = "",
		blank = True,
	)

	def __str__(self):
		if(self.workout==None):
			wo = 'Unknown Workout'
		else:
			wo = self.workout.name

		if(self.excercise==None):
			e = 'Unknown Excercise'
		else:
			e = str(self.excercise.excercise)

		r = str(self.reps)
		w = str(self.weight)

		return wo + ': ' + e + ' ' + r + 'x' + w
