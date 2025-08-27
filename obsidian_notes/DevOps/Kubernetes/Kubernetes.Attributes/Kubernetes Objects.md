
![Kubernetes objects](kuber-objects.png)
## 📌 Definition

- What it is: This is all persistent elements of the kubernetes logic workcycle.
	- **Pods** → run containers
	    
	- **ReplicaSet** → ensures right number of Pods
	    
	- **Deployment** → manages updates/rollbacks
	    
	- **Service** → stable networking
	    
	- **ConfigMap/Secret** → config & sensitive data
	    
	- **Namespace** → organization
	    
	- **Ingress** → external access
	    
	- **StatefulSet/DaemonSet** → special workloads
	    
	- **Job/CronJob** → one-time & scheduled tasks

- How useful it is:
	It can be used for creating development logic for a distributed apps.

- How to implement:
  ```
  kubectl apply -f ...
  kubectl delete -f ...
  kubectl run ...
  kubectl exec -it ...
  kubectl rollout ...
	  
  ```

- Simple analogy:
  Kubernetes objects like a business processes in a big company that make all big profit, but they are split into small logical units.

- Problem it solves:
  It has the whole reason of exist of Kubernetes.

- My thoughts:
  Objects of the Kubernetes provide logical units to set up distributed apps and make them orchestrated

  

## 🔗 Related Topics
- [[Pod]]
- [[ReplicaSet]]
- [[Deployments]]
- [[Services]]


## 🛠 Commands / Syntax

```bash

# List all objects (pods, services, deployments, etc.) in the current namespace
kubectl get all

# Describe a specific object in detail (example: pod)
kubectl describe pod <pod-name>

# Create an object from a YAML manifest
kubectl apply -f <manifest.yaml>

# Delete an object
kubectl delete -f <manifest.yaml>

# Edit a running object (example: deployment)
kubectl edit deployment <deployment-name>

# Scale a deployment to N replicas
kubectl scale deployment <deployment-name> --replicas=<number>

# Expose a deployment as a service
kubectl expose deployment <deployment-name> --type=NodePort --port=80

# Get logs of a pod
kubectl logs <pod-name>

# Execute a command inside a running pod
kubectl exec -it <pod-name> -- /bin/sh

# Show YAML definition of an object (example: service)
kubectl get svc <service-name> -o yaml

```

  

## List of tasks / Execution

- [] Create the whole app with deployment, service, temporary PV and RS

  

🏷️ Tags: #object #pod #deploy #service #index #set #secret