from django.contrib import admin

# Register your models here.
from django.contrib.auth import forms
from django.forms import ModelForm
from inventory.models import Location, Type, Item

#===================== ACTION ================================
def generate_qr_code(modeladmin, request, queryset):
    print('QR-code Generate ')
    items = queryset.all()
    for item in items:
        print(item.id)
    generate_qr_code.short_description = "QR-code Generate "


def get_win_audit(modeladmin, request, queryset):
    print('QR-code Generate ')
    items = queryset.all()
    for item in items:
        print(item.id)
    generate_qr_code.short_description = "QR-code Generate "

def print_qr_code(modeladmin, request, queryset):
    print('QR-code Print')
    items = queryset.all()
    for item in items:
        print(item.id)
    generate_qr_code.short_description = "QR-code Print"


#===================== ACTION ================================


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    location = ('__str__', 'location')
    search_fields = ['location']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    type = ('__str__', 'type')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]
    change_list_template = 'admin/inventory/inventory_change_list_admin.html'
    search_fields = ['item', 'owner', 'location']
    autocomplete_fields = ['owner', 'location']
    item = ('__str__', 'item')
    list_filter = ['type', 'owner', 'location']
    actions = [generate_qr_code , print_qr_code]