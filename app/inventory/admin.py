from django.contrib import admin

# Register your models here.
from inventory.models import Location, Type, Item


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    location = ('__str__', 'location')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    type = ('__str__', 'type')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    item = ('__str__', 'item')
    list_display= [field.name for field in Item._meta.fields]
    list_filter = ['type', 'location']