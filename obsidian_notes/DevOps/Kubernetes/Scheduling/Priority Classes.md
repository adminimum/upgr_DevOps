# 🗓️ Scheduling Type: Pod Scheduling / Preemption

  

## 📌 Description

A **PriorityClass** defines the **priority level of pods** in Kubernetes. Higher priority pods are scheduled before lower priority ones.  

## ⚙️ Implementation

Ensures that **critical workloads** run even when cluster resources are limited. Can trigger **preemption** of lower-priority pods.  
- Create a `PriorityClass` resource specifying a name, value, and optional description.  
- Assign the `priorityClassName` to pods that should use that priority.  
- Kubernetes scheduler uses this to decide **which pods get scheduled first** and which pods may be **preempted** if resources are tight.  

## ✅ Advantages

- Guarantees resources for **critical applications**.  
- Helps prevent **important workloads from being starved**.  
- Supports **preemption** for effective cluster resource management.  

## 📋 YAML

```YAML
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000                 # Higher number → higher priority
globalDefault: false         # Optional, default priority if no class assigned
description: "Critical workload priority"
# preemtion...
---
apiVersion: v1
kind: Pod
metadata:
  name: critical-pod
spec:
  containers:
  - name: app
    image: nginx
  priorityClassName: high-priority
```

  

### 🔖 Tags
#scheduling #preemption #priority #1000000p #pod