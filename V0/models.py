from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
	uname = models.CharField(max_length=50)
	pword = models.CharField(max_length=50)
	def __str__(self):
		return self.uname


class Task(models.Model):
	owner = models.ForeignKey(User, related_name="tasks")
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
	done = models.BooleanField(default=False)
	def __str__(self):
		return self.title

