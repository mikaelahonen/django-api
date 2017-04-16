#Import django libraries
from django import forms
#You could also use from sjango import forms
    #in which case you should pass arguments forms.Form
    #and then you should define all fields just as in models

#Import models
from .models import Plan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        #widgets = {'PlanForm': forms.TextInput(attrs={'class':'form-control'}),}
        #fields = ['name']
        #exclude = ['some_var_name']