from django.db import models
from django import forms 

import json

class Job(models.Model):
    date_published = models.DateTimeField('date published', auto_now_add=True)
    date_updated = models.DateTimeField('date updated', auto_now=True)
    status = models.IntegerField(editable=False, default=0)
    title = models.CharField(max_length = 100)
    output = models.CharField(editable=False, max_length = 100)
    file = models.FileField(upload_to="JOB_UPLOADS")
    
    def __unicode__(self):
        return self.title
    
class JobForm(forms.ModelForm):
    class Meta:
        model = Job