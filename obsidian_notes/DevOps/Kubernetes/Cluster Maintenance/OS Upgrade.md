## 📌 Definition

- What it is:
  The process of upgrading the underlying **host operating system** (nodes) in a Kubernetes cluster without disrupting workloads.

- How useful it is:
  Ensures nodes are patched, secure, and compatible with the Kubernetes version.

- How to implement:
  Typically involves cordoning, draining, upgrading, and rejoining nodes to the cluster.

- Simple analogy:
  Think of it like renovating one room at a time in a house while the rest of the house remains livable.

- Problem it solves:
  Prevents security vulnerabilities, maintains compatibility with Kubernetes features, and ensures long-term cluster stability.

- My thoughts:
  This is possibility in the Kubernetes to update and patch nodes without outage of the apps running inside cluster. Just simple way to turn off node of scheduling and then update it. 
  

## 🛠 Commands / Syntax

```bash
# Mark node as unschedulable
kubectl cordon <node-name>

# Drain workloads from node
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data

# Upgrade OS (done via package manager or image replacement depending on distro)
# Example for Ubuntu:
sudo apt update && sudo apt upgrade -y

# Reboot node after upgrade
sudo reboot

# Mark node schedulable again
kubectl uncordon <node-name>

```


## List of tasks / Execution
-  Identify which nodes need upgrade (security patches or OS version).
-  Cordon and drain node to protect workloads.
-  Apply OS upgrade (manual or automated via tooling).
-  Reboot node and verify kubelet re-registers.
-  Uncordon node.
-  Repeat for all nodes in rolling fashion.
-  Validate workloads are healthy post-upgrade.
  

🏷️ Tags: #cordon #drain #node #os #patching #security