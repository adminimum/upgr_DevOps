![DaemonSet](daemonset.png)

## 📌 Definition

- What it is:
  A **DaemonSet** ensures that a copy of a pod runs on **all (or selected) nodes** in a Kubernetes cluster.  

- How useful it is:
  Useful for running **cluster-wide services** like monitoring agents, log collectors, or networking daemons.  

- How to implement:
  Create a DaemonSet YAML manifest specifying the pod template. Kubernetes automatically schedules one pod per matching node.  As ReplicaSet template

- Simple analogy:
  Think of it like a **janitor assigned to every building in a city**—every building gets exactly one janitor, no more, no less.  

- Problem it solves:|
  Ensures that essential services are running **uniformly across all nodes**, without manual pod scheduling.  

- My thoughts:
  Daemon Set is an object of Kubernetes, which is kindly useful for system services which provides you special type of services where you need to run something essential on each node for performing some necessary actions.

  
## 🔹 YAML Example: Simple DaemonSet

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-monitor
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: node-monitor
  template:
    metadata:
      labels:
        app: node-monitor
    spec:
      containers:
      - name: node-monitor
        image: busybox
        command: ["sh", "-c", "while true; do echo monitoring node; sleep 30; done"]
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 100m
            memory: 128Mi

```

## 🔗 Related Topics
  

## 🛠 Commands / Syntax

```bash


# Check the rollout status of a DaemonSet update

kubectl rollout status daemonset <name>

```

  

## List of tasks / Execution

 - [] Run a daemon set which getting logs from the all resources of kubernetes on the node

🏷️ Tags:
#daemonset #node #pod #monitoring #logs #network