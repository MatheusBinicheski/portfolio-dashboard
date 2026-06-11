"""Conteúdo PT-BR do portfolio dashboard — versão enxuta e visual."""

from __future__ import annotations


IDENTITY = {
    "name": "Matheus Binicheski",
    "title": "Engenheiro Sênior · IA em produção",
    "tagline": "Sistemas que entregam, são medidos e não caem às 3 da manhã.",
    "location": "Brasília · UTC-3",
    "email": "binimasteritguy@gmail.com",
    "linkedin": "https://www.linkedin.com/in/matheus-binicheski-81354ba8",
    "github": "https://github.com/MatheusBinicheski",
    "portfolio_repo": "https://github.com/MatheusBinicheski/portfolio",
    "phone_display": "+55 61 9·8639·0503",
}


KPIS = [
    {
        "metric": "10+",
        "unit": "anos",
        "label": "Engenharia sênior",
        "detail": "Backend, infra, IA em paralelo.",
    },
    {
        "metric": "US$ 1,2M",
        "unit": "/ ano",
        "label": "Custo cortado",
        "detail": "Automação Node.js em produção.",
    },
    {
        "metric": "360×",
        "unit": "mais rápido",
        "label": "Performance",
        "detail": "Batch público: 2h → <20s.",
    },
    {
        "metric": "~40%",
        "unit": "SDR",
        "label": "Custo cortado com IA",
        "detail": "Classificador em Claude.",
    },
]


SELECTED_WORK = [
    {
        "slug": "performance-media-dashboard",
        "title": "Dashboard executivo de mídia paga",
        "client": "Cliente paid media · Brasília · NDA",
        "highlights": [
            "Meta Graph API direto, sem Looker no meio",
            "Reconciliação diária com base de vendas",
            "Ranking de criativo, fadiga e eficiência",
        ],
        "metric": "Leitura do dia: 25 min → 90s",
        "stack": ["Python", "FastAPI", "Chart.js", "Meta API v21", "PostgreSQL"],
        "screenshot": "/static/img/projects/pedro_rehn.webp",
        "screenshot_caption": "Painel executivo · números anonimizados",
        "link": None,
        "year": "2025 – atual",
    },
    {
        "slug": "saude-meta-ads-dashboard",
        "title": "Diagnóstico Meta Ads + dashboard 360°",
        "client": "Clínica multiunidades DF · NDA",
        "highlights": [
            "90 dias de diagnóstico · +R$ 800k investidos",
            "Allowlist por conta de anúncio",
            "Sweet spot mapeado: mulheres 25–54 DF",
        ],
        "metric": "Realocação defendida com dados",
        "stack": ["Python", "FastAPI", "Meta API", "Chart.js"],
        "screenshot": "/static/img/projects/croe_odonto.webp",
        "screenshot_caption": "Painel multi-conta · dados anonimizados",
        "link": None,
        "year": "2026",
    },
    {
        "slug": "iag-operations",
        "title": "Painel operacional 360° do time",
        "client": "Consultoria empresarial · NDA",
        "highlights": [
            "5 pilares: KPI, entregáveis, tarefas, processos, time",
            "Cliente edita conteúdo sem mexer no código",
            "Substituiu 4 planilhas + 2 SaaS",
        ],
        "metric": "1 painel, fonte única da operação",
        "stack": ["Python", "FastAPI", "Jinja2", "Tailwind"],
        "screenshot": "/static/img/projects/iag_operations.webp",
        "screenshot_caption": "Identidade visual do cliente preservada",
        "link": None,
        "year": "2026",
    },
    {
        "slug": "ceo-presenca-digital",
        "title": "Dashboard CEO de presença digital",
        "client": "Figura pública nacional · NDA",
        "highlights": [
            "Coleta diária via Meta Graph API + cron",
            "Histórico de 12+ meses preservado",
            "1 leitor, 2 minutos no celular pela manhã",
        ],
        "metric": "Decisão da semana em 2 minutos",
        "stack": ["Python", "FastAPI", "Three.js", "PostgreSQL"],
        "screenshot": "/static/img/projects/pradoclima.webp",
        "screenshot_caption": "Dashboard CEO · números reais ocultados",
        "link": None,
        "year": "2025 – atual",
    },
    {
        "slug": "greenn-meta-capi",
        "title": "Bridge Greenn → Meta Conversions API",
        "client": "Operação DTC paid media",
        "highlights": [
            "Dedup por event_id sobrevive a apagão de 4h da Meta",
            "Hash PII na spec + retry/backoff",
            "Endpoints /raw e /raw-logs pra debug",
        ],
        "metric": "Dedup Pixel + CAPI: 18% → +80% em 48h",
        "stack": ["Python", "FastAPI", "Pydantic", "httpx", "Meta API v21"],
        "screenshot": "/static/img/projects/greenn_capi.webp",
        "screenshot_caption": "Bridge open-source · referência pública",
        "link": "https://github.com/MatheusBinicheski/portfolio/tree/main/meta-capi-bridge-example",
        "year": "2025 – atual",
    },
    {
        "slug": "ubec-automation",
        "title": "Plataforma que cortou US$ 1,2M/ano",
        "client": "Cliente B2B serviços · via Webum",
        "highlights": [
            "Triagem manual → pipeline orientado a eventos",
            "Classificação + roteamento sem humano no meio",
            "Em produção há 2+ anos",
        ],
        "metric": "US$ 1,2M USD/ano de economia recorrente",
        "stack": ["Node.js", "TypeScript", "Express", "PostgreSQL", "AWS"],
        "screenshot": None,
        "link": None,
        "year": "2022 – 2024",
    },
    {
        "slug": "gov-mt-perf",
        "title": "Batch público: 2 horas → 20 segundos",
        "client": "Gov. Mato Grosso · via Webum",
        "highlights": [
            "Análise de query plan + refactor de DDL",
            "PgCat na frente do Postgres pra pooling",
            "Reescrita dos hot-paths em Express",
        ],
        "metric": "~7.200s → <20s · 360× mais rápido",
        "stack": ["Node.js", "Express", "PostgreSQL", "PgCat"],
        "screenshot": None,
        "link": None,
        "year": "2023",
    },
]


EXPERIENCE_TIMELINE = [
    {
        "company": "Webum",
        "role": "Engenheiro Sênior",
        "period": "jan/2021 – atual",
        "summary": "Backend Node.js + Postgres pra setor público e enterprise.",
        "stack": ["Node.js", "TypeScript", "PostgreSQL", "PgCat", "React"],
        "current": True,
    },
    {
        "company": "Contratante PJ Independente",
        "role": "Full-stack · Consultor IA",
        "period": "jan/2021 – atual",
        "summary": "B2B em paralelo: automação seguros, marketing events, SDR bots.",
        "stack": ["Python", "FastAPI", "Claude", "Playwright", "Docker", "Railway"],
        "current": True,
    },
    {
        "company": "Synapse Brasil",
        "role": "Engenheiro Frontend Pleno",
        "period": "abr/2017 – dez/2020",
        "summary": "React/Next.js de alta performance. Refactor cortou load inicial em ~40%.",
        "stack": ["React", "Next.js", "TailwindCSS", "GraphQL"],
        "current": False,
    },
    {
        "company": "Synapse Brasil",
        "role": "Analista de Infra & Telecom",
        "period": "jan/2015 – dez/2020 · paralelo",
        "summary": "VMware, Asterisk/FreePBX, PFSense, OpenVPN/IPsec, Active Directory.",
        "stack": ["Asterisk", "FreePBX", "PFSense", "VMware", "AD"],
        "current": False,
    },
    {
        "company": "Central IT",
        "role": "Estagiário Telefonia IP",
        "period": "2014 – 2015",
        "summary": "Asterisk: ramais, URAs, filas, troncos. Suporte 2º nível.",
        "stack": ["Asterisk", "PHP", "JavaScript"],
        "current": False,
    },
]


STACK_GROUPS = [
    {
        "label": "Linguagens",
        "items_list": ["Python", "TypeScript", "JavaScript", "Node.js", "SQL", "PHP"],
    },
    {
        "label": "Backend & API",
        "items_list": ["FastAPI", "Express.js", "REST", "GraphQL", "WebSockets", "Pydantic"],
    },
    {
        "label": "Frontend",
        "items_list": ["React", "Next.js", "React Native", "Tailwind", "Redux"],
    },
    {
        "label": "Dados",
        "items_list": ["PostgreSQL", "PgCat", "SQL Server", "MySQL", "Vector DB"],
    },
    {
        "label": "Cloud & DevOps",
        "items_list": ["Docker", "AWS", "Railway", "GitHub Actions", "Linux"],
    },
    {
        "label": "IA",
        "items_list": ["Claude API", "OpenAI", "Claude Code", "Playwright", "Meta Graph API"],
    },
    {
        "label": "VoIP",
        "items_list": ["Asterisk (DCAA)", "FreePBX", "SIP", "OpenVPN", "PFSense"],
    },
]


CERTIFICATIONS = [
    {"name": "MBA Executivo", "issuer": "Unyleya", "year": "2025"},
    {"name": "Bacharel em Sistemas de Informação", "issuer": "UNIP", "year": "2017"},
    {"name": "DCAA · Digium Certified Asterisk Administrator", "issuer": "Digium / Sangoma", "year": "2018"},
]


CASE_STUDIES_LINK = "https://github.com/MatheusBinicheski/portfolio"

RESUME_PDF_RELATIVE = "/static/resume/Resume Matheus Binicheski.pdf"
