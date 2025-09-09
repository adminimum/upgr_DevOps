## 📌 Definition

- What it is:
  Special containers in a Pod that run **before** the main application containers start. They always run to completion.

- How useful it is:
  They allow you to set up prerequisites (e.g., downloading configs, checking dependencies, initializing state) before your main app runs.

- How to implement:
  Defined under `spec.initContainers[]` in the Pod manifest. Each init container must complete successfully before the next one (or the main containers) starts.

- Simple analogy:
  Like **prep chefs in a kitchen** who chop vegetables and prepare sauces before the head chef starts cooking

- Problem it solves:
  Ensures proper startup ordering and environment setup without bloating the main container image.

- My thoughts:
  It's a simple way to predefine some actions that should be executed before main container starts. 

## 🛠 Commands / Syntax

```bash
# Apply Pod with init container
kubectl apply -f pod-with-init.yaml

# Check Pod init status
kubectl get pod mypod -o wide

# Describe Pod to see init container logs/status
kubectl describe pod mypod

# Get logs of an init container
kubectl logs mypod -c init-myservice

```

  

## 🗒️ YAML format example with explaining

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: init-demo
spec:
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'echo Initializing... && sleep 5']
  containers:
  - name: main-app
    image: nginx
    ports:
    - containerPort: 80

  

```

  

## List of tasks / Execution
-  Write a Pod with multiple init containers (e.g., download config, wait for service).
-  Test Pod startup order and logs.
-  Practice mounting shared volumes between init and app containers.
-  Combine init + sidecar to build resilient apps.
  

🏷️ Tags:
#init #initcontainer #prerequires #lifecycle #requirenments