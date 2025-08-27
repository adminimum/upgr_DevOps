# 🗓️ Scheduling Type:  Manual Scheduling

## 📌 Description

- Pods are created without a scheduler.
- The user explicitly assigns a Pod to a Node by setting the `nodeName` field.

## ⚙️ Implementation

- Define `nodeName` directly in the Pod spec.
- Example:
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: manual-pod
  spec:
    containers:
    - name: nginx
      image: nginx
    nodeName: node1```

## ✅ Advantages

- Full control over which node a Pod runs on.
    
- Useful for testing, debugging, or special placement needs.

### 🔖 Tags 
#kubernetes #scheduling #manual