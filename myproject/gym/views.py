#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.models import User

from rest_framework import viewsets
from gym.serializers import WorkoutSerializer

#Python libraries
import datetime as dt
import json

# Import models and forms
from .models import *

class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Workout.objects.all().order_by('-id')
    serializer_class = WorkoutSerializer