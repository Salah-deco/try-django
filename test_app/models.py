from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.TextField() 
    last_name  = models.TextField()
    age        = models.IntegerField()