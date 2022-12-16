from django.db import models
import datetime
# Create your models here.
class BurstModel(models.Model):
    #in seconds
    rise_time = models.IntegerField()
    decay_time = models.IntegerField()
    #in seconds elapsed from JD
    time_of_occurence = models.IntegerField()
    type_of_burst = models.CharField(max_length=50) 

class XRayDataModel(models.Model):
    plot_data = models.CharField(max_length=1000, default="")
    file_name = models.CharField(max_length=50)
    date_uploaded = models.DateField(default=datetime.date.today)
    bursts = models.ManyToManyField(BurstModel)


