from django.contrib import admin

# Register your models here.
from .models import Gym
from .models import Excercise
from .models import MuscleGroup

admin.site.register(Gym)
admin.site.register(Excercise)
admin.site.register(MuscleGroup)