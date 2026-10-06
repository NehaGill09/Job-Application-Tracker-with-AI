from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum,Avg,Count
from .services import AIService
from .models import AIRequest
class AIBase(APIView):
    permission_classes=[IsAuthenticated]
    def run(self,r,feature,fields):
        data={k:r.data.get(k,'') for k in fields}
        if any(not str(v).strip() for v in data.values()): return Response({'detail':'Missing required input.'},status=400)
        try: return Response(AIService().run(r.user,feature,**data))
        except Exception: return Response({'detail':'AI provider request failed.'},status=502)
class AIAnalyzeJobView(AIBase):
    def post(self,r): return self.run(r,'analyze_job',['job','profile'])
class AITailorResumeView(AIBase):
    def post(self,r): return self.run(r,'tailor_resume',['job','resume'])
class AICoverLetterView(AIBase):
    def post(self,r): return self.run(r,'cover_letter',['job','profile'])
class AIInterviewPrepView(AIBase):
    def post(self,r): return self.run(r,'interview_prep',['job','application'])
class AIUsageView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,r): return Response(AIRequest.objects.filter(user=r.user).aggregate(requests=Count('id'),tokens=Sum('total_tokens'),avg_latency_ms=Avg('latency_ms'),cost=Sum('estimated_cost_usd')))
