from employees.api.viewsets import EmployeesViewSets ,PositionViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeesViewSets)
router.register('position', PositionViewSets)