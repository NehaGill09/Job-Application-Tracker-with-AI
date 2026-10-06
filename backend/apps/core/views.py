from django.db import connection
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db.models import Count
from apps.jobs.models import Application
class HealthView(APIView):
    permission_classes=[]
    def get(self,request): connection.ensure_connection(); return JsonResponse({'status':'ok','database':'ok'})
class DashboardView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        qs=Application.objects.filter(user=request.user)
        return JsonResponse({'total':qs.count(),'active':qs.exclude(status__in=['rejected','withdrawn','accepted']).count(),'by_status':list(qs.values('status').annotate(count=Count('id')))})
