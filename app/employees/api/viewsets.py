from django.shortcuts import render
from employees.models import Employee, Position
from .serializers import EmployeeSerializers, PositionSerializers
from rest_framework import viewsets


def index(request):
    return render(request, 'employees/index.html')


class EmployeesViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class PositionViewSets(viewsets.ModelViewSet):
     queryset = Position.objects.all()
     serializer_class = PositionSerializers
