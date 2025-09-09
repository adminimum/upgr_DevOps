  

## 📌 Definition

- What it is:
  A Kubernetes feature (stable in v1.27+) that allows you to adjust a Pod’s **CPU and memory requests/limits** without deleting and recreating the Pod.

- How useful it is:
  Lets you dynamically adapt running Pods to workload changes, avoiding downtime and preserving ephemeral state

- How to implement:
  Enabled by default in newer versions. You edit the Pod (or its controller like Deployment) with new resource values, and the kubelet applies changes **in-place** where possible.

- Simple analogy:
  Like **resizing a container ship while it’s at sea**, instead of recalling it back to port to build a new one.

- Problem it solves:
  Previously, resizing required Pod deletion → downtime, loss of local state, or restart delays

- My thoughts:
  This is Kuberenetes's ability to scale resources of the pod without restarting it. Can come in handy.


## 🛠 Commands / Syntax

```bash
# Edit resource requests/limits of a running Pod
kubectl edit pod mypod

# Patch resource requests/limits (example: increase memory)
kubectl patch pod mypod -p '{"spec":{"containers":[{"name":"myapp","resources":{"requests":{"memory":"1Gi"},"limits":{"memory":"2Gi"}}}]}}'

# Check updated resources
kubectl describe pod mypod | grep -A5 "Containers"

```

  

## 🗒️ YAML format example with explaining

```YAML

  apiVersion: v1
kind: Pod
metadata:
  name: resize-demo
spec:
  containers:
  - name: myapp
    image: nginx
    resources:
      requests:
        cpu: "200m"
        memory: "256Mi"
      limits:
        cpu: "500m"
        memory: "512Mi"


```

  

## List of tasks / Execution
-  Deploy a test Pod with CPU/memory limits.
-  Resize memory request/limit while it’s running.
-  Observe metrics with `kubectl top pod`.
-  Test resizing both upward and downward.
-  Compare behavior with VPA.
  

🏷️ Tags:
#inplace #inplaceresize #resize #scaling #vertical