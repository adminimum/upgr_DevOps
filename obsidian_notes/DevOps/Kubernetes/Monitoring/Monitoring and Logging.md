## 📌 Description

- Logging and monitoring are critical for observing cluster health, troubleshooting workloads, and ensuring system reliability.
- Kubernetes does not provide a built-in centralized logging/monitoring solution; you need to integrate external tools.
- Commonly used tools: **Prometheus, Grafana, EFK/ELK stack (Elasticsearch + Fluentd/Fluent Bit + Kibana), Loki, Datadog**.

## ⚙️ Implementation

1. **Logging**
    
    - Deploy a **log collector** (e.g., Fluentd, Fluent Bit) as a DaemonSet to gather logs from all nodes.
    - Forward logs to a backend like **Elasticsearch** or **Loki**.    
    - Visualize logs in **Kibana** or **Grafana**.
        
2. **Monitoring**
    
    - Deploy **Prometheus** (commonly with the Prometheus Operator).    
    - Collect cluster and application metrics via exporters (node_exporter, kube-state-metrics).
    - Visualize and create alerts in **Grafana**.

## ✅ Advantages

- Centralized view of logs and metrics.
- Easier troubleshooting and debugging.
- Enables proactive alerting.
- Long-term storage for audits and compliance.
- Helps with autoscaling decisions based on real metrics.

## 🛠️ Commands

```bash
# Check pod logs directly
kubectl logs <pod-name> -n <namespace>

# Stream logs
kubectl logs -f <pod-name> -n <namespace>

# Get cluster events (basic monitoring)
kubectl get events --sort-by=.metadata.creationTimestamp

# Check metrics server availability
kubectl top nodes
kubectl top pods

```

## 📋 YAML

```YAML
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
  namespace: logging
spec:
  selector:
    matchLabels:
      app: fluent-bit
  template:
    metadata:
      labels:
        app: fluent-bit
    spec:
      containers:
      - name: fluent-bit
        image: fluent/fluent-bit:latest
        resources:
          limits:
            cpu: "100m"
            memory: "200Mi"
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      volumes:
      - name: varlog
        hostPath:
          path: /var/log

```


## 📂 Subtopics
- [[Monitor Cluster Components]]
- [[Managing Application Logs]]
## Tags
#monitoring #logging #troubleshooting #metrics #events