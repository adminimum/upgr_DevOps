# 🗓️ Scheduling Type: Pod Scheduling / Custom Scheduling Policies

## 📌 Description

- **What it is:**  
Scheduler profiles allow the **default kube-scheduler** to run with **multiple scheduling behaviors** at the same time.  
- **Purpose:**  
Each profile defines a set of **plugins, scoring rules, and filters**. Pods select a profile using the `spec.schedulerName` field.  

## ⚙️ Implementation

- Define profiles inside a **KubeSchedulerConfiguration** object.  
- Each profile must include a unique `schedulerName`.  
- Start kube-scheduler with `--config` pointing to the config file.  
- Pods use `spec.schedulerName` to select the correct profile. 

## ✅ Advantages

- Multiple scheduling strategies in a **single scheduler instance**.  
- Allows **fine-grained control** for different workloads (e.g., critical apps, batch jobs).  
- Avoids running **multiple scheduler binaries** while still supporting customization.  

## 📋 YAML

```YAML
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: default-scheduler
    plugins:
      score:
        enabled:
          - name: NodeResourcesFit
  - schedulerName: batch-scheduler
    plugins:
      score:
        enabled:
          - name: PodTopologySpread
---
apiVersion: v1
kind: Pod
metadata:
  name: batch-job
spec:
  schedulerName: batch-scheduler   # Uses second profile
  containers:
  - name: worker
    image: busybox
    command: ["sh", "-c", "echo running batch job; sleep 3600"]
```

## Steps of schedulint

```CSS
[Scheduling Queue]
  └─ QueueSort, (optional) PreEnqueue
           ↓
[Filtering]
  └─ PreFilter → Filter → PostFilter
           ↓
[Scoring]
  └─ PreScore → Score → NormalizeScore → PostScore
           ↓
[Reserve / Permit] (optional)
  └─ Reserve → Permit (wait/deny/approve)
           ↓
[Binding]
  └─ PreBind → Bind → PostBind

Pod selects profile via: Pod.spec.schedulerName
Profile defined in: KubeSchedulerConfiguration.profiles[].schedulerName
Plugins are attached per hook (PreFilter/Filter/…/Bind).

```

### 🔖 Tags
#custom #policies #scheduling #configuration #score #filtering #bind #calculation