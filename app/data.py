"""Source of truth for the portfolio dashboard.

Edit this file to update content; the FastAPI app re-reads it on each request.
"""

from __future__ import annotations


IDENTITY = {
    "name": "Matheus Binicheski",
    "title": "Senior Software Engineer · AI / Agentic Systems · Node + Python + PostgreSQL",
    "tagline": "I build production AI systems that ship, measure, and don't fall over at 3 AM.",
    "location": "Brasília, Brazil · UTC-3 · Full US Eastern overlap",
    "email": "binimasteritguy@gmail.com",
    "linkedin": "https://www.linkedin.com/in/matheus-binicheski-81354ba8",
    "github": "https://github.com/MatheusBinicheski",
    "portfolio_repo": "https://github.com/MatheusBinicheski/portfolio",
    "phone_display": "+55 61 9·8639·0503",
}


KPIS = [
    {
        "metric": "10+",
        "unit": "years",
        "label": "Senior engineering practice",
        "detail": "Backend, full-stack, infra/telecom, and AI in parallel.",
        "icon": "clock",
    },
    {
        "metric": "$1.2M",
        "unit": "USD/yr",
        "label": "Cost reduction shipped",
        "detail": "Node.js automation platform · UBEC client · in production for years.",
        "icon": "dollar",
    },
    {
        "metric": "360×",
        "unit": "faster",
        "label": "Performance rebuild",
        "detail": "Public-sector Postgres batch: ~2 hours → under 20 seconds.",
        "icon": "bolt",
    },
    {
        "metric": "~40%",
        "unit": "SDR cost",
        "label": "Cut via LLM lead pipeline",
        "detail": "Anthropic Claude classifier · structured outputs · evals as artifact.",
        "icon": "ai",
    },
]


SELECTED_WORK = [
    {
        "slug": "ubec-automation",
        "title": "$1.2M / year operational cost reduction",
        "client": "UBEC · via Webum",
        "summary": (
            "Replaced a manual customer-service triage operation with an event-driven "
            "Node.js automation platform. Customer requests are normalized, classified, "
            "and routed to the right downstream workflow without human triage in the "
            "middle. I owned end-to-end architecture, implementation, and rollout."
        ),
        "metric": "$1.2M USD/year recurring savings",
        "stack": ["Node.js", "TypeScript", "Express", "PostgreSQL", "Queue workers", "AWS", "Docker"],
        "link": None,
        "year": "2022 – 2024",
    },
    {
        "slug": "gov-mt-perf",
        "title": "Public-sector batch: 2 hours → under 20 seconds",
        "client": "Mato Grosso State Government · via Webum",
        "summary": (
            "Re-architected a public vaccination and service management system. "
            "Query-plan analysis, DDL refactoring, PgCat connection pooling, and "
            "hot-path rewrites in Express moved the workflow from an overnight batch "
            "to a real-time service."
        ),
        "metric": "~7,200s → <20s end-to-end (≈ 360× faster)",
        "stack": ["Node.js", "Express", "PostgreSQL", "PgCat", "DDL refactoring"],
        "link": None,
        "year": "2023",
    },
    {
        "slug": "meta-capi-bridge",
        "title": "Meta Conversions API bridge with event_id dedup",
        "client": "Multiple direct-to-consumer brands (B2B)",
        "summary": (
            "Server-side conversion pipeline that ingests checkout postbacks from several "
            "providers with different schemas, deduplicates by event_id with a TTL store "
            "that outlasts 4-hour Meta outages, hashes PII to spec, and forwards to "
            "Meta v21 with retry-and-backoff. Replaced fragile Pixel-only attribution; "
            "recovered an estimated 20–30% of lost conversion volume."
        ),
        "metric": "Pixel + CAPI dedup back above 80% in 48h",
        "stack": ["Python", "FastAPI", "Pydantic", "httpx", "Docker", "Meta Graph API v21"],
        "link": "https://github.com/MatheusBinicheski/portfolio/tree/main/meta-capi-bridge-example",
        "year": "2024 – present",
    },
    {
        "slug": "jobhunter",
        "title": "JobHunter — ATS-tailored resumes + remote job aggregation",
        "client": "Personal · open-source",
        "summary": (
            "End-to-end remote-job platform: aggregates from RemoteOK, WeWorkRemotely, "
            "and HN public APIs, scores postings against my profile, picks a CV variant "
            "(Senior SWE / Infra+VoIP / Eng Manager / MarTech Operator), and renders a "
            "tailored PDF per application with a JSON audit sidecar. Built over a weekend, "
            "refined daily."
        ),
        "metric": "From 0 to 22 ATS-tailored applications in 2 days",
        "stack": ["Python", "FastAPI", "Jinja2", "Headless Chrome", "Public job APIs"],
        "link": "https://github.com/MatheusBinicheski/portfolio/tree/main/jobhunter",
        "year": "2026",
    },
]


EXPERIENCE_TIMELINE = [
    {
        "company": "Webum",
        "role": "Senior Software Engineer",
        "period": "Jan 2021 – Present",
        "summary": (
            "Architect and ship Node.js services and modern web apps for public-sector "
            "and enterprise clients. Backend, distributed systems, database optimization, "
            "automation."
        ),
        "stack": ["Node.js", "TypeScript", "Express", "PostgreSQL", "SQL Server", "PgCat", "React", "Next.js"],
        "current": True,
    },
    {
        "company": "Independent Contractor (PJ)",
        "role": "Full-stack Engineer / AI Automation Consultant",
        "period": "Jan 2021 – Present",
        "summary": (
            "Parallel B2B contracting. Insurance automation platforms, marketing event "
            "bridges, executive analytics dashboards, conversational SDR bots. Stack: "
            "FastAPI + Postgres + Anthropic Claude + Playwright on Docker + Railway."
        ),
        "stack": ["Python", "FastAPI", "PostgreSQL", "Docker", "AWS", "Railway", "Anthropic API", "Playwright"],
        "current": True,
    },
    {
        "company": "Synapse Brasil Tecnologia",
        "role": "Mid-Level Frontend Engineer",
        "period": "Apr 2017 – Dec 2020",
        "summary": (
            "Built high-performance React/Next.js UIs and integrated them with backend "
            "services. Performance refactor cut initial load time by ~40%."
        ),
        "stack": ["React", "Next.js", "TailwindCSS", "Node.js", "GraphQL", "Redux"],
        "current": False,
    },
    {
        "company": "Synapse Brasil Tecnologia",
        "role": "Infrastructure & Telecom Analyst",
        "period": "Jan 2015 – Dec 2020 · parallel role",
        "summary": (
            "VMware / Hyper-V / Xen hosts; Asterisk/FreePBX/Elastix VoIP platforms; "
            "PFSense edge firewalls with VLAN, captive portal, traffic shaping; OpenVPN "
            "and IPsec with OSPF redundancy. Active Directory, DNS, DHCP, LDAP-backed "
            "endpoint security."
        ),
        "stack": ["Asterisk", "FreePBX", "PFSense", "OpenVPN", "IPsec", "OSPF", "VMware", "Hyper-V", "Active Directory"],
        "current": False,
    },
    {
        "company": "Central IT",
        "role": "Telecom / IP Telephony Intern",
        "period": "2014 – 2015",
        "summary": (
            "Asterisk-based phone platforms: extensions, IVRs, queues, trunks between "
            "digital PBXs. PHP/JavaScript automation for reporting. 2nd-level call-center "
            "support."
        ),
        "stack": ["Asterisk", "PHP", "JavaScript"],
        "current": False,
    },
]


STACK_GROUPS = [
    {
        "label": "Languages",
        "items_list": ["Python", "TypeScript", "JavaScript", "Node.js", "SQL", "PHP", "HTML", "CSS"],
    },
    {
        "label": "Backend & API",
        "items_list": ["FastAPI", "Express.js", "REST", "GraphQL", "WebSockets", "Pydantic"],
    },
    {
        "label": "Frontend",
        "items_list": ["React", "React Native", "Next.js", "TailwindCSS", "Redux"],
    },
    {
        "label": "Data",
        "items_list": ["PostgreSQL", "PgCat", "SQL Server", "MySQL", "Vector DBs"],
    },
    {
        "label": "Cloud & DevOps",
        "items_list": ["Docker", "AWS", "Railway", "GitHub Actions", "GitLab CI", "Linux"],
    },
    {
        "label": "AI / Automation",
        "items_list": ["Anthropic Claude API", "OpenAI API", "Claude Code", "Playwright", "Selenium", "Meta Graph API"],
    },
    {
        "label": "VoIP / Telecom",
        "items_list": ["Asterisk (DCAA)", "FreePBX", "Elastix", "SIP", "OpenVPN", "IPsec", "PFSense"],
    },
]


CERTIFICATIONS = [
    {"name": "Executive MBA — Entrepreneurship, Marketing and Finance", "issuer": "Unyleya", "year": "2025"},
    {"name": "B.Sc. — Management Information Systems", "issuer": "Universidade Paulista (UNIP)", "year": "2017"},
    {"name": "DCAA — Digium Certified Asterisk Administrator", "issuer": "Digium / Sangoma", "year": "2018"},
]


CASE_STUDIES_LINK = "https://github.com/MatheusBinicheski/portfolio"


# Optional download — set to the path of your most up-to-date PDF
RESUME_PDF_RELATIVE = "/static/resume/Resume Matheus Binicheski.pdf"
