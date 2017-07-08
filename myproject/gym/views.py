#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.forms import inlineformset_factory

#Generic form for editing records
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

#Python libraries
import datetime as dt
import json

# Import models and forms
from .models import *
from .forms import *

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
    
    
    
    
#SET
@login_required
def sets(request):
    # return HttpResponse('Hello from Python!')
    txt='Page for gym sets <br>Now it\'s '
    date=dt.datetime.now()
    return HttpResponse(txt + str(date)+hLink)

def setUpdate(request, pk, pk2):
    obj = Set.objects.get(id=pk)
    form = SetForm(request.POST or None, instance=obj)
    template = "workout-view"
    if request.method=='POST':
        if form.is_valid():
            form.save()                       
        return redirect('gym:workout-set-2', pk, pk2)
    else:
        context = {
            'obj': obj,
            'form': form,
            'request': request,
        }
        return render(request, template, context)
    
    
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
    plans = Plan.objects.annotate(Count('routineplan'))
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
    routines = Routine.objects.filter(routineplan__plan=pk).all()
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
    
@login_required
def planStart(request, pk):
    plan = Plan.objects.get(id=pk)
    Plan.start(plan)
    return redirect('gym:workout-list')
    
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
    return redirect('gym:routine-section', pk=obj.routine.id)

@login_required  
def sectionDelete(request, pk):
    obj = Section.objects.get(id=pk)
    obj.delete()
    return redirect('gym:section-list')

@login_required    
def sectionUpdate(request, pk):
    obj = Section.objects.get(id=pk)
    form = SectionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()                         
    return render(request,"update.html",{'obj':obj, 'form':form})
    
    
    
    
#routine-PLAN  

@login_required  
def routinePlanCreate(request):

    if request.method=='POST':
        formData=RoutinePlanForm(request.POST)
        
        if formData.is_valid():
            routinePlan = formData.save()
            #name = form.cleaned_data['name']
        else:
            formData = RoutinePlanForm()
    return render(request,"add.html",{'obj':routinePlan,'request':request})

@login_required  
def routinePlanManage(request, pk):
    routinePlans = RoutinePlan.objects.filter(plan=pk)
    form = RoutinePlanForm()
    return render(request,"routineplan-manage.html",{"routinePlans":routinePlans,"form":form,"pk":pk})

@login_required  
def routinePlanUpdate(request, routinepk):
    obj = RoutinePlan.objects.get(id=routinepk)
    form = RoutinePlanForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() 
    return render(request,"update.html",{'obj':routinePlan, 'form':form,'request':request})
    
@login_required      
def routinePlanDelete(request, pk):
    routinePlan = RoutinePlan.objects.get(id=pk)
    routinePlan.delete()
    return render(request,"delete.html",{'obj':routinePlan,'request':request})
    
    
    
    
#ROUTINE-SECTION  

@login_required  
def routineSectionCreate(request):

    if request.method=='POST':
        formData=RoutineSectionForm(request.POST)
        
        if formData.is_valid():
            routineSection = formData.save()
        else:
            formData = RoutineSectionForm()
    return render(request,"add.html",{'obj':routineSection,'request':request})

@login_required  
def routineSectionManage(request, pk):
    routineSections = RoutineSection.objects.filter(plan=pk)
    form = RoutineSectionForm()
    return render(request,"routinesection-manage.html",{"routineSections":routineSections,"form":form,"pk":pk})

@login_required  
def routineSectionUpdate(request, routinepk):
    obj = RoutineSection.objects.get(id=routinepk)
    form = RoutineSectionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() 
    return render(request,"update.html",{'obj':routineSection, 'form':form,'request':request})

@login_required  
def routineSectionDelete(request, pk):
    routineSection = RoutineSection.objects.get(id=pk)
    routineSection.delete()
    return render(request,"delete.html",{'obj':routineSection,'request':request})



    
#WORKOUT

@login_required
def workoutList(request):
    head = "All workouts"
    template = "workout.html"
    objs = Workout.objects.all()
    context = {
        "objs": objs,
        "form": WorkoutForm(),
        "head": head,
    }
    return render(request, template, context) 
    
    
@login_required
def workoutView(request, pk):
    template = "workout-view.html"
    sets = Set.objects.filter(workout=pk)
    workout = Workout.objects.get(id=pk)
    head = "Current workout: " + workout.name
   
    context = {
        "sets": sets,
        "head": head,
        "workout": workout
    }
    return render(request, template, context) 
    
@login_required
def workoutSet(request, pk, pk2=None):
    template = "workout-view.html"
    sets = Set.objects.filter(workout=pk)
    workout = Workout.objects.get(id=pk)
    head = "Current workout: " + workout.name
    if pk2 is None:
        setCurrent = sets.first()
    else:
        setCurrent = Set.objects.get(id=pk2)      
    form = WorkoutSetForm(request.POST or None, instance=setCurrent)
    
    
    if request.method=='POST':
        if form.is_valid():
            form.save()                       
    context = {
        "setCurrent":setCurrent,
        "sets": sets,
        "head": head,
        "workout": workout,
        "form": form,
    }
    return render(request, template, context)
    
    
    
# React test
def reactTest(request):
    # return HttpResponse('Hello from Python!')
    template = 'react-test.html'
    context = {
        'head': 'React head',
        'component': 'react-component.js',
        'props': {
            'color': 'Red',
            'time':  dt.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        },
    }
    return render(request, template, context)
    
def fetchTime(request):
    t = dt.datetime.now().strftime("%I:%M:%S %d.%m.%Y")
    jsonStr = {
        'time': t
    }
    jsonStr = json.dumps(jsonStr)
    return HttpResponse(jsonStr)
