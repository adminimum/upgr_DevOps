## 📌 Definition

- What it is:
  Network Policies in Kubernetes define **how pods can communicate** with each other and with other network endpoints.  
  They act as **firewall rules** for pod-level communication within a cluster.

- How useful it is:
  They enhance **security and isolation** by controlling which pods can send or receive traffic. Without them, all pods can communicate freely — which is risky in multi-tenant or production environments

- Main details:
	- Network Policies are applied at the **namespace** level.
	- They work only if the cluster network plugin (CNI) supports them (e.g., Calico, Cilium, Weave Net).
	- You can define rules for **Ingress** (incoming traffic) and **Egress** (outgoing traffic).
	- Policies use labels to select pods and define rules about what’s allowed.

- How to implement:
	- Label the pods you want to control.
	- Define a `NetworkPolicy` manifest specifying which traffic is allowed.
	- Apply it using `kubectl apply -f policy.yaml`.
	- Ensure your CNI plugin supports network policies.

- Simple analogy:
  Think of Network Policies as **“doors and walls”** between your pods — by default, all doors are open, but you can close some and allow only specific pods (or namespaces) to talk to each other.

- Problem it solves:
	- Prevents unauthorized access between pods.
	- Reduces lateral movement in case of a security breach.
	- Helps comply with segmentation and zero-trust principles.

- Attributes:
	- Namespace-scoped
	- Label-based
	- Ingress/Egress control
	- Declarative YAML format
	- Depends on CNI provider

- My thoughts:
	This is an object in Kubernetes that allows you to create rules that allow or deny traffic between pods or services. Only supported when CNI plugin is installed.

## 🛠 Commands / Syntax

```bash
# Apply a network policy
kubectl apply -f network-policy.yaml

# List all network policies
kubectl get networkpolicy -A

# Describe a specific policy
kubectl describe networkpolicy allow-frontend
```

  

## 🗒️ YAML format example with explaining if needed

```YAML
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: app-space
spec:
  podSelector:
    matchLabels:
      role: frontend               # Target pods with label "role=frontend"
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: backend            # Allow traffic only from pods labeled "backend"
       namespaceSelector:
         matchLabels:
           kubernetes.io/metadata.name: prop
    - ipBlock:
      cidr: 192.168.102.11
    ports:
    - protocol: TCP
      port: 80                     # Allow traffic on port 80
  egress:
  - to:
    - podSelector:
        matchLabels:
          role: database           # Allow outgoing connections to database pods
    ports:
    - protocol: TCP
      port: 5432                   # PostgreSQL port

```

  

## List of tasks / Execution
-  Label pods consistently for traffic control.
-  Create namespace-specific network policies.
-  Restrict ingress from untrusted namespaces.
-  Limit egress to only required services (e.g., database, API).
-  Audit network flows using Cilium or Calico.
  

🏷️ Tags:
#network #policies #traffic #security #ingress #egress