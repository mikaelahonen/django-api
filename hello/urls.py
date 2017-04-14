from django.conf.urls import include, url
#from django.contrib import admin
#admin.autodiscover()

from . import views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^sets$', views.sets, name='sets'),
    url(r'^muscle-groups$',views.muscleGroups, name="muscleGroups"),
    url(r'^excercises$',views.excercises, name="excercises"),
    url(r'^excercise/(?P<eId>[0-9]+)$',views.excercise, name="excercise"),
    #Include function chops off the rest and sends remaining to URLconf
    #url(r'^sessions', include('gymsessions.urls'))
]
