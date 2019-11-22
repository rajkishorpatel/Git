from django.db import models

class Employee(models.Model):
    Eid = models.IntegerField()
    Ename = models.CharField(max_length=30)
    Edesignation = models.CharField(max_length=30)
    Eadreess = models.CharField(max_length=30)
    Esalery = models.IntegerField()


