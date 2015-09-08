from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from .models import Task, Owner


#def index(request):
#	return render(request, 'V0/login.html')
#	return HttpResponse('7rawm')

#    tasks_list = Task.objects.all()#order_by('-pub_date')[:5]
#    context = {'tasks_list': tasks_list}
#    return render(request, 'V0/index.html')#, context)

'''
	url(r'^$', views.login, name='login'),
	url(r'^auth$', views.auth_login),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^loggedin$', views.loggedin, name='home'),
	url(r'^invalid_login$', views.invalid_login),
'''
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('V0/login.html',c)


def auth_login(request):
	uname = request.POST['username']
	pword = request.POST['password']
	user = auth.authenticate(username=uname, password=pword)
#	return HttpResponse(user.username)
	if user :
		auth.login(request, user)
		print "HIiiiiiiiiiiiiiii"
#		return HttpResponseRedirect('V0:home')
		return HttpResponseRedirect(reverse('V0:home'))

	else:
#		return HttpResponse('WTF')
		return HttpResponseRedirect(reverse('V0:invalid_login'))
#		return HttpResponseRedirect('V0:invalid_login')


def home(request):
	return render_to_response('V0/home.html', {'uname': request.user.username})

def invalid_login(request):
	return render_to_response('V0/invalid_login.html')#, {'message': 'username or password not correct'})

def logout(request):
	auth.logout(request)
	return render_to_response('V0/logout.html')