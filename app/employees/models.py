from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField('Name', max_length=80)
    first_day = models.DateField()
    last_day = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
