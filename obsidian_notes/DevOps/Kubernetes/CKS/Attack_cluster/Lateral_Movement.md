# Lateral Movement

After initial access to a pod, an attacker moves **laterally through the cluster** — escalating privileges, stealing secrets, and reaching other namespaces or nodes.

---

## ⚠️ Movement Vectors

### 1. Service Account Token Abuse
- Every pod gets a SA token mounted at `/var/run/secrets/kubernetes.io/serviceaccount/token`.
- If the SA has broad RBAC permissions, attacker uses the token to call the API server.

```bash
# Inside a compromised pod
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
CA=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
API=https://kubernetes.default.svc

# List all secrets (if SA has permission)
curl -s $API/api/v1/namespaces/default/secrets \
  --header "Authorization: Bearer $TOKEN" \
  --cacert $CA
```

### 2. RBAC Privilege Escalation
- `cluster-admin` or wildcard roles (`*`) give full access.
- Overly permissive bindings: `system:authenticated` bound to powerful roles.
- Attacker with `create pods` permission can create a privileged pod and escape to the node.

```bash
# Check what the current SA can do
kubectl auth can-i --list --as=system:serviceaccount:default:my-sa
```

### 3. Secrets Theft
- Secrets stored in ETCD in base64 (not encrypted by default).
- Any pod with `get secrets` permission can read them.
- Env-var mounted secrets are visible in `kubectl describe pod`.

```bash
# Attacker lists and reads secrets via API
curl -s $API/api/v1/namespaces/kube-system/secrets \
  --header "Authorization: Bearer $TOKEN" --cacert $CA \
  | jq '.items[].data'
```

### 4. Moving to Other Namespaces
- ClusterRoleBindings let a SA access resources across all namespaces.
- Attacker pivots from a low-privilege app namespace to `kube-system`.

### 5. Creating Backdoor Resources
- Attacker with `create` permissions plants:
  - A new SA with `cluster-admin` binding
  - A CronJob that exfiltrates data
  - A DaemonSet that runs on every node

---

## 🛡 Defenses (CKS exam focus)

| Attack | Defense |
|---|---|
| SA token abuse | `automountServiceAccountToken: false`, least-privilege SA roles |
| RBAC escalation | Audit bindings, no wildcards, no `cluster-admin` for apps |
| Secrets theft | Encrypt secrets at rest, use Secret Store CSI Driver |
| Cross-namespace pivot | Namespace-scoped Roles instead of ClusterRoles |
| Backdoor resources | Audit logs, OPA policies restricting resource creation |

---

## 🔗 Related

- [[The_Attack]]
- [[API Server Attacks]]
- [[Container_Escape]]
- [[Network Attacks]]

🏷️ Tags: #cks #attack #lateral-movement #rbac #service-account #secrets #privilege-escalation
