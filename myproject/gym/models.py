#__str__()
from django.utils.encoding import python_2_unicode_compatible
#Create forms
from django.forms import ModelForm
#In django 1.10 this would be from django.urls import reverse
from django.core.urlresolvers import reverse
from django.db import models
import datetime
import random

# Muscle groups
class MuscleGroup(models.Model):
    muscle_group = models.CharField(
        max_length=50
    )    
    #Make single object to show "Chest" instead of "MuscleGroup object"
    def __str__(self):
        return self.muscle_group

# Excercises
class Excercise(models.Model):
    # String for random excercise
    rndStr = "Random"
        
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
        
# Plan is a template for program      
class Plan(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
        
    #Initialize Workouts from a Plan template
    def start(plan):
        # Get list RoutinePlans
        # id routine plan
        routinePlanList = RoutinePlan.objects.filter(plan=plan)
        # Loop all RoutinePlans
        for routinePlan in routinePlanList:
            # Get Routine Id from the RoutinePlan
            # routineId = routinePlan.routine
            # Get routine object by id
            routine = Routine.objects.get(id=routinePlan.routine.id)
            # Create new Workout from Routine and save to variable
            newWorkout = Workout.objects.create(name = routine.name)
            # Get Sections
            sectionList = Section.objects.filter(routine=routine.id)
            # Loop Sections
            for section in sectionList:
                # If excercise is random choose on from the muscle group excluding the random itself
                if section.excercise.excercise  == Excercise.rndStr:
                    excercises = Excercise.objects.filter(muscle_group=section.excercise.muscle_group).exclude(excercise=Excercise.rndStr)
                    excercise = random.choice(excercises)
                else:
                    excercise = section.excercise
                # Loop section by the number of sets    
                for i in range(0, section.sets):
                    #Create Set object where foreign key is the related Workout
                    Set.objects.create(
                        workout = newWorkout,
                        excercise = excercise
                    )
            
        return True
        # Create program
        # Create workout

#Routine is a template for workout
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

# A Section of a Routine
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
class RoutinePlan(models.Model):
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
        
class Workout(models.Model):
    name = models.CharField(
        default = "Workout X",
        max_length = 50,
    )
    start_time = models.DateTimeField(
        null = True,
    )
    end_time = models.DateTimeField(
        null = True,
    )
    location = models.CharField(
        default = "Gym X",
        max_length = 50,
        null = True,
    )
    def __str__(self):
        return self.name
        
class Set(models.Model):
    excercise = models.ForeignKey(
        Excercise,
        on_delete = models.CASCADE
    )
    workout = models.ForeignKey(
        Workout,
        on_delete = models.SET_NULL,
        null = True,
		related_name = 'sets',
    )
    reps = models.IntegerField(
        default = None,
        null = True,
    )
    weight = models.IntegerField(
        default = None,
        null = True,
    )
    
        

    
    