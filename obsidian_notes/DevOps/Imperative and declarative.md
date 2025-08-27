![Imperative and delcarative](imperdeclar.png) 

### 📖 **Simple Analogy**
- **Imperative:** Like telling a chef _step by step_ how to cook a dish.   
- **Declarative:** Like giving the chef a _picture of the dish_ and letting them figure out the steps.

## Difference between declarative and imperative approaches 

## 🟦 **Imperative vs Declarative in Kubernetes**

### 1. **Imperative Approach**
- **What it is:** You tell Kubernetes _exactly what to do, step by step_ (like running commands to create/update/delete resources).
    
- **How it works:**
    - Uses commands such as:
        `kubectl run nginx --image=nginx kubectl expose pod nginx --port=80`
    - Or `kubectl create`, `kubectl delete`, `kubectl replace`.
        
- **Pros:**
    - Quick for testing or simple changes.
    - Easy to learn for beginners.
        
- **Cons:**
    - Hard to track changes (no record of desired state).    
    - Doesn’t scale well for large teams or CI/CD pipelines

### 2. **Declarative Approach**
- **What it is:** You declare _the desired state_ in a file (YAML/JSON), and Kubernetes ensures reality matches that state.
    
- **How it works:**
    - You define resources in YAML:        
        `apiVersion: apps/v1 kind: Deployment metadata:   name: nginx-deploy spec:   replicas: 3   selector:     matchLabels:       app: nginx   template:     metadata:       labels:         app: nginx     spec:       containers:         - name: nginx           image: nginx:1.27`
    - Apply with:
        `kubectl apply -f deployment.yaml`
        
- **Pros:**
    - Version control friendly (store YAML in Git).
    - Easy rollback, reproducibility, team collaboration.
    - Works well with GitOps and automation.
- **Cons:**
    - Steeper learning curve initially.
    - Need discipline to maintain manifests.


## Difference between create/replace and apply commands
### 1. **`kubectl create`**
- **What it does:** Creates a new resource from a YAML/JSON manifest.
- **Fails if resource already exists.**
- **Example:**
    `kubectl create -f deployment.yaml`
- ✅ Good for **first-time creation** of objects.
- ❌ Not good for updates (you’ll get “AlreadyExists” error
### 2. **`kubectl replace`**
- **What it does:** Deletes the existing resource and creates it again with the new definition.
- **Replaces entire object** → if you remove fields in YAML, they are gone.
- **Example:**    
    `kubectl replace -f deployment.yaml`
- ✅ Good if you want to **completely overwrite** a resource.
- ❌ Bad if you want incremental changes, because it wipes out unspecified fields.
- ❌ If resource has downtime-sensitive workloads → replacement can cause disruptions.
### 3. **`kubectl apply`**
- **What it does:** Performs a **smart update (patch)**.
- It merges the differences between the YAML and the live cluster state.
- Kubernetes keeps track of “last-applied-configuration” in annotations.
- **Example:**
    `kubectl apply -f deployment.yaml`
- ✅ Safe for **incremental changes**.
- ✅ Keeps fields not defined in the YAML but managed by the cluster (e.g., status, selectors).
- ✅ Preferred in **GitOps / CI/CD pipelines** because you can repeatedly `apply` same file and Kubernetes reconciles it.


#declarative #imperative #approach #kubectl #yaml #manage