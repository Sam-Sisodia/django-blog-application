from django.db import models

# Create your models here.



class Bugger(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='staic/media')
    cusine = models.CharField(max_length=200)
    rating  = models.CharField(max_length=200)
    flavor  = models.CharField(max_length=200)