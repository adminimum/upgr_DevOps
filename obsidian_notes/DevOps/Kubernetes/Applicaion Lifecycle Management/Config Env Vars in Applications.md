## 📌 Definition

- What it is:
  Configuration values, environment variables (envs), and application variables are ways to pass dynamic data into applications without hardcoding it in code. In Kubernetes/Docker, they are defined outside the app and injected at runtime.

- How useful it is:
  They make applications portable, secure, and easy to configure across different environments (dev, staging, production) without rebuilding images.

- How to implement:
	  - In Docker: `ENV` in Dockerfile, or `-e` flag in `docker run`.
	- In Kubernetes: via `env` in Pod spec, or from ConfigMaps and Secrets.
	- In apps: use OS environment variable APIs (e.g., `os.getenv` in Python, `process.env` in Node.js).

- Simple analogy:
  Think of envs/vars as _sticky notes on the outside of a box_. The contents (code) stay the same, but the notes change depending on where the box is delivered.

- Problem it solves:
  Avoids hardcoding sensitive or environment-specific values in code, enabling better security, flexibility, and CI/CD pipelines.

- My thoughts:
  It's ability that help us store all config information during process of runtime, whatever it be. We specify them and then use them inside our apps.

  

## 🔗 Related Topics

- [[ConfigMaps in Kubernetes]]
- [[Secrets]]

  

## 🛠 Commands / Syntax

```bash

# Docker run with environment variable
docker run -e APP_MODE=production my-app

# Kubernetes set env var from literal
kubectl create configmap app-config --from-literal=APP_MODE=production

# View environment variables inside a pod
kubectl exec -it pod-name -- printenv | grep APP_MODE


```

  

## 🗒️ YAML format example with explaining

```YAML

  apiVersion: v1
kind: Pod
metadata:
  name: env-example
spec:
  containers:
  - name: demo
    image: nginx
    env:
    - name: APP_MODE          # String, mandatory
      value: "production"     # String, hardcoded value
    - name: API_KEY           # String
      valueFrom:              # Replaceable{value, valueFrom}
        secretKeyRef:         # Using Secret
          name: api-secrets
          key: key1
    - name: CONFIG_FILE       # String
      valueFrom:
        configMapKeyRef:      # Using ConfigMap
          name: app-config
          key: config.yaml


```

  

## List of tasks / Execution

- Inject values via `kubectl run --env`.
- Use a ConfigMap for non-sensitive configs.
- Use a Secret for sensitive configs.
- Print and validate envs inside a running pod.
  

🏷️ Tags: #env #variables #secret #configs #app