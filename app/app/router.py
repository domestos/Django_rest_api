from employees.api.viewsets import EmployeesViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeesViewSets)