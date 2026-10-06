import hashlib,json,time
from openai import OpenAI
from django.conf import settings
from .models import AIRequest,AIArtifact
PROMPTS={'analyze_job':('You are a senior recruiter. Return JSON with match_score,strengths,gaps,keywords,recommendations.','Analyze this job against this profile. JOB:{job}\nPROFILE:{profile}'),'tailor_resume':('You are an ATS resume expert. Preserve truth; never invent facts. Return JSON with summary,skills,bullets,rationale.','Tailor this resume for this job. JOB:{job}\nRESUME:{resume}'),'cover_letter':('Write a concise specific cover letter. Never invent facts.','Write a tailored cover letter. JOB:{job}\nPROFILE:{profile}'),'interview_prep':('You are an expert interview coach. Return JSON with questions,model_points,stories,questions_to_ask.','Prepare coaching. JOB:{job}\nAPPLICATION:{application}')}
class AIService:
    def __init__(self): self.client=OpenAI(api_key=settings.OPENAI_API_KEY); self.model=settings.OPENAI_MODEL
    def run(self,user,feature,**data):
        system,template=PROMPTS[feature]; prompt=template.format(**data); started=time.perf_counter()
        try:
            r=self.client.chat.completions.create(model=self.model,messages=[{'role':'system','content':system},{'role':'user','content':prompt}],response_format={'type':'json_object'})
            raw=r.choices[0].message.content or '{}'; output=json.loads(raw); u=r.usage; pt=u.prompt_tokens if u else 0; ct=u.completion_tokens if u else 0
            artifact=AIArtifact.objects.create(user=user,feature=feature,input_hash=hashlib.sha256(prompt.encode()).hexdigest(),output=output)
            AIRequest.objects.create(user=user,feature=feature,model=self.model,prompt_tokens=pt,completion_tokens=ct,total_tokens=pt+ct,latency_ms=int((time.perf_counter()-started)*1000),metadata={'artifact_id':artifact.id})
            return output
        except Exception as exc:
            AIRequest.objects.create(user=user,feature=feature,model=self.model,status='error',latency_ms=int((time.perf_counter()-started)*1000),metadata={'error':str(exc)[:300]}); raise
