from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Job,Application,Resume,Interview,FollowUp
from .serializers import JobSerializer,ApplicationSerializer,ResumeSerializer,InterviewSerializer,FollowUpSerializer
class UserScoped(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    def get_queryset(self): return self.queryset.filter(user=self.request.user)
    def perform_create(self,serializer): serializer.save(user=self.request.user)
class JobViewSet(UserScoped): queryset=Job.objects.all(); serializer_class=JobSerializer
class ApplicationViewSet(UserScoped): queryset=Application.objects.select_related('job'); serializer_class=ApplicationSerializer
class ResumeViewSet(UserScoped): queryset=Resume.objects.all(); serializer_class=ResumeSerializer
class InterviewViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]; queryset=Interview.objects.all(); serializer_class=InterviewSerializer
    def get_queryset(self): return self.queryset.filter(application__user=self.request.user)
class FollowUpViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]; queryset=FollowUp.objects.all(); serializer_class=FollowUpSerializer
    def get_queryset(self): return self.queryset.filter(application__user=self.request.user)
