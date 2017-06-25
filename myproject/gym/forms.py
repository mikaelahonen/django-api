#Import django libraries
#You could also use from django import forms
    #in which case you should pass arguments forms.Form
    #and then you should define all fields just as in models
from django import forms

#Import models
from .models import  Excercise, Plan, Routine, Section, RoutinePlan, RoutineSection, Workout


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        #widgets = {'PlanForm': forms.TextInput(attrs={'class':'form-control'}),}
        #fields = ['name']
        #exclude = ['some_var_name']
        
    editAction = 'gym:plan-update'
    addAction = 'gym:plan-create'
   
class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'
        
    editAction = 'gym:routine-update'
    addAction = 'gym:routine-create'
        
class RoutinePlanForm(forms.ModelForm):
    class Meta:
        model = RoutinePlan
        fields = '__all__'
       
    editAction = 'gym:routineplans-update'
    addAction = 'gym:routineplans-create'
    
class RoutineSectionForm(forms.ModelForm):
    class Meta:
        model = RoutineSection
        fields = '__all__'
       
    editAction = 'gym:routinesections-update'
    addAction = 'gym:routinesections-create'

class ExcerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = '__all__'
        
    editAction = 'gym:excercise-update'
    addAction = 'gym:excercise-create'
    
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
        
    editAction = 'gym:section-update'
    addAction = 'gym:section-create'
    
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'
        
    editAction = 'gym:workout-list'
    addAction = 'gym:workout-list'