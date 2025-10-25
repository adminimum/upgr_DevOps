## 📌 Definition

- What it is:
  A **Persistent Volume** is a piece of storage in a Kubernetes cluster that has been **provisioned by an administrator** or **dynamically provisioned** using a `StorageClass`. It is a cluster resource **independent of any individual pod**.

- How useful it is:
   Extremely useful for **data persistence** across pod restarts, rescheduling, or even redeployment. Without PVs, all data in containers is ephemeral and lost once the pod stops.

- Main details:
	- It exists independently of the Pod lifecycle.
	- Pods claim PVs via **Persistent Volume Claims (PVCs)**.
	- It supports a wide range of backends: local disk, NFS, AWS EBS, GCE PD, Azure Disk, etc.
	- Access modes:
	    - `ReadWriteOnce` (RWO) – mounted as read-write by a single node
	    - `ReadOnlyMany` (ROX) – mounted read-only by many nodes
	    - `ReadWriteMany` (RWX) – mounted as read-write by many nodes
	- Reclaim policies: `Retain`, `Recycle`, `Delete`.

- How to implement:
	1. Create a **PersistentVolume** object (optional if using dynamic provisioning).
	2. Create a **PersistentVolumeClaim** object.
	3. Mount the PVC into your pod spec.
	4. Use data like a normal directory inside your container.

- Simple analogy:
  Think of a Persistent Volume as a **USB drive** plugged into your computer. You can restart your apps, but the data stays unless you physically remove or delete the drive.

- Problem it solves:
  It solves the **ephemeral nature of containers** by allowing data to persist independently of pod lifecycle, enabling stateful applications like databases.

- Attributes:
	- Static or dynamic provisioning
	- Reclaim policies (retain, delete, recycle)
	- Access modes
	- Storage backend abstraction

- My thoughts:
  It's an object that set up your storage where the data will be stored for using it though out your pods without depending on state of the pod.


## 🛠 Commands / Syntax

```bash
kubectl get pv
kubectl get pvc
kubectl describe pv <pv-name>
kubectl describe pvc <pvc-name>


```

  

## 🗒️ YAML format example with explaining if needed

```YAML
# Persistent Volume (static)
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /mnt/data

---

# Persistent Volume Claim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi

  

```

  

## List of tasks / Execution
-  Create a `PersistentVolume`
-  Create a `PersistentVolumeClaim`
-  Mount the PVC into your pod under `volumes`
-  Use dynamic provisioning via `StorageClass` for flexibility

  

🏷️ Tags:
#pvc #pv #volume #data #pod #persistentvolume