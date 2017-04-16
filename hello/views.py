#Import django libraries
from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import TemplateView,ListView
#from django.views.generic.edit import CreateView,UpdateView,DeleteView
#In django 1.10 this would be from django.urls import reverse
#from django.core.urlresolvers import reverse

#Python libraries
import datetime as dt

#Import models
from .models import Greeting
from .models import MuscleGroup
from .models import Excercise
from .models import RndProgram
from .models import Plan
from .models import Workout

#import forms
from .forms import PlanForm

hLink="<br><a href='/'>Back to home</a>"

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'main.html')

def sets(request):
    # return HttpResponse('Hello from Python!')
    txt='Page for gym sets <br>Now it\'s '
    date=dt.datetime.now()
    return HttpResponse(txt + str(date)+hLink)

def muscleGroups(request):
    txt="Muscle Groups here"
    mgs=MuscleGroup.objects.all()
    return render(request,"muscle-groups.html",{'mgs': mgs})
    
def excercises(request):
    txt="Excercises"
    exs=Excercise.objects.all()
    return render(request,"excercises.html",{"exs":exs})
    
def excercise(request, eId):
    return HttpResponse(eId + hLink)
    
def rndProgram(request):
    var= RndProgram.create()
    return render(request,"rnd-program.html",{"var":var})
  
def plansView(request):
    plans = Plan.objects.all()
    form = PlanForm()
    return render(request,"plans.html",{"plans":plans,"form":form})
    
def planAdd(request):
    
    if request.method=='POST':
        form=PlanForm(request.POST)
        
        if form.is_valid():
            plan = form.save()
            name = form.cleaned_data['name']
        else:
            form = PlanForm()
    post = request
    return render(request,"plan-add.html",{'name':name})
    
def planView(request, plan_id):
    return HttpResponse("Show a single plan")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

