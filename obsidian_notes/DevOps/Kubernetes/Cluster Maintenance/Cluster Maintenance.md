# Cluster Maintenance

## 📌 Description

Cluster maintenance covers the lifecycle operations needed to keep a Kubernetes cluster healthy: **OS patching, Kubernetes version upgrades, and data backup/restore**.

## 🧩 Key Areas

| Topic | What it covers |
|---|---|
| [[OS Upgrade]] | Safely drain and upgrade a node's OS without disrupting workloads |
| [[Cluster Upgrade Process]] | Upgrade Kubernetes version (control plane → worker nodes) |
| [[Backup and Restore]] | Back up etcd and restore cluster state from snapshots |

## 📂 Subtopics

- [[OS Upgrade]]
- [[Cluster Upgrade Process]]
- [[Backup and Restore]]

## 🔗 Useful Links

- [Kubernetes API Overview](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
- [API Conventions](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md)
- [etcd Backup](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/#backing-up-an-etcd-cluster)
- [etcd Recovery](https://github.com/etcd-io/website/blob/main/content/en/docs/v3.5/op-guide/recovery.md)
- [Video: Cluster Upgrade](https://www.youtube.com/watch?v=qRPNuT080Hk)

🏷️ Tags: #maintenance #upgrade #backup #etcd #k8s
