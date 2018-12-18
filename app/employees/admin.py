from django.contrib import admin

# Register your models here.
from employees.models import Employee
from employees.models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    position = ('__str__', 'position')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    name = ('__str__', 'name', 'email', 'position')
    search_fields = ('name', 'email', 'position')
    # DISPLAYS MODEL'S COLUMNS IN ADMIN PAGE      ======
    # ****** Shows selected columns ******
    # list_display = ['name', 'email', 'first_work_day', 'position_id']
    # ****** Shows all columns  ******
    list_display= [field.name for field in Employee._meta.fields]
    # ****** Dont show these columns in form
    # exclude = ['name', 'email']
    # ****** Show only these columns in form
    # fields = ['name']
    list_filter = ['position_id', 'first_work_day']