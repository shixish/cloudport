from django.db import models
import json

class Job(models.Model):
    date = models.DateTimeField('date published')
    title = models.CharField(max_length = 100)
    status = models.IntegerField()
    output = models.CharField(max_length = 100)
    
    #def toJSON():
    #    
    
    def __unicode__(self):
        #return json.dumps([self.title, self.date, self.status, self.output])
        return self.title