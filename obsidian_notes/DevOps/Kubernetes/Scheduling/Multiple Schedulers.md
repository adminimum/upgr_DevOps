# 🗓️ Scheduling Type: Pod Scheduling / Custom Scheduling

## 📌 Description

- **What it is:**  
Kubernetes allows **running multiple schedulers** in parallel, each responsible for scheduling specific pods based on different criteria.  
- **Purpose:**  
Enables **custom scheduling logic** beyond the default Kubernetes scheduler (`kube-scheduler`), such as prioritizing certain workloads, nodes, or resources.

## ⚙️ Implementation

- Deploy a **custom scheduler** as a separate deployment or static pod.  
- Specify the scheduler in pod manifests using `schedulerName`.  
- The custom scheduler watches **unscheduled pods** and binds them to nodes based on its logic.  
- Default scheduler still runs for pods without a custom `schedulerName`.  

## ✅ Advantages

- Enables **specialized scheduling policies** for certain workloads.  
- Supports **workload isolation**, ensuring critical pods are scheduled on dedicated nodes.  
- Allows **experimentation** with scheduling strategies without affecting the default scheduler.  

## 📋 YAML

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: custom-scheduled-pod
spec:
  schedulerName: my-custom-scheduler  # Use custom scheduler
  containers:
  - name: app
    image: nginx
---
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: my-scheduler
  name: my-scheduler
  namespace: kube-system
spec:
  serviceAccountName: my-scheduler
  containers:
  - command:
    - /usr/local/bin/kube-scheduler
    - --config=/etc/kubernetes/my-scheduler/my-scheduler-config.yaml
    image: <use-correct-image>
    livenessProbe:
      httpGet:
        path: /healthz
        port: 10259
        scheme: HTTPS
      initialDelaySeconds: 15
    name: kube-second-scheduler
    readinessProbe:
      httpGet:
        path: /healthz
        port: 10259
        scheme: HTTPS
    resources:
      requests:
        cpu: '0.1'
    securityContext:
      privileged: false
    volumeMounts:
      - name: config-volume
        mountPath: /etc/kubernetes/my-scheduler
  hostNetwork: false
  hostPID: false
  volumes:
    - name: config-volume
      configMap:
        name: my-scheduler-config

```

  

### 🔖 Tags
#scheduler #custom #scheduling #service #difficult