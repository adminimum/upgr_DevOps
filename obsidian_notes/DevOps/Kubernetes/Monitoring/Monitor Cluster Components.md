## 📌 Description

- Monitoring cluster components means tracking the health and performance of core Kubernetes components like the **API server, etcd, scheduler, controller-manager, kubelet, and kube-proxy**.
- Ensures that the control plane and worker nodes are functioning correctly, which is critical for cluster stability.

## ⚙️ Implementation

- Use **metrics-server** for resource usage metrics.
- Deploy **Prometheus** + **Grafana** stack to scrape metrics and visualize them.
- Enable **kube-state-metrics** to monitor the state of Kubernetes objects.
- Configure alerts with **Alertmanager** (e.g., API server down, etcd unhealthy, kubelet not responding).

## ✅ Advantages

- Detect failures in critical components before they impact workloads.
- Provide visibility into cluster resource consumption.
- Enable proactive scaling and capacity planning.
- Improve reliability with automated alerting and dashboards.

## 🛠️ Commands

```bash
# Deploy metrics-server (lightweight monitoring)
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Check API server health
kubectl get --raw='/readyz?verbose'

# Check component statuses
kubectl get componentstatuses   # deprecated in v1.24+, use /healthz endpoints instead

# Example: check kube-scheduler
kubectl get --raw='/healthz?verbose' | grep scheduler

```

## 📋 YAML

```YAML
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: kube-apiserver-monitor
  namespace: monitoring
spec:
  selector:
    matchLabels:
      component: apiserver
  namespaceSelector:
    matchNames:
      - default
  endpoints:
    - port: https
      scheme: https
      tlsConfig:
        insecureSkipVerify: true
      interval: 30s

```

### Tags
#monitoring #cluster #metric-server #metrics #logs 