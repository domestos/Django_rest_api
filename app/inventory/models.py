from django.db import models
from employees.models import Employee
# Create your models here.

class Type(models.Model):
    type = models.CharField('type', max_length=80, unique=True)
    class Meta:
        #set the name of table into admin panel
        verbose_name = "Types"
        verbose_name_plural = "Type"
        ordering = ["type"]

    def __str__(self):
        return self.type


class Location(models.Model):
    location = models.CharField('location', max_length=80, unique=True)
    class Meta:
        #set the name of table into admin panel
        verbose_name = "Locations"
        verbose_name_plural = "Location"
        ordering = ["location"]

    def __str__(self):
        return self.location


class Item(models.Model):
    item =  models.CharField('item', max_length=80)
    number = models.CharField('number', max_length=80)
    type = models.ForeignKey(Type, default='', on_delete=models.SET_DEFAULT, null=True )
    owner = models.ForeignKey(Employee, default='', on_delete=models.SET_DEFAULT, null=True )
    location = models.ForeignKey(Location, default='', on_delete=models.SET_DEFAULT, null=True )
    description = models.TextField(blank=True, null=True)