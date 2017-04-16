#Import django libraries
#You could also use from django import forms
    #in which case you should pass arguments forms.Form
    #and then you should define all fields just as in models
from django import forms
#Generic form for editing records
from django.views.generic.edit import UpdateView 

#Import models
from .models import Plan
from .models import Workout
from .models import WorkoutPlan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        #widgets = {'PlanForm': forms.TextInput(attrs={'class':'form-control'}),}
        #fields = ['name']
        #exclude = ['some_var_name']
   
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'
        
class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'
       

    