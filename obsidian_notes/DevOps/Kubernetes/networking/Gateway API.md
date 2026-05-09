![Gateway API](gateway-api.png)

## 📌 Description

**Gateway API** is the modern successor to Ingress in Kubernetes. It provides a more expressive, role-oriented, and extensible API for managing **L4 and L7 traffic routing** — covering HTTP, HTTPS, TCP, gRPC, and more.

It splits responsibilities into separate objects: infrastructure teams manage **Gateways**, app teams manage **Routes**.

## 🛠 Usage / Where

- Advanced HTTP routing (header-based, method-based, weight-based traffic splitting).
- Multi-team clusters where infra and app teams manage routing separately.
- TCP/UDP routing (not possible with Ingress).
- Canary releases and traffic mirroring.

## ⚡ Advantages over Ingress

| Feature | Ingress | Gateway API |
|---|---|---|
| TCP/UDP support | No | Yes |
| Traffic splitting | Via annotations | Native |
| Multi-team roles | Single object | Gateway + Route separation |
| Header routing | Via annotations | Native |
| Extensibility | Annotations (hacky) | Proper API extensions |

## ⚠️ Limitations

- Still maturing — not all controllers support all features yet.
- More complex to set up than Ingress for simple use cases.
- Requires a compatible controller (Envoy Gateway, Traefik v3, NGINX Gateway Fabric).

## 🧰 Key Objects

| Object | Managed by | Purpose |
|---|---|---|
| `GatewayClass` | Cluster admin | Defines which controller to use |
| `Gateway` | Infra team | Declares listener ports and protocols |
| `HTTPRoute` | App team | Routes HTTP traffic to services |
| `TCPRoute` | App team | Routes TCP traffic |
| `GRPCRoute` | App team | Routes gRPC traffic |

## 📋 YAML Example

```yaml
# Gateway — managed by infra team
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: main-gateway
spec:
  gatewayClassName: envoy
  listeners:
    - name: http
      port: 80
      protocol: HTTP

---
# HTTPRoute — managed by app team
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: my-app-route
spec:
  parentRefs:
    - name: main-gateway
  hostnames:
    - myapp.example.com
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: api-service
          port: 8080
```

## 🔗 Related Topics

- [[Ingress]]
- [[Main Networking]]
- [[Services]]

## 🔗 Documentation

- [Gateway API Docs](https://gateway-api.sigs.k8s.io/)
- [Gateway API vs Ingress](https://gateway-api.sigs.k8s.io/concepts/gamma/)

🏷️ Tags: #gateway-api #networking #http #routing #traffic #kubernetes #k8s
