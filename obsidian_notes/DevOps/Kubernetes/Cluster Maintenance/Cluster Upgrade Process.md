![ClusterUpgrade](clusupgr.jpg)
## 📌 Definition

- What it is:
  The controlled process of upgrading a Kubernetes control plane (master components) and worker nodes to a newer version.

- How useful it is:
  Ensures security patches, compatibility, and access to new Kubernetes features.

- How to implement:
  Typically performed using `kubeadm` for on-prem clusters, or through managed services upgrade tools in cloud environments.

- Simple analogy:
  Like renovating a building floor by floor—first upgrading the control systems (elevator, electricity) before upgrading each room.

- Problem it solves:
  Keeps the cluster secure, avoids deprecated API breakage, and maintains long-term support.
  
- **Order of actions:**
	1. Back up cluster state (etcd + manifests).
	2. Upgrade `kubeadm` on the control plane node(s).  
	3. Apply control plane upgrade (`kubeadm upgrade apply`).
	4. Upgrade `kubelet` and `kubectl` on control plane nodes.
	5. Repeat process for worker nodes (drain, upgrade, uncordon).
	6. Validate workloads and cluster health.

- My thoughts:
  This is approach for upgrading the whole cluster with minimum outage and break downs of  applications. Step by step method. 

## 🔗 Related Topics

- [[OS Upgrade]]

## 🛠 Commands for updating Master / Syntax

```bash
# Check repo of current kubeadm
cat /etc/apt/sources.list

# Create correct repo for updating kubeadm

# Upgrade kubeadm on master
apt-cache madison kubeadm
apt-get update && apt-get install -y kubeadm=1.28.0-00

# Plan the upgrade (shows what will be upgraded)
kubeadm upgrade plan

# Apply upgrade for control plane
sudo kubeadm upgrade apply v1.28.0

# Upgrade kubelet and kubectl
apt-get install -y kubelet=1.28.0-00 kubectl=1.28.0-00

# Restart kubelet
sudo systemctl daemon-reload
sudo systemctl restart kubelet


```

##  🛠 Commands for updating Nodes / Syntax

```bash

# On each worker node:

# Upgrade kubeadm
apt-get update && apt-get install -y kubeadm=1.28.0-00

# Drain node before upgrade
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data

# Upgrade node
sudo kubeadm upgrade node

# Upgrade kubelet and kubectl
apt-get install -y kubelet=1.28.0-00 kubectl=1.28.0-00

# Restart kubelet
sudo systemctl daemon-reload
sudo systemctl restart kubelet

# Uncordon node
kubectl uncordon <node-name>

```

## List of tasks / Execution
-  Back up etcd and cluster configuration.
-  Upgrade `kubeadm` on control plane nodes.
-  Run `kubeadm upgrade plan` and `kubeadm upgrade apply`.
-  Upgrade `kubelet` + `kubectl` on masters.
-  Drain each worker node and repeat the upgrade steps.
-  Validate workloads after each node is uncordoned.
-  Verify cluster health (`kubectl get nodes`, `kubectl get pods -A`

  

🏷️ Tags: #patching #upgradecluster #cluster #version #upgrade #nodes #controle-plane