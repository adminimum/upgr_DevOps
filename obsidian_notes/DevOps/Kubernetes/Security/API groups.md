
## 📌 Definition

- What it is:
  API Groups in Kubernetes are a way to logically organize and version RESTful APIs. Each resource in Kubernetes (like Pods, Deployments, Services) belongs to a specific **API group**, which helps manage its evolution and extensions over time.

- How useful it is:
  They make it possible to evolve the Kubernetes API without breaking older versions. API groups also let you organize custom resources cleanly and enable/disable specific functionalities

- How to implement:
	- Core Kubernetes resources (like Pods, Namespaces) belong to the **core group**, which has no name and appears at the root (`/api/v1`).    
	- Other groups (like `apps`, `batch`, `rbac.authorization.k8s.io`, etc.) appear under `/apis/GROUP_NAME/VERSION`.

- Simple analogy:
  Think of API groups like **departments in a company**. Each department (group) handles related tasks (resources), and you can version each department's policies separately.

- Problem it solves:
  API groups avoid a monolithic structure and allow Kubernetes to evolve safely with modular versioning. They also enable separation between built-in and custom APIs

- Attributes:
	  - Versioned (`v1`, `v1beta1`, etc.)
	- Modular
	- Extensible (Custom Resource Definitions – CRDs use their own groups)
	- Defined via OpenAPI spec

- My thoughts:
  It's just sortification that allows you to request specific info from API of the Kubernetes. These info is logically sorted by groups and versions of these groups.

## 🛠 Commands / Syntax

```bash
# List all API groups available on the cluster
kubectl api-versions

# Get detailed info about a resource’s API group and version
kubectl explain deployment

# Get resource with explicit group/version
kubectl get deployments.v1.apps

# use Api without certificates
kubectl proxy

```

  

## 🗒️ YAML format example with explaining if needed

```YAML

  apiVersion: apps/v1   # <- This defines the API group "apps" and version "v1"
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app
          image: nginx


```

  

## List of tasks / Execution
-  Understand which group a resource belongs to using `kubectl explain <kind>`
    
-  Configure RBAC rules with correct group names:
    `apiGroups: ["apps"] resources: ["deployments"] verbs: ["get", "list", "watch"]`
    
-  Create a CRD with a unique group name, e.g., `apiVersion: mygroup.example.com/v1`
  

🏷️ Tags:
#api #groups #restful #request #managing