from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#admin.autodiscover()

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.schemas import get_schema_view

#Views
import project.views
import gym.views

#Schema
schema_view = get_schema_view(title='Pastebin API')

#Default route
router = routers.DefaultRouter()

#Project
router.register(r'users', project.views.UserViewSet)
router.register(r'groups', project.views.GroupViewSet)

#Gym
router.register(r'gym/workouts', gym.views.WorkoutViewSet)
router.register(r'gym/sets', gym.views.SetViewSet)
router.register(r'gym/excercises', gym.views.ExcerciseViewSet)
router.register(r'gym/musclegroups', gym.views.MuscleGroupViewSet)
router.register(r'gym/routines', gym.views.RoutineViewSet)
router.register(r'gym/sections', gym.views.SectionViewSet)

#Other urls
urlpatterns = router.urls

#Administrative urls
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api-token-auth/', obtain_jwt_token),
    #Admin panel
    url(r'^admin/', include(admin.site.urls)),
    #Get schema for data model
	url(r'^schema/$', schema_view),

]

#Urls for dimensional model
urlpatterns += [
    url(r'^dm/workout-excercise$', project.views.WorkoutExcerciseDM),
]
