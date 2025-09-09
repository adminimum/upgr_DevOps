## 📌 Definition

- What it is:
  A Kubernetes object that stores **non-confidential key-value pairs** to configure applications without rebuilding containers.

- How useful it is:
  Lets you **decouple configuration from application code**, making apps flexible and portable across environments (dev, staging, prod).

- How to implement:
  You can create ConfigMaps imperatively or declaratively from literal values, files, or YAML definitions, then mount them as **environment variables** or **volumes** into pods.

- Simple analogy:
  Think of a ConfigMap as a **settings file or config notebook** that your app reads at runtime.

- Problem it solves:
  Avoids hardcoding configuration into images or code, centralizes configs, and allows updates without redeploying code.

- My thoughts:
  It's powerful ability to put env variables even multiple amount in the same time. And sometimes let keep values in one place to get them one by one.

  

## 🔗 Related Topics

- [[]]

  

## 🛠 Commands / Syntax

```bash

# Create ConfigMap from literal
kubectl create configmap app-config --from-literal=APP_MODE=production

# Create ConfigMap from file
kubectl create configmap app-config --from-file=./config.properties

# Describe ConfigMap
kubectl describe configmap app-config

# Get ConfigMap in YAML
kubectl get configmap app-config -o yaml

# Delete ConfigMap
kubectl delete configmap app-config


```

  

## 🗒️ YAML format example with explaining

```YAML
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config        # String, mandatory
  namespace: default      # String, optional
data:                     # Map, mandatory (holds key-value pairs)
  APP_MODE: "production"  # String
  LOG_LEVEL: "debug"      # String
  config.json: |          # String (multi-line), Optional
    {
      "maxConnections": 100,   # Number
      "timeout": 30            # Number
    }
---
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
  namespace: default
spec:
  containers:
    - name: demo-container
      image: nginx:latest
      envFrom:
        - configMapRef:
            name: app-config   # String, mandatory -> name of the ConfigMap

```

  

## List of tasks / Execution

- Create ConfigMap from a literal value.
- Create ConfigMap from a file.
- Mount ConfigMap into a Pod as an environment variable.
- Mount ConfigMap as a volume to load config files.
- Update a ConfigMap and reload it in a running pod.

  

🏷️ Tags: #config #configmap #envfrom #variables