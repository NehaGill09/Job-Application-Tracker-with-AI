from django.conf import settings
from django.db import models
class AIRequest(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); feature=models.CharField(max_length=100); model=models.CharField(max_length=100); status=models.CharField(max_length=30,default='success')
    prompt_tokens=models.PositiveIntegerField(default=0); completion_tokens=models.PositiveIntegerField(default=0); total_tokens=models.PositiveIntegerField(default=0); latency_ms=models.PositiveIntegerField(default=0)
    estimated_cost_usd=models.DecimalField(max_digits=12,decimal_places=8,default=0); metadata=models.JSONField(default=dict); created_at=models.DateTimeField(auto_now_add=True)
class PromptVersion(models.Model):
    key=models.CharField(max_length=120); version=models.CharField(max_length=30); system_prompt=models.TextField(); user_template=models.TextField(); active=models.BooleanField(default=False); created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['key','version'],name='unique_prompt_version')]
class AIArtifact(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); feature=models.CharField(max_length=100); input_hash=models.CharField(max_length=64); output=models.JSONField(default=dict); created_at=models.DateTimeField(auto_now_add=True)
