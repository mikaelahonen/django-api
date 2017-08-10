from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Excercise)
admin.site.register(MuscleGroup)
admin.site.register(Plan)
admin.site.register(Routine)
admin.site.register(RoutinePlan)
admin.site.register(Section)
admin.site.register(Workout)