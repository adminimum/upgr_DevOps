![Troubleshooting](troubleshooting.png)

## 📌 Description

Kubernetes troubleshooting means **systematically diagnosing why workloads, nodes, or networking are not behaving as expected**. Most issues fall into: Pod lifecycle problems, resource constraints, network failures, or control plane issues.

## 🧩 Common Problem Areas

| Area | Typical Symptoms |
|---|---|
| Pod not starting | `Pending`, `CrashLoopBackOff`, `ImagePullBackOff`, `OOMKilled` |
| Service not reachable | Traffic doesn't reach pods, DNS fails |
| Node issues | `NotReady`, resource pressure, disk/memory eviction |
| Control plane | API server unreachable, etcd issues, scheduler not assigning pods |
| Persistent storage | PVC stuck in `Pending`, volume not mounting |

## 🛠 Debugging Workflow

```
1. kubectl get pods / nodes — get high-level state
2. kubectl describe pod <name> — read Events section
3. kubectl logs <pod> [--previous] — check container output
4. kubectl exec -it <pod> -- sh — inspect inside the container
5. kubectl get events --sort-by=.metadata.creationTimestamp
```

## 🛠 Commands / Syntax

```bash
# Pod status overview
kubectl get pods -A -o wide

# Detailed pod info + events
kubectl describe pod <pod-name> -n <namespace>

# Current logs
kubectl logs <pod-name> -n <namespace>

# Logs from previous crash
kubectl logs <pod-name> --previous

# Exec into a running container
kubectl exec -it <pod-name> -- /bin/sh

# Check resource usage
kubectl top pods -n <namespace>
kubectl top nodes

# Check events (sorted)
kubectl get events -n <namespace> --sort-by=.metadata.creationTimestamp

# Describe a node
kubectl describe node <node-name>

# Check service endpoints (are pods registered?)
kubectl get endpoints <service-name>

# DNS test from inside a pod
kubectl exec -it <pod> -- nslookup kubernetes.default

# Port-forward for direct testing
kubectl port-forward pod/<pod-name> 8080:80
```

## 🔍 Pod Status Cheatsheet

| Status | Meaning | Common Fix |
|---|---|---|
| `Pending` | No node assigned | Resource shortage, taints, affinity |
| `ImagePullBackOff` | Can't pull image | Wrong image name, missing pull secret |
| `CrashLoopBackOff` | Container keeps crashing | Check logs, fix app error or config |
| `OOMKilled` | Out of memory | Increase memory limit |
| `Evicted` | Node ran out of resources | Scale node, clean up resources |
| `Terminating` | Stuck on deletion | Finalizer issue — patch to remove finalizer |

## 🔗 Documentation

- [Kubernetes Debugging Docs](https://kubernetes.io/docs/tasks/debug/)
- [Application Introspection](https://kubernetes.io/docs/tasks/debug/debug-application/)

🏷️ Tags: #troubleshooting #debug #crashloopbackoff #pending #logs #kubectl #k8s
