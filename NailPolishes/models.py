from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Allpolishes(models.Model):
    brandname = models.CharField(max_length=200) 
    color = models.CharField(max_length=100)
    startedfrom = models.DateTimeField('startedfrom')

    def __str__(self):
        return self.brandname
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.startedfrom <= now
#note: always makemigrations, sqlmigrate and migrate after creating models
class polishdetails(models.Model):
    polishtype = models.ForeignKey(Allpolishes, on_delete = models.CASCADE)
    nailtype = models.CharField(max_length= 500)
    your_choice  = models.BooleanField(default= False)

    def __str__(self):
        return str (self.nailtype)