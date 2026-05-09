# CKS — Certified Kubernetes Security Specialist

## 📌 About the Exam

- **Duration:** 2 hours
- **Format:** Performance-based (hands-on terminal tasks)
- **Passing score:** 67%
- **Prerequisite:** Active CKA certification

---

## 🗺 Exam Domains & Weights

| Domain | Weight |
|---|---|
| Cluster Setup | 10% |
| Cluster Hardening | 15% |
| System Hardening | 15% |
| Minimize Microservice Vulnerabilities | 20% |
| Supply Chain Security | 20% |
| Monitoring, Logging & Runtime Security | 20% |

---

## 🧰 Key Tools to Know

| Tool | Purpose |
|---|---|
| **Falco** | Runtime threat detection |
| **Trivy** | Container image vulnerability scanning |
| **OPA / Gatekeeper** | Policy enforcement |
| **kube-bench** | CIS benchmark checks for cluster config |
| **Kubesec** | Static security risk analysis of manifests |
| **AppArmor** | Linux kernel MAC — restrict container syscalls |
| **Seccomp** | Filter syscalls at container level |
| **Audit logs** | Track API server requests |

---

## 📋 Study Checklist

### Cluster Setup
- [ ] Network policies — default deny all ingress/egress
- [ ] Ingress with TLS
- [ ] CIS benchmark with kube-bench
- [ ] Kubernetes dashboard security

### Cluster Hardening
- [ ] RBAC — least privilege roles
- [ ] Service account token restrictions
- [ ] Upgrade Kubernetes frequently
- [ ] Restrict API server access

### System Hardening
- [ ] Minimize OS footprint
- [ ] AppArmor profiles
- [ ] Seccomp profiles
- [ ] Remove unnecessary packages / open ports

### Minimize Microservice Vulnerabilities
- [ ] PodSecurityAdmission (restricted profile)
- [ ] OPA Gatekeeper policies
- [ ] Security contexts (runAsNonRoot, readOnlyRootFilesystem)
- [ ] Secrets management — avoid env vars, use volumes

### Supply Chain Security
- [ ] Trivy — scan images for CVEs
- [ ] Allowed registries (ImagePolicyWebhook)
- [ ] Sign and verify images
- [ ] Dockerfile best practices (distroless, non-root)

### Monitoring, Logging & Runtime Security
- [ ] Falco rules — detect suspicious behavior
- [ ] Audit policy — log sensitive API calls
- [ ] Immutable containers
- [ ] Detect deleted/modified binaries at runtime

---

## 🔗 Official Resources

- [CKS Exam Curriculum](https://github.com/cncf/curriculum)
- [Kubernetes Security Docs](https://kubernetes.io/docs/concepts/security/)
- [Killer.sh CKS Simulator](https://killer.sh)
- [Falco Docs](https://falco.org/docs/)
- [Trivy Docs](https://aquasecurity.github.io/trivy/)

---

🏷️ Tags: #cks #security #kubernetes #exam #preparation
