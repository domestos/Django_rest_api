from rest_framework import serializers
from employees.models import *

#https://www.pythonblog.tk/post/drf-filtering-sorting-related-objects

class PositionSerializers(serializers.HyperlinkedModelSerializer):
   # id = serializers.IntegerField(read_only=True)
    position=serializers.StringRelatedField()
    class Meta:
        model = Position
        fields = ("id", "position")



class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    position_id = serializers.StringRelatedField(many=False)
    class Meta:
        model = Employee
        fields = (
            'name', 'email', 'first_work_day', 'position_id',  'last_work_dat', 'description'
        )
