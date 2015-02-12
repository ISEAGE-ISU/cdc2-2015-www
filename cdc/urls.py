from django.conf.urls import patterns, include, url
from cdc import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^testimonials$', views.testimonials, name='testimonials'),
    url(r'^form$', views.form, name='form'),
    url(r'^accounts/login$', views.login, name='login'),
    url(r'^accounts/logout$', views.logout, name='logout'),
    url(r'^accounts/home$', views.account_home, name='account'),
    url(r'^accounts/admin$', views.admin, name='admin'),
    url(r'^accounts/login/admin$', views.login_admin, name='login_admin'),
    url(r'^accounts/settings$', views.settings, name='settings'),
    url(r'^accounts/upload$', views.upload, name='upload'),
    url(r'^accounts/loans$', views.loans, name='loans'),
    url(r'^accounts/filings$', views.filings, name='filings'),
    url(r'^accounts/warnings$', views.warnings, name='warnings'),
    url(r'^accounts/reports$', views.reports, name='reports'),
    url(r'^accounts/success$', views.success, name='success'),
)
