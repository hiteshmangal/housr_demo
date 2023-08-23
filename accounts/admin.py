from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Resident, Employee, CommunityEvent


# Custom admin class for Group with filter_horizontal for permissions
class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


# Unregister and reregister Group with the custom admin class
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = (
        'resident_name', 'resident_building_name', 'phone_number', 'email_id', 'contract_start_date', 'contract_end_date')
    list_filter = ('resident_building_name', 'contract_start_date', 'contract_end_date')
    search_fields = ('resident_name', 'phone_number', 'email_id')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    filter_horizontal = ('assigned_groups',)
    list_display = ('user', 'employee_name', 'contact_number', 'email_id', 'get_assigned_groups')

    def get_assigned_groups(self, obj):
        return ", ".join([group.name for group in obj.assigned_groups.all()])

    get_assigned_groups.short_description = 'Assigned Groups'


@admin.register(CommunityEvent)
class CommunityEventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_description')
    list_filter = ('event_date',)
    search_fields = ('event_name', 'event_description')
