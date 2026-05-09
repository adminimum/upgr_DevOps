# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is an **Obsidian vault** — a personal DevOps knowledge base (CKA/CKS exam prep, Kubernetes, Linux, networking, TLS, Bash, etc.). There are no build, lint, or test commands. All work here is creating and editing Markdown notes.

---

## Note Templates

Every topic note must follow this structure:

```markdown
![Topic Image](image-filename.ext)

## 📌 Description
## 🛠 Usage / Where
## ⚡ Advantages
## ⚠️ Limitations
## 🧰 Key Concepts / Tools
## 🛠 Commands / Syntax
## 📋 YAML Example
## 🔗 Related Topics
## 🔗 Documentation
🏷️ Tags: #tag1 #tag2
```

Index/home notes (one per major folder) use this structure:

```markdown
![image](image.ext)

## 📌 Description
## 🧩 Key Areas       ← table: topic | what it covers
## 📂 Subtopics       ← [[wikilinks]] list
## 🔗 Documentation
🏷️ Tags: #index #topic
```

---

## Wikilinks and Images

- Internal links: always `[[Note Name]]` — never markdown `[text](path.md)`
- Image references: filename only — `![alt](filename.ext)` — Obsidian resolves vault-wide
- **Never use relative paths** for images (e.g. `../../images/x.png`)
- All images live in `images/` at the vault root — never inside topic subfolders
- Download images locally; do not embed external URLs
- Preferred: `.svg` for logos/diagrams, `.png` for screenshots

---

## Tags

- Lowercase hyphenated: `#cluster-setup`, `#api-server`
- `#cks` — required on all CKS notes; renders nodes gold in graph view
- `#index` — index/home pages
- `#main` — main topic pages (styled yellow and large via CSS)

---

## CKS Section Rules

- CKS notes live in `Kubernetes/CKS/` and are **intentionally isolated** in the graph view
- Do not add links from CKS notes to main K8s notes unless explicitly asked
- CKS domains and exam weights:

| Folder | Domain | Weight |
|---|---|---|
| `Cluster_Setup_&_Hardening/` | Cluster Setup + Cluster Hardening | 10% + 15% |
| `System_Hardening/` | System Hardening | 15% |
| `Minimize_Microservice_Vulnerabilities/` | Minimize Microservice Vulnerabilities | 20% |
| `Supply_Chain_Security/` | Supply Chain Security | 20% |
| `Monitoring_Logging_Runtime/` | Monitoring, Logging & Runtime Security | 20% |
| `Attack_cluster/` | Attack surface (cross-domain) | — |

---

## Graph View Gotcha

Obsidian rewrites `.obsidian/graph.json` every time graph settings are changed via the UI, resetting `colorGroups` to `[]`. If CKS nodes lose their gold color, restore it:

```json
"colorGroups": [
  { "query": "tag:#cks", "color": { "a": 1, "rgb": 16766720 } }
]
```

CSS for graph and node styling lives in `.obsidian/snippets/head.css`.

---

## Git

- **Never commit** `.obsidian/workspace.json` — it changes on every vault open
- **Do commit:** `.md` files, `images/`, `head.css`, `graph.json`, `core-plugins.json`
- Commit messages should name the topics or notes added/changed
