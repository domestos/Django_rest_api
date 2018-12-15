from django.shortcuts import render
from employees.models import Employee, Position
from .serializers import EmployeeSerializers  , PositionSerializers
from rest_framework import viewsets
from rest_framework import filters


def index(request):
    return render(request, 'employees/index.html')


class EmployeesViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    # filter_backends = (filters.SearchFilter,) # add this line
    # ordering_fields = (
    #      'name',
    #  )
    search_fields = (
         'name',
     )

class PositionViewSets(viewsets.ModelViewSet):
     queryset = Position.objects.all()
     serializer_class = PositionSerializers
