# AI Job Application Tracker with AI

A production-oriented **Job Application Tracker** built as a full-stack portfolio project with Django, Django REST Framework, PostgreSQL, React/TypeScript, Celery, Redis, and OpenAI.

## What is implemented

### Career workspace
- User-scoped job records with company, title, location, URL, salary, remote status, source, tags, and parsed requirements.
- Application lifecycle: saved → applied → screening → interview → offer → accepted/rejected/withdrawn.
- Priority, notes, next-action tracking, and timestamps.
- Resume records plus immutable resume-version history.
- Interview scheduling, interviewer details, meeting links, outcomes, and notes.
- Follow-up planning with due-state Celery automation.
- Profile and audit-event foundations for a larger career workspace.

### AI career copilot
- **Job fit analysis**: match score, strengths, gaps, keywords, and recommendations.
- **ATS-safe resume tailoring**: structured output while explicitly prohibiting invented experience.
- **Cover letter generation**: job-specific, concise, fact-preserving copy.
- **Interview preparation**: questions, model talking points, STAR-story prompts, and questions to ask.
- Prompt-version model and AI artifact history.
- AI telemetry for model, latency, token counts, status, and artifact references.
- Throttled AI endpoints and isolated provider service layer.

### Engineering
- JWT authentication.
- Strict per-user query scoping.
- Nested-resource ownership validation.
- PostgreSQL-ready configuration with Docker Compose.
- Redis + Celery worker.
- Health endpoint.
- Django migrations.
- Pytest foundation.
- React + TypeScript + Vite command-center UI.
- GitHub Actions CI for Python checks and frontend builds.

## API surface

- `POST /api/auth/token/`
- `POST /api/auth/token/refresh/`
- `GET/POST /api/jobs/`
- `GET/POST /api/applications/`
- `GET/POST /api/resumes/`
- `GET/POST /api/interviews/`
- `GET/POST /api/follow-ups/`
- `GET /api/dashboard/`
- `POST /api/ai/analyze-job/`
- `POST /api/ai/tailor-resume/`
- `POST /api/ai/cover-letter/`
- `POST /api/ai/interview-prep/`
- `GET /api/ai/usage/`
- `GET /health/`

## Run locally

1. Copy `.env.example` to `.env` and provide an OpenAI API key.
2. Run `docker compose up --build`.
3. Create a Django user with `docker compose exec backend python manage.py createsuperuser`.
4. Obtain a JWT from `/api/auth/token/`.
5. Start the frontend with `cd frontend && npm install && npm run dev`.
6. Paste the JWT access token into the frontend command center.

## Architecture

See [docs/architecture.md](docs/architecture.md).

## Roadmap for the next production layer

The current repository deliberately separates foundations from features that would require external integrations. Natural next modules are job-board ingestion connectors, email/calendar connectors, resume PDF parsing/rendering, semantic job search with pgvector, advanced analytics, notification delivery, workspace/team RBAC, and LLM-as-judge evaluation suites.

> AI output must be reviewed by the candidate. The system is designed to assist with truthful career materials, not fabricate qualifications.
