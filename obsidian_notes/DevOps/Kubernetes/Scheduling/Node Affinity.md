# 🗓️ Scheduling Type: Node Affinity

## 📌 Description

- A more flexible way than `nodeSelector` to control pod placement on nodes.
- Supports **required** rules (must match) and **preferred** rules (soft preferences).
- Allows expressions like `In`, `NotIn`, `Exists`, `DoesNotExist`, `Gt`, `Lt`.

## ⚙️ Implementation

- Defined under `.spec.affinity.nodeAffinity` in a Pod spec.
- Two types:
    - `requiredDuringSchedulingIgnoredDuringExecution` → strict rules (pod won’t schedule if not met).
    - `preferredDuringSchedulingIgnoredDuringExecution` → soft rules (scheduler tries but not guaranteed).
    - `requiredDuringSchedulingRequiredDuringExecution` → strict rules (pod won’t schedule if not met and all existing pods will be rescheduled).

## ✅ Advantages

- More expressive than `nodeSelector`.
- Allows ranking of nodes with weights.
- Provides fallback scheduling options when exact match isn’t possible.

## 📋 YAML

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: affinity-pod
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: region
            operator: In
            values:
            - us-east
  containers:
  - name: nginx
    image: nginx

```

  

### 🔖 Tags 
#nodeaffinity #node #affinity #scheduling #selected