from django.db import models

# Create your models here.

class Owner(models.Model):
	uname = models.CharField(max_length=50)
	pword = models.CharField(max_length=50)
	def __str__(self):
		return self.uname


class Task(models.Model):
	owner = models.ForeignKey(Owner)
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
	done = models.BooleanField(default=False)
	def __str__(self):
		return self.title

