#Import django libraries
#You could also use from django import forms
    #in which case you should pass arguments forms.Form
    #and then you should define all fields just as in models
from django import forms

#Import models
from .models import Plan, Workout, WorkoutPlan, Excercise


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        #widgets = {'PlanForm': forms.TextInput(attrs={'class':'form-control'}),}
        #fields = ['name']
        #exclude = ['some_var_name']
        
    editAction = 'gym:planEdit'
    addAction = 'gym:planAdd'
   
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'
        
    editAction = 'gym:workouts-update'
    addAction = 'gym:workouts-add'
        
class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'
       
    editAction = 'gym:workoutplans-update'
    addAction = 'gym:workoutplans-add'

class ExcerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = '__all__'
    