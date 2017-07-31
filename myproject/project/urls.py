from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#admin.autodiscover()

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

#Views
import project.views
import gym.views

#Default route
router = routers.DefaultRouter()

#Project
router.register(r'users', project.views.UserViewSet)
router.register(r'groups', project.views.GroupViewSet)

#Gym
router.register(r'gym/workouts', gym.views.WorkoutViewSet)

#Other urls
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^admin/', include(admin.site.urls)),       
]


urlpatterns += router.urls