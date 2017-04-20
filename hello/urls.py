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
    
    #PLAN
    url(r'^plan/list$',v.planList, name="plan-list"),
    url(r'^plan/create$',v.planCreate, name="plan-create"),
    url(r'^plan/'+pk+'/delete$',v.planDelete, name="plan-delete"),
    url(r'^plan/'+pk+'/edit$',v.planUpdate, name="plan-update"),
    url(r'^plan/'+pk+'$',v.planDetail, name="plan-detail"),
    
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
    #url(r'^workoutplans/all$',v.WorkoutPlanView.all, name="workoutplans-all"),
    url(r'^workoutplan/create',v.workoutPlanCreate, name="workoutplan-create"),
    url(r'^workoutplan/'+pk+'/delete$',v.workoutPlanDelete, name="workoutplan-delete"),
    url(r'^workoutplan/'+pk+'/update$',v.workoutPlanUpdate, name="workoutplan-update"),
    #url(r'^workoutplans/'+workoutplan_id+'$',v.WorkoutPlanView.view, name="workoutplans-view"),
    url(r'^workoutplan/'+pk+'/manage$',v.workoutPlanManage, name="workoutplan-manage"),
    
    
    #Include function chops off the rest and sends remaining to URLconf
    #url(r'^sessions', include('gymsessions.urls'))
]
