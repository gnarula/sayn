from django.conf.urls import patterns, include, url
from django.contrib import admin
from progress import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sayn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/$', views.dashboard),
    url(r'^dashboard/society$', views.society),
    url(r'^dashboard/society/new$', views.newsociety),
    url(r'^dashboard/society/(?P<id>\d+)/edit$',views.editsociety),
    url(r'^dashboard/user$', views.user),
    url(r'^dashboard/user/new$',views.newuser),
    url(r'^dashboard/user/(?P<id>\d+)/edit$',views.edituser),
)
