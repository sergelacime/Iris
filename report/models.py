from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    filename = models.CharField(max_length=100, default="FileIris")
    date = models.DateField(default=datetime.datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField()
    
    
    class Meta:
        verbose_name_plural = 'Report'

    def __str__(self):
        return self.filename


class Resume(models.Model):
    text = models.TextField()
    date = models.DateField(default=datetime.datetime.now)
    Report = models.ForeignKey(Report,on_delete=models.CASCADE,verbose_name="Report")

    class Meta:
        verbose_name_plural = 'Resume'

    def __str__(self):
        return self.Report.filename



class Request(models.Model):
    query = models.CharField(max_length=100000)
    answer = models.CharField(max_length=1000000)
    date = models.DateField(default=datetime.datetime.now)
    filename = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Request'

    def __str__(self):
        return self.query
