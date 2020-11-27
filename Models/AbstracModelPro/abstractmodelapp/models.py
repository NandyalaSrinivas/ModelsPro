#Abstract model is used to reduce duplicate coding from non-abstact model
# when in Meta class abstract = True
# Abstracl model does't create database table for abstract class
# No need register admin for abstract class 

from django.db import models


class BasicModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    address = models.TextField()
    email = models.EmailField(max_length=100, unique= True)


    class Meta:
        abstract = True


class CustomerModel(BasicModel):
    customerid = models.CharField(max_length=10)
    customerphone = models.CharField(max_length=10, unique= True)


class StaffModel(BasicModel):
    staffid = models.CharField(max_length=10)
    position = models.CharField(max_length=100)
