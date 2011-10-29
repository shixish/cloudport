from django.db import models

class Job(models.Model):
    date = models.DateTimeField('date published')
    title = models.CharField(max_length = 100)
    status = models.IntegerField()
    output = models.CharField(max_length = 100)