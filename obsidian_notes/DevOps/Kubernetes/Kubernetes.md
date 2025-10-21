
  
![Kubernetes Logo](images/kuber-logo.png)

## 📌 Description

- **Kubernetes** is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.
- **What it does:** Manages containers (like Docker) across multiple hosts, ensuring applications run reliably and scale automatically.
- **Key components:** Pods, Nodes, Deployments, Services, Ingress, ConfigMaps, Secrets, and Controllers.
  

## 🛠 Usage / Where

- **Cloud-native applications** – running microservices at scale.
- **CI/CD pipelines** – automate deployment and testing of apps.
- **Web services & APIs** – ensure high availability and load balancing.
- **Big data / ML workloads** – manage distributed processing jobs.
- **Hybrid or multi-cloud environments** – unify workloads across clouds and on-premises.
- **Self-healing systems** – automatically restart failed containers and reschedule pods.

  

## ⚡ Advantages

- High availability, automatic scaling, self-healing (restarts failed containers), declarative configuration.

  

## ⚠️ Limitations / Where it is ineffective

- Learning curve is steep; overkill for very small/simple projects.

  

## 📝 Requirements

- Container runtime (Docker, containerd), Linux hosts, network connectivity between nodes.

  

## 🧰 Instruments / Tools

- **kubectl** – CLI to interact with clusters.
- **kubeadm** – bootstrap Kubernetes clusters.
- **Helm** – package manager for applications (charts).
- **Minikube / Kind** – local development clusters.
- **Kustomize** – configuration templating.
- **Calico / Flannel / Cilium** – pod networking plugins.
- **ArgoCD / Flux** – GitOps automated deployments.
- **Etcd** – cluster state key-value store.
- **Lens** – GUI for cluster management.
- **Rancher** – full-featured multi-cluster management platform with UI.
- **Velero** – backup and restore for clusters.
- **K9s** – terminal UI for navigating and managing clusters.
  

## 🔗 Documentation / Cheatsheet

- Official documentation: [Link](https://kubernetes.io/docs/home/)

- Online cheatsheet: [Link](https://spacelift.io/blog/kubernetes-cheat-sheet)

  

## 📂 Subtopics

- [[Cluster Architecture]]
- [[Kubernetes Objects]]
- [[Imperative and declarative]]
- [[Scheduling]]
- [[Monitoring and Logging]]
- [[Application LifeCycle Management]]
- [[Cluster Maintenance]]
- [[Security Main Page]]
- [[Storage Main Page]]
  

## 🔗 Related Topics

- [[]]

  

## 🌐 Resources

- Book: **Kubernetes: Up and Running**

  

## ✅ Examples of Usefulness

- **Microservices deployment** – easily deploy and scale multiple microservices across nodes.
- **High availability web applications** – automatic pod rescheduling and self-healing ensures uptime.
- **CI/CD pipelines** – deploy and test applications automatically across multiple environments.
- **Rolling updates / zero-downtime deployments** – update applications without stopping services.
- **Resource optimization** – automatically balance workloads across cluster nodes.

  

## ❌ Examples of Ineffectiveness

- **Very small/simple applications** – overkill for a single-container app or one-node project.
- **Low-resource environments** – Kubernetes requires memory, CPU, and stable networking; tiny servers may struggle.
- **Legacy monolithic applications** – difficult or inefficient to containerize fully.
- **High operational complexity** – managing networking, storage, security, and scaling can be cumbersome for small teams.

  

---

📅 Created: {{ 21.08.2025 }}

🏷️ Tags: #index #kubectl #linux #cloud #k8s #cka #containers #DevOps #main