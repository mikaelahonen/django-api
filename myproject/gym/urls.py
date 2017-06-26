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
pk2 = '(?P<pk2>[0-9]+)'

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
    url(r'^plan/'+pk+'/start$',v.planStart, name="plan-start"),
    
    #Excercise
    #url(r'^excercise/'+pk+'/$',ExcerciseView.detail,name='excercise-detail'),
    url(r'^excercise/$',v.excerciseList,name='excercise-list'),
    url(r'^excercise/create$',v.excerciseCreate,name='excercise-create'),
    url(r'^excercise/'+pk+'/delete$',v.excerciseDelete,name='excercise-delete'),
    url(r'^excercise/'+pk+'/update$',v.excerciseUpdate,name='excercise-update'),
    
    #Workout
    url(r'^routine/$',v.routineList, name="routine-list"),
    url(r'^routine/create$',v.routineCreate, name="routine-create"),
    url(r'^routine/'+pk+'/delete$',v.routineDelete, name="routine-delete"),
    url(r'^routine/'+pk+'/update$',v.routineUpdate, name="routine-update"),
    #url(r'^routine/'+pk+'/section$',v.routineSection, name="routine-section"),
    #url(r'^routines/'+routine_id+'$',v.routineView.view, name="routine-detail"),
    
    #WorkoutPlan
    #url(r'^routineplans/all$',v.WorkoutPlanView.all, name="routineplans-all"),
    url(r'^routineplan/create',v.routinePlanCreate, name="routineplan-create"),
    url(r'^routineplan/'+pk+'/delete$',v.routinePlanDelete, name="routineplan-delete"),
    url(r'^routineplan/'+pk+'/update$',v.routinePlanUpdate, name="routineplan-update"),
    url(r'^routineplan/'+pk+'/manage$',v.routinePlanManage, name="routineplan-manage"),
    
    #RoutineSection
    url(r'^routinesection/create',v.routineSectionCreate, name="routinesection-create"),
    url(r'^routinesection/'+pk+'/delete$',v.routineSectionDelete, name="routinesection-delete"),
    url(r'^routinesection/'+pk+'/update$',v.routineSectionUpdate, name="routinesection-update"),
    url(r'^routinesection/'+pk+'/manage$',v.routineSectionManage, name="routinesection-manage"),
    
    #Section
    url(r'^section/$',v.sectionList, name="section-list"),
    url(r'^section/create/'+pk+'$',v.sectionCreate, name="section-create"),
    url(r'^section/'+pk+'/delete$',v.sectionDelete, name="section-delete"),
    url(r'^section/'+pk+'/update$',v.sectionUpdate, name="section-update"),
    
    #Workout
    url(r'^workout/$',v.workoutList, name="workout-list"),
    #url(r'^workout/create$',v.workoutCreate, name="workout-create"),
    #url(r'^workout/'+pk+'/delete$',v.workoutDelete, name="workout-delete"),
    #url(r'^workout/'+pk+'/update$',v.workoutUpdate, name="workout-update"),
    #url(r'^workouts/'+workout_id+'$',v.WorkoutView.view, name="workout-detail"),
    
    #Include function chops off the rest and sends remaining to URLconf
    #url(r'^sessions', include('gymsessions.urls'))
    
    #React test
    url(r'^react-test/$',v.reactTest,name='react-test'),
    
    #Ajax
    url(r'ajax/fetch-time/$',v.fetchTime, name='fetch-time'),
]
