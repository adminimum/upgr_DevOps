![Controller-Manager](controle-manager.jpg)
## 📌 Definition

- What it is:
  A core Kubernetes component that runs _controllers_ — background processes that constantly check the cluster state and try to make it match the desired state.

- How useful it is:
	It automates tasks like making sure pods are running, replacing failed pods, updating replicas, handling jobs, etc. Without it, you’d have to manually fix everything.

- How to implement:
	It runs automatically when you set up a cluster (with kubeadm, managed Kubernetes, etc.). You don’t usually install it separately — it’s part of the control plane.

- Simple analogy:
	Like an **autopilot in a plane** — constantly checking if the plane is on course and correcting it when needed.

- Problem it solves:
	Humans can’t constantly watch the cluster for failures or mismatches. The controller-manager automates that monitoring and correction.

- Consists of: 
	1. Deployment-controller
	2. Namespace-controller
	3. Endpoint-controller
	4. CronJob-controller
	5. Job-controller
	6. PV-Protection-controller
	7. Service-Account-controller
	8. Stateful-set-controller
	9. Replicaset-controller
	10. Node-controller
	11. PV-Binder-controller
	12. Replication-controller

  
## 🔗 Related Topics


## 🛠 Commands / Syntax

```bash

# See available deployments
kubectl get deployments

# Controllers ensures that 5 pods exist
kubectl scale deployment my-app --replicas=5

# Watch controller manage updates
kubectl rollout status deployment my-app

# Check batch jobs managed by Job controller
kubectl get jobs

# Inspect what ReplicaSet controller is maintaining
kubectl describe replicaset my-app-rs

```

  

## List of tasks / Execution

- [] Investigation task. Destroy totally controller-manager and check what's going on
  

🏷️ Tags: #controller #manager #architecture