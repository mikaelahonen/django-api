#Import django libraries
#You could also use from django import forms
    #in which case you should pass arguments forms.Form
    #and then you should define all fields just as in models
from django import forms

#Import models
from .models import Plan, Workout, WorkoutPlan, Excercise, Section


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        #widgets = {'PlanForm': forms.TextInput(attrs={'class':'form-control'}),}
        #fields = ['name']
        #exclude = ['some_var_name']
        
    editAction = 'gym:plan-update'
    addAction = 'gym:plan-create'
   
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'
        
    editAction = 'gym:workout-update'
    addAction = 'gym:workout-create'
        
class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'
       
    editAction = 'gym:workoutplans-update'
    addAction = 'gym:workoutplans-create'

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