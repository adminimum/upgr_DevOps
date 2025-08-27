![ReplicaSet](replicaset.webp)

```
❗️Note that:

ReplicaSet != ReplicaController

ReplicaController doesn't need field "selector"
```
## 📌 Definition

- What it is:
  A **ReplicaSet** is a Kubernetes object that ensures a specified number of identical **Pods** are always running. If a Pod crashes, it will create a new one.

- How useful it is:
	- Maintains **high availability** by keeping the desired number of replicas.
	- Provides **scalability** by easily increasing/decreasing replicas.    
	- Used as a foundation for **Deployments**.

- How to implement:
  You create a **ReplicaSet** YAML file with a `spec.replicas` field and a **Pod template** under `spec.template`. Then apply it with:
  ```Bash
	  kubectl apply -f replicaset.yaml
    ```

- Simple analogy:
  Think of it like a **classroom teacher**: if 3 students leave, the teacher makes sure new students come in so that the class always has 30 students

- Problem it solves:
	- Keeps applications always running at the desired scale.
	- Prevents downtime from Pod crashes.
	- Allows scaling workloads efficiently.

- My thoughts:
  This unit lets Kubernetes to start and maintain a number of pods as a one kit of the same Pods for stability working app if one of them are dropped.

## 🔗 Related Topics

- [[]]


## 🛠 Commands / Syntax

```bash
# Get all ReplicaSets in current namespace
kubectl get rs

# Describe a ReplicaSet in detail
kubectl describe rs <replicaset-name>

# Create a ReplicaSet from YAML
kubectl apply -f replicaset.yaml

# Delete a ReplicaSet
kubectl delete rs <replicaset-name>

# Scale ReplicaSet to a specific number of replicas
kubectl scale rs <replicaset-name> --replicas=5

# View Pods controlled by a ReplicaSet
kubectl get pods --selector=app=<label-value>

# Update ReplicaSet (e.g., change image)
kubectl set image rs/<replicaset-name> <container-name>=nginx:1.25

```

  

## 🗒️ YAML format example with explaining

```YAML
apiVersion: apps/v1   # API group and version for ReplicaSet
kind: ReplicaSet      # Resource type
metadata:
  name: my-replicaset # Name of the ReplicaSet
  namespace: default  # Namespace (default if not set)
  labels:             # Labels for identifying the ReplicaSet
    app: myapp
  annotations:        # Optional metadata annotations
    description: "ReplicaSet to run multiple Pods of myapp"

spec:
  replicas: 3         # Desired number of Pods (scalable)
  selector:           # Defines how ReplicaSet finds Pods to manage
    matchLabels:      # Pods must have these labels
      app: myapp
    matchExpressions: # More advanced selection rules
      - key: tier
        operator: In
        values:
          - frontend
          - backend

  template:           # Pod template: defines how Pods should look
    metadata:
      labels:         # Labels applied to Pods created by ReplicaSet
        app: myapp
        tier: frontend
      annotations:    # Extra info for Pods
        sidecar.istio.io/inject: "false"
    spec:             # Pod spec (this part is powerful & detailed)
      restartPolicy: Always         # Pod restart behavior
      terminationGracePeriodSeconds: 30  # Time to gracefully shut down
      dnsPolicy: ClusterFirst       # DNS resolution setting
      serviceAccountName: default   # Service account for Pod
      nodeSelector:                 # Scheduling constraint: only on specific nodes
        disktype: ssd
      tolerations:                  # Tolerate node taints
        - key: "key1"
          operator: "Equal"
          value: "value1"
          effect: "NoSchedule"
      affinity:                     # Advanced scheduling rules
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: kubernetes.io/e2e-az-name
                    operator: In
                    values:
                      - e2e-az1
                      - e2e-az2
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values:
                      - myapp
              topologyKey: "kubernetes.io/hostname"
      containers:                   # Main application containers
        - name: myapp-container
          image: nginx:1.25         # Container image
		  ...

```

  

## List of tasks / Execution

-

-

  

🏷️ Tags: