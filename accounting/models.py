from django.db import models

# Create your models here.

class C_Details(models.Model):
    CustID = models.AutoField(primary_key=True)
    CustName = models.CharField(max_length=200)
    AddStreet = models.CharField(max_length=200)
    AddDistrict = models.CharField(max_length=200)
    AddState = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=10)
    PendingAmount = models.IntegerField(default=0)

class Manager(models.Model):
    ManaID = models.AutoField(primary_key=True)
    ManaName = models.CharField(max_length=200)
    ManaAuth = models.CharField(max_length=10, default='Normal') #can be normal or superuser
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
