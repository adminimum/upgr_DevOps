# The Attack — Kubernetes Cluster Attack Vectors

Understanding how attackers compromise clusters is the foundation of CKS. You defend what you understand.

---

## 🗺 Attack Surface Model — The 4Cs

```
┌──────────────────────────────────┐
│             CLOUD                │  ← infrastructure, IAM, network
│  ┌────────────────────────────┐  │
│  │         CLUSTER            │  │  ← API server, ETCD, RBAC
│  │  ┌──────────────────────┐  │  │
│  │  │     CONTAINER        │  │  │  ← escapes, privileges
│  │  │  ┌────────────────┐  │  │  │
│  │  │  │      CODE      │  │  │  │  ← app vulns, dependencies
│  │  │  └────────────────┘  │  │  │
│  │  └──────────────────────┘  │  │
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

Each layer can be breached independently. A breach in an outer layer puts all inner layers at risk.

---

## 📂 Attack Topics

- [[API Server Attacks]] — exposed API, anonymous auth, ETCD access
- [[Container Escape]] — privileged containers, hostPath, host namespaces
- [[Lateral Movement]] — service account abuse, secrets theft, RBAC escalation
- [[Network Attacks]] — traffic sniffing, DNS spoofing, egress exfiltration

---

## ⚡ Quick Attack Timeline (typical cluster breach)

```
1. Recon        → scan open ports, find exposed API server / dashboard
2. Initial access → exploit unauth API, steal SA token, malicious image
3. Execution    → run code in a pod
4. Escalation   → escape container → gain node access
5. Lateral move → use SA tokens, access secrets, RBAC misconfig
6. Persistence  → create backdoor SA, plant malicious cronjob
7. Exfiltration → dump ETCD, steal secrets
```

---

## 🔗 Related CKS Domains

- [[CKS Home]]

🏷️ Tags: #cks #attack #security #4cs #kubernetes
