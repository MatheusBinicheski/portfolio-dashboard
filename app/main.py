"""Portfolio dashboard — FastAPI + Jinja2 SSR."""

from __future__ import annotations

import importlib
import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader, select_autoescape

from app import data as _data

ROOT = Path(__file__).resolve().parent.parent

# Disable Jinja2's template cache to dodge a Py3.14 dict-as-cache-key incompatibility.
_jinja_env = Environment(
    loader=FileSystemLoader(str(ROOT / "app" / "templates")),
    autoescape=select_autoescape(["html", "xml"]),
    cache_size=0,
)
TEMPLATES = Jinja2Templates(env=_jinja_env)

app = FastAPI(title="Matheus Binicheski — Engineering Portfolio")

app.mount("/static", StaticFiles(directory=str(ROOT / "static")), name="static")


def fresh_data():
    """Re-import data on every request so edits show up without a redeploy."""
    importlib.reload(_data)
    return _data


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    d = fresh_data()
    return TEMPLATES.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "identity": d.IDENTITY,
            "kpis": d.KPIS,
            "selected_work": d.SELECTED_WORK,
            "experience": d.EXPERIENCE_TIMELINE,
            "stack_groups": d.STACK_GROUPS,
            "certifications": d.CERTIFICATIONS,
            "resume_pdf": d.RESUME_PDF_RELATIVE,
            "case_studies_link": d.CASE_STUDIES_LINK,
        },
    )


@app.get("/resume.pdf")
def resume_pdf():
    """Direct download link for recruiters."""
    d = fresh_data()
    rel = d.RESUME_PDF_RELATIVE.lstrip("/")
    full = ROOT / rel
    if full.exists():
        return FileResponse(str(full), media_type="application/pdf",
                            filename="Resume Matheus Binicheski.pdf")
    return HTMLResponse(
        "<h1>Resume not bundled yet</h1><p>Add the PDF to "
        "<code>static/resume/Resume Matheus Binicheski.pdf</code> and redeploy.</p>",
        status_code=404,
    )


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/robots.txt", response_class=HTMLResponse)
def robots():
    return HTMLResponse("User-agent: *\nAllow: /\n", media_type="text/plain")
