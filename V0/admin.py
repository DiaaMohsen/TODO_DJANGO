from django.contrib import admin
from .models import Owner, Task
# Register your models here.



class TasksView(admin.TabularInline):
	model = Task
	extra = 1

class OwnersView(admin.ModelAdmin):
#	list_filter = ['uname',]
	search_fields = ['uname']
#	list_display = ('question_text','pub_date','was_published_recently')
	list_display = ['uname', 'pword']
#	fields = [('pub_date', 'question_text')]
	inlines = [TasksView]

admin.site.register(Owner, OwnersView)
