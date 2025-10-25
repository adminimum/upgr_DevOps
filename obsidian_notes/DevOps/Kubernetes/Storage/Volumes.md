## 📌 Definition

- What it is:
  A **Volume** in Kubernetes is a storage abstraction that allows containers to **persist and share data**, even beyond the container’s lifecycle.

- How useful it is:
  Without volumes, data in a container is **ephemeral** — lost when a container restarts. Volumes provide **durability**, **sharing**, and **stateful behavior**, which is essential for databases, caches, and other stateful apps.

- Main details:
	- Kubernetes supports many volume types: `emptyDir`, `hostPath`, `persistentVolumeClaim`, `configMap`, `secret`, `nfs`, `CSI`, etc.
	- Volumes can be defined at the **Pod level**, not container level.
	- Multiple containers in a pod can **mount the same volume**.
	- Volumes can persist data across container restarts (but not always pod restarts unless backed by PV)

- How to implement:
	- Declare the volume in the `volumes:` section of the Pod spec.
	- Mount it inside one or more containers with `volumeMounts:`.
	- Use `PersistentVolume` and `PersistentVolumeClaim` for longer storage life and dynamic provisioning.

- Simple analogy:
  A container without a volume is like a **whiteboard** — everything you write disappears when the room is cleaned. A volume is like a **notebook** — it stays even if you leave and return.

- Problem it solves:
	- Prevents data loss on container restarts.
	- Allows data sharing between containers.
	- Supports persistent applications (e.g., databases).
	- Decouples storage from the container lifecycle.

- Attributes:
	- Defined in the pod spec.
	- Multiple types: `emptyDir`, `PVC`, `hostPath`, `CSI`, etc.
	- Shared between containers in a pod.
	- Lifecycle tied to Pod (unless PV is used).

- My thoughts:
	It's just different ways to save your data after running and destroying your pod. Volumes stay the same. They let you to store data for a required period of time.



## 🛠 Commands / Syntax

```bash
# View PVCs and their statuses
kubectl get pvc

# View PVs in the cluster
kubectl get pv

# Describe a PVC to debug binding
kubectl describe pvc <name>


```

  

## 🗒️ YAML format example with explaining if needed

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: volume-demo
spec:
  containers:
  - name: app
    image: busybox
    command: ["/bin/sh", "-c", "sleep 3600"]
    volumeMounts:
    - name: my-storage
      mountPath: /data
  volumes:
  - name: my-storage
    emptyDir: {}   # Temporary storage; cleared when pod deleted

  

```

  

## List of tasks / Execution
-  Try `emptyDir` to share temp data between init and main container.
-  Create a `hostPath` volume for dev test with local storage.
-  Use `PersistentVolumeClaim` to store MySQL data persistently.
-  Mount a `configMap` volume to inject configs as files.

  

🏷️ Tags:
#volumes #data #storage #claim #persistenclaim #path