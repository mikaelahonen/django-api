from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

from .models import Greeting
from .models import MuscleGroup

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
    return HttpResponse(txt+hLink)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

