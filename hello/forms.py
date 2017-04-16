#Import django libraries
from django.forms import ModelForm

#Import models
from models import Plan


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['name']