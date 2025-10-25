## 📌 Definition

- What it is:
  A **Persistent Volume Claim (PVC)** is a **user request for storage** in Kubernetes. It acts as a **bridge between a Pod and a Persistent Volume (PV)**, allowing pods to use storage without knowing the underlying storage details.

- How useful it is:
  It allows developers to **request and attach storage dynamically** without manual admin intervention. PVCs abstract away the complexity of storage provisioning and enable portability of workloads across environments.

- Main details:
	- PVCs define **how much storage** a pod needs and **what access mode** it requires.
	- The **Kubernetes control plane** automatically finds a matching PV or creates one dynamically (if `StorageClass` is set).
	- PVCs are namespaced — a claim belongs to a single namespace.
	- Once a PVC is bound to a PV, it can be **mounted** by pods as a volume.
	- When a PVC is deleted, behavior depends on the PV’s **reclaim policy** (`Retain`, `Delete`, `Recycle`).

- How to implement:
	1. Define a PVC manifest specifying storage size, access mode, and optional `storageClassName`.
	2. Apply it using `kubectl apply -f`.
	3. Mount it inside your pod under the `volumes` section and reference it by name.

- Simple analogy:
	Think of a PVC as a **reservation request** for a hotel room (the Persistent Volume). You don’t need to know which exact room (disk) you’ll get — Kubernetes assigns one that fits your request.

- Problem it solves:
  It solves the issue of **manually managing and attaching storage** to pods. With PVCs, you can dynamically and declaratively request storage in your manifests.

- Attributes:
	- Defines storage **requests** and **access modes** (`ReadWriteOnce`, `ReadWriteMany`, `ReadOnlyMany`)
	- Can reference a **StorageClass** for dynamic provisioning
	- Bound to one PV at a time
	- Namespaced resource

- My thoughts:
	It's just a reservation of the data from PV. It helps to lend a physical space of the storage with specific rules and then you can attach it to the pod.


## 🛠 Commands / Syntax

```bash

kubectl get pvc
kubectl describe pvc <claim-name>
kubectl delete pvc <claim-name>

```

  

## 🗒️ YAML format example with explaining if needed

```YAML

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce         # The volume can be mounted as read-write by a single node
  resources:
    requests:
      storage: 1Gi          # The requested storage size
  storageClassName: standard # Optional; defines dynamic provisioning class
  
---
1. apiVersion: v1
2. kind: Pod
3. metadata:
4. name: mypod
5. spec:
6. containers:
7. - name: myfrontend
8. image: nginx
9. volumeMounts:
10. - mountPath: "/var/www/html"
11. name: mypd
12. volumes:
13. - name: mypd
14. persistentVolumeClaim:
15. claimName: myclaim
  

```

  

## List of tasks / Execution
-  Create a `PersistentVolume` or ensure `StorageClass` exists
-  Define and apply a `PersistentVolumeClaim`
-  Reference the PVC in your pod spec under `volumes`
-  Mount it in containers under `volumeMounts`
  

🏷️ Tags:
#pvc #data #storage #mount #volume #stateful