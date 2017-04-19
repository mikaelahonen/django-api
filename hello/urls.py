from django.conf.urls import include, url
#from django.contrib import admin
#admin.autodiscover()

from . import views as v

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
    url(r'^sets$', v.sets, name='sets'),
    url(r'^muscle-groups$',v.muscleGroups, name="muscleGroups"),
    
    #Excercise
    #url(r'^excercise/'+pk+'/$',ExcerciseView.detail,name='excercise-detail'),
    url(r'^excercise/$',v.excerciseList,name='excercise-list'),
    url(r'^excercise/create$',v.excerciseCreate,name='excercise-create'),
    url(r'^excercise/'+pk+'/delete$',v.excerciseDelete,name='excercise-delete'),
    url(r'^excercise/'+pk+'/update$',v.excerciseUpdate,name='excercise-update'),
    
    #Workout
    url(r'^workout/$',v.workoutList, name="workout-list"),
    url(r'^workout/create$',v.workoutCreate, name="workout-create"),
    url(r'^workout/'+pk+'/delete$',v.workoutDelete, name="workout-delete"),
    url(r'^workout/'+pk+'/update$',v.workoutUpdate, name="workout-update"),
    #url(r'^workouts/'+workout_id+'$',v.WorkoutView.view, name="workout-detail"),
    
    #WorkoutPlan
    url(r'^workoutplans/all$',v.WorkoutPlanView.all, name="workoutplans-all"),
    url(r'^workoutplans/add$',v.WorkoutPlanView.add, name="workoutplans-add"),
    url(r'^workoutplans/'+workoutplan_id+'/delete$',v.WorkoutPlanView.delete, name="workoutplans-delete"),
    url(r'^workoutplans/'+workoutplan_id+'/edit$',v.WorkoutPlanView.update, name="workoutplans-update"),
    #url(r'^workoutplans/'+workoutplan_id+'$',v.WorkoutPlanView.view, name="workoutplans-view"),
    url(r'^workoutplans/'+plan_id+'/manage$',v.WorkoutPlanView.manage, name="workoutplans-manage"),
    
    #Plans
    url(r'^plans/all$',v.plansView, name="plansView"),
    url(r'^plans/add$',v.planAdd, name="planAdd"),
    url(r'^plans/'+plan_id+'/delete$',v.planDelete, name="planDelete"),
    url(r'^plans/'+plan_id+'/edit$',v.planEdit, name="planEdit"),
    url(r'^plans/'+plan_id+'$',v.planView, name="planView"),
    #Include function chops off the rest and sends remaining to URLconf
    #url(r'^sessions', include('gymsessions.urls'))
]
