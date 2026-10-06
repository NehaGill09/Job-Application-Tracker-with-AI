# Architecture

The platform is a user-scoped career workspace. Django/DRF owns domain rules and authorization, PostgreSQL stores jobs/applications/resume versions/interviews, Redis/Celery handles deferred work, and React consumes REST APIs.

AI workflows: job-fit analysis, ATS-safe resume tailoring, cover letters, and interview preparation. AI calls are isolated behind `AIService` and record latency, token usage, model, feature, and artifact references.

Security: authenticated user scoping, throttled endpoints, environment-only provider secrets, audit foundations, and an explicit rule that AI must never invent candidate experience.
