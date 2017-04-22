from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#admin.autodiscover()

import gym.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^$', gym.views.index, name='index'),
    url(r'^db', gym.views.db, name='db'),
    url(r'^gym/', include('gym.urls')),
]

