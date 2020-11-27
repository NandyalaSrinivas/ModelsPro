# proxy means making duplicate and controlling
# Proxey model is used to control or manage the main model when  proxy =True
# abstact model does't create database table

from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    contact = models.CharField(max_length=10)


class Emp(Person):
    class Meta:
        proxy = True
