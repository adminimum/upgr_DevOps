# API Server Attacks

The **API server is the single entry point** to a Kubernetes cluster. Compromising it = full cluster control.

---

## ⚠️ Attack Vectors

### 1. Anonymous Authentication Enabled
- If `--anonymous-auth=true` (default in some versions), unauthenticated requests are allowed as `system:anonymous`.
- An attacker can enumerate resources, or worse — if RBAC binds permissions to `system:unauthenticated`.

```bash
# Check if anonymous access works
curl https://<api-server>:6443/api/v1/namespaces --insecure
```

### 2. Exposed API Server (no firewall)
- Port `6443` exposed to the internet.
- Attacker brute-forces or steals kubeconfig/service account token.

### 3. ETCD Exposed (port 2379)
- ETCD stores the **entire cluster state including Secrets in base64**.
- If port 2379 is open without mTLS, attacker reads all secrets directly.

```bash
# Attacker dumps all secrets from exposed ETCD
etcdctl get / --prefix --keys-only
etcdctl get /registry/secrets/default/my-secret
```

### 4. Insecure Kubelet API (port 10250)
- Kubelet exposes a read/write API.
- If `--anonymous-auth=true` on kubelet, attacker can exec into any pod on that node.

```bash
# List pods on node via exposed kubelet
curl -sk https://<node-ip>:10250/pods

# Exec into a container via kubelet
curl -sk https://<node-ip>:10250/run/<namespace>/<pod>/<container> \
  -d "cmd=id"
```

### 5. Kubernetes Dashboard (unauthenticated)
- Default dashboard install in older versions had no authentication.
- Attacker uses dashboard UI to create privileged pods or read secrets.

---

## 🛡 Defenses (CKS exam focus)

| Attack | Defense |
|---|---|
| Anonymous auth | `--anonymous-auth=false` on API server and kubelet |
| Exposed API | Firewall port 6443, restrict to VPN/bastion |
| ETCD exposed | mTLS on ETCD, restrict port 2379 to control plane only |
| Insecure kubelet | `--anonymous-auth=false`, `--authorization-mode=Webhook` |
| Dashboard | Enable authentication, use RBAC, don't expose externally |

---

## 🔗 Related

- [[The_Attack]]
- [[Lateral Movement]]

🏷️ Tags: #cks #attack #api-server #etcd #kubelet #authentication
