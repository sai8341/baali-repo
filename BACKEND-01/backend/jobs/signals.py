# jobs/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Job, Category

@receiver(post_save, sender=Job)
def update_category_job_count_on_create(sender, instance, created, **kwargs):
    if created:
        instance.category.update_job_count()


@receiver(post_delete, sender=Job)
def update_category_job_count_on_delete(sender, instance, **kwargs):
    instance.category.update_job_count()
