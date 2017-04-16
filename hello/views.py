#Import django libraries
from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import TemplateView,ListView
#from django.views.generic.edit import CreateView,UpdateView,DeleteView


from django.db.models import Count

#Python libraries
import datetime as dt

#Import models
from .models import Greeting
from .models import MuscleGroup
from .models import Excercise
from .models import Plan
from .models import Workout
from .models import WorkoutPlan

#import forms
from .forms import PlanForm
from .forms import WorkoutForm
from .forms import WorkoutPlanForm

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
        
    return render(request,"plan-edit.html",{'plan':plan, 'form':form})
    
def planDelete(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    plan.delete()
    return render(request,"delete.html",{'obj':plan,'request':request})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
class WorkoutView:
    def all(request):
        workouts = Workout.objects.all()
        form = WorkoutForm()
        return render(request,"workouts.html",{"workouts":workouts,"form":form})
        
    def add(request):
    
        if request.method=='POST':
            formData=WorkoutForm(request.POST)
            
            if formData.is_valid():
                workout = formData.save()
                #name = form.cleaned_data['name']
            else:
                formData = WorkoutForm()
        return render(request,"add.html",{'obj':workout,'request':request})
    
    def view(request, workout_id):
        return HttpResponse("Show a single workout")
    
    def update(request, workout_id):
        workout = Workout.objects.get(id=workout_id)
        form = WorkoutForm(request.POST or None, instance=workout)
        if form.is_valid():
            form.save()        
            #formData = 
            
        return render(request,"workout-edit.html",{'workout':workout, 'form':form})
        
    def delete(request, workout_id):
        workout = Workout.objects.get(id=workout_id)
        workout.delete()
        return render(request,"delete.html",{'obj':workout,'request':request})
        
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
            
        return render(request,"edit.html",{'obj':workoutPlan, 'form':form,'request':request})
        
    def delete(request, workoutplan_id):
        workoutPlan = WorkoutPlan.objects.get(id=workoutplan_id)
        workoutPlan.delete()
        return render(request,"delete.html",{'obj':workoutPlan,'request':request})

