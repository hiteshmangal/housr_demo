from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, m2m_changed
from accounts.models import Employee

@receiver(m2m_changed, sender=Employee.assigned_groups.through)
def something(sender, instance, action, **kwargs):
    if action=="post_add" or action=="post_remove" or action=="post_clear":
        instance.user.groups.set(instance.assigned_groups.all())
