from django.shortcuts import render
from employees.models import Employee
from .serializers import EmployeeSerializers
from rest_framework import viewsets


def index(request):
    return render(request, 'employees/index.html')


class EmployeesViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
