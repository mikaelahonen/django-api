from django.contrib import admin

# Register your models here.
from .models import Excercise
from .models import MuscleGroup
from .models import Plan
from .models import Routine
from .models import WorkoutPlan
from .models import Section

admin.site.register(Excercise)
admin.site.register(MuscleGroup)
admin.site.register(Plan)
admin.site.register(Routine)
admin.site.register(WorkoutPlan)
admin.site.register(Section)