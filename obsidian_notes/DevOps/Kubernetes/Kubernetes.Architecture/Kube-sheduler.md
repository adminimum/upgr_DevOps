![scheduler](scheduler.gif)
## 📌 Definition

- What it is:
	A core Kubernetes component that decides **which node a new Pod should run on**.

- How useful it is:
	It ensures pods are placed on the best possible nodes, considering resources (CPU, RAM), policies, and constraints. Without it, you’d have to manually assign pods to nodes.

- How to implement:
	Usually runs by default when you set up a cluster with `kubeadm` or a managed service (like GKE, EKS). If building from scratch, you deploy it as a control-plane component (manifest in `/etc/kubernetes/manifests/kube-scheduler.yaml`).

- Simple analogy:
	Usually runs by default when you set up a cluster with `kubeadm` or a managed service (like GKE, EKS). If building from scratch, you deploy it as a control-plane component (manifest in `/etc/kubernetes/manifests/kube-scheduler.yaml`).

- Problem it solves:
	Automates **workload placement**. Without it, admins would have to constantly decide and assign resources for every pod manually.

  

## 🔗 Related Topics

 
## 🛠 Commands / Syntax

```bash
# Describe a pod to see scheduling issues
kubectl describe pod <pod-name>

# List all nodes with details
kubectl get nodes -o wide

# Check nodes with their labels
kubectl get nodes --show-labels

# Simulate scheduling with dry-run
kubectl apply -f pod.yaml --dry-run=server

```

  

## List of tasks / Execution

- [] Create Pod with different requirements including all of possible options for getting pending status without matching to any node and then create full requirements it the yaml configuration for the pod to get successful placing. 

  

🏷️ Tags: #scheduler #architecture