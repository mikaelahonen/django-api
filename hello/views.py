#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

#Generic form for editing records
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

#Python libraries
import datetime as dt

#Import models
from .models import Greeting, MuscleGroup, Excercise, Plan, Workout, WorkoutPlan

#import forms
from .forms import PlanForm, WorkoutForm, WorkoutPlanForm, ExcerciseForm

hLink="<br><a href='/'>Back to home</a>"

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'home.html')

def sets(request):
    # return HttpResponse('Hello from Python!')
    txt='Page for gym sets <br>Now it\'s '
    date=dt.datetime.now()
    return HttpResponse(txt + str(date)+hLink)

def muscleGroups(request):
    txt="Muscle Groups here"
    mgs=MuscleGroup.objects.all()
    return render(request,"muscle-groups.html",{'mgs': mgs})
    
"""class ExcerciseView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')"""

      
   
#EXCERCISES
def excerciseList(request):
    objs = Excercise.objects.order_by('-id')
    form = ExcerciseForm()               
    return render(request,"excercise.html",{"form":form,"objs":objs})
    
def excerciseDelete(request, pk):
    obj = Excercise.objects.get(id=pk)
    obj.delete()
    return redirect('gym:excercise-list')
    
def excerciseCreate(request):
    if request.method=='POST':
        formData=ExcerciseForm(request.POST)            
        if formData.is_valid():
            excercise = formData.save()
        else:
            formData = ExcerciseForm()
    return redirect('gym:excercise-list')
    #return render(request,"add.html",{'obj':excercise,'request':request})
    
def excerciseUpdate(request, pk):
    obj = Excercise.objects.get(id=pk)
    form = ExcerciseForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()        
    return render(request,"update.html",{'obj':obj, 'form':form})
  
def plansView(request):
    plans = Plan.objects.annotate(Count('workoutplan'))
    #plans = Plan.objects.all()
    form = PlanForm()
    return render(request,"plans.html",{"plans":plans,"form":form})
    
def planAdd(request):
    
    if request.method=='POST':
        formData=PlanForm(request.POST)
        
        if formData.is_valid():
            plan = formData.save()
            #name = form.cleaned_data['name']
        else:
            formData = PlanForm()
    return render(request,"add.html",{'obj':plan,'request':request})


def planView(request, plan_id):
    return HttpResponse("Show a single plan")
    
def planEdit(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    form = PlanForm(request.POST or None, instance=plan)
    if form.is_valid():
        form.save()        
        #formData = 
        
    return render(request,"update.html",{'obj':plan, 'form':form})
    
def planDelete(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    plan.delete()
    return render(request,"delete.html",{'obj':plan,'request':request})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
    
    
    
#WORKOUT

def workoutList(request):
    objs = Workout.objects.all()
    form = WorkoutForm()
    return render(request,"workout.html",{"objs":objs,"form":form})
            
def workoutCreate(request):        
    if request.method=='POST':
        formData=WorkoutForm(request.POST)                
        if formData.is_valid():
            obj = formData.save()
            #name = form.cleaned_data['name']
        else:
            formData = WorkoutForm()
    return redirect('gym:workout-list')
        
def workoutDetail(request, pk):
    return HttpResponse("Show a single workout")
        
def workoutUpdate(request, pk):
    obj = Workout.objects.get(id=pk)
    form = WorkoutForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()        
        #formData =                 
    return render(request,"update.html",{'obj':obj, 'form':form})
            
def workoutDelete(request, pk):
    obj = Workout.objects.get(id=pk)
    obj.delete()
    return redirect('gym:workout-list')
        
class WorkoutPlanView:
    def all(request):
        workoutPlans = WorkoutPlan.objects.all()
        form = WorkoutPlanForm()
        return render(request,"workoutPlans.html",{"workoutPlans":workoutPlans,"form":form})
        
    def add(request):
    
        if request.method=='POST':
            formData=WorkoutPlanForm(request.POST)
            
            if formData.is_valid():
                workoutPlan = formData.save()
                #name = form.cleaned_data['name']
            else:
                formData = WorkoutPlanForm()
        return render(request,"add.html",{'obj':workoutPlan,'request':request})
    
    def manage(request, plan_id):
        workoutPlans = WorkoutPlan.objects.filter(plan=plan_id)
        form = WorkoutPlanForm()
        return render(request,"workoutplans-manage.html",{"workoutPlans":workoutPlans,"form":form,"plan_id":plan_id})
    
    def update(request, workoutplan_id):
        workoutPlan = WorkoutPlan.objects.get(id=workoutplan_id)
        form = WorkoutPlanForm(request.POST or None, instance=workoutPlan)
        if form.is_valid():
            form.save()        
            #formData = 
            
        return render(request,"update.html",{'obj':workoutPlan, 'form':form,'request':request})
        
    def delete(request, workoutplan_id):
        workoutPlan = WorkoutPlan.objects.get(id=workoutplan_id)
        workoutPlan.delete()
        return render(request,"delete.html",{'obj':workoutPlan,'request':request})

