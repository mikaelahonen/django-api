from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

from .models import Greeting
from .models import MuscleGroup
from .models import Excercise
from .models import RndProgram

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
    
def planDesign(request):
    return render(request,"plan-design.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

