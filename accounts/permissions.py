from django.contrib.auth.models import Group, Permission
from django.db.models import Q


def create_custom_permissions():
    # Resident model permissions
    resident_permissions = [
        ('view_resident', 'Can view resident'),
        ('change_resident', 'Can change resident'),
        ('delete_resident', 'Can delete resident'),
    ]

    # Employee model permissions
    employee_permissions = [
        ('view_employee', 'Can view employee'),
        ('change_employee', 'Can change employee'),
        ('delete_employee', 'Can delete employee'),
    ]

    # CommunityEvent model permissions
    community_event_permissions = [
        ('view_communityevent', 'Can view community event'),
        ('change_communityevent', 'Can change community event'),
        ('delete_communityevent', 'Can delete community event'),
    ]

    # Create permissions
    for codename, name in resident_permissions + employee_permissions + community_event_permissions:
        Permission.objects.get_or_create(codename=codename, name=name)

    # Create groups
    resident_manager_group, _ = Group.objects.get_or_create(name='Resident Manager')
    operations_manager_group, _ = Group.objects.get_or_create(name='Operations Manager')
    sales_executive_group, _ = Group.objects.get_or_create(name='Sales Executive')
    community_manager_group, _ = Group.objects.get_or_create(name='Community Manager')

    # Assign permissions to groups
    resident_manager_group.permissions.add(*Permission.objects.filter(codename__startswith='view_resident'))
    operations_manager_group.permissions.add(
        *Permission.objects.filter(Q(codename__startswith='view_')|Q(codename__startswith='change_')|Q(codename__startswith='delete_'))
    )
    sales_executive_group.permissions.add(*Permission.objects.filter(codename__startswith='view_'))
    community_manager_group.permissions.add(
        *Permission.objects.filter(Q(codename__startswith='view_')|Q(codename__startswith='change_')|Q(codename__startswith='delete_'))
    )
