from django.conf.urls import patterns, include, url
from cdc import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login$', views.login, name='login'),
    url(r'^accounts/logout$', views.logout, name='logout'),
    url(r'^accounts/home$', views.account_home, name='account'),
)
