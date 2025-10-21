## 📌 Definition

- What it is:
  A **ServiceAccount (SA)** in Kubernetes is an **identity used by applications, pods, or controllers** to authenticate with the Kubernetes API server and perform actions on cluster resources — similar to how users authenticate, but for **machines and workloads**.

- How useful it is:
  ServiceAccounts let your workloads (e.g., pods, CI/CD jobs, controllers) safely interact with cluster resources **without needing user credentials**.  
  They are essential for **automation**, **RBAC security**, and **fine-grained access control** in production environments.

- Main details:
	- Each namespace automatically has a **default service account** (`default`).
	- Service accounts are bound to **secrets** containing:
	    - A token (used for authentication)
	    - A certificate
	    - Namespace and API endpoint info
	- Pods can:
	    - Use the **default service account**
	    - Or specify a **custom service account** in their spec
	- Typically used together with **RBAC (Role/RoleBinding)** to control what a pod can access.

- How to implement:
	1. **Create** a new service account.
	2. **Create a Role/ClusterRole** that defines what it can do.
	3. **Bind** that Role to the service account using a RoleBinding or ClusterRoleBinding.
	4. **Assign** the service account to a pod via `spec.serviceAccountName`.

- Simple analogy:
  Imagine Kubernetes as a company.  
  **Users** are employees who log in directly.  
  **Service accounts** are like _robot badges_ that let automated systems (like Jenkins or a monitoring agent) access certain departments without using a real employee’s badge.

- Problem it solves:
    -  Avoids using **human credentials** (users or kubeconfigs) for automation.
	- Grants **minimum required privileges** to workloads, reducing risk.
	- Enables secure communication between **in-cluster components** (e.g., controllers, pods, operators).

- Attributes:

|Attribute|Description|
|---|---|
|**Scope**|Namespace-scoped|
|**Authentication**|Uses tokens mounted into pods|
|**Authorization**|Controlled by RBAC roles/bindings|
|**Default behavior**|Pods use `default` service account unless overridden|
|**Best practice**|Create dedicated service accounts for each app/component with minimal permissions|

- My thoughts:
  This is simple identity for creating account which won't be used for manual work. The only need in this account is to put it inside application to make some automatic actions.

## 🛠 Commands / Syntax

```bash
# Create a service account
kubectl create serviceaccount my-serviceaccount -n dev

# View all service accounts
kubectl get serviceaccounts -n dev

# Describe a specific service account
kubectl describe sa my-serviceaccount -n dev

# Show the secret token linked to a service account
kubectl get secret $(kubectl get sa my-serviceaccount -n dev -o jsonpath='{.secrets[0].name}') -n dev -o yaml

# Assign service account to a running pod (via deployment)
kubectl set serviceaccount deployment/my-app my-serviceaccount -n dev


```

  

## 🗒️ YAML format example with explaining if needed

```YAML

  # 1️⃣ Create Service Account
apiVersion: v1
kind: ServiceAccount
metadata:
  name: webapp-sa
  namespace: dev
---
# 2️⃣ Create Role (permissions)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev
  name: webapp-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
---
# 3️⃣ Bind the Role to the Service Account
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods-binding
  namespace: dev
subjects:
- kind: ServiceAccount
  name: webapp-sa
  namespace: dev
roleRef:
  kind: Role
  name: webapp-reader
  apiGroup: rbac.authorization.k8s.io
---
# 4️⃣ Use Service Account in Pod
apiVersion: v1
kind: Pod
metadata:
  name: webapp
  namespace: dev
spec:
  serviceAccountName: webapp-sa
  containers:
  - name: nginx
    image: nginx:alpine


```

  

## List of tasks / Execution
-  Create a namespace-specific ServiceAccount for an app.
-  Bind a Role with read-only access to pods.
-  Assign this SA to your deployment.
-  Test with `kubectl auth can-i list pods --as=system:serviceaccount:dev:webapp-sa`.
  

🏷️ Tags:
#service #account #automation #access #user #robot