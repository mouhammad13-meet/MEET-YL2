from django.db import models
class Polls(models.Model):
	question = models.CharField(max_length = 200)	
class answer(models.Model):
	answer = models.CharField(max_length = 60)
	votes = models.IntegerField(default=0)
	poll = models.ForeignKey(Polls)
	


# Create your models(classes) here.
