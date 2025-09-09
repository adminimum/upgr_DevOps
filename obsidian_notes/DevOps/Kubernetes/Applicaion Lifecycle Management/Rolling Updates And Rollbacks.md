![Roll](rollback.jpg)
## 📌 Definition

- What it is:
  A process in Kubernetes Deployments that updates pods to a new version gradually (rolling update) or reverts back to the previous version if something goes wrong (rollback).

- How useful it is:
  It minimizes downtime, reduces the risk of failures during upgrades, and ensures smooth application delivery.

- How to implement:
  By updating the Deployment object (changing image, replicas, strategy). Kubernetes replaces old pods with new ones step by step while keeping the app available. Rollbacks are done with `kubectl rollout undo`.

- Simple analogy:
  Like replacing car tires one at a time while the car is still running, instead of stopping the car completely.

- Problem it solves:
  Prevents downtime during upgrades, provides safe fallback if updates fail, and allows controlled gradual rollout.

- My thoughts:
  This ability provide functions to update application smoothly. Without breakdown, step by step. And even if something goes wrong, you can undo your changes by one command.

  

## 🔗 Related Topics

- [[]]

## 🛠 Commands / Syntax

```bash
# Check rollout status
kubectl rollout status deployment/my-app
kubectl rollout history deployment/my-app   

# Update deployment image (triggers rolling update)
kubectl set image deployment/my-app my-app=nginx:1.25.1  

# Rollback to previous version
kubectl rollout undo deployment/my-app  

# Rollback to a specific revision
kubectl rollout undo deployment/my-app --to-revision=2  

# Pause a rollout
kubectl rollout pause deployment/my-app  

# Resume a rollout
kubectl rollout resume deployment/my-app

```

  

## 🗒️ YAML format example with explaining

```YAML

  apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3   # Number of pods
  selector:
    matchLabels:
      app: my-app
  strategy: 
    type: RollingUpdate   # Can be RollingUpdate or Recreate
    rollingUpdate:
      maxUnavailable: 1   # Number of pods that can be down during update
      maxSurge: 1         # Number of extra pods created temporarily
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: nginx:1.25.1   # Updating this triggers rolling update

```

  

## List of tasks / Execution

- Understand `strategy` in Deployments (`RollingUpdate` vs `Recreate`).
- Practice `kubectl set image` to trigger rolling updates.
- Try `kubectl rollout undo` for rollback.
- Experiment with `pause` and `resume` rollout to control speed.
- Monitor rollout progress with `kubectl rollout status`.

  

🏷️ Tags: #rollout #update #upgrade #deploy #undo #status #history #rollingupdate