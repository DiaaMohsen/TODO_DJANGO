from django.conf.urls import url

from . import views

urlpatterns = [


 # ex: /polls/5/vote/
#    url(r'^(?<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


#	url(r'^login/$', views.login, name='login'),
	url(r'^$', views.login, name='login'),
    url(r'^show_tasks/$', views.show_tasks, name='show_tasks'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^validate_signup/$', views.validate_signup, name='validate_signup'),
	url(r'^validate_login/$', views.validate_login, name='validate_login'),
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),


]
