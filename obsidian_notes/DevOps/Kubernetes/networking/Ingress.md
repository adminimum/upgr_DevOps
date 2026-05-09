![Ingress](ingress.svg)

## 📌 Description

**Ingress** is a Kubernetes API object that manages **external HTTP/HTTPS access** to services inside the cluster. It provides URL-based routing, TLS termination, and virtual hosting — all without needing a separate LoadBalancer per service.

Ingress requires an **Ingress Controller** to be installed (e.g. NGINX, Traefik, HAProxy).

## 🛠 Usage / Where

- Route `/api` → backend service, `/` → frontend service on the same domain.
- Terminate TLS at the ingress level (handle certs centrally).
- Host multiple apps on one IP via virtual hosting (`app1.example.com`, `app2.example.com`).

## ⚡ Advantages

- Single external IP/LoadBalancer for many services.
- Centralized TLS management (works with cert-manager).
- Path-based and host-based routing rules.

## ⚠️ Limitations

- Only covers HTTP/HTTPS — no TCP/UDP routing (use Service type LoadBalancer for that).
- Requires an Ingress Controller — extra component to maintain.
- Being superseded by the **Gateway API** for advanced use cases.

## 🧰 Key Concepts

| Concept | Description |
|---|---|
| **Ingress Controller** | Pod that reads Ingress rules and configures the proxy (NGINX, Traefik) |
| **IngressClass** | Selects which controller handles the Ingress |
| **TLS** | Terminate HTTPS using a Secret with cert/key |
| **Path types** | `Exact`, `Prefix`, `ImplementationSpecific` |

## 📋 YAML Example

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - myapp.example.com
      secretName: myapp-tls
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 8080
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend-service
                port:
                  number: 80
```

## 🛠 Commands

```bash
# List ingresses
kubectl get ingress -A

# Describe ingress (check rules + events)
kubectl describe ingress <name>

# Check ingress controller pods
kubectl get pods -n ingress-nginx
```

## 🔗 Related Topics

- [[Main Networking]]
- [[Gateway API]]
- [[Services]]
- [[TLS in kubernetes]]

## 🔗 Documentation

- [Ingress Docs](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)

🏷️ Tags: #ingress #networking #http #tls #routing #nginx #k8s
