from rest_framework import serializers
from employees.models import *


class PositionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        filds = ('position')


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    position = serializers.HyperlinkedRelatedField(view_name='position', many=False, read_only=True)
    class Meta:
        model = Employee
        fields = ('name', 'first_work_day', 'position', 'last_work_dat')

