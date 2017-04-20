#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

@login_required

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'home.html')

@login_required
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
    
@login_required
def sets(request):
    # return HttpResponse('Hello from Python!')
    txt='Page for gym sets <br>Now it\'s '
    date=dt.datetime.now()
    return HttpResponse(txt + str(date)+hLink)
    
@login_required
def muscleGroups(request):
    txt="Muscle Groups here"
    mgs=MuscleGroup.objects.all()
    return render(request,"muscle-groups.html",{'mgs': mgs})

      
   
#EXCERCISE
@login_required
def excerciseList(request):
    objs = Excercise.objects.order_by('-id')
    form = ExcerciseForm()               
    return render(request,"excercise.html",{"form":form,"objs":objs})

@login_required   
def excerciseDelete(request, pk):
    obj = Excercise.objects.get(id=pk)
    obj.delete()
    return redirect('gym:excercise-list')

@login_required    
def excerciseCreate(request):
    if request.method=='POST':
        formData=ExcerciseForm(request.POST)            
        if formData.is_valid():
            excercise = formData.save()
        else:
            formData = ExcerciseForm()
    return redirect('gym:excercise-list')
    #return render(request,"add.html",{'obj':excercise,'request':request})

@login_required    
def excerciseUpdate(request, pk):
    obj = Excercise.objects.get(id=pk)
    form = ExcerciseForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()        
    return render(request,"update.html",{'obj':obj, 'form':form})

    
    
#PLAN
@login_required  
def planList(request):
    plans = Plan.objects.annotate(Count('workoutplan'))
    #plans = Plan.objects.all()
    form = PlanForm()
    return render(request,"plan.html",{"plans":plans,"form":form})
 
@login_required 
def planCreate(request):
    
    if request.method=='POST':
        formData=PlanForm(request.POST)
        
        if formData.is_valid():
            obj = formData.save()
            #name = form.cleaned_data['name']
        else:
            formData = PlanForm()
    return redirect('gym:plan-list')

@login_required
def planDetail(request, pk):
    return HttpResponse("Show a single plan")

@login_required    
def planUpdate(request, pk):
    obj = Plan.objects.get(id=pk)
    form = PlanForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()                
    return render(request,"update.html",{'obj':obj, 'form':form})

@login_required
def planDelete(request, pk):
    plan = Plan.objects.get(id=pk)
    plan.delete()
    return redirect('gym:plan-list')  
    
    
    
#WORKOUT
@login_required
def workoutList(request):
    objs = Workout.objects.all()
    form = WorkoutForm()
    return render(request,"workout.html",{"objs":objs,"form":form})

@login_required
def workoutCreate(request):        
    if request.method=='POST':
        formData=WorkoutForm(request.POST)                
        if formData.is_valid():
            obj = formData.save()
            #name = form.cleaned_data['name']
        else:
            formData = WorkoutForm()
    return redirect('gym:workout-list')
    
@login_required        
def workoutDetail(request, pk):
    return HttpResponse("Show a single workout")

@login_required    
def workoutUpdate(request, pk):
    obj = Workout.objects.get(id=pk)
    form = WorkoutForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()        
        #formData =                 
    return render(request,"update.html",{'obj':obj, 'form':form})

@login_required    
def workoutDelete(request, pk):
    obj = Workout.objects.get(id=pk)
    obj.delete()
    return redirect('gym:workout-list')

    
    
    
#WORKOUT-PLAN
@login_required    


#def workoutPlanList(request):
    #workoutPlans = WorkoutPlan.objects.all()
    #form = WorkoutPlanForm()
    #return render(request,"workoutplan.html",{"workoutPlans":workoutPlans,"form":form})

def workoutPlanCreate(request):

    if request.method=='POST':
        formData=WorkoutPlanForm(request.POST)
        
        if formData.is_valid():
            workoutPlan = formData.save()
            #name = form.cleaned_data['name']
        else:
            formData = WorkoutPlanForm()
    return render(request,"add.html",{'obj':workoutPlan,'request':request})

def workoutPlanManage(request, pk):
    workoutPlans = WorkoutPlan.objects.filter(plan=pk)
    form = WorkoutPlanForm()
    return render(request,"workoutplan-manage.html",{"workoutPlans":workoutPlans,"form":form,"pk":pk})

def workoutPlanUpdate(request, workoutpk):
    workoutPlan = WorkoutPlan.objects.get(id=workoutpk)
    form = WorkoutPlanForm(request.POST or None, instance=workoutPlan)
    if form.is_valid():
        form.save()        
        #formData = 
        
    return render(request,"update.html",{'obj':workoutPlan, 'form':form,'request':request})
    
def workoutPlanDelete(request, workoutpk):
    workoutPlan = WorkoutPlan.objects.get(id=workoutpk)
    workoutPlan.delete()
    return render(request,"delete.html",{'obj':workoutPlan,'request':request})

