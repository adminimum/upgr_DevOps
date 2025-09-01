## 📌 Description

- **Taints** are applied to nodes to repel certain pods. 
- **Tolerations** are applied to pods to allow them to be scheduled on tainted nodes. 
- Together, they control which pods can (or cannot) run on specific nodes.
## ⚙️ Implementation

- Add a taint to a node:
    `kubectl taint nodes <node-name> key=value:NoSchedule`
- Add a toleration to a pod spec so it can run on the tainted node.
- Types of taint effects:
    - **NoSchedule** → new pods won’t schedule unless they tolerate.
    - **PreferNoSchedule** → try to avoid scheduling, but not guaranteed.    
    - **NoExecute** → evict running pods without toleration and block new ones.

## ✅ Advantages

- Provides fine-grained control over pod placement.
- Ensures critical workloads are isolated to dedicated nodes.
- Helps prevent resource conflicts between different workloads.

## 📋 YAML

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: tolerant-pod
spec:
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoSchedule"
  containers:
  - name: nginx
    image: nginx

```


## 🎬  Create taints for node
```
# 1. Add a taint to a node
kubectl taint nodes <node-name> key=value:NoSchedule

# 2. Remove a taint from a node
kubectl taint nodes <node-name> key:NoSchedule-

# 3. Check taints on nodes
kubectl describe node <node-name> | grep Taints

```

### 🔖 Tags
#taints #toleration #scheduling #yaml #tolerations #NoExecute #NoSchedule