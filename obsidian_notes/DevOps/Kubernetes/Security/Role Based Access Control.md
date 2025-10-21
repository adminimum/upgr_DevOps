
## 📌 Definition

- What it is:
  RBAC (Role-Based Access Control) in Kubernetes is a security mechanism that **controls access to resources** based on the roles assigned to users, groups, or service accounts.

- How useful it is:
  RBAC allows you to **implement the principle of least privilege**, ensuring that entities (users or workloads) can only perform the actions they are explicitly allowed to

- Main details:
	- RBAC uses **4 core object types**:
	    - `Role` and `ClusterRole`: define _what_ actions are allowed
	    - `RoleBinding` and `ClusterRoleBinding`: define _who_ gets those permissions
	- **Roles** are namespace-scoped.
	- **ClusterRoles** apply across the entire cluster (and can also be used in namespaces).

- How to implement:
	1. Define a `Role` or `ClusterRole` with specific permissions.
	2. Bind it to a subject (user, group, or service account) using a `RoleBinding` or `ClusterRoleBinding`.

- Simple analogy:
  Think of it like a company:
	- **Roles** = job descriptions (what the employee _can_ do)
	- **RoleBindings** = assigning that job to a specific person

- Problem it solves:
  Prevents **unauthorized access** and **accidental misconfiguration** by ensuring users and processes only have the permissions they need

- Attributes:
	- Namespace-scoped or cluster-scoped
	- Declarative via YAML
	- Tightly integrated into Kubernetes API
	- Used with `kubectl auth can-i` for testing

- My thoughts:
  From my perspective it's something like access in linux system. You can give permissions to the users by specifying what they can do and what objects with. 

## 🛠 Commands / Syntax

```bash
# Test what a user or service account can do
kubectl auth can-i create pods --as=system:serviceaccount:dev:my-app-sa

# View all cluster roles
kubectl get clusterroles

# View all role bindings in a namespace
kubectl get rolebindings -n dev

# Apply a role and binding
kubectl apply -f role.yaml
kubectl apply -f rolebinding.yaml


```

  

## 🗒️ YAML format example with explaining if needed

```YAML
# Role: defines permission to read pods in a namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
---
# RoleBinding: assigns the role to a user
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods-binding
  namespace: dev
subjects:
- kind: User
  name: alice
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io

  

```

  

🏷️ Tags:
#roles #role #binding #control #access #api #environment