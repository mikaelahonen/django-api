from django.contrib import admin

# Register your models here.
from .models import Gym
from .models import Excercise
from .models import MuscleGroup
from .models import Plan
from .models import Workout
from .models import WorkoutPlan

admin.site.register(Gym)
admin.site.register(Excercise)
admin.site.register(MuscleGroup)
admin.site.register(Plan)
admin.site.register(Workout)
admin.site.register(WorkoutPlan)