![kube-proxy](kube-proxy.svg)
## 📌 Definition

- What it is:
  A network component in Kubernetes that runs on each node. It maintains network rules and makes sure Pods can talk to each other and to Services. By iptables

- How useful it is:
  It enables stable communication inside the cluster and between services, even if Pods are constantly changing or moving between nodes.

- How to implement:
  Normally, kube-proxy is installed automatically by `kubeadm` or your Kubernetes distribution. You can check it as a DaemonSet:
  ```kubectl get daemonset kube-proxy -n kube-system```

- Simple analogy:
  Think of kube-proxy like a **traffic cop at an intersection** — directing cars (requests) so they reach the right building (Pod), even if the building address changes.

- Problem it solves:
  Without kube-proxy, Pods wouldn’t know how to consistently reach Services, because Pod IPs are temporary. kube-proxy creates **stable routes** for communication.

-  My thoughts: It's connection between pods by services. All pods have different IPs when they starting or destroying. But kube-proxy provides that some type of pods will have something common and this is service ip. Then each server will have note that match ip of the pods with IP of the service

  

## 🔗 Related Topics

  

## 🛠 Commands / Syntax

```bash

# Check kube-proxy state
kubectl get daemonset kube-proxy -n kube-system

# Describe kube-proxy to see details
kubectl describe daemonset kube-proxy -n kube-system

# Check kube-proxy prods
kubectl get pods -n kube-system -l k8s-app=kube-proxy -o wide

# Check logs of the kube-proxy
kubectl logs -n kube-system -l k8s-app=kube-proxy

# Change kube-proxy config (like switching ot IPVS mode)
kubectl edit configmap kube-proxy -n kube-system



```

  

## List of tasks / Execution

- [] Check all parameters in describe mode. Then try to rich service inside some pod. Then destroy kube-proxe. Try to rich again and check logs.

  

🏷️ Tags: #kube-proxy #architecture #Structure #network