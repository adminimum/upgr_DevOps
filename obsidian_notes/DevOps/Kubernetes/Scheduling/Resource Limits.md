# 🖥️ Resource Limits in Kubernetes

Understanding **resource limits** in Kubernetes is essential for maintaining cluster stability, avoiding resource starvation, and ensuring fair resource distribution across namespaces and pods.

---

## 1️⃣ Key Concepts

| Term | Description |
|------|-------------|
| **LimitRange** | Defines default **requests** and **limits** for pods or containers in a namespace. Helps enforce consistent resource usage. |
| **Requests** | The amount of CPU/memory **guaranteed** for a container. Scheduler uses this value to place pods on nodes. |
| **Limits** | The **maximum** CPU/memory a container can use. If exceeded, container may be throttled or killed. |
| **ResourceQuota** | Sets maximum total resource consumption for a namespace. Prevents any single team or workload from exhausting cluster resources. |

---

## 2️⃣ Requests vs Limits

| Resource | Request | Limit | Effect |
|----------|---------|-------|--------|
| CPU      | Minimum CPU guaranteed | Maximum CPU allowed | If CPU exceeds limit → throttling occurs |
| Memory   | Minimum memory guaranteed | Maximum memory allowed | If memory exceeds limit → container may be OOMKilled |

> 💡 **Tip:** Always set requests and limits for production workloads to avoid node instability.

---

## 3️⃣ LimitRange Example

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: example-limitrange
  namespace: dev
spec:
  limits:
  - type: Container
    default:
      cpu: 500m       # Default max CPU
      memory: 256Mi   # Default max memory
    defaultRequest:
      cpu: 200m       # Default requested CPU
      memory: 128Mi   # Default requested memory
    max:
      cpu: 1
      memory: 512Mi
    min:
      cpu: 100m
      memory: 64Mi
```

## 4️⃣ ResourceQuota Example

```YAML
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: dev
spec:
  hard:
    pods: "10"               # Max number of pods
    requests.cpu: "4"        # Max total CPU requests
    requests.memory: 2Gi     # Max total memory requests
    limits.cpu: "8"          # Max total CPU limits
    limits.memory: 4Gi       # Max total memory limits
```

> ⚠️ **Note:** ResourceQuota ensures that combined resource usage in a namespace does not exceed specified limits.

## 5️⃣ Best Practices

- Always define **requests** and **limits** for containers in production.
- Use **LimitRange** for default values in a namespace.
- Use **ResourceQuota** to prevent a namespace from monopolizing cluster resources.
- Monitor pod usage with `kubectl top pods` and adjust accordingly.
- Start with conservative limits and refine based on metrics.

## 6️⃣ Visual Summary

```CSS
Namespace
│
├─ LimitRange → Default requests/limits for pods
│
├─ ResourceQuota → Maximum total resources allowed
│
└─ Pods
   ├─ Container A → Requests + Limits
   └─ Container B → Requests + Limits
```

> 🎯 **Goal:** Ensure predictable performance, fair resource sharing, and cluster stability.


# Tags

#limits #range #quota #resources #top #cpu #memory