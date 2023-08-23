from django.db import models
from django.contrib.auth.models import Group


class Resident(models.Model):
    resident_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    resident_building_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    move_in_date = models.DateField(null=True, blank=True)
    move_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.resident_name


class Employee(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    employee_name = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    assigned_groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.employee_name

class CommunityEvent(models.Model):
    event_name = models.CharField(max_length=100, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    event_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.event_name
