from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Gym(models.Model):
    gym_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')