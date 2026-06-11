"""Conteúdo em português do portfolio dashboard.

Versão PT-BR — usada na rota /pt. Inclui screenshots anonimizados de
dashboards de cliente reais (nomes substituídos por descritores genéricos).
"""

from __future__ import annotations


IDENTITY = {
    "name": "Matheus Binicheski",
    "title": "Engenheiro de Software Sênior · IA / Sistemas Agentivos · Node + Python + PostgreSQL",
    "tagline": "Construo sistemas de IA em produção que entregam, são medidos e não caem às 3 da manhã.",
    "location": "Brasília, Brasil · UTC-3 · Sobreposição total com horário comercial EUA Eastern",
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
        "label": "Engenharia sênior em produção",
        "detail": "Backend, full-stack, infraestrutura/telecom e IA em paralelo.",
    },
    {
        "metric": "US$ 1,2M",
        "unit": "por ano",
        "label": "Redução de custo operacional entregue",
        "detail": "Plataforma de automação em Node.js · cliente B2B serviços · em produção há anos.",
    },
    {
        "metric": "360×",
        "unit": "mais rápido",
        "label": "Reescrita de performance",
        "detail": "Batch público em PostgreSQL: cerca de 2 horas para menos de 20 segundos.",
    },
    {
        "metric": "~40%",
        "unit": "custo SDR",
        "label": "Corte via pipeline de leads com LLM",
        "detail": "Classificador em Claude da Anthropic · saída estruturada · evals como artefato.",
    },
]


# Selected work, agora com screenshots anonimizados dos dashboards reais.
# Imagens em /static/img/projects/*.png — capturadas via Playwright headless.
SELECTED_WORK = [
    {
        "slug": "performance-media-dashboard",
        "title": "Dashboard executivo de mídia paga · cliente high-ticket",
        "client": "Cliente de mídia paga · Brasília · NDA",
        "summary": (
            "Painel executivo full-stack que conecta direto na Meta Graph API, normaliza "
            "métricas por conta de anúncio, faz reconciliação diária com a base de vendas e "
            "expõe rankings de criativos, fadiga de público e eficiência por campanha. "
            "Backend em FastAPI, frontend com Chart.js. O cliente substituiu um Looker "
            "Studio que já não cabia mais no ritmo de decisão dele."
        ),
        "metric": "Tempo de leitura do dia: 25 min → 90 segundos",
        "stack": ["Python", "FastAPI", "Chart.js", "Meta Graph API v21", "PostgreSQL", "Railway"],
        "screenshot": "/static/img/projects/pedro_rehn.webp",
        "screenshot_caption": "Dashboard de mídia paga · números anonimizados",
        "link": None,
        "year": "2025 – atual",
    },
    {
        "slug": "saude-meta-ads-dashboard",
        "title": "Diagnóstico Meta Ads + dashboard 360° · clínica multiunidades",
        "client": "Cliente saúde · clínica odontológica DF · NDA",
        "summary": (
            "Diagnóstico de 90 dias da conta Meta Ads (mais de R$ 800k investidos) seguido "
            "do dashboard executivo. Identifiquei quality rankings ruins, sobreinvestimento "
            "em IG Feed e queima de TOFU sem retorno. O painel mostra investimento por "
            "público, criativos saturando, e o sweet spot real (mulheres 25-54 DF). Allowlist "
            "por conta de anúncio para garantir que cada cliente só vê o que é dele."
        ),
        "metric": "Realocação de orçamento defendida com dados, sem achismo",
        "stack": ["Python", "FastAPI", "Meta Graph API", "Chart.js", "Allowlist multi-conta"],
        "screenshot": "/static/img/projects/croe_odonto.webp",
        "screenshot_caption": "Painel multi-conta com paleta teal/coral · dados anonimizados",
        "link": None,
        "year": "2026",
    },
    {
        "slug": "iag-operations",
        "title": "Painel operacional 360° · consultoria empresarial",
        "client": "Cliente consultoria empresarial · NDA",
        "summary": (
            "Painel único de operação para o time de uma consultoria: 5 pilares (KPIs do "
            "trimestre, entregáveis por consultor, tarefas em aberto, processos em "
            "andamento, status do time). Toda a configuração mora em um único arquivo "
            "data.py — o cliente edita conteúdo sem mexer em código. Sucessor de uma "
            "planilha que já não cabia mais."
        ),
        "metric": "1 painel substituiu 4 planilhas + 2 ferramentas SaaS",
        "stack": ["Python", "FastAPI", "Jinja2 SSR", "Tailwind", "Railway"],
        "screenshot": "/static/img/projects/iag_operations.webp",
        "screenshot_caption": "Painel operacional · identidade visual do cliente preservada",
        "link": None,
        "year": "2026",
    },
    {
        "slug": "ceo-presenca-digital",
        "title": "Dashboard CEO de presença digital · figura pública",
        "client": "Cliente mídia / influência · figura pública nacional · NDA",
        "summary": (
            "Dashboard CEO que mostra evolução de seguidores em Instagram, picos de "
            "engajamento, sazonalidade mês a mês e snapshots semanais. Coleta via Meta "
            "Graph API com cron diário, persistência em PostgreSQL, visualização em "
            "Three.js. Pensado para 1 leitor — o cliente abre no celular pela manhã e "
            "decide o eixo da semana em 2 minutos."
        ),
        "metric": "Coleta diária automática · histórico de 12+ meses preservado",
        "stack": ["Python", "FastAPI", "Three.js", "Meta Graph API", "PostgreSQL", "Cron"],
        "screenshot": "/static/img/projects/pradoclima.webp",
        "screenshot_caption": "Dashboard CEO · números reais ocultados",
        "link": None,
        "year": "2025 – atual",
    },
    {
        "slug": "greenn-meta-capi",
        "title": "Bridge Greenn → Meta Conversions API",
        "client": "Cliente paid media · operação direct-to-consumer",
        "summary": (
            "Serviço FastAPI que recebe postback do checkout (Greenn), normaliza o "
            "payload, deduplica eventos por event_id usando TTL store que sobrevive a "
            "apagões de 4 horas da Meta, hasheia PII no formato da spec e encaminha para "
            "o Meta CAPI v21 com retry e backoff. Endpoints /raw e /raw-logs para debugar "
            "qualquer evento dos últimos N minutos sem ir no banco. Recuperou de 20% a "
            "30% das conversões que o Pixel sozinho perdia para o iOS/Safari ITP."
        ),
        "metric": "Dedup Pixel + CAPI de 18% para mais de 80% em 48 horas",
        "stack": ["Python", "FastAPI", "Pydantic v2", "httpx", "Docker", "Meta Graph API v21"],
        "screenshot": "/static/img/projects/greenn_capi.webp",
        "screenshot_caption": "Endpoint de bridge · referência pública open-source",
        "link": "https://github.com/MatheusBinicheski/portfolio/tree/main/meta-capi-bridge-example",
        "year": "2025 – atual",
    },
    {
        "slug": "ubec-automation",
        "title": "Plataforma de automação que cortou US$ 1,2M/ano em custo",
        "client": "Cliente B2B serviços · via Webum",
        "summary": (
            "Substituí uma operação manual de triagem de atendimento por uma plataforma "
            "Node.js orientada a eventos. Pedidos são normalizados, classificados e "
            "encaminhados pro fluxo correto sem triagem humana no meio. Arquitetura, "
            "implementação e rollout sob minha responsabilidade fim a fim."
        ),
        "metric": "Economia recorrente de US$ 1,2M USD por ano",
        "stack": ["Node.js", "TypeScript", "Express", "PostgreSQL", "Workers de fila", "AWS", "Docker"],
        "screenshot": None,
        "link": None,
        "year": "2022 – 2024",
    },
    {
        "slug": "gov-mt-perf",
        "title": "Batch público: 2 horas → menos de 20 segundos",
        "client": "Governo do Mato Grosso · via Webum",
        "summary": (
            "Reescrita de arquitetura num sistema público de vacinação e gestão de "
            "serviços. Análise de query plan, refactor de DDL, PgCat na frente do "
            "Postgres pra pooling e reescrita dos hot-paths em Express. O batch noturno "
            "virou serviço em tempo real."
        ),
        "metric": "~7.200s → menos de 20s ponta a ponta (≈ 360× mais rápido)",
        "stack": ["Node.js", "Express", "PostgreSQL", "PgCat", "Refactor de DDL"],
        "screenshot": None,
        "link": None,
        "year": "2023",
    },
]


EXPERIENCE_TIMELINE = [
    {
        "company": "Webum",
        "role": "Engenheiro de Software Sênior",
        "period": "jan/2021 – atual",
        "summary": (
            "Arquiteto e entrego serviços Node.js e aplicações web modernas para clientes "
            "do setor público e enterprise. Backend, sistemas distribuídos, otimização "
            "de banco de dados, automação."
        ),
        "stack": ["Node.js", "TypeScript", "Express", "PostgreSQL", "SQL Server", "PgCat", "React", "Next.js"],
        "current": True,
    },
    {
        "company": "Contratante PJ Independente",
        "role": "Engenheiro Full-Stack / Consultor de Automação com IA",
        "period": "jan/2021 – atual",
        "summary": (
            "Contratos B2B em paralelo. Plataformas de automação de seguros, bridges de "
            "eventos de marketing, dashboards executivos de analytics, bots de SDR "
            "conversacionais. Stack: FastAPI + Postgres + Anthropic Claude + Playwright "
            "em Docker + Railway."
        ),
        "stack": ["Python", "FastAPI", "PostgreSQL", "Docker", "AWS", "Railway", "API Anthropic", "Playwright"],
        "current": True,
    },
    {
        "company": "Synapse Brasil Tecnologia",
        "role": "Engenheiro Frontend Pleno",
        "period": "abr/2017 – dez/2020",
        "summary": (
            "Construí UIs de alta performance em React/Next.js e integrei com serviços "
            "de backend. Refactor de performance cortou tempo de load inicial em ~40%."
        ),
        "stack": ["React", "Next.js", "TailwindCSS", "Node.js", "GraphQL", "Redux"],
        "current": False,
    },
    {
        "company": "Synapse Brasil Tecnologia",
        "role": "Analista de Infraestrutura e Telecom",
        "period": "jan/2015 – dez/2020 · paralelo",
        "summary": (
            "Hosts VMware / Hyper-V / Xen; plataformas VoIP Asterisk/FreePBX/Elastix; "
            "firewalls PFSense com VLAN, captive portal, traffic shaping; OpenVPN e "
            "IPsec com redundância OSPF. Active Directory, DNS, DHCP, segurança de "
            "endpoints via LDAP."
        ),
        "stack": ["Asterisk", "FreePBX", "PFSense", "OpenVPN", "IPsec", "OSPF", "VMware", "Hyper-V", "Active Directory"],
        "current": False,
    },
    {
        "company": "Central IT",
        "role": "Estagiário Telecom / Telefonia IP",
        "period": "2014 – 2015",
        "summary": (
            "Plataformas de telefonia em Asterisk: ramais, URAs, filas, troncos entre "
            "PABXs digitais. Automação em PHP/JavaScript para relatórios. Suporte de "
            "2º nível em call center."
        ),
        "stack": ["Asterisk", "PHP", "JavaScript"],
        "current": False,
    },
]


STACK_GROUPS = [
    {
        "label": "Linguagens",
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
        "label": "Dados",
        "items_list": ["PostgreSQL", "PgCat", "SQL Server", "MySQL", "Bancos vetoriais"],
    },
    {
        "label": "Cloud & DevOps",
        "items_list": ["Docker", "AWS", "Railway", "GitHub Actions", "GitLab CI", "Linux"],
    },
    {
        "label": "IA / Automação",
        "items_list": ["API Anthropic Claude", "API OpenAI", "Claude Code", "Playwright", "Selenium", "Meta Graph API"],
    },
    {
        "label": "VoIP / Telecom",
        "items_list": ["Asterisk (DCAA)", "FreePBX", "Elastix", "SIP", "OpenVPN", "IPsec", "PFSense"],
    },
]


CERTIFICATIONS = [
    {"name": "MBA Executivo — Empreendedorismo, Marketing e Finanças", "issuer": "Unyleya", "year": "2025"},
    {"name": "Bacharelado — Sistemas de Informação", "issuer": "Universidade Paulista (UNIP)", "year": "2017"},
    {"name": "DCAA — Digium Certified Asterisk Administrator", "issuer": "Digium / Sangoma", "year": "2018"},
]


CASE_STUDIES_LINK = "https://github.com/MatheusBinicheski/portfolio"

RESUME_PDF_RELATIVE = "/static/resume/Resume Matheus Binicheski.pdf"
