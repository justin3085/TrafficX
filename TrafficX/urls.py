from django.conf.urls import include, url, patterns
from complaintlog.backends import MyRegistrationView
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

urlpatterns = patterns('',

    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/create_complaint/$',
        'complaintlog.views.create_complaint',
        name='registration_create_complaint'),

    url(r'^accounts/password/reset/$', password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),

    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name="password_reset_done"),

    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),

    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),

    url(r'^$', 'complaintlog.views.index', name='home'),

    url(r'^complaints/(?P<slug>[-\w]+)/$',
         'complaintlog.views.complaint_detail',
         name='complaint_detail'),

    url(r'^about/$', TemplateView.as_view(template_name='about.html'),
        name='about'),

    url(r'^complaints/(?P<slug>[-\w]+)/edit/$',
        'complaintlog.views.edit_complaint', name='edit_complaint'),

    url(r'^accounts/', include('registration.backends.simple.urls')),


    url(r'^admin/', include(admin.site.urls)),
)