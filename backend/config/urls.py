from django.urls import include,path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from apps.jobs.views import JobViewSet,ApplicationViewSet,ResumeViewSet,InterviewViewSet,FollowUpViewSet
from apps.ai.views import AIAnalyzeJobView,AITailorResumeView,AICoverLetterView,AIInterviewPrepView,AIUsageView
from apps.core.views import DashboardView,HealthView
router=DefaultRouter()
router.register('jobs',JobViewSet,basename='job'); router.register('applications',ApplicationViewSet,basename='application'); router.register('resumes',ResumeViewSet,basename='resume'); router.register('interviews',InterviewViewSet,basename='interview'); router.register('follow-ups',FollowUpViewSet,basename='followup')
urlpatterns=[path('health/',HealthView.as_view()),path('api/dashboard/',DashboardView.as_view()),path('api/',include(router.urls)),path('api/ai/analyze-job/',AIAnalyzeJobView.as_view()),path('api/ai/tailor-resume/',AITailorResumeView.as_view()),path('api/ai/cover-letter/',AICoverLetterView.as_view()),path('api/ai/interview-prep/',AIInterviewPrepView.as_view()),path('api/ai/usage/',AIUsageView.as_view()),path('api/auth/token/',TokenObtainPairView.as_view()),path('api/auth/token/refresh/',TokenRefreshView.as_view())]
