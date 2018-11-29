from rest_framework import serializers
from employees.models import *


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'first_day', 'last_day')
