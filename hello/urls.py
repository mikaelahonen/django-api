from django.conf.urls import include, url
#from django.contrib import admin
#admin.autodiscover()

from . import views
from hello.views import ExcerciseTemplate, ExcerciseDetail, ExcerciseList, ExcerciseCreate #ExcerciseView, 

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

#For URL namespacing
app_name = 'gym'

#constants
pk = '(?P<pk>[0-9]+)'
plan_id = '(?P<plan_id>[0-9]+)'
workout_id = '(?P<workout_id>[0-9]+)'
workoutplan_id = '(?P<workoutplan_id>[0-9]+)'

#URL patterns
urlpatterns = [
    url(r'^sets$', views.sets, name='sets'),
    url(r'^muscle-groups$',views.muscleGroups, name="muscleGroups"),
    
    #url(r'^excercises$',views.excercises, name="excercises"),
    #url(r'^excercise/', ExcerciseView.as_view(), name='excercise-view'),
    #Template class
    #url(r'^$', ExcerciseTemplate.as_view(), name='excercise-template'),
    #Detail view
    url(r'^excercise/'+pk+'/$',ExcerciseDetail.as_view(),name='excercise-detail'),
    url(r'^excercise/$',ExcerciseList.as_view(),name='excercise-list'),
    url(r'^excercise/create$',ExcerciseCreate.as_view(),name='excercise-create'),
    
    #Workout
    url(r'^workouts/all$',views.WorkoutView.all, name="workouts-all"),
    url(r'^workouts/add$',views.WorkoutView.add, name="workouts-add"),
    url(r'^workouts/'+workout_id+'/delete$',views.WorkoutView.delete, name="workouts-delete"),
    url(r'^workouts/'+workout_id+'/edit$',views.WorkoutView.update, name="workouts-update"),
    url(r'^workouts/'+workout_id+'$',views.WorkoutView.view, name="workouts-view"),
    
    #WorkoutPlan
    url(r'^workoutplans/all$',views.WorkoutPlanView.all, name="workoutplans-all"),
    url(r'^workoutplans/add$',views.WorkoutPlanView.add, name="workoutplans-add"),
    url(r'^workoutplans/'+workoutplan_id+'/delete$',views.WorkoutPlanView.delete, name="workoutplans-delete"),
    url(r'^workoutplans/'+workoutplan_id+'/edit$',views.WorkoutPlanView.update, name="workoutplans-update"),
    #url(r'^workoutplans/'+workoutplan_id+'$',views.WorkoutPlanView.view, name="workoutplans-view"),
    url(r'^workoutplans/'+plan_id+'/manage$',views.WorkoutPlanView.manage, name="workoutplans-manage"),
    
    #Plans
    url(r'^plans/all$',views.plansView, name="plansView"),
    url(r'^plans/add$',views.planAdd, name="planAdd"),
    url(r'^plans/'+plan_id+'/delete$',views.planDelete, name="planDelete"),
    url(r'^plans/'+plan_id+'/edit$',views.planEdit, name="planEdit"),
    url(r'^plans/'+plan_id+'$',views.planView, name="planView"),
    #Include function chops off the rest and sends remaining to URLconf
    #url(r'^sessions', include('gymsessions.urls'))
]
