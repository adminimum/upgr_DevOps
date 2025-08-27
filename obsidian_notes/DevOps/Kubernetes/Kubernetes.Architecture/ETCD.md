![ETCD](etcd.png)
## 📌 Definition

- What it is: **etcd** is a **distributed key-value store** that Kubernetes uses to keep all the cluster’s state and configuration data.

- How useful it is: it’s not just “one of the components,” it’s the **core brain of Kubernetes**. 
1. Stores the cluster state, 
2. Provides consistency, 
3. Fault tolerance, 
4. Security and configuration, 
5. Backup & restore = cluster recovery

- How to implement: It's already implemented inside Kubernetes by default. But you can download it as binary and use it as a key-value storage. 

- Simple analogy: Apache ZooKeeper, HashiCorp’s Consul, any other KV databases. 

- Problem it solves: It solves problems of maintaining correct version of the apps. Configuration for the whole Kubernetes cluster. It might keep secrets and certificates. So the main idea of this asset is to store main and vital information in the safe and comfort place. 

## 🎬 Contains Info about
 - Nodes
 - PODs
 - Configs
 - Secrets
 - Accounts
 - Roles
 - Bindings
 - Others

## 🛠 Commands / Syntax

```bash

# Tool

etcdctl --version

kubectl exec etcd-master -n kube-sysetem etcdctl get / --prefix -keys-only
```

### ❗️Commands depend on version of API in ***etcdctl***
```bash

etcdctl snapshot save
etcdctl endpoint health
etcdctl get
etcdctl put

```

### If needed specify version etcdctl API and certificates before working with db
```bash
kubectl exec etcd-master -n kube-system -- sh -c "ETCDCTL_API=3 etcdctl get / --prefix --keys-only --limit=10 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key"
```
## List of tasks / Execution

- [] Try to find some parameters of the kubernetes cluster directly from etcd

🏷️ Tags: #ETCD #Structure #Controle-plane