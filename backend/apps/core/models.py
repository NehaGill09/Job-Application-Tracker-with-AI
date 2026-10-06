from django.conf import settings
from django.db import models
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    headline=models.CharField(max_length=255,blank=True); location=models.CharField(max_length=255,blank=True)
    target_roles=models.JSONField(default=list); skills=models.JSONField(default=list); preferences=models.JSONField(default=dict)
    created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
class AuditEvent(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL); action=models.CharField(max_length=120); entity_type=models.CharField(max_length=80); entity_id=models.CharField(max_length=80,blank=True); metadata=models.JSONField(default=dict); created_at=models.DateTimeField(auto_now_add=True)
