![image](networking.jpg)
## 🧠 Kubernetes Networking — Main Concepts

### 📡 1. **Pod-to-Pod Communication**

- Each **Pod gets its own IP** address.
- **All Pods can talk to each other** directly without NAT.
- This is enabled by the **CNI plugin** (e.g., Calico, Flannel).
    

---

### 🧭 2. **Services & Discovery**

- A **Service** exposes a group of Pods under a stable virtual IP.
- Internal DNS name:  
    `my-service.my-namespace.svc.cluster.local`
    
- **Service types**:
    - `ClusterIP`: internal-only (default)
    - `NodePort`: exposed on a static port on each Node
    - `LoadBalancer`: provisioned by cloud provider (GCP, AWS, etc.)
        

---

### 🌐 3. **Ingress (HTTP Routing)**

- Ingress routes external HTTP/HTTPS traffic to Services.
- Requires an **Ingress Controller** (like NGINX, Traefik).
- Supports TLS, virtual hosts, path-based routing, and authentication.

---

### 📦 4. **CNI Plugin (Container Network Interface)**

- Handles IP allocation, routing, and connectivity.
- Examples: `Calico`, `Flannel`, `Cilium`, `Weave`.
- Every Pod-to-Pod and Node-to-Pod traffic goes through the CNI layer.

---

### 🔒 5. **Network Policies**

- Used to **control which Pods can talk to each other**.
- Define **allow/deny** rules based on:
    - Pod labels
    - Namespaces
    - Ports 
- Only work with CNI plugins that support them (e.g., Calico).
    

---

## 🚀 Quick Reference
```
# Check connection from one pod to a service
kubectl exec -it <pod> -- curl <service>:<port>

# View services
kubectl get svc -A

# View Ingress rules
kubectl get ingress -A

# Apply a network policy
kubectl apply -f policy.yaml

```

---

## 🔗 Related Topics
- [[]]