from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Grade


@receiver(post_save, sender=Grade)
def calculate_total_grade(sender, instance, created, **kwargs):
    total = (instance.midterm or 0) + (instance.final or 0)

    if instance.total != total:
        instance.total = total
        instance.save(update_fields=['total'])
