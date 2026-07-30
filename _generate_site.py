#!/usr/bin/env python3
"""Generate portfolio index + per-project pages from structured content."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent

CSS = """
:root {
  --bg: #ececec;
  --ink: #1d1d1f;
  --muted: #6e6e73;
  --line: #c3c3c7;
  --card: #f7f7f8;
  --accent: #0a64f2;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  color: var(--ink);
  background: linear-gradient(180deg, #d8d8dc 0%, var(--bg) 36%, #e8e8ea 100%);
  line-height: 1.5;
  text-align: center;
}
main {
  max-width: 880px;
  margin: 0 auto;
  padding: 40px 20px 96px;
  text-align: center;
}
main.narrow { max-width: 680px; padding-top: 56px; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.back {
  display: inline-block;
  margin-bottom: 18px;
  color: var(--muted);
  font-size: 14px;
  text-decoration: none;
}
.back:hover { color: var(--accent); }
h1 {
  margin: 0 0 6px;
  font-size: 28px;
  letter-spacing: -0.02em;
  font-weight: 650;
}
.tag {
  margin: 0 0 28px;
  color: var(--muted);
  font-size: 15px;
}
h2 {
  font-size: 12px;
  font-weight: 600;
  margin: 36px 0 12px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
.prose {
  font-size: 15px;
  max-width: 42em;
}
.prose p { margin: 0 0 12px; }
.meta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 14px;
  margin: 0 0 8px;
  font-size: 13px;
  color: var(--muted);
}
.meta-row a { color: var(--muted); }
.meta-row a:hover { color: var(--accent); }
.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 0 0 8px;
}
.chip {
  border: 1px solid var(--line);
  background: #fff;
  border-radius: 6px;
  padding: 4px 9px;
  font-size: 12px;
  color: var(--ink);
}
.shots {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
}
@media (min-width: 700px) {
  .shots.two { grid-template-columns: 1fr 1fr; }
}
.shots figure {
  margin: 0;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: hidden;
  padding: 10px 10px 0;
}
.shots.hero figure { padding: 0; }
.shots.hero img { border-radius: 0; }
.shots img {
  display: block;
  width: 100%;
  height: auto;
  background: #ddd;
}
.shots figcaption {
  padding: 8px 0 10px;
  font-size: 12px;
  color: var(--muted);
}
.shots.hero figcaption { padding-left: 10px; padding-right: 10px; }
.visual {
  margin: 0 0 8px;
  background: #f3f3f5;
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: hidden;
}
.visual svg { display: block; width: 100%; height: auto; }
.flow {
  display: grid;
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.flow li {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px 14px;
  font-size: 14px;
}
.flow strong { display: block; margin-bottom: 2px; }
.flow span { color: var(--muted); font-size: 13px; }
.arch {
  display: grid;
  gap: 8px;
  grid-template-columns: 1fr;
}
@media (min-width: 640px) {
  .arch.cols-3 { grid-template-columns: repeat(3, 1fr); }
  .arch.cols-4 { grid-template-columns: repeat(4, 1fr); }
}
.arch .box {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  font-size: 13px;
}
.arch .box strong { display: block; margin-bottom: 4px; font-size: 14px; }
.arch .box span { color: var(--muted); }
header.home { margin-bottom: 48px; }
header.home h1 { font-size: 32px; letter-spacing: -0.03em; }
.lede {
  margin: 0;
  color: var(--muted);
  font-size: 16px;
  max-width: 36em;
}
.links { margin-top: 14px; font-size: 14px; }
.links a { margin-right: 14px; }
section.list h2 {
  margin: 40px 0 14px;
  border-top: 1px solid var(--line);
  padding-top: 28px;
}
section.list:first-of-type h2 {
  border-top: 0;
  padding-top: 0;
  margin-top: 0;
}
dl { margin: 0; }
.project {
  display: grid;
  grid-template-columns: minmax(7.5rem, 9.5rem) 1fr;
  gap: 6px 18px;
  padding: 12px 0;
  border-bottom: 1px solid rgba(195, 195, 199, 0.55);
}
.project:last-child { border-bottom: 0; }
dt { margin: 0; font-weight: 600; font-size: 15px; letter-spacing: -0.01em; }
dt a { color: inherit; }
dt a:hover { color: var(--accent); }
dd { margin: 0; font-size: 14px; }
dd p { margin: 0 0 4px; }
.meta { color: var(--muted); font-size: 12px; }
.meta a { color: var(--muted); }
.meta a:hover { color: var(--accent); }
footer {
  margin-top: 56px;
  padding-top: 20px;
  border-top: 1px solid var(--line);
  font-size: 12px;
  color: var(--muted);
}
@media (max-width: 560px) {
  header.home h1 { font-size: 28px; }
  .project { grid-template-columns: 1fr; gap: 2px; padding: 14px 0; }
}
""".strip()

def esc(s: str) -> str:
    return html.escape(s, quote=True)

def render_images(images: list[dict], hero: bool = False) -> str:
    if not images:
        return ""
    cls = "shots hero" if hero and len(images) == 1 else ("shots two" if len(images) > 1 else "shots")
    figs = []
    for img in images:
        cap = f"<figcaption>{esc(img['caption'])}</figcaption>" if img.get("caption") else ""
        figs.append(
            f'<figure><img src="{esc(img["src"])}" alt="{esc(img.get("alt") or img.get("caption") or "")}" loading="lazy" />{cap}</figure>'
        )
    return f'<div class="{cls}">' + "".join(figs) + "</div>"

def render_flow(steps: list[dict]) -> str:
    if not steps:
        return ""
    items = "".join(
        f"<li><strong>{esc(s['title'])}</strong><span>{esc(s['body'])}</span></li>" for s in steps
    )
    return f'<ol class="flow">{items}</ol>'

def render_arch(boxes: list[dict], cols: int = 3) -> str:
    if not boxes:
        return ""
    items = "".join(
        f'<div class="box"><strong>{esc(b["title"])}</strong><span>{esc(b["body"])}</span></div>'
        for b in boxes
    )
    return f'<div class="arch cols-{cols}">{items}</div>'

def render_visual(p: dict) -> str:
    """SVG strip from flow or arch when no photo hero exists."""
    nodes = p.get("flow") or [
        {"title": b["title"], "body": b.get("body", "")} for b in (p.get("arch") or [])
    ]
    if not nodes:
        nodes = [{"title": p["title"], "body": p["tag"]}]
    nodes = nodes[:4]
    n = len(nodes)
    width = 840
    height = 140
    pad = 18
    gap = 14
    box_w = (width - 2 * pad - gap * (n - 1)) / n
    box_h = 88
    y = 26

    parts = [
        f'<div class="visual" role="img" aria-label="{esc(p["title"])} overview">',
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">',
        f'<rect width="{width}" height="{height}" fill="#f3f3f5"/>',
    ]
    for i, node in enumerate(nodes):
        x = pad + i * (box_w + gap)
        title = esc(node["title"])
        parts.append(
            f'<rect x="{x:.1f}" y="{y}" width="{box_w:.1f}" height="{box_h}" rx="10" fill="#fff" stroke="#c3c3c7"/>'
        )
        parts.append(
            f'<text x="{x + 16:.1f}" y="{y + 28}" fill="#6e6e73" font-size="11" font-family="-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif" letter-spacing="0.06em">{i + 1:02d}</text>'
        )
        parts.append(
            f'<text x="{x + 16:.1f}" y="{y + 56}" fill="#1d1d1f" font-size="16" font-family="-apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif" font-weight="600">{title}</text>'
        )
        if i < n - 1:
            ax1 = x + box_w + 3
            ax2 = x + box_w + gap - 3
            mid = y + box_h / 2
            parts.append(
                f'<path d="M{ax1:.1f} {mid:.1f} L{ax2:.1f} {mid:.1f}" stroke="#0a64f2" stroke-width="2" fill="none"/>'
            )
            parts.append(
                f'<path d="M{ax2 - 6:.1f} {mid - 5:.1f} L{ax2:.1f} {mid:.1f} L{ax2 - 6:.1f} {mid + 5:.1f}" stroke="#0a64f2" stroke-width="2" fill="none"/>'
            )
    parts.append("</svg></div>")
    return "".join(parts)

def project_page(p: dict) -> str:
    parts = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8" />',
        '  <meta name="viewport" content="width=device-width, initial-scale=1" />',
        f"  <title>{esc(p['title'])} — Arno Van Eetvelde</title>",
        f'  <meta name="description" content="{esc(p["tag"])}" />',
        "  <style>",
        CSS,
        "  </style>",
        "</head>",
        "<body>",
        "  <main>",
        '    <a class="back" href="../../">← Arno Van Eetvelde</a>',
        f"    <h1>{esc(p['title'])}</h1>",
        f'    <p class="tag">{esc(p["tag"])}</p>',
    ]

    meta_bits = []
    if p.get("status"):
        meta_bits.append(esc(p["status"]))
    if p.get("github"):
        meta_bits.append(f'<a href="{esc(p["github"])}">github</a>')
    if p.get("links"):
        for link in p["links"]:
            meta_bits.append(f'<a href="{esc(link["href"])}">{esc(link["label"])}</a>')
    if meta_bits:
        parts.append(f'    <p class="meta-row">{" · ".join(meta_bits)}</p>')

    if p.get("stack"):
        chips = "".join(f'<span class="chip">{esc(s)}</span>' for s in p["stack"])
        parts.append(f'    <div class="chips">{chips}</div>')

    if p.get("hero"):
        parts.append("    <h2>Overview</h2>")
        parts.append(f'    {render_images(p["hero"], hero=True)}')
    else:
        parts.append("    <h2>Overview</h2>")
        parts.append(f"    {render_visual(p)}")

    if p.get("about"):
        parts.append('    <div class="prose">')
        for para in p["about"]:
            parts.append(f"      <p>{esc(para)}</p>")
        parts.append("    </div>")

    if p.get("flow"):
        parts.append(f'    <h2>{esc(p.get("flow_title") or "How it works")}</h2>')
        parts.append(f"    {render_flow(p['flow'])}")

    if p.get("arch"):
        parts.append(f'    <h2>{esc(p.get("arch_title") or "Architecture")}</h2>')
        parts.append(f"    {render_arch(p['arch'], p.get('arch_cols', 3))}")

    if p.get("images"):
        parts.append(f'    <h2>{esc(p.get("images_title") or "Gallery")}</h2>')
        parts.append(f"    {render_images(p['images'])}")

    if p.get("notes"):
        parts.append("    <h2>Notes</h2>")
        parts.append('    <div class="prose">')
        for para in p["notes"]:
            parts.append(f"      <p>{esc(para)}</p>")
        parts.append("    </div>")

    parts += ["  </main>", "</body>", "</html>", ""]
    return "\n".join(parts)

# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------

PROJECTS: list[dict] = [
    {
        "slug": "infurn",
        "href": "projects/infurn/",
        "list_title": "infurn",
        "list_blurb": "Photoreal virtual staging — empty room photo to furnished room, architecture preserved.",
        "list_meta": "demo · private",
        "section": "AI wrapper",
        "todo": False,
        "external_page": True,  # handcrafted template page at projects/infurn/
    },
    
    {
        "slug": "cutsched",
        "href": "projects/cutsched/",
        "list_title": "CutSched",
        "list_blurb": "LLM optimization benchmark: speed up a cutting-stock + scheduling CP-SAT solver without breaking the contract.",
        "list_meta": "private",
        "section": "Vision & ML",
        "title": "CutSched",
        "tag": "LLM optimization benchmark · cutting stock + scheduling",
        "status": "private",
        "stack": ["Python", "CP-SAT", "Docker", "benchmarking"],
        "about": [
            "CutSched measures how well an LLM or agent can speed up a working combinatorial-optimization solver without breaking it.",
            "The problem couples cutting-stock with parallel-machine scheduling. A correct-but-modest CP-SAT baseline ships with the suite; models may rewrite anything as long as the contract and quality targets hold.",
        ],
        "flow": [
            {"title": "Contract", "body": "solve.sh is the frozen entry point. Feasibility and objective checking are canonical."},
            {"title": "Baseline", "body": "A CP-SAT solver sets quality floors on generated gate instances."},
            {"title": "Score", "body": "Wall-clock time on hidden instances inside a resource-pinned Docker container."},
        ],
        "arch": [
            {"title": "SPEC.md", "body": "Frozen problem, contract, and scoring rules."},
            {"title": "PROMPT.md", "body": "What the model under test sees."},
            {"title": "Verifier", "body": "Canonical feasibility + objective checker."},
            {"title": "Hidden set", "body": "Speed instances the model never trains on."},
        ],
        "arch_cols": 4
},
    {
        "slug": "quant-arena",
        "href": "projects/quant-arena/",
        "list_title": "Quant Arena",
        "list_blurb": "Competitive playground where agents submit stock-trading algorithms and race on a shared backtest leaderboard.",
        "list_meta": "private",
        "section": "Markets",
        "title": "Quant Arena",
        "tag": "agent trading algorithms · shared backtest leaderboard",
        "status": "private",
        "stack": ["Python", "yfinance", "backtesting", "HTML leaderboard"],
        "about": [
            "A competitive playground where AI agents build stock trading algorithms and compete on a shared leaderboard.",
            "Algorithms land as Python plugins. The arena supplies market data, a backtesting engine, holdout evaluation, and a static HTML leaderboard.",
        ],
        "flow": [
            {"title": "Submit", "body": "Drop an algorithm in algorithms/NNN/ with metadata."},
            {"title": "Backtest", "body": "Train split 2018–2022, then official holdout from 2023+."},
            {"title": "Rank", "body": "Evaluate all algorithms and regenerate the leaderboard dashboard."},
        ],
        "arch": [
            {"title": "Data", "body": "~500 stocks via yfinance, local store."},
            {"title": "Engine", "body": "Costs, metrics, and robust evaluation."},
            {"title": "Leaderboard", "body": "Static HTML report of rankings."},
        ]
},
    {
        "slug": "factory-os",
        "href": "projects/factory-os/",
        "list_title": "factory-os",
        "list_blurb": "AI layer on a MQTT Unified Namespace — chat with plant data, configure agents, surface detections and actions.",
        "list_meta": "private",
        "section": "Homelab & IoT",
        "title": "factory-os",
        "tag": "AI industrial OS on a MQTT Unified Namespace",
        "status": "private",
        "stack": ["MQTT", "UNS", "LLM agents", "Postgres historian"],
        "about": [
            "An AI-driven industrial OS on top of a Unified Namespace. Talk to plant data, configure agents, and get detections and actions out of industrial telemetry.",
            "A simulated (or later real) factory publishes over MQTT. Data is also historized. The hub layer adds chat, agents, and insight tooling.",
        ],
        "arch": [
            {"title": "Data layer", "body": "Factory simulator → MQTT UNS + historian."},
            {"title": "AI / OS layer", "body": "Chatbot, agents, detections, actions."},
            {"title": "Interface", "body": "Ask why output drops or which machine looks abnormal."},
        ],
        "hero": [{"src": "assets/diagram-1.png", "caption": "System sketch", "alt": "factory-os diagram"}],
        "images": [
            {"src": "assets/diagram-2.png", "caption": "Hub flow"},
            {"src": "assets/diagram-3.png", "caption": "Agent / data paths"},
            {"src": "assets/diagram-4.png", "caption": "Interface concept"},
        ],
        "images_title": "Design sketches"
},
    
    
    {
        "slug": "roborock-mqtt",
        "href": "projects/roborock-mqtt/",
        "list_title": "Roborock MQTT",
        "list_blurb": "Bridge Roborock vacuum telemetry into MQTT for a k3s / Home Assistant setup.",
        "list_meta_html": '<a href="https://github.com/Arno1235/RoborockMQTTBridge">github</a>',
        "section": "Homelab & IoT",
        "title": "Roborock MQTT Bridge",
        "tag": "Roborock vacuum → MQTT → Home Assistant",
        "status": "public",
        "github": "https://github.com/Arno1235/RoborockMQTTBridge",
        "stack": ["Python", "MQTT", "k3s", "buildah"],
        "about": [
            "A containerized bridge that publishes Roborock vacuum state onto MQTT so Home Assistant and other consumers can use it.",
            "Built for the Raspberry Pi k3s cluster: build the image, import into containerd, push to a local registry, and run with login secrets.",
        ],
        "flow": [
            {"title": "Authenticate", "body": "Roborock login credentials as a Kubernetes secret."},
            {"title": "Bridge", "body": "Translate vacuum telemetry onto filtered MQTT topics."},
            {"title": "Consume", "body": "Home Assistant or custom UNS tooling reads the topics."},
        ]
},
    {
        "slug": "mqtt-ha",
        "href": "projects/mqtt-ha/",
        "list_title": "MQTT → HA",
        "list_blurb": "Auto Home Assistant MQTT discovery from wildcard topics, packaged for Kubernetes.",
        "list_meta": "private",
        "section": "Homelab & IoT",
        "title": "MQTT → Home Assistant Discovery",
        "tag": "automatic HA device discovery from MQTT wildcards",
        "status": "private",
        "stack": ["Python", "MQTT", "Home Assistant", "k3s"],
        "about": [
            "A service that listens to MQTT topics and automatically creates Home Assistant MQTT discovery payloads.",
            "It watches wildcards, infers sensor types from topic names, and updates devices as new subtopics appear — meant to run as a container on the k3s cluster.",
        ],
        "flow": [
            {"title": "Watch", "body": "Subscribe to configured topic patterns."},
            {"title": "Infer", "body": "Detect device/entity shape from topic structure and names."},
            {"title": "Discover", "body": "Publish Home Assistant discovery messages and keep them fresh."},
        ]
},
    {
        "slug": "sparkplug",
        "href": "projects/sparkplug/",
        "list_title": "Sparkplug B",
        "list_blurb": "Python client framework for MQTT Sparkplug B — birth/death, publish, subscribe, callbacks.",
        "list_meta_html": '<a href="https://github.com/Arno1235/MQTT_SparkplugB_Client">github</a>',
        "section": "Homelab & IoT",
        "title": "MQTT Sparkplug B Client",
        "tag": "Python framework for Sparkplug B messaging",
        "status": "public",
        "github": "https://github.com/Arno1235/MQTT_SparkplugB_Client",
        "stack": ["Python", "MQTT", "Sparkplug B"],
        "about": [
            "A small framework for MQTT communications using the Sparkplug B protocol.",
            "Connect, publish structured payloads, subscribe with callbacks, and automatically handle birth and death certificates.",
        ],
        "arch": [
            {"title": "Connect", "body": "Broker session with Sparkplug identity."},
            {"title": "Publish", "body": "Structured Sparkplug payloads."},
            {"title": "Subscribe", "body": "Topic handlers via custom callbacks."},
        ]
},
    {
        "slug": "yamal",
        "href": "projects/yamal/",
        "list_title": "YAMAL",
        "list_blurb": "Lightweight ROS-inspired Python framework for parallel nodes and messaging via YAML launch files.",
        "list_meta_html": '<a href="https://github.com/Arno1235/YAMAL">github</a>',
        "section": "Homelab & IoT",
        "title": "YAMAL",
        "tag": "Yet Another Messaging and Asynchronous Launch framework",
        "status": "public",
        "github": "https://github.com/Arno1235/YAMAL",
        "stack": ["Python", "YAML", "multiprocessing"],
        "about": [
            "A lightweight Python framework for running nodes in parallel and communicating between them using YAML launch files.",
            "Inspired by ROS, but intentionally minimal for resource-constrained environments.",
        ],
        "hero": [{"src": "assets/example.jpg", "caption": "Imaging node example", "alt": "YAMAL imaging example"}],
        "flow": [
            {"title": "Define", "body": "Describe nodes and wiring in a YAML launch file."},
            {"title": "Launch", "body": "Start parallel processes from that config."},
            {"title": "Message", "body": "Nodes exchange data through the messaging layer."},
        ]
},
    {
        "slug": "hivemq-uns",
        "href": "projects/hivemq-uns/",
        "list_title": "HiveMQ UNS ext.",
        "list_blurb": "HiveMQ extension experiments around Unified Namespace monitoring.",
        "list_meta": "private",
        "section": "Homelab & IoT",
        "title": "HiveMQ UNS monitoring extension",
        "tag": "HiveMQ extension experiments for UNS monitoring",
        "status": "private",
        "stack": ["Java", "HiveMQ", "MQTT", "UNS"],
        "about": [
            "Extension work on HiveMQ aimed at monitoring and inspecting Unified Namespace traffic.",
            "Started from HiveMQ’s extension model (client lifecycle hooks and publish interceptors) and steered toward UNS-oriented observability.",
        ],
        "arch": [
            {"title": "Lifecycle", "body": "Observe connecting/disconnecting clients."},
            {"title": "Intercept", "body": "Inspect or reshape inbound publishes."},
            {"title": "Monitor", "body": "Surface UNS topic health and anomalies."},
        ]
},
    {
        "slug": "market-ops",
        "href": "projects/market-ops/",
        "list_title": "Market Ops",
        "list_blurb": "Trading research — pipelines, Saxo flows, biotech angles, and agent-built strategies.",
        "list_meta": "private",
        "section": "Markets",
        "title": "Market Ops",
        "tag": "trading research · pipelines · agent strategies",
        "status": "private",
        "stack": ["Python", "Saxo", "n8n", "research notes"],
        "about": [
            "An umbrella for market research and trading tooling: strategy outlines, biotech focus areas, Saxo flows, automation in n8n, and agent-assisted algorithm work.",
            "Related code lives across MarketOps, stockbook, roboquant, and Quant Arena.",
        ],
        "hero": [{"src": "assets/diagram.jpg", "caption": "System diagram", "alt": "Market Ops diagram"}],
        "images": [{"src": "assets/screenshot.png", "caption": "Research / tooling snapshot"}],
        "flow": [
            {"title": "Ingest", "body": "Market and fundamentals data into research pipelines."},
            {"title": "Research", "body": "Strategy notes, biotech screens, backtest ideas."},
            {"title": "Operate", "body": "Saxo flows, alerts, and agent-built algorithms."},
        ]
},
    {
        "slug": "openinsider",
        "href": "projects/openinsider/",
        "list_title": "OpenInsider",
        "list_blurb": "Telegram alerts when multiple executives buy or sell large blocks on openinsider.com.",
        "list_meta": "private",
        "section": "Markets",
        "title": "OpenInsider notifier",
        "tag": "insider transaction Telegram alerts",
        "status": "private",
        "stack": ["Python", "Telegram", "Docker"],
        "about": [
            "Polls openinsider.com every few hours for insider transactions.",
            "When three or more executives at a company each buy or sell shares worth at least $200k, a Telegram alert fires with company details, names, and amounts.",
        ],
        "flow": [
            {"title": "Poll", "body": "Fetch recent insider filings on a schedule."},
            {"title": "Filter", "body": "Require clustered large buys/sells at one company."},
            {"title": "Alert", "body": "Send a concise Telegram message."},
        ]
},
    
    {
        "slug": "cryptoai",
        "href": "projects/cryptoai/",
        "list_title": "CryptoAI",
        "list_blurb": "Early crypto prediction experiments. Discontinued.",
        "list_meta_html": '<a href="https://github.com/Arno1235/CryptoAI">github</a>',
        "section": "Markets",
        "title": "CryptoAI",
        "tag": "crypto prediction experiments · discontinued",
        "status": "public · discontinued",
        "github": "https://github.com/Arno1235/CryptoAI",
        "stack": ["Python", "ML"],
        "about": [
            "Early experiments predicting crypto price moves with classical ML models.",
            "Kept as an archive of charts and test runs; the project is discontinued.",
        ],
        "images": [
            {"src": "assets/actual.png", "caption": "Actual series"},
            {"src": "assets/prediction.png", "caption": "Model prediction"},
        ],
        "images_title": "Example run"
},
    {
        "slug": "mvtec-yolo",
        "href": "projects/mvtec-yolo/",
        "list_title": "MVTec YOLO",
        "list_blurb": "Run YOLO models on the MVTec anomaly detection dataset.",
        "list_meta_html": '<a href="https://github.com/Arno1235/MVTec_YOLO">github</a>',
        "section": "Vision & ML",
        "title": "MVTec YOLO",
        "tag": "YOLO on the MVTec anomaly detection dataset",
        "status": "public",
        "github": "https://github.com/Arno1235/MVTec_YOLO",
        "stack": ["Python", "YOLO", "MVTec AD"],
        "about": [
            "Experiments running YOLO detection/segmentation models on the MVTec anomaly detection dataset.",
            "Useful as a bridge between industrial inspection datasets and modern YOLO tooling.",
        ],
        "hero": [{"src": "assets/predictions.jpg", "caption": "Validation batch predictions", "alt": "YOLO predictions on MVTec"}]
},
    {
        "slug": "sam-lora",
        "href": "projects/sam-lora/",
        "list_title": "SAM LoRA",
        "list_blurb": "Fine-tuning Segment Anything with LoRA.",
        "list_meta": "private",
        "section": "Vision & ML",
        "title": "SAM LoRA fine-tuning",
        "tag": "Segment Anything · LoRA adaptation",
        "status": "private",
        "stack": ["Python", "SAM", "LoRA"],
        "about": [
            "Fine-tuning Segment Anything with LoRA adapters for domain-specific segmentation.",
            "Explored as part of broader industrial vision and staging work.",
        ],
        "flow": [
            {"title": "Base", "body": "Start from a SAM checkpoint."},
            {"title": "Adapt", "body": "Train low-rank adapters on target masks."},
            {"title": "Infer", "body": "Segment domain images with the adapted model."},
        ]
},
    
    {
        "slug": "catch-the-dot",
        "href": "projects/catch-the-dot/",
        "list_title": "Catch The Dot",
        "list_blurb": "Webcam finger-tracking game with MediaPipe, built for an Ordina case.",
        "list_meta_html": '<a href="https://github.com/Arno1235/CatchTheDot">github</a>',
        "section": "Vision & ML",
        "title": "Catch The Dot",
        "tag": "webcam finger-tracking game · Ordina case",
        "status": "public",
        "github": "https://github.com/Arno1235/CatchTheDot",
        "stack": ["Python", "MediaPipe", "OpenCV"],
        "about": [
            "A webcam game where you touch floating dots with your index finger. Built for an Ordina case.",
            "Supports multiple players, configurable dot count/size, and uses MediaPipe hand landmarks for fingertip tracking.",
        ],
        "flow": [
            {"title": "Track", "body": "MediaPipe estimates hand landmarks from the webcam."},
            {"title": "Hit-test", "body": "Index fingertip against active dots."},
            {"title": "Score", "body": "Dots respawn; play solo or against others."},
        ],
        "arch": [
            {"title": "Input", "body": "Live webcam frames."},
            {"title": "Hands", "body": "MediaPipe landmark model."},
            {"title": "Game loop", "body": "Configurable players, dots, sizes."},
        ]
},
    {
        "slug": "dl-scratch",
        "href": "projects/dl-scratch/",
        "list_title": "DL from scratch",
        "list_blurb": "Small neural-net framework written from scratch in Python.",
        "list_meta_html": '<a href="https://github.com/Arno1235/DeepLearning_from_scratch">github</a>',
        "section": "Vision & ML",
        "title": "Deep Learning from scratch",
        "tag": "neural net framework in pure Python",
        "status": "public",
        "github": "https://github.com/Arno1235/DeepLearning_from_scratch",
        "stack": ["Python", "NumPy"],
        "about": [
            "A deep learning framework built from scratch to learn the internals — tensors, layers, losses, and training loops without relying on PyTorch or TensorFlow.",
        ],
        "arch": [
            {"title": "Tensors", "body": "Array ops and autograd-style basics."},
            {"title": "Layers", "body": "Composable network building blocks."},
            {"title": "Train", "body": "Losses, optimizers, and loop glue."},
        ]
},
    
    {
        "slug": "datalab",
        "href": "projects/datalab/",
        "list_title": "DataLab",
        "list_blurb": "Desktop toolkit for CSV anonymization and progressive statistical / ML analysis.",
        "list_meta": "private",
        "section": "Vision & ML",
        "title": "DataLab",
        "tag": "CSV anonymizer + automatic analysis desktop app",
        "status": "private",
        "stack": ["Python", "tkinter", "privacy", "stats", "ML"],
        "about": [
            "A desktop app for data scientists that anonymizes CSVs while preserving utility, then runs progressively deeper analysis — from descriptive stats to anomaly detection and modelling.",
            "Designed as a self-contained tool under a shared tooling monorepo.",
        ],
        "flow": [
            {"title": "Anonymize", "body": "Detect PII / quasi-identifiers; apply k-anonymity and related methods."},
            {"title": "Profile", "body": "Descriptive stats, tests, correlations."},
            {"title": "Model", "body": "Anomaly detection, clustering, time-series / AutoML-lite."},
        ]
},
    
    {
        "slug": "pcb-drone",
        "href": "projects/pcb-drone/",
        "list_title": "PCB drone",
        "list_blurb": "Raspberry Pi Pico flight controller on custom PCBs — ESC, IMU, power, SBUS, printable frame.",
        "list_meta": "private",
        "section": "Hardware",
        "title": "PCB raspi drone",
        "tag": "custom flight-controller PCBs on Raspberry Pi Pico",
        "status": "private",
        "stack": ["KiCad", "Pico", "MicroPython", "IMU", "ESC"],
        "about": [
            "A from-scratch drone built around custom PCBs and Raspberry Pi Pico boards — flight controller, motor drivers, IMU, power, and a 3D-printable frame.",
            "Work spans part selection, SBUS decoding, ESC experiments, JLCPCB manufacturing, and camera / ROS2 research for future autonomy.",
        ],
        "hero": [{"src": "assets/board.jpg", "caption": "Board / assembly work", "alt": "PCB drone hardware"}],
        "images": [
            {"src": "assets/screenshot.jpg", "caption": "Design / debug snapshot"},
            {"src": "assets/digikey.jpg", "caption": "Parts basket"},
        ],
        "flow": [
            {"title": "Design", "body": "Schematics and PCB versions in KiCad for JLCPCB."},
            {"title": "Bring-up", "body": "Test IMU, motor driver, buck converter, SBUS."},
            {"title": "Fly", "body": "Frame, ESCs, and control firmware on Pico."},
        ]
},
    {
        "slug": "volvo-widgets",
        "href": "projects/volvo-widgets/",
        "list_title": "Volvo widgets",
        "list_blurb": "Swift battery widget and trip rendering for a Volvo EV.",
        "list_meta": "private",
        "section": "Hardware",
        "title": "Volvo widgets",
        "tag": "battery widget · trip rendering for a Volvo EV",
        "status": "private",
        "stack": ["Swift", "WidgetKit", "Python"],
        "about": [
            "Apple widgets and rendering utilities around a Volvo EV — battery state at a glance, plus trip visualization.",
            "Keeps car status visible without opening the manufacturer app.",
        ],
        "hero": [{"src": "assets/car.jpg", "caption": "Widget car artwork", "alt": "Volvo car graphic"}],
        "arch": [
            {"title": "Battery widget", "body": "SwiftUI glanceable charge state."},
            {"title": "Trips", "body": "Render recorded trips into readable views."},
            {"title": "Refresh", "body": "Periodic updates via WidgetKit."},
        ]
},
    {
        "slug": "gimbal",
        "href": "projects/gimbal/",
        "list_title": "Gimbal / tracking",
        "list_blurb": "Object-tracking gimbal software so a camera follows a selected target.",
        "list_meta": "private",
        "section": "Hardware",
        "title": "Gimbal & object tracking",
        "tag": "vision-guided gimbal follow",
        "status": "private",
        "stack": ["Python", "OpenCV", "embedded"],
        "about": [
            "Software that tracks a selected object so a gimbal can keep the camera pointed at it.",
            "Part of a longer hardware thread that also includes ground-station and drone control experiments.",
        ],
        "flow": [
            {"title": "Select", "body": "Choose the object to follow in the video feed."},
            {"title": "Track", "body": "Computer vision estimates target motion."},
            {"title": "Actuate", "body": "Gimbal motors keep the camera locked on."},
        ]
},
    
    
    {
        "slug": "ble-notificator",
        "href": "projects/ble-notificator/",
        "list_title": "BLE Notificator",
        "list_blurb": "Android app that notifies when Bluetooth Low Energy devices appear.",
        "list_meta_html": '<a href="https://github.com/Arno1235/BLENotificator">github</a> · <a href="https://play.google.com/store/apps/details?id=com.arnovaneetvelde.blenotificator">Play Store</a>',
        "section": "Apps & misc",
        "title": "BLE Notificator",
        "tag": "Android BLE device presence alerts",
        "status": "public",
        "github": "https://github.com/Arno1235/BLENotificator",
        "links": [
            {
                "href": "https://play.google.com/store/apps/details?id=com.arnovaneetvelde.blenotificator",
                "label": "Play Store"
}
        ],
        "stack": ["Java", "Android", "Bluetooth LE"],
        "about": [
            "An Android app that notifies you when configured Bluetooth Low Energy devices come into range.",
            "Published on the Google Play Store.",
        ],
        "images": [
            {"src": "assets/screen-1.png", "caption": "Device list"},
            {"src": "assets/screen-2.png", "caption": "Notification settings"},
        ],
        "images_title": "App screens"
},
    {
        "slug": "touchid",
        "href": "projects/touchid/",
        "list_title": "Touch ID password",
        "list_blurb": "Pock Touch Bar widget that unlocks a password with Touch ID.",
        "list_meta_html": '<a href="https://github.com/Arno1235/TouchID_password">github</a>',
        "section": "Apps & misc",
        "title": "Touch ID password",
        "tag": "Pock Touch Bar widget · Touch ID",
        "status": "public",
        "github": "https://github.com/Arno1235/TouchID_password",
        "stack": ["Swift", "Pock", "Touch ID"],
        "about": [
            "A Pock widget for the MacBook Touch Bar that reveals or fills a password after Touch ID authentication.",
            "Small utility for keeping a secret behind biometrics on the Touch Bar.",
        ],
        "flow": [
            {"title": "Tap", "body": "Trigger the widget from the Touch Bar."},
            {"title": "Auth", "body": "Confirm with Touch ID."},
            {"title": "Unlock", "body": "Expose or use the stored password."},
        ]
},
    {
        "slug": "fitnessapp",
        "href": "projects/fitnessapp/",
        "list_title": "FitnessApp",
        "list_blurb": "Workout builder and progress tracker — mainly to practice app design.",
        "list_meta_html": '<a href="https://github.com/Arno1235/FitnessApp">github</a>',
        "section": "Apps & misc",
        "title": "FitnessApp",
        "tag": "workout builder · design practice",
        "status": "public · on hold",
        "github": "https://github.com/Arno1235/FitnessApp",
        "stack": ["Java", "Android"],
        "about": [
            "An app to create workouts and track progress, built primarily to get better at app design.",
            "Currently on hold.",
        ],
        "images": [
            {"src": "assets/pic00.jpg", "caption": "Screen 1"},
            {"src": "assets/pic01.jpg", "caption": "Screen 2"},
            {"src": "assets/pic02.jpg", "caption": "Screen 3"},
            {"src": "assets/pic03.jpg", "caption": "Screen 4"},
        ],
        "images_title": "UI"
},
    {
        "slug": "farmy",
        "href": "projects/farmy/",
        "list_title": "Farmy",
        "list_blurb": "AR tower-defense game from a hackathon. Discontinued.",
        "list_meta_html": '<a href="https://github.com/Arno1235/Farmy--Hackathon-">github</a>',
        "section": "Apps & misc",
        "title": "Farmy",
        "tag": "AR tower defense · hackathon · discontinued",
        "status": "public · discontinued",
        "github": "https://github.com/Arno1235/Farmy--Hackathon-",
        "stack": ["C#", "Unity", "AR Foundation"],
        "about": [
            "Farmy is an AR tower-defense game created during a hackathon competition.",
            "The project is discontinued; the repo remains as an archive of the Unity/AR Foundation experiment.",
        ],
        "arch": [
            {"title": "AR", "body": "Place the defense field in the real world."},
            {"title": "Defend", "body": "Tower defense loop on the tracked plane."},
            {"title": "Hackathon", "body": "Built under time pressure as a team demo."},
        ]
},
    
    {
        "slug": "chess-bot",
        "href": "projects/chess-bot/",
        "list_title": "chess bot",
        "list_blurb": "Chess engine challenge — numpy only, move within three seconds.",
        "list_meta": "private",
        "section": "Apps & misc",
        "title": "chess bot",
        "tag": "numpy-only chess engine challenge",
        "status": "private",
        "stack": ["Python", "NumPy"],
        "about": [
            "A chess bot built for a constrained challenge: use the provided board template, no external libraries except NumPy, and decide a move within three seconds.",
        ],
        "arch": [
            {"title": "Rules", "body": "Template board + legal move generation."},
            {"title": "Search", "body": "Evaluate positions under a hard time budget."},
            {"title": "Constraint", "body": "NumPy only — no chess libraries."},
        ]
},
    
    {
        "slug": "mcdo-bots",
        "href": "projects/mcdo-bots/",
        "list_title": "McDo bots",
        "list_blurb": "Small Python bots for McDonald’s web games.",
        "list_meta_html": '<a href="https://github.com/Arno1235/McDo_CandyCrush">candy</a> · <a href="https://github.com/Arno1235/McDo_FlappyWacko">flappy</a> · <a href="https://github.com/Arno1235/McDo_BurgerBuilding">burger</a>',
        "section": "Apps & misc",
        "title": "McDo bots",
        "tag": "Python bots for McDonald’s browser games",
        "status": "public",
        "links": [
            {"href": "https://github.com/Arno1235/McDo_CandyCrush", "label": "Candy Crush"},
            {"href": "https://github.com/Arno1235/McDo_FlappyWacko", "label": "Flappy"},
            {"href": "https://github.com/Arno1235/McDo_BurgerBuilding", "label": "Burger Building"},
            {"href": "https://github.com/Arno1235/McDo_KeepingUp", "label": "Keeping Up"},
        ],
        "stack": ["Python", "computer vision", "automation"],
        "about": [
            "A series of small Python programs that play McDonald’s promotional browser games — Candy Crush-style match-3, Flappy, burger building, and more.",
            "Mostly vision and input automation experiments wrapped around seasonal games.",
        ],
        "images": [
            {"src": "assets/candycrush.jpg", "caption": "Candy Crush bot in action"},
            {"src": "assets/el1.png", "caption": "Tile sprite"},
            {"src": "assets/flappy-1.png", "caption": "Flappy template 1"},
            {"src": "assets/flappy-2.png", "caption": "Flappy template 2"},
        ],
        "images_title": "Captures"
},
]

# Approx start dates from related GitHub repos / notes (YYYY-MM-DD).
DATES: dict[str, str] = {
    "infurn": "2026-02-15",

    "cutsched": "2026-07-22",
    "quant-arena": "2026-06-25",
    "factory-os": "2026-04-23",

    "roborock-mqtt": "2025-12-12",
    "mqtt-ha": "2026-02-06",
    "sparkplug": "2024-09-18",
    "yamal": "2024-02-07",
    "hivemq-uns": "2025-06-13",
    "market-ops": "2025-03-11",
    "openinsider": "2026-03-09",

    "cryptoai": "2021-04-04",
    "mvtec-yolo": "2024-09-28",
    "sam-lora": "2024-03-21",

    "catch-the-dot": "2023-08-02",
    "dl-scratch": "2023-01-29",

    "datalab": "2026-07-12",

    "pcb-drone": "2025-08-09",
    "volvo-widgets": "2025-04-22",
    "gimbal": "2019-05-31",

    "ble-notificator": "2020-08-19",
    "touchid": "2023-05-31",
    "fitnessapp": "2020-06-26",
    "farmy": "2020-11-29",

    "chess-bot": "2023-01-22",

    "mcdo-bots": "2022-12-05"
}

CAREER = [
    {
        "role": "AI & Software Engineer",
        "organization": "Coretecs",
        "type": "Job",
        "period": "2023-09 – present",
        "link": "https://www.coretecs.be/about/arno-van-eetvelde",
        "link_label": "coretecs.be",
        # From local Coretecs project folders (Documents + Extreme SSD); period = folder birth date.
        "projects": [
{
                "subject": "Coretecs AI internal development",
                "client": "Coretecs",
                "period": "2026-06-08",
                "link": "",
            },
{
                "subject": "Air Liquide engagement — phase 2",
                "client": "Air Liquide",
                "period": "2026-05-18",
                "link": "",
            },
{
                "subject": "Coretecs LEID internal initiative",
                "client": "Coretecs",
                "period": "2026-04-14",
                "link": "",
            },
{
                "subject": "Atvise Modbus driver work for SWDE",
                "client": "SWDE",
                "period": "2026-04-09",
                "link": "",
            },
{
                "subject": "Bekaert cut-to-length industrial software / automation",
                "client": "Bekaert",
                "period": "2026-03-31",
                "link": "",
            },
{
                "subject": "SWDE CSC2732 delivery",
                "client": "SWDE",
                "period": "2026-03-09",
                "link": "",
            },
{
                "subject": "Soudal functional design / industrial software engagement",
                "client": "Soudal",
                "period": "2026-03-06",
                "link": "",
            },
{
                "subject": "Yokogawa CIServer documentation and reference materials",
                "client": "Coretecs",
                "period": "2026-03-03",
                "link": "",
            },
{
                "subject": "IMEC SCADA / SD work targeting MEI 2026",
                "client": "IMEC",
                "period": "2026-03-03",
                "link": "",
            },
{
                "subject": "SWDE support — phase / version 2",
                "client": "SWDE",
                "period": "2026-03-03",
                "link": "",
            },
{
                "subject": "Coretecs internal portal",
                "client": "Coretecs",
                "period": "2026-02-20",
                "link": "",
            },
{
                "subject": "IMEC CI103 fix",
                "client": "IMEC",
                "period": "2026-02-09",
                "link": "",
            },
{
                "subject": "Coretecs AI knowledge-sharing / KSS materials",
                "client": "Coretecs",
                "period": "2026-01-26",
                "link": "",
            },
{
                "subject": "JECO industrial software / automation engagement",
                "client": "JECO",
                "period": "2026-01-07",
                "link": "",
            },
{
                "subject": "IMEC SCADA recode / SD rework",
                "client": "IMEC",
                "period": "2025-12-25",
                "link": "",
            },
{
                "subject": "Unilin presentation / pitch materials",
                "client": "Unilin",
                "period": "2025-11-25",
                "link": "",
            },
{
                "subject": "VAARR AI object reconstruction — follow-up / v2",
                "client": "VAARR",
                "period": "2025-11-17",
                "link": "",
            },
{
                "subject": "SWDE object-change handling and support",
                "client": "SWDE",
                "period": "2025-11-04",
                "link": "",
            },
{
                "subject": "Virtualization of IMEC SCADA / related infrastructure",
                "client": "IMEC",
                "period": "2025-11-04",
                "link": "",
            },
{
                "subject": "UNS monitoring deployment / adaptation for IMEC",
                "client": "IMEC",
                "period": "2025-10-31",
                "link": "",
            },
{
                "subject": "Coretecs general demo materials and prototypes",
                "client": "Coretecs",
                "period": "2025-09-26",
                "link": "",
            },
{
                "subject": "IMEC FAIN analysis form application",
                "client": "IMEC",
                "period": "2025-09-17",
                "link": "",
            },
{
                "subject": "SWDE diagnostics tooling and support",
                "client": "SWDE",
                "period": "2025-09-15",
                "link": "",
            },
{
                "subject": "Technoform laser label detection — phase 2 / v2",
                "client": "Technoform",
                "period": "2025-08-26",
                "link": "",
            },
{
                "subject": "Computer vision demo refresh for Coretecs",
                "client": "Coretecs",
                "period": "2025-08-06",
                "link": "",
            },
{
                "subject": "SWDE — automated generation / change tooling",
                "client": "SWDE",
                "period": "2025-07-29",
                "link": "",
            },
{
                "subject": "HiveMQ and Grafana monitoring stack for MQTT / UNS demos",
                "client": "Coretecs",
                "period": "2025-07-04",
                "link": "",
            },
{
                "subject": "AI exploration / PoC work for IMEC",
                "client": "IMEC",
                "period": "2025-07-03",
                "link": "",
            },
{
                "subject": "UNS monitoring platform (MQTT, observability) — internal Coretecs productization",
                "client": "Coretecs",
                "period": "2025-06-03",
                "link": "",
            },
{
                "subject": "Unified Namespace (UNS) exploration and setup for Nitto",
                "client": "Nitto",
                "period": "2025-06-03",
                "link": "",
            },
{
                "subject": "PILZ safety PLC / SCADA work for IMEC FAB23",
                "client": "IMEC",
                "period": "2025-03-26",
                "link": "",
            },
{
                "subject": "High-availability PostgreSQL setup for MQTT device authentication and authorization",
                "client": "Fluvius",
                "period": "2025-03-06",
                "link": "",
            },
{
                "subject": "Emergency stop / shutdown circuit integration into Yokogawa CIServer SCADA via OPC UA",
                "client": "IMEC",
                "period": "2024-12-26",
                "link": "",
            },
{
                "subject": "Nanoscope nutsmeter vision / measurement application",
                "client": "Nanoscope",
                "period": "2024-11-22",
                "link": "",
            },
{
                "subject": "Real-time laser label detection on extruded strips (line-scan camera, YOLO, OCR)",
                "client": "Technoform",
                "period": "2024-11-20",
                "link": "",
            },
{
                "subject": "SWDE support — SCADA / industrial software delivery (PX)",
                "client": "SWDE",
                "period": "2024-11-15",
                "link": "",
            },
{
                "subject": "Feasibility study: AI point-cloud reconstruction for repairing damaged 3D-scanned parts",
                "client": "VAARR",
                "period": "2024-10-23",
                "link": "",
            },
{
                "subject": "Computer vision demo application for Coretecs showcases",
                "client": "Coretecs",
                "period": "2024-10-16",
                "link": "",
            },
{
                "subject": "Advantech hardware / edge platform evaluation for Coretecs solutions",
                "client": "Coretecs",
                "period": "2024-10-16",
                "link": "",
            },
{
                "subject": "Air Liquide industrial software / automation engagement",
                "client": "Air Liquide",
                "period": "2024-10-11",
                "link": "",
            },
{
                "subject": "Evaluation and setup of AI / computer vision frameworks for delivery work",
                "client": "Coretecs",
                "period": "2024-09-11",
                "link": "",
            },
{
                "subject": "Accelerator Program: in-line computer vision quality control for surface anomalies on plastic extrusion",
                "client": "Technoform",
                "period": "2024-08-14",
                "link": "files/van-eetvelde-technoform-accelerator-inline-quality-control-blogpost.pdf",
                "link_label": "PDF",
                "todo": False,
            },
            {
                "subject": "R&D: LoRA fine-tuning of SAM for segmenting electrical cabinet components",
                "client": "Coretecs",
                "period": "2024-06-18",
                "link": "files/van-eetvelde-sam-lora-electrical-cabinet-segmentation-whitepaper.pdf",
                "link_label": "PDF",
                "todo": False,
            },
{
                "subject": "SCADA and Power BI integration for sensors off a PILZ safety PLC",
                "client": "IMEC",
                "period": "2024-04-02",
                "link": "",
                "todo": False,
            },
{
                "subject": "Computer vision dataset generation, YOLO training, and anomaly detection framework testing",
                "client": "Flanders Make",
                "period": "2023-12-22",
                "link": "",
                "todo": False,
            },
{
                "subject": "Multithreaded Python demo / simulation environment for Coretecs",
                "client": "Coretecs",
                "period": "2023-10-18",
                "link": "",
                "todo": False,
            },
{
                "subject": "Yokogawa CIServer state-machine tracking with SQL storage and Power Apps time-utilization views",
                "client": "MCAM",
                "period": "2023-10-12",
                "link": "",
                "todo": False,
            },
{
                "subject": "Gas measurement system (SIFT-MS) integration into Yokogawa CIServer SCADA",
                "client": "IMEC",
                "period": "2023-10-06",
                "link": "",
                "todo": False,
            },
        ],

    },
    {
        "role": "Advanced Master of Artificial Intelligence",
        "organization": "KU Leuven",
        "type": "Education",
        "period": "2022 – 2023",
        "link": "https://www.kuleuven.be/",
        "link_label": "kuleuven.be",
        "projects": [
            {
                "subject": "Thesis: Titanium 3D printing — computer vision-based anomaly detection and classification for critical components",
                "client": "Materialise",
                "period": "2022 – 2023",
                "link": "confidential",
                "todo": False,
            },
        ],
    },
    {
        "role": "Master of Industrial Engineering",
        "organization": "KU Leuven",
        "type": "Education",
        "period": "2021 – 2022",
        "link": "https://www.kuleuven.be/",
        "link_label": "kuleuven.be",
        "projects": [
            {
                "subject": "Thesis: End-to-end approach to detect food on a compartmentalized plate (segmentation and classification)",
                "client": "KU Leuven",
                "period": "2021 – 2022",
                "link": "files/van-eetvelde-end-to-end-food-detection-thesis.pdf",
                "link_label": "PDF",
                "todo": False,
            },
        ],
    },
    {
        "role": "Bachelor of Industrial Engineering",
        "organization": "KU Leuven",
        "type": "Education",
        "period": "2018 – 2021",
        "link": "https://www.kuleuven.be/",
        "link_label": "kuleuven.be",
        "projects": [],
    },
]

def todo_flag(item: dict) -> str:
    """Show a todo marker until the project page is finished (set todo=False to clear)."""
    return "todo" if item.get("todo", True) else ""


def progress_counts(projects: list[dict], career: list[dict]) -> tuple[int, int]:
    """Done / total across personal + career table rows (todo=False counts as done)."""
    items: list[dict] = list(projects)
    for row in career:
        items.extend(row.get("projects") or [])
    total = len(items)
    done = sum(1 for item in items if not todo_flag(item))
    return done, total


def project_link_cell(proj: dict) -> str:
    """Render link cell: plain text for 'confidential', otherwise optional hyperlink."""
    link = (proj.get("link") or "").strip()
    if not link:
        return ""
    if link.lower() == "confidential":
        return "confidential"
    label = proj.get("link_label") or ("PDF" if link.lower().endswith(".pdf") else link)
    # Relative file links from nested career section need to stay site-root relative.
    return f'<a href="{esc(link)}">{esc(label)}</a>'

def github_cell(p: dict) -> str:
    if p.get("github"):
        return f'<a href="{esc(p["github"])}">{esc(p["github"].rstrip("/").split("/")[-1])}</a>'
    links = p.get("links") or []
    gh_links = [l for l in links if "github.com" in l.get("href", "")]
    if gh_links:
        return " · ".join(
            f'<a href="{esc(l["href"])}">{esc(l["label"])}</a>' for l in gh_links
        )
    # pull first github link from list_meta_html if present
    meta = p.get("list_meta_html") or ""
    if "github.com" in meta:
        return meta
    return ""

def render_index(projects: list[dict]) -> str:
    """Home page: pure HTML table — no CSS, no JS."""
    rows = sorted(
        projects,
        key=lambda p: DATES.get(p["slug"], "0000-00-00"),
        reverse=True,
    )
    done, total = progress_counts(projects, CAREER)
    pct = round(100 * done / total) if total else 0
    parts = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8" />',
        '  <meta name="viewport" content="width=device-width, initial-scale=1" />',
        "  <title>Arno Van Eetvelde</title>",
        "</head>",
        "<body>",
        "  <center>",
        "  <h1>Arno Van Eetvelde</h1>",
        '  <p><a href="https://github.com/Arno1235">GitHub</a></p>',
        # Temporary personal progress tracker — remove before going live.
        f"  <p>Progress: {done}/{total} done ({pct}%)</p>",
        "  <h2>Personal Projects</h2>",
        "  <br>",
        '  <table border="1" cellpadding="6" cellspacing="0" align="center">',
        "    <thead>",
        "      <tr>",
        '        <th align="center">Project</th>',
        '        <th align="center">Type</th>',
        '        <th align="center">Date</th>',
        '        <th align="center">GitHub</th>',
        '        <th align="center">Flag</th>',
        "      </tr>",
        "    </thead>",
        "    <tbody>",
    ]
    for p in rows:
        date = DATES.get(p["slug"], "")
        parts.append("      <tr>")
        parts.append(
            f'        <td align="center"><a href="{esc(p["href"])}">{esc(p["list_title"])}</a></td>'
        )
        parts.append(f'        <td align="center">{esc(p["section"])}</td>')
        parts.append(f'        <td align="center">{esc(date)}</td>')
        parts.append(f'        <td align="center">{github_cell(p)}</td>')
        parts.append(f'        <td align="center">{esc(todo_flag(p))}</td>')
        parts.append("      </tr>")
    parts += [
        "    </tbody>",
        "  </table>",
        "  <br><br><br>",
        "  <h2>Career</h2>",
        "  <br>",
    ]
    for row in CAREER:
        link = row.get("link") or ""
        link_bit = (
            f' · <a href="{esc(link)}">{esc(row.get("link_label") or link)}</a>'
            if link
            else ""
        )
        parts.append(f"  <h3>{esc(row['role'])} — {esc(row['organization'])}</h3>")
        parts.append(
            f"  <p>{esc(row['type'])} · {esc(row['period'])}{link_bit}</p>"
        )
        projects = row.get("projects") or []
        if not projects:
            parts.append("  <br>")
            continue
        show_flag = any(todo_flag(proj) for proj in projects)
        parts += [
            "  <br>",
            '  <table border="1" cellpadding="6" cellspacing="0" align="center">',
            "    <thead>",
            "      <tr>",
            '        <th align="center">Subject</th>',
            '        <th align="center">Client</th>',
            '        <th align="center">Period</th>',
            '        <th align="center">Link</th>',
        ]
        if show_flag:
            parts.append('        <th align="center">Flag</th>')
        parts += [
            "      </tr>",
            "    </thead>",
            "    <tbody>",
        ]
        for proj in projects:
            parts.append("      <tr>")
            parts.append(
                f'        <td align="center">{esc(proj.get("subject") or proj.get("name") or "")}</td>'
            )
            parts.append(f'        <td align="center">{esc(proj.get("client") or "")}</td>')
            parts.append(f'        <td align="center">{esc(proj.get("period") or "")}</td>')
            parts.append(f'        <td align="center">{project_link_cell(proj)}</td>')
            if show_flag:
                parts.append(f'        <td align="center">{esc(todo_flag(proj))}</td>')
            parts.append("      </tr>")
        parts += ["    </tbody>", "  </table>", "  <br><br><br>"]

    parts += [
        "  </center>",
        "</body>",
        "</html>",
        "",
    ]
    return "\n".join(parts)

def main() -> None:
    (ROOT / "index.html").write_text(render_index(PROJECTS), encoding="utf-8")
    print("wrote index.html")

    type_dir = ROOT / "type"
    if type_dir.exists():
        for f in type_dir.glob("*.html"):
            f.unlink()
            print(f"removed {f.relative_to(ROOT)}")
        try:
            type_dir.rmdir()
            print("removed type/")
        except OSError:
            pass

    for p in PROJECTS:
        if p.get("external_page"):
            continue
        out = ROOT / "projects" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(project_page(p), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
