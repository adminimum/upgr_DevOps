## 📌 Definition

- What it is:
  A Kubernetes object used to store sensitive data such as passwords, API tokens, certificates, or SSH keys.

- How useful it is:
  It prevents exposing secrets in Pod specs or ConfigMaps and provides a secure way to inject sensitive data into containers.

- How to implement:
   Secrets are created as Kubernetes objects, encoded in Base64, and mounted as files or injected as environment variables in Pods.

- Simple analogy:
  Think of a Secret as a **locked envelope** you give to your application. The application can open it and read the sensitive data, but you don’t want it written on the whiteboard for everyone to see.

- Problem it solves:
  Avoids hardcoding sensitive information in application manifests or source code.

- My thoughts:
  Secret is Kubernetes object that provide us an ability to store and put the information inside containers-Pods in a secure and safe way.

## 🔗 Related Topics


## 🛠 Commands / Syntax

```bash

# encode
echo -n "ext" | base64

# Create secret from literal values
kubectl create secret generic my-secret --from-literal=username=admin --from-literal=password=12345

# Create secret from file
kubectl create secret generic my-tls --from-file=cert.crt --from-file=cert.key

# Describe secret
kubectl describe secret my-secret

# Get secret (Base64 encoded values)
kubectl get secret my-secret -o yaml

# Decode secret
kubectl get secret my-secret -o jsonpath="{.data.password}" | base64 --decode


```

  

## 🗒️ YAML format example with explaining

```YAML

apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque # other types: kubernetes.io/tls, kubernetes.io/dockerconfigjson
data:
  username: YWRtaW4=   # "admin" base64-encoded
  password: MTIzNDU=   # "12345" base64-encoded


```

  

## List of tasks / Execution

-  Enable **encryption at rest** for Secrets in cluster configuration.
-  Restrict RBAC so only necessary services can access Secrets.
-  Use external Secret manager integration for production workloads.
-  Regularly rotate Secrets and audit access logs.
  

🏷️ Tags: #secret #secure #safe #envFrom #secretRef