![Kubelet](kubelet.png)
## 📌 Definition

- What it is:
  An agent that runs on every node in a Kubernetes cluster. It makes sure containers described in Pod manifests are running as they should.

- How useful it is:
  Without kubelet, nodes wouldn’t know what to run. It’s the direct bridge between Kubernetes (control plane) and the actual machine (worker node).

- How to implement:
  It is installed as a system service (e.g., `systemctl start kubelet`). On joining a node to the cluster, kubeadm automatically sets it up.

- Simple analogy:
  Think of kubelet as a **factory floor manager**: the head office (API server) sends orders, and the manager makes sure machines (containers) are running properly on the floor (node).

- Problem it solves:
  Ensures your workloads (Pods/containers) are actually running on the nodes, restarts them if they fail, and reports back to the API server.


## 🔗 Related Topics


## 🛠 Commands / Syntax

```bash
# Check kubelet status
systemctl status kubelet

# Start kubelet
systemctl start kubelet

# Check kubelet logs
journalctl -u kubelet -f

# Check config of the kubelet on the node
cat /var/lib/kubelet/config.yaml

```

  

## List of tasks / Execution

- [] Check logs of Kubelet on the node. Stop it and try to put the Pod on this node. What will happen. 


  

🏷️ Tags: #Kubelet #architecture #Structure 