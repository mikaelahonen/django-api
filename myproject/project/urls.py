from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#admin.autodiscover()

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from project import views

import gym.views
import project.views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^admin/', include(admin.site.urls)),    
    #url(r'^db', gym.views.db, name='db'),
    #url(r'^gym/', include('gym.urls')),

]

