![StaticPod](staticpod.png)
## 📌 Definition

- What it is:
  A **Static Pod** is a pod managed **directly by the kubelet** on a node, without the use of the Kubernetes API server.  

- How useful it is:
  Useful for running **critical system-level pods** like `kube-apiserver`, `kube-controller-manager`, or `kube-proxy` on a specific node.  

- How to implement:
  Place a pod manifest YAML file in the **kubelet's static pod directory** (usually `/etc/kubernetes/manifests`). The kubelet automatically creates and monitors the pod.  
  Path to manifests is stored inside kubelet configuration. There two places where it stored.

- Simple analogy:
  Think of it as a **personal assistant hired directly by the boss**, bypassing middle management—the pod runs because the kubelet tells it to, not because of the API server.  

- Problem it solves:
  Ensures that **critical pods run on specific nodes**, even if the Kubernetes control plane is not fully operational.  

- My thoughts:
  Static pods provide ability to run independent pods inside nodes without managing them through API server. It works by itself. The only need is to place manifest in the predesignated path inside kubelet configuration and it will be running and monitoring by kubelet itself.


## 🔗 Related Topics

  

## 🛠 Commands / Syntax

```bash

# Delete or move a static pod YAML (kubelet will recreate it automatically)
rm /etc/kubernetes/manifests/<pod>.yaml

```

  

## List of tasks / Execution

- [] Run a specific pod inside node, check the path where it should be placed then try to work with it through API
  

🏷️ Tags: 
#static #pod #node #controle #selfmanaged #kubelet #path