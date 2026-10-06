from django.conf import settings
from django.db import models

class Job(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='jobs')
    company=models.CharField(max_length=255); title=models.CharField(max_length=255); location=models.CharField(max_length=255,blank=True)
    url=models.URLField(blank=True); description=models.TextField(); source=models.CharField(max_length=40,default='manual')
    salary_min=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True); salary_max=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    remote=models.BooleanField(default=False); tags=models.JSONField(default=list); parsed_requirements=models.JSONField(default=dict)
    created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)

class Application(models.Model):
    STATUS=[('saved','Saved'),('applied','Applied'),('screening','Screening'),('interview','Interview'),('offer','Offer'),('accepted','Accepted'),('rejected','Rejected'),('withdrawn','Withdrawn')]
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='applications'); job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    status=models.CharField(max_length=30,choices=STATUS,default='saved'); applied_at=models.DateTimeField(null=True,blank=True); notes=models.TextField(blank=True)
    priority=models.PositiveSmallIntegerField(default=3); next_action=models.CharField(max_length=255,blank=True); next_action_at=models.DateTimeField(null=True,blank=True); metadata=models.JSONField(default=dict)
    created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['user','job'],name='unique_user_job_application')]

class Resume(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='resumes'); name=models.CharField(max_length=255); summary=models.TextField(blank=True)
    content=models.JSONField(default=dict); is_default=models.BooleanField(default=False); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)

class ResumeVersion(models.Model):
    resume=models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='versions'); version=models.PositiveIntegerField(); content=models.JSONField(default=dict); change_note=models.CharField(max_length=255,blank=True); created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['resume','version'],name='unique_resume_version')]

class Interview(models.Model):
    application=models.ForeignKey(Application,on_delete=models.CASCADE,related_name='interviews'); scheduled_at=models.DateTimeField(); duration_minutes=models.PositiveIntegerField(default=60)
    interview_type=models.CharField(max_length=80,default='video'); interviewer=models.CharField(max_length=255,blank=True); meeting_url=models.URLField(blank=True); notes=models.TextField(blank=True); outcome=models.CharField(max_length=255,blank=True)

class FollowUp(models.Model):
    application=models.ForeignKey(Application,on_delete=models.CASCADE,related_name='follow_ups'); due_at=models.DateTimeField(); channel=models.CharField(max_length=50,default='email')
    subject=models.CharField(max_length=255,blank=True); message=models.TextField(blank=True); sent_at=models.DateTimeField(null=True,blank=True); status=models.CharField(max_length=30,default='planned')
