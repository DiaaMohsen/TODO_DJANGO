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



#	features
	url(r'^add_task$', views.add_task, name='add_task'),
	url(r'^add_task_to_tasks$', views.add_task_to_tasks, name='add_task_to_tasks'),
	url(r'^delete_dtask$', views.delete_dtask, name='delete_dtask'),
	url(r'^edit_task$', views.edit_task, name='edit_task')
]
