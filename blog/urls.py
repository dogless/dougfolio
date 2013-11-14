from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^resume/$', views.resume, name='resume'),
	url(r'^contact/$', views.contact, name='contact'),
)