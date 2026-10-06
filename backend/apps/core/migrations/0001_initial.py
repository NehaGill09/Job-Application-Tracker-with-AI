from django.conf import settings
from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
 operations=[migrations.CreateModel(name='Profile',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('headline',models.CharField(blank=True,max_length=255)),('location',models.CharField(blank=True,max_length=255)),('target_roles',models.JSONField(default=list)),('skills',models.JSONField(default=list)),('preferences',models.JSONField(default=dict)),('created_at',models.DateTimeField(auto_now_add=True)),('updated_at',models.DateTimeField(auto_now=True)),('user',models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,related_name='profile',to=settings.AUTH_USER_MODEL))]),migrations.CreateModel(name='AuditEvent',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('action',models.CharField(max_length=120)),('entity_type',models.CharField(max_length=80)),('entity_id',models.CharField(blank=True,max_length=80)),('metadata',models.JSONField(default=dict)),('created_at',models.DateTimeField(auto_now_add=True)),('user',models.ForeignKey(blank=True,null=True,on_delete=django.db.models.deletion.SET_NULL,to=settings.AUTH_USER_MODEL))])]
