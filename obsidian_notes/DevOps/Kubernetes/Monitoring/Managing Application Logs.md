## 📌 Description

- Application logs provide insights into the behavior and health of workloads running in the cluster.
- Monitoring them helps detect errors, performance issues, and unexpected behavior.
- Typically implemented with logging agents (e.g., Fluentd, Fluent Bit, or Logstash) that ship logs to centralized storage and monitoring tools (e.g., Elasticsearch, Loki, or Cloud Logging).

## ⚙️ Implementation

1. **Sidecar or DaemonSet log collectors**
    - Deploy a DaemonSet (Fluentd, Fluent Bit) on each node to collect logs from `/var/log/containers`.
    - Alternatively, use a sidecar container per pod to capture and forward logs.
        
2. **Centralized log storage**
    - Send logs to Elasticsearch, Loki, or cloud-native solutions (e.g., GCP Logging, AWS CloudWatch, Azure Monitor).
        
3. **Visualization and alerting**
    - Integrate with Grafana, Kibana, or Lens for log queries and dashboards.

## ✅ Advantages

- Centralized log management makes troubleshooting faster.
- Real-time monitoring and alerting for critical errors.
- Helps correlate application issues with cluster events.
- Improves observability in multi-tenant and large-scale environments.

## 🛠️ Commands

```bash
# View logs of a specific pod
kubectl logs my-pod

# View logs of a specific container inside a pod
kubectl logs my-pod -c my-container

# Stream logs in real time
kubectl logs -f my-pod

# Check logs across multiple pods using a selector
kubectl logs -l app=my-app --all-containers=true

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
      serviceAccountName: fluent-bit
      containers:
      - name: fluent-bit
        image: fluent/fluent-bit:1.9
        resources:
          limits:
            memory: 200Mi
            cpu: 200m
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers

```


### Tags
#logger #pod #logs #monitoring #events