from celery import shared_task
from django.utils import timezone
from apps.jobs.models import FollowUp
@shared_task
def mark_due_followups(): return FollowUp.objects.filter(status='planned',due_at__lte=timezone.now()).update(status='due')