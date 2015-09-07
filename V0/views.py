from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from .models import Task, Owner
from django.utils import timezone




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")