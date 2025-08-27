![NameSpaces](namespaces.png) 

## 📌 Definition

- What it is:
  A **Namespace** in Kubernetes is a way to logically divide a cluster into multiple virtual clusters. It’s like creating separate “folders” inside your cluster to organize and isolate resources.

- How useful it is:
	- Helps **organize** resources (pods, services, configs) in large clusters.
	- Provides **isolation** between environments (dev, staging, prod).
	- Enables **resource quotas & limits** per namespace.
	- Allows **RBAC (role-based access control)** per namespace.

- How to implement:
  Namespaces are created and managed using `kubectl` or YAML. By default, resources go into the `default` namespace unless specified.

- Simple analogy:
  Think of a **Kubernetes cluster as an apartment building**.
	- Each **namespace** = an individual apartment.
	- The building (cluster) has shared infrastructure (plumbing, electricity), but each apartment can be organized and controlled separately.

- Problem it solves:
	- Avoids **name collisions** (two teams can both use `webapp` service in different namespaces).
	- Provides **isolation** for teams/projects.
	- Allows easier **multi-tenant environments**.

- Communication of pods with service in another namespace:
  Works by this domain structure:
  ```<service-name>.<namespace>.svc.cluster.local```

- My thoughts:
  Namespaces are like different virtual environments where can be same-called objects, can be different access for different group provided. And especially isolation that provides work within one environment with no worrying about affecting Prod environment.

## 🔗 Related Topics

- [[]]

  

## 🛠 Commands / Syntax

```bash

# 1. List all namespaces
kubectl get namespaces

# 2. Create a new namespace
kubectl create namespace dev

# 3. Switch context to a namespace (using kubens or kubectl config)
kubectl config set-context --current --namespace=dev

# 4. Get resources inside a specific namespace
kubectl get pods -n dev

# 5. Delete a namespace (deletes all its resources!)
kubectl delete namespace dev

```

  

## 🗒️ YAML format example with explaining

```YAML

apiVersion: v1
kind: Namespace
metadata:
  name: dev

---
apiVersion: v1
kind: Pod
metadata:
  name: simple-pod
  namespace: dev
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80


```

  

## List of tasks / Execution

- [] Create db service stateless in one namespace and try to connect it from pod in different namespace by correct domain note.


  

🏷️ Tags: #namespace #env #dev #prod #qa #logic #name