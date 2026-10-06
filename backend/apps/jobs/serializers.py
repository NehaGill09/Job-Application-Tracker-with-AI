from rest_framework import serializers
from .models import Job,Application,Resume,Interview,FollowUp
class OwnedSerializer(serializers.ModelSerializer):
    def create(self,validated_data): return self.Meta.model.objects.create(user=self.context['request'].user,**validated_data)
class JobSerializer(OwnedSerializer):
    class Meta: model=Job; fields='__all__'; read_only_fields=['user']
class ApplicationSerializer(OwnedSerializer):
    class Meta: model=Application; fields='__all__'; read_only_fields=['user']
class ResumeSerializer(OwnedSerializer):
    class Meta: model=Resume; fields='__all__'; read_only_fields=['user']
class InterviewSerializer(serializers.ModelSerializer):
    class Meta: model=Interview; fields='__all__'
class FollowUpSerializer(serializers.ModelSerializer):
    class Meta: model=FollowUp; fields='__all__'
