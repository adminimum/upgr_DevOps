![Deployments](deploy.avif)
## 📌 Definition

- What it is:
  A higher-level Kubernetes object that manages **ReplicaSets** and ensures Pods are running in a desired state.

- How useful it is:
	-  Provides **declarative updates** (rollouts, rollbacks).
	- Manages scaling up/down automatically.
	- Ensures self-healing (recreates failed Pods).
	- Simplifies managing multiple versions of applications.

- How to implement:
  You create a **Deployment YAML manifest**, apply it with `kubectl apply -f`, and Kubernetes ensures Pods are created, updated, and maintained.

- Simple analogy:
  A Deployment is like a **project manager**: you tell it _“I want 3 workers (Pods), running this app version”_. The manager makes sure there are always exactly 3 workers, replaces lazy ones, and smoothly swaps them when a new version arrives.

- Problem it solves:
	- Automates scaling, rollout, and rollback of apps.
	- Handles failures gracefully.
	- Provides a consistent way to manage stateless apps without manual intervention.

- My thoughts:
  Deployment is that type of elements in kubernetes that extend abilities of the ReplicaSet objects. And add these functionalities as Autoscaling, rollouts and updates.

  

## 🔗 Related Topics

- [[]]

## 🛠 Commands / Syntax

```bash

# Create a deployment
kubectl create deployment my-deployment --image=nginx

# Get all deployments in the cluster
kubectl get deployments

# Describe detailed info about a deployment
kubectl describe deployment my-deployment

# Scale deployment to 5 replicas
kubectl scale deployment my-deployment --replicas=5

# Update the image of a deployment
kubectl set image deployment/my-deployment nginx=nginx:1.21

# Check the rollout status of a deployment
kubectl rollout status deployment/my-deployment

# Undo last rollout (rollback)
kubectl rollout undo deployment/my-deployment

# View rollout history
kubectl rollout history deployment/my-deployment

# Delete a deployment
kubectl delete deployment my-deployment

# Apply deployment config from a YAML file
kubectl apply -f deployment.yaml

```

  

## 🗒️ YAML format example with explaining

```YAML

apiVersion: apps/v1  # API group and version for Deployment
kind: Deployment     # Type of Kubernetes object
metadata:
  name: my-deployment           # Name of the deployment
  namespace: default            # Namespace where this will be created
  labels:                       # Optional: key-value pairs for grouping/selection
    app: my-app
  annotations:                  # Optional: non-identifying metadata
    description: "Example Deployment manifest with all fields"

spec:
  replicas: 3                   # Number of desired Pod replicas
  selector:                     # Required: defines how to find Pods managed by this Deployment
    matchLabels:                # Pods must have these labels to be selected
      app: my-app
    # matchExpressions:         # Optional: more complex selection logic
    #   - key: tier
    #     operator: In
    #     values:
    #       - frontend
  strategy:                     # Optional: Deployment strategy
    type: RollingUpdate         # Default is RollingUpdate
    rollingUpdate:              # Only used if type is RollingUpdate
      maxSurge: 1               # Max number of extra Pods allowed during update
      maxUnavailable: 1         # Max number of unavailable Pods during update

  minReadySeconds: 5            # Minimum time a Pod should be ready before considered available
  revisionHistoryLimit: 10      # Number of old ReplicaSets to keep
  progressDeadlineSeconds: 600  # Max time for a rollout to make progress before failing

  template:                     # Pod template that describes the Pods to be created
    metadata:
      labels:
        app: my-app             # Must match selector.matchLabels
      annotations:
        purpose: "Pod managed by Deployment"
    spec:
      containers:
        - name: my-container
          image: nginx:latest
          imagePullPolicy: IfNotPresent  # When to pull the image (Always / IfNotPresent / Never)
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          env:                          # Optional: environment variables
            - name: ENVIRONMENT
              value: production
            - name: SECRET_TOKEN
              valueFrom:
                secretKeyRef:
                  name: my-secret
                  key: token
          resources:                    # Optional: resource requests and limits
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "256Mi"
          livenessProbe:               # Optional: check if container is alive
            httpGet:
              path: /healthz
              port: 80
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:              # Optional: check if container is ready to receive traffic
            httpGet:
              path: /ready
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
          lifecycle:                   # Optional: lifecycle hooks
            preStop:
              exec:
                command: ["/bin/sh", "-c", "echo Stopping"]
      restartPolicy: Always            # Pod-level: Always / OnFailure / Never
      nodeSelector:                    # Optional: schedule Pods on specific nodes
        disktype: ssd
      tolerations:                     # Optional: allow scheduling on tainted nodes
        - key: "key1"
          operator: "Equal"
          value: "value1"
          effect: "NoSchedule"
      affinity:                        # Optional: advanced scheduling rules
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: kubernetes.io/e2e-az-name
                    operator: In
                    values:
                      - e2e-az1
                      - e2e-az2
      dnsPolicy: ClusterFirst          # Optional: DNS policy (Default, ClusterFirst, None)
      securityContext:                 # Optional: security settings for the entire Pod
        runAsUser: 1000
        runAsGroup: 3000
        fsGroup: 2000
      terminationGracePeriodSeconds: 30  # Time to wait before forcefully killing containers


```

  

## List of tasks / Execution

- [] Create full deployment with different types of update and check how they are updating. Update app with wrong image and make rollback.

  

🏷️ Tags: #deploy #autoscaling #update #rollout #app