from django.conf.urls import url

from . import views

urlpatterns = [


 # ex: /polls/5/vote/
#    url(r'^(?<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


#	url(r'^login/$', views.login, name='login'),
	url(r'^$', views.login, name='login'),
	url(r'^auth_login$', views.auth_login, name='auth_login'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^home$', views.home, name='home'),
	url(r'^invalid_login$', views.invalid_login, name='invalid_login'),


]
'''
    url(r'^show_tasks/$', views.show_tasks, name='show_tasks'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^validate_signup/$', views.validate_signup, name='validate_signup'),
	url(r'^validate_login/$', views.validate_login, name='validate_login'),
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
'''