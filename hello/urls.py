from django.conf.urls import include, url
#from django.contrib import admin
#admin.autodiscover()

from . import views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^sets$', views.sets, name='sets'),
    #Include function chops off the rest and sends remaining to URLconf
    #url(r'^sessions', include('gymsessions.urls'))
]
