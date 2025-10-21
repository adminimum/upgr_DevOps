
## 📌 Definition

- What it is:
  A `ClusterRole` is a **non-namespaced RBAC object** in Kubernetes that defines a set of **permissions** (verbs + resources) that apply **cluster-wide**, including across all namespaces and cluster-level resources.

- How useful it is:
	- ClusterRoles allow admins to define reusable sets of permissions that can be:
	- Bound to **users, groups, or service accounts**
	- Applied **across all namespaces**
	- Used to control access to **non-namespaced resources** (like nodes or persistent volumes)

- Main details:
	- Unlike `Role`, which is **namespace-scoped**, `ClusterRole` is **cluster-scoped**.
	- Can be used in:
	    - `ClusterRoleBinding` → gives access **across the entire cluster**
	    - `RoleBinding` → reuses a `ClusterRole` **within a specific namespace**
	- Can grant access to **namespaced** and **non-namespaced** resources.

- How to implement:
	1. Create a `ClusterRole` YAML with desired **verbs**, **resources**, and **apiGroups**.
	2. Bind it using `ClusterRoleBinding` (for global access) or `RoleBinding` (for namespace-specific access).

- Simple analogy:
  Imagine a `ClusterRole` like a **“master keycard”** in a hotel – it works in every room, not just one

- Problem it solves:
	- Avoids duplication of `Role` definitions in every namespace.
	- Enables central control over permissions that span the whole cluster.
	- Makes it easier to grant read-only or admin access for monitoring, CI/CD, or system services.

- Attributes:
	- **Cluster-scoped**
	- Can include:
	    - `apiGroups`: e.g. `""` for core, `"apps"` for deployments
	    - `resources`: e.g. `pods`, `nodes`
	    - `verbs`: e.g. `get`, `list`, `create`, `watch`
	- Used with `ClusterRoleBinding` or `RoleBinding`

- My thoughts:
  It's just like Roles but for the whole cluster, likewise can add nodes as object for managing.

## 🛠 Commands / Syntax

```bash
# Create ClusterRole
kubectl create clusterrole my-reader-role \
  --verb=get,list,watch \
  --resource=pods,deployments

# Bind ClusterRole to user (cluster-wide access)
kubectl create clusterrolebinding read-all \
  --clusterrole=my-reader-role \
  --user=devuser@example.com

# View existing ClusterRoles
kubectl get clusterroles

# Describe a ClusterRole
kubectl describe clusterrole <name>


```

  

## 🗒️ YAML format example with explaining if needed

```YAML

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-pods-global
subjects:
- kind: User
  name: devuser@example.com
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io


```

  

## List of tasks / Execution
-  Create ClusterRole for `get/list/watch` on deployments
-  Bind ClusterRole to a service account used by Jenkins
-  Test access with `kubectl auth can-i`
-  Audit permissions using `kubectl describe clusterrolebinding <name>`
  

🏷️ Tags:
#cluster #role #cluster_role #access #account #user