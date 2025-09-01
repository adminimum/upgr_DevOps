# 🗓️ Scheduling Type: Labels & Selectors

## 📌 Description

- **Labels** are key-value pairs attached to Kubernetes objects (Pods, Deployments, etc.).
- **Selectors** are queries that filter objects based on labels.
- They are the foundation for grouping, managing, and targeting workloads.

## ⚙️ Implementation

- Add `labels` in the metadata of objects.
- Use `selector` in Services, ReplicaSets, or Deployments to match Pods with specific labels.

## ✅ Advantages

- Organizes resources logically (e.g., by environment, version, app).
- Enables rolling updates and scaling by targeting specific Pods.
- Simplifies management of large clusters.

## 📋 YAML

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
    env: prod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
        env: prod
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        
```
---

  

### 🔖 Tags 
#labels #tags #marks #selector #scheduling #search #sort