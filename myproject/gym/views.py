#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.forms import inlineformset_factory



#Python libraries
import datetime as dt
import json

# Import models and forms
from .models import *
from .forms import *

