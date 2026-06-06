# portfolio-dashboard

Live executive-style portfolio dashboard for Matheus Binicheski. FastAPI + Jinja2 SSR + Three.js particle network background. Deployed on Railway.

## Local development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://localhost:8000`.

## Editing content

Everything lives in `app/data.py`. Update KPIs, selected work, experience, stack groups, and certifications there. The FastAPI app re-reads the module on every request so local edits show up without a restart.

## Resume PDF download

Drop the latest tailored PDF at:

```
static/resume/Resume Matheus Binicheski.pdf
```

The `/resume.pdf` route and the Download button serve that file. If it is missing, the route returns a 404 with a friendly message.

## Deploy on Railway

1. Push this repo to GitHub.
2. In Railway: `New Project` → `Deploy from GitHub repo` → select this repo.
3. Railway auto-detects Nixpacks + Python. No env vars required.
4. The `Procfile` and `railway.json` cover both build paths.
5. Healthcheck is at `/healthz`.

After the first deploy, copy the public Railway URL (e.g. `https://portfolio-dashboard-production.up.railway.app`) into your job applications as the **Portfolio URL**.

## Structure

```
app/
  main.py              # FastAPI app, routes, static mount
  data.py              # single source of truth — edit content here
  templates/index.html # Jinja2 template
static/
  css/style.css        # executive palette + responsive grid
  js/main.js           # Three.js particle network + scroll reveals
  img/                 # any avatars or screenshots
  resume/              # drop your latest tailored PDF here
requirements.txt
Procfile
railway.json
README.md
```

## Why this exists

A recruiter scanning a job application has ~45 seconds for your portfolio link. A static GitHub README is fine for engineers reviewing your code; a polished landing page is what a sourcer or hiring manager actually wants when they say "send me your portfolio."

This site is the second one (the landing page). The actual code repos at `github.com/MatheusBinicheski/portfolio` are the first one. The two complement each other.
