from django.db import models

# Create your models here.
class Features(models.Model):

    Name = models.CharField(max_length=200)
    Age =  models.IntegerField()
    Status = models.CharField(max_length=200)
