from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.login, name='login'),
	url(r'^auth_login$', views.auth_login, name='auth_login'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^home$', views.home, name='home'),
	url(r'^invalid_login$', views.invalid_login, name='invalid_login'),


	url(r'^sign_up$', views.sign_up, name='sign_up'),
	url(r'^auth_signup$', views.auth_signup, name='auth_signup'),
#	url(r'^invalid_signup$', views.invalid_signup, name='invalid_signup'),
	url(r'^signup_success$', views.signup_success, name='signup_success'),
	url(r'^signup_req$', views.signup_req, name='signup_req'),

]
'''
    url(r'^show_tasks/$', views.show_tasks, name='show_tasks'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^validate_signup/$', views.validate_signup, name='validate_signup'),
	url(r'^validate_login/$', views.validate_login, name='validate_login'),
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
'''