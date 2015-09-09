from django.contrib import admin
from .models import Owner, Task
from django.contrib.auth.models import User
# Register your models here.



class TasksView(admin.TabularInline):
	model = Task
	extra = 1

class OwnersView(admin.ModelAdmin):
#	list_filter = ['uname',]
	search_fields = ['username']
#	list_display = ['username', 'pword']
#	fields = [('pub_date', 'question_text')]
	inlines = [TasksView]

#admin.site.register(User, OwnersView)




class OwnersView(admin.ModelAdmin):
#	list_filter = ['uname',]
	search_fields = ['owner.username']
#	list_display = ('question_text','pub_date','was_published_recently')
	list_display = ['title', 'desc', 'done']
#	fields = [('pub_date', 'question_text')]


admin.site.register(Task,OwnersView)