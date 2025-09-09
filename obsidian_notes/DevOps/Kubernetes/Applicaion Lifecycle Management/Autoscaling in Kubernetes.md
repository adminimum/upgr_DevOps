![Autoscaling](autoscaling.gif)
  

## 📌 Definition

- What it is:
  A Kubernetes feature that automatically adjusts resources (Pods, nodes) based on load or usage metrics.

- How useful it is:
  Ensures applications scale up when demand increases and scale down when idle, optimizing cost and performance.

- How to implement:
	 Use Kubernetes objects like:
	- **Horizontal Pod Autoscaler (HPA)** → scales Pods based on CPU/memory/custom metrics.
	- **Vertical Pod Autoscaler (VPA)** → adjusts container resource requests/limits
	- **Cluster Autoscaler (CA)** → adds/removes worker nodes in the cluster.

- Simple analogy:
  Like a **restaurant adding more tables and waiters during peak hours** and removing them when business slows down.

- Problem it solves:
  Prevents over-provisioning (wasting resources) and under-provisioning (slow apps).

- My thoughts:
  This is Kubernetes's ability to increase and decrease count of the apps  or amount of resources they use.


## 🛠 Commands / Syntax

```bash
# Enable metrics server (required for HPA)
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Create HPA from CLI
kubectl autoscale deployment myapp --cpu-percent=50 --min=2 --max=10

# View HPA status
kubectl get hpa

# Scale down/up manually (for testing)
kubectl scale deployment myapp --replicas=5

```

  

## 🗒️ YAML format example with explaining

```YAML

  apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:          # Target resource to scale
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2           # Lower limit for Pods
  maxReplicas: 10          # Upper limit for Pods
  metrics:                 # Metric to watch
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
---
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: myapp-vpa
  namespace: default
spec:
  targetRef:                      # Target workload
    apiVersion: "apps/v1"
    kind:       Deployment
    name:       myapp
  updatePolicy:                   # How VPA applies recommendations
    updateMode: "Auto"            # Options: Off, Initial, Auto
  resourcePolicy:                 # (Optional) fine-grained resource limits
    containerPolicies:
    - containerName: '*'
      minAllowed:
        cpu: "200m"
        memory: "256Mi"
      maxAllowed:
        cpu: "2"
        memory: "2Gi"


```

  
## Vertical Pod Autoscaling Enabling feature

### 1. 📥 Download the VPA release

The VPA project is maintained under Kubernetes Autoscaler.

`git clone https://github.com/kubernetes/autoscaler.git 
`cd autoscaler/vertical-pod-autoscaler/`

---

### 2. 🚀 Apply VPA components

Install the CustomResourceDefinitions (CRDs) and controllers:

`kubectl apply -f deploy/vpa-v1-crd.yaml 
`kubectl apply -f deploy/vpa-rbac.yaml
`kubectl apply -f deploy/vpa-deployment.yaml`

These install:

- **CRDs** → `VerticalPodAutoscaler` resource
- **Admission Controller** → mutates pod specs with recommendations
- **Updater** → evicts pods if needed for new resources
- **Recommender** → calculates CPU/memory recommendations
    

---

### 3. ✅ Verify CRD

Check if VPA CRDs are installed:
`kubectl get crd | grep verticalpodautoscalers`
You should see:
`verticalpodautoscalers.autoscaling.k8s.io`

---

### 4. 🔗 Enable MutatingAdmissionWebhook (if not already)

VPA relies on the admission controller to inject new requests.  
Make sure your API server has this admission plugin enabled (usually default in managed clusters like GKE, EKS, AKS).  
Check with:
`kubectl api-versions | grep admissionregistration`
If `mutatingwebhookconfigurations` exists, you’re good.

---
### 5. 📊 Deploy a VPA object
 Now you can create your first VPA
---

## List of tasks / Execution
-  Deploy and configure **metrics-server**.
-  Create an **HPA** for a test Deployment.
-  Generate load (e.g., `kubectl run -it load --image=busybox sh`).
-  Observe Pods scale up and back down.
-  Explore **VPA** and **Cluster Autoscaler** in cloud environments.

  

🏷️ Tags:
#hpa #vpa #autoscaling #scalers #pods