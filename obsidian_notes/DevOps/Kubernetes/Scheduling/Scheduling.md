`![Scheduling](scheduler.png)
## ❓What is it in Kubernetes

Scheduling in Kubernetes is the process of deciding **which node a Pod should run on**. The **kube-scheduler** looks at available resources, constraints, and policies, then assigns Pods to nodes.

## 💡 Types of scheduling

1. **Default Scheduling**
    - Performed automatically by the `kube-scheduler`.
    - Considers CPU, memory, affinity/anti-affinity, taints, tolerations, etc.
2. **Manual Scheduling**
    - User sets the `nodeName` field in the Pod spec.
3. **NodeSelector**
    - Assigns Pods to nodes with a specific label.
4. **Node Affinity / Anti-Affinity**
    - More expressive version of NodeSelector (soft vs hard rules).
5. **Taints and Tolerations**
    - Restrict which Pods can run on which nodes.
6. **Custom Scheduling**
    - Using your own scheduler instead of the default one.

## ⌕ Order of scheduling

1. Pod creation request is received by API server.
2. Pod goes into **Pending** state.
3. `kube-scheduler` evaluates available nodes.
4. Scheduler checks constraints (resources, affinity, taints, etc).
5. Pod is bound to the best-fitting node.
6. `kubelet` on that node pulls images and starts the Pod.

## 🛠️ Tools for scheduling

- **NodeSelector** – bind Pods to labeled nodes.
- **Node Affinity / Anti-Affinity** – advanced placement rules.
- **Taints & Tolerations** – keep unwanted Pods away from certain nodes.
- **Pod Affinity / Anti-Affinity** – schedule Pods near/away from other Pods.
- **Resource Requests & Limits** – ensure Pods land on nodes with enough capacity.

## 📂 Subtopics

- [[Manual Scheduling]]

  

## 🛠 Commands / Syntax

```bash
# 1. Check node labels (important for scheduling decisions)
kubectl get nodes --show-labels

# 2. Add a label to a node
kubectl label node <node-name> disktype=ssd

# 3. Create a pod using a specific nodeSelector
kubectl apply -f pod-nodeselector.yaml

# 4. Add a taint to a node
kubectl taint nodes <node-name> key=value:NoSchedule

# 5. Remove taint from a node
kubectl taint nodes <node-name> key:NoSchedule-


```

## 📝 Example Learning Task

- Label one node as `role=frontend`.
    
- Create a Deployment with 3 replicas of `nginx`.
    
- Use `nodeSelector` to schedule Pods only on nodes labeled `role=frontend`.
    
- Add a taint to the node and configure Pods with matching toleration.
    
- Observe how scheduling changes when taints/tolerations are added or removed

  

🏷️ Tags: #scheduler #scheduling #affinity #selector #labels

