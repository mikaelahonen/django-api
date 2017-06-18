#__str__()
from django.utils.encoding import python_2_unicode_compatible
#Create forms
from django.forms import ModelForm
#In django 1.10 this would be from django.urls import reverse
from django.core.urlresolvers import reverse
from django.db import models


#This class must be introduced before it can be referenced
class MuscleGroup(models.Model):
    muscle_group = models.CharField(max_length=50)
    
    #Make single object to show "Chest" instead of "MuscleGroup object"
    def __str__(self):
        return self.muscle_group
    
class Excercise(models.Model):
    excercise = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(
        MuscleGroup,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,)
    #Distance from movement axis in meters
    lever = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True)
    #Portion of body mass moving in the excercise  
    mass_share = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True)
    
    def __str__(self):
        return self.excercise
    
    def get_absolute_url(self):
        return reverse('excercise-detail', kwargs={'pk': self.pk})
        
      
class Plan(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Routine(models.Model):
    TYPE_CHOICES = (
        ('SS','Superset'), #Change between two exercises
        ('SF','Set first'), #Execute first set from each excercise first
        ('EF','Excercise first'), #Execute the first excercise before moving to next
        ('','Excercise first'), #Execute the first excercise before moving to next
    )
    name = models.CharField(
        max_length = 100,
    )
    #plan = models.ForeignKey(
      #  Plan,
        #on_delete = models.SET_NULL,
        #blank = True,
        #null = True,
    #)
    type = models.CharField(
        choices=TYPE_CHOICES,
        default='EF',
        max_length=2,
    )
    
    def __str__(self):
        return self.name

class Section(models.Model):
    index = models.IntegerField(
        default = 1,
    )
    excercise = models.ForeignKey(
        Excercise,
        on_delete = models.CASCADE
    )
    #How many sets to do
    sets = models.IntegerField(
        default = 4,
    )
    #Target repetitions
    target = models.IntegerField(
        default = 10,
    )
    routine = models.ForeignKey(
        Routine,
        on_delete = models.CASCADE
    )
     
#Connection table between PLans and Routines
class WorkoutPlan(models.Model):
    plan = models.ForeignKey(
        Plan,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )
    routine = models.ForeignKey(
        Routine,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )
    def __str__(self):
        return self.plan.name + " -- " + self.routine.name

#Connection table between Routines and Sections
class RoutineSection(models.Model):
    routine = models.ForeignKey(
        Routine,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )
    section = models.ForeignKey(
        Section,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )
    def __str__(self):
        return self.routine.name + " -- " + self.section.name
        

    
    