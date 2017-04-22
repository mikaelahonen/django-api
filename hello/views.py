#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
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
from .models import Greeting, MuscleGroup, Excercise, Plan, Routine, WorkoutPlan, Section

#import forms
from .forms import PlanForm, RoutineForm, WorkoutPlanForm, ExcerciseForm, SectionForm

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
    context = {
        'img':'https://sanescohealth.com/wp-content/uploads/2016/12/exercise-man-woman-gym-shutterstock_337161530.jpg',
        'form': form,
        'objs': objs,
    }
    return render(request,"excercise.html",context)

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
    context = {
        'img': 'https://s-media-cache-ak0.pinimg.com/736x/a2/79/83/a27983b763d89382d5c8db3b79677367.jpg',
        'plans': plans,
        'form': form,
    }
    return render(request,"plan.html",context)
 
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
    plan = Plan.objects.get(id=pk)
    routines = Routine.objects.filter(workoutplan__plan=pk).all()
    context = {
        'head': 'Plan: "' + plan.name + '"',
        'routines': routines,
        'plan': plan,
    }
    return render(request,"plan-detail.html",context)

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
    
    
    
#ROUTINE
@login_required
def routineList(request):
    objs = Routine.objects.all()
    context = {
        'objs': objs,
        'form': RoutineForm(),
        'head': 'Routines',
        'img': 'http://www.kaylainthecity.com/wp-content/uploads/gym.jpg'
    }
    return render(request,"routine.html",context)

@login_required
def routineCreate(request):        
    if request.method=='POST':
        formData=RoutineForm(request.POST)                
        if formData.is_valid():
            obj = formData.save()
        else:
            formData = RoutineForm()
    return redirect('gym:routine-list')
    
@login_required        
def routineDetail(request, pk):
    return HttpResponse("Show a single routine")

@login_required    
def routineUpdate(request, pk):
    obj = Routine.objects.get(id=pk)
    form = RoutineForm(request.POST or None, instance=obj)
    if request.method=='POST':
        if form.is_valid():
            form.save()                       
        return redirect('gym:routine-list')
    else:
        context = {
            'obj': obj,
            'form': form,
            'request': request,
        }
        return render(request,"update.html",context)
        

@login_required    
def routineDelete(request, pk):
    obj = Routine.objects.get(id=pk)
    obj.delete()
    return redirect('gym:routine-list')

@login_required
def routineSection(request, pk):
    routine = Routine.objects.get(id=pk)
    objs = Section.objects.filter(routine=pk)
    form = SectionForm()
    context = {
        'head': 'Sections for routine: "' + routine.name + '"',
        'objs': objs,
        'routine': routine,
        'form': form,
    }
    return render(request,"routine-section.html",context)
    
#WORKOUT-PLAN
  

@login_required  
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
    obj = WorkoutPlan.objects.get(id=workoutpk)
    form = WorkoutPlanForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() 
    return render(request,"update.html",{'obj':workoutPlan, 'form':form,'request':request})
    
def workoutPlanDelete(request, pk):
    workoutPlan = WorkoutPlan.objects.get(id=pk)
    workoutPlan.delete()
    return render(request,"delete.html",{'obj':workoutPlan,'request':request})
    

    
    
#SECTION
@login_required
def sectionList(request):
    objs = Section.objects.all()
    form = SectionForm()
    return render(request,"section.html",{"objs":objs,"form":form})
    
@login_required
def sectionCreate(request,pk):        
    if request.method=='POST':
        formData=SectionForm(request.POST)                
        if formData.is_valid():
            obj = formData.save()
        else:
            formData = SectionForm()
    return redirect('gym:routine-section', pk=obj.workout.id)

@login_required  
def sectionDelete(request, pk, pk2):
    obj = Section.objects.get(id=pk)
    obj.delete()
    return redirect('gym:routine-section', pk=pk2)

@login_required    
def sectionUpdate(request, pk):
    obj = Section.objects.get(id=pk)
    form = SectionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()                         
    return render(request,"update.html",{'obj':obj, 'form':form})