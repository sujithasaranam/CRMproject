from django.db import models
class User(models.Model):
    ROLE=(
        ('Employee','Employee'),
        ('StudentCounselor','StudentCounselor'),
        ('SystemAdmin','SystemAdmin'))
    Id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    roleoftheUser=models.CharField(max_length=20,choices=ROLE)

class EnquiryForm(models.Model):
    Id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    course=models.CharField(max_length=50)
    interst=models.CharField(max_length=100)

class claimedEmployee(models.Model):
    Id=models.AutoField(primary_key=True)
    cuser=models.ForeignKey(EnquiryForm,on_delete=models.CASCADE,null=True,blank=True)



# Create your models here.
