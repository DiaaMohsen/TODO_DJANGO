from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from .models import Task, Owner

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

#def index(request):
#	return render(request, 'V0/login.html')
#	return HttpResponse('7rawm')

#    tasks_list = Task.objects.all()#order_by('-pub_date')[:5]
#    context = {'tasks_list': tasks_list}
#    return render(request, 'V0/index.html')#, context)


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
#		return HttpResponseRedirect('V0:home')
		return HttpResponseRedirect(reverse('V0:home'))

	else:
		return HttpResponseRedirect(reverse('V0:invalid_login'))
#		return HttpResponseRedirect('V0:invalid_login')


def home(request):
	user = User.objects.get(username=request.user.username)
	context = {'user': user}
#	return render(request, 'V0/show_tasks.html', context)	
	return render_to_response('V0/home.html', context)#{'username': request.user.username})

def invalid_login(request):
	return render_to_response('V0/invalid_login.html')#, {'message': 'username or password not correct'})

def logout(request):
	auth.logout(request)
	return render_to_response('V0/logout.html')

def sign_up(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('V0/signup.html', c)

def signup_req(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('V0:signup_success'))
		else:
			print form.cleaned_data['username']
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
#	return HttpResponse('this username is exist already')
	return render_to_response('V0/signup.html', args)

def signup_success(request):
	return render_to_response('V0/signup_success.html')


def invalid_signup(request): # to be done later
	return HttpResponse('this username is exist already')




def auth_signup(request):
	
	uname = request.POST['username']
	pwrd1 = request.POST['password1']
	pwrd2 = request.POST['password2']

	user = User.objects.filter(username=uname).exists()


	if user:# b3den 5liha view l-w7dha
#		return HttpResponseRedirect(reverse(V0:invalid_signup))
		return HttpResponse('this username is exist already') 

	else:
		if pwrd1 != pwrd2:
			return HttpResponse('rewrite passwords fields again')

	nuser = User.objects.create_user(uname, pwrd1)
	nuser.user_permissions = [	Permission.objects.get(codename='add_task'),
								Permission.objects.get(codename='change_task'),
								Permission.objects.get(codename='delete_task')
							]
	nuser.save()
	return HttpResponseRedirect(reverse('V0:login'))
