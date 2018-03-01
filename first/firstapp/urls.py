from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import index, form_name_view, createtopic, register

app_name = 'firstapp'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^we$', form_name_view, name='demoform'),
    url(r'^create$', createtopic, name='create'),

    url(r'^register/$', register, name='userregistration'),
    # url(r'login/$', user_login, name='login')
]
