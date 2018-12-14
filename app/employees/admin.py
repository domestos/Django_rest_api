from django.contrib import admin

# Register your models here.
from employees.models import Employee
from employees.models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    position = ('__str__', 'position')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    name = ('__str__', 'name', 'position')
    search_fields = ('name', 'first_work_day')