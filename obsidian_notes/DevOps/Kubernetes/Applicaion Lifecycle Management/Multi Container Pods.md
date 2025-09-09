## 📌 Definition

- What it is:
  A Pod that contains **two or more containers** that run together on the same node, share the same network namespace (IP, port space), and optionally share storage volumes.

- How useful it is:
  Enables building tightly coupled services that must run together (e.g., sidecars, adapters, or ambassadors).

- How to implement:
  Define multiple containers inside the same `spec.containers[]` section of a Pod manifest. They can communicate via `localhost` and share mounted volumes.

- Simple analogy:
  Think of a Pod as a **shared apartment**, and containers as **roommates**—each has its own room (process space) but shares the same kitchen (network) and storage (volumes).

- Problem it solves:
  Allows decomposition of application logic into multiple specialized containers instead of bloating a single one.

- My thoughts:
  It's an opportunity to split your app into microservices and then you can run them with the same storage, same network interface.

  
## 🛠 Commands / Syntax

```bash

# Run a Pod with multiple containers
kubectl apply -f multi-container-pod.yaml

# Get logs from specific container
kubectl logs mypod -c sidecar-container

# Exec into a specific container
kubectl exec -it mypod -c main-app -- /bin/sh


```

  

## 🗒️ YAML format example with explaining

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: main-app
    image: nginx
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-data
      mountPath: /usr/share/nginx/html
  - name: sidecar
    image: busybox
    command: ["/bin/sh", "-c"]
    args:
    - while true; do echo "Hello from sidecar" > /shared-data/index.html; sleep 5; done
    volumeMounts:
    - name: shared-data
      mountPath: /shared-data
  volumes:
  - name: shared-data
    emptyDir: {}  

```

  

## List of tasks / Execution
-  Understand communication between containers using `localhost`.
-  Practice mounting shared volumes (`emptyDir`, `configMap`)    
-  Try sidecar logging or service mesh patterns.
-  Explore init containers + multi-container Pod combo.
  

🏷️ Tags:
#multicontainer #pod #init #microservices