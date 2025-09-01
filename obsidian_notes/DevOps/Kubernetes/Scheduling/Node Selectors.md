# 🗓️ Scheduling Type: Node Selectors

## 📌 Description

- Node selectors are the simplest form of node selection constraint in Kubernetes.
- They allow you to schedule Pods onto specific nodes by matching Pod labels with node labels.

## ⚙️ Implementation

- Label the node with a key-value pair.
- Add the same key-value pair in the Pod specification under `nodeSelector`.
- The scheduler will place the Pod only on nodes that have the matching labels.

## ✅ Advantages

- Very simple and easy to understand.    
- Ensures Pods are scheduled only on specific nodes with required characteristics.
- Useful for separating workloads, e.g., GPU nodes vs. CPU-only nodes.

## 📋 YAML

```YAML
# Label a node
kubectl label nodes <node-name> disktype=ssd

# Pod definition using nodeSelector
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mycontainer
    image: nginx
  nodeSelector:
    disktype: ssd

```


### 🔖 Tags
#lables #nodeSelector #node #Selector #scheduling