from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from .models import Task, Owner
from django.utils import timezone
from django.contrib import messages


#def index(request):
#	return render(request, 'V0/login.html')
#	return HttpResponse('7rawm')

#    tasks_list = Task.objects.all()#order_by('-pub_date')[:5]
#    context = {'tasks_list': tasks_list}
#    return render(request, 'V0/index.html')#, context)


def signup(request):
	return render(request, 'V0/signup.html')


def validate_signup(request): # 34an asht3'l bs dlwa2ti
	#uname = request.POST['username']
	if Owner.objects.filter(uname = request.POST['username']):
	#	messages.warning(request, 'Your account expires in three days.')
	#	messages.add_message(request, messages.INFO, "Existed Username")
		return HttpResponseRedirect(reverse('V0:signup'))
	else:
		return HttpResponseRedirect(reverse('V0:login'))
#	return render(request, 'V0/login.html')

def login(request):
	return render(request, 'V0/login.html')
#	return HttpResponse('LOGIN?')

def validate_login(request):
#	if Owner.objects.filter(uname = request.POST['username']):	# login
#	else: arert w 5lik mkank
#	return HttpResponse("here")
	if request.POST:
		uname = request.POST["username"]
	#	return HttpResponse(reverse('V0:show_tasks', args=(uname,)))
		return HttpResponse(show_tasks(request,uname))
	else:
		return HttpResponse("hello")
		
#	return HttpResponseRedirect(reverse('V0:show_tasks', args=(uname)))

def show_tasks(request,u_name):

#	id_ = Owner.objects.get(uname=str(request.POST.get("username",""))).pk
#	tasks_list = Task.objects.filter(owner_id=id_)#request.POST.get("username",""))
#	context = {'tasks_list': tasks_list}

	ownr = Owner.objects.get(uname=u_name)
	context = {'ownr': ownr}
	return render(request, 'V0/show_tasks.html', context)
#	return HttpResponse("ads")

'''
    context = {'tasks_list': tasks_list}
    return render(request, 'V0/show_tasks.html', context)
'''
#	return render(request, 'V0/show_tasks.html')
'''
    tasks_list = Task.objects.all()#order_by('-pub_date')[:5]
    context = {'tasks_list': tasks_list}

    return render(request, 'V0/index.html')#, context)
'''

#def validate(request):

''''
def index(request):
    owner_tasks_list = Task.objects.get(pk=owner_id)#order_by('-pub_date')[:5]
    context = {'owner_tasks_list': owner_tasks_list}
    return render(request, 'V0/index.html', context)
'''