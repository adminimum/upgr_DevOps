# CLAUDE.md

This is a personal DevOps learning repository containing Obsidian vaults, lab notes, and automation projects.

---

## Repository Structure

```
upgr_DevOps/
├── obsidian_notes/
│   ├── DevOps/          ← main Obsidian vault (Kubernetes, CKS, TLS, Bash, etc.)
│   └── English/         ← English learning vault (grammar, vocabulary)
├── CKA_notes/           ← CKA exam preparation materials
├── Go_AutoConfig/       ← Go automation project
├── Kubernetes/          ← additional Kubernetes resources/manifests
├── obsidian_templates/  ← Obsidian note templates
├── pet/                 ← pet CLI config
└── README.md
```

---

## Obsidian Vault — DevOps

**Vault root:** `obsidian_notes/DevOps/`
**Theme:** Obsidian gruvbox (dark, warm tones)
**Entry point:** `obsidian_notes/DevOps/HOME.md`

### Folder layout

```
DevOps/
├── HOME.md                          ← master vault index
├── images/                          ← ALL images go here (shared across vault)
├── Kubernetes/
│   ├── Kubernetes.md                ← K8s main index
│   ├── Kubernetes.Architecture/     ← control plane components
│   ├── Kubernetes.Attributes/       ← workload objects
│   ├── Applicaion Lifecycle Management/
│   ├── CKS/                         ← CKS exam prep (isolated in graph)
│   │   ├── CKS Home.md
│   │   ├── Attack_cluster/
│   │   ├── Cluster_Setup_&_Hardening/
│   │   ├── System_Hardening/
│   │   ├── Minimize_Microservice_Vulnerabilities/
│   │   ├── Supply_Chain_Security/
│   │   └── Monitoring_Logging_Runtime/
│   ├── Cluster Maintenance/
│   ├── Helm/
│   ├── Kustomize/
│   ├── Monitoring/
│   ├── Scheduling/
│   ├── Security/
│   ├── Storage/
│   ├── Troubleshooting/
│   └── networking/
├── Bash/
└── TLS/
```

---

## Note Conventions

### Standard note template

Every topic note follows this structure — use it when creating new notes:

```markdown
![Topic Image](image-filename.ext)

## 📌 Description
## 🛠 Usage / Where
## ⚡ Advantages
## ⚠️ Limitations
## 🧰 Key Concepts / Tools
## 🛠 Commands / Syntax     ← bash/yaml code blocks
## 📋 YAML Example          ← if applicable
## 🔗 Related Topics        ← wikilinks to connected notes
## 🔗 Documentation
🏷️ Tags: #tag1 #tag2
```

### Index / home page template

Each major folder has an index note that links to its subtopics:

```markdown
![image](image.ext)

## 📌 Description
## 🧩 Key Areas            ← table: topic | what it covers
## 📂 Subtopics            ← [[wikilinks]] list
## 🔗 Documentation
🏷️ Tags: #index #topic
```

### Wikilinks

- Internal links always use Obsidian wikilink syntax: `[[Note Name]]`
- Images are referenced by **filename only** — Obsidian resolves them vault-wide: `![alt](filename.ext)`
- Never use relative paths for images (e.g. `../../images/x.png`) — use just the filename

### Images

- **All images live in `obsidian_notes/DevOps/images/`** — never inside topic subfolders
- Download images locally before referencing; do not embed external URLs in notes
- Preferred formats: `.svg` for logos/diagrams, `.png` for screenshots/photos

### Tags

- Use lowercase hyphenated tags: `#cluster-setup`, `#api-server`
- CKS notes must include `#cks` tag — this makes them appear gold in the graph view
- Index/home pages get `#index` tag
- Main topic pages get `#main` tag (styled yellow and large via CSS)

---

## Graph View Configuration

**CSS file:** `obsidian_notes/DevOps/.obsidian/snippets/head.css`

Current graph colors (gruvbox palette):
- Lines: red `rgba(204, 36, 29, 0.75)`
- Arrows: gruvbox yellow
- Nodes: dark blue `#1a3a5c`
- Focused node: gruvbox red
- Unresolved links: muted gray
- `#cks` tagged nodes: gold `#FFD700` (via colorGroups in graph.json)

**Important:** Obsidian rewrites `graph.json` every time the user adjusts graph settings via the UI, which resets `colorGroups` to `[]`. If the CKS gold color disappears, re-add it to `graph.json`:
```json
"colorGroups": [
  { "query": "tag:#cks", "color": { "a": 1, "rgb": 16766720 } }
]
```

**CKS notes are intentionally isolated in the graph** — avoid adding links from CKS notes to the main K8s notes unless the user explicitly asks.

---

## Git Conventions

- **Branch:** `main`
- **Remote:** `git@github.com:adminimum/upgr_DevOps.git`
- **Never commit:** `workspace.json` — this is Obsidian's session state (open files, pane layout); it changes on every vault open
- **Do commit:** all `.md` files, images, `head.css`, `graph.json`, `core-plugins.json`
- Commit messages should summarize what topics/notes were added or changed

---

## CKS Exam Notes

The `CKS/` folder is structured around the 6 official exam domains:

| Folder | Exam domain | Weight |
|---|---|---|
| `Cluster_Setup_&_Hardening/` | Cluster Setup + Cluster Hardening | 10% + 15% |
| `System_Hardening/` | System Hardening | 15% |
| `Minimize_Microservice_Vulnerabilities/` | Minimize Microservice Vulnerabilities | 20% |
| `Supply_Chain_Security/` | Supply Chain Security | 20% |
| `Monitoring_Logging_Runtime/` | Monitoring, Logging & Runtime Security | 20% |
| `Attack_cluster/` | Attack surface understanding (cross-domain) | — |

---

## Lab Credentials (README reference)

Practice lab servers are documented in `README.md`. These are Stratos DC / KodeKloud lab environments — not production systems.
