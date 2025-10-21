
## 📌 Definition

- What it is:
	Authorization in Kubernetes is the process of determining whether a user, group, or service account is **allowed** to perform a specific action (e.g., `get`, `create`, `delete`) on a specific Kubernetes resource (e.g., pods, secrets, nodes).
- How useful it is:
   It ensures **controlled access** to cluster resources, enabling secure multi-tenant environments, fine-grained permissions, and **role-based access control (RBAC)** across users and workloads.

- How to implement:
	- Kubernetes uses **authorization modules** like:
	- **RBAC (Role-Based Access Control)**
	- **ABAC (Attribute-Based Access Control)**
	- **Webhook authorizers** (for custom logic)
	- **Node authorization** (for kubelets)
	The most commonly used method is **RBAC**, where `Role` or `ClusterRole` objects define what actions are allowed, and `RoleBinding` or `ClusterRoleBinding` assign those roles to users or service accounts

- Simple analogy:
  Think of **authorization** like a **bouncer at a nightclub**. Even if you have an ID (authentication), you still need to be on the **guest list** or have **special access** to get into VIP sections. Authorization checks that list.

- Problem it solves:
  Prevents unauthorized actions and **enforces least-privilege access**, minimizing the blast radius of compromised users or misconfigured services.

- Attributes:
	- Action-specific (verbs: get, list, delete, etc.)
	- Resource-specific (pods, configmaps, etc.)
	- Namespace-scoped or cluster-wide
	- Evaluated after authentication

- My thoughts:
  This is just ways to get access to your cluster for some actions. It can be set up that way, that specific user can perform specific actions and not more.


## 🛠 Commands / Syntax

```bash
# Check if a user or service account is authorized to perform an action
kubectl auth can-i create deployment --namespace dev --as=system:serviceaccount:dev:myapp-sa

# View all current roles in a namespace
kubectl get roles -n dev

# View all current rolebindings
kubectl get rolebindings -n dev

# View detailed access of a user
kubectl describe clusterrolebinding <binding-name>


```

  

## 🗒️ YAML format example with explaining if needed

```YAML
# This defines a Role that allows reading pods
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
# This binds the Role to a specific user
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

  

## List of tasks / Execution
-  Audit existing RBAC policies using:
    `kubectl get clusterrolebindings -o wide`
    
-  Create a least-privilege service account for an application.
-  Test access with `kubectl auth can-i` before deploying sensitive services.
-  Set up `Role` and `RoleBinding` per namespace for team isolation.

  

🏷️ Tags:
#auth #roles #users #binding #apis #access