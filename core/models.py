from django.db import models

class Student(models.Model):
    name= models.CharField(max_length=60)
    roll= models.IntegerField()
    city= models.CharField(max_length=100)
    age= models.IntegerField(null=True)
