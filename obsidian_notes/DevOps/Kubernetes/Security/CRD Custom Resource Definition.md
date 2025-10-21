## 📌 Definition

- What it is:
  A **Custom Resource Definition (CRD)** is a Kubernetes API extension that allows you to define your **own resource types**(like `MyApp`, `Database`, etc.) that behave like native Kubernetes resources (`Pods`, `Services`, etc.).

- How useful it is:
  It lets you **extend Kubernetes** to fit domain-specific needs without modifying Kubernetes core. Many tools like **Cert-Manager**, **Istio**, **ArgoCD** rely on CRDs to define custom behavior.

- Main details:
	  - CRDs define the **schema, structure, and validation** rules of your custom resource.
	- Once a CRD is created, you can use `kubectl get`, `apply`, etc. on your new resource.
	- Often used with a **controller/operator** that watches for these resources and reacts accordingly.

- How to implement:
	1. Define the CRD YAML (`apiextensions.k8s.io/v1`)
	2. Apply it to the cluster (`kubectl apply -f crd.yaml`)
	3. (Optional) Deploy a **controller** that watches for instances of the custom resource and acts on them

- Simple analogy:
  Think of Kubernetes as a **customizable game engine**. CRDs let you define **your own game objects**, like "Dragon" or "Treasure Chest", and then write logic (controllers) for how they behave

- Problem it solves:
  Without CRDs, you are limited to core Kubernetes types. CRDs solve the problem of **flexibility and domain-specific automation**, enabling teams to build **Kubernetes-native apps and APIs**.

- Attributes:
	- `spec.names.kind` defines the resource name (e.g., `MyApp`)
	- `spec.scope` can be `Namespaced` or `Cluster`
	- `spec.versions.schema` allows OpenAPI-style validation
	- Optional `status` section for feedback from controllers

- My thoughts:
	This is just an ability to create your own type of objects in kubernetes. So you can write their logic and then use it as you want.
  

## 🛠 Commands / Syntax

```bash

# Apply a CRD
kubectl apply -f my-crd.yaml

# See existing CRDs
kubectl get crds

# Get instances of a custom resource (e.g., MyApp)
kubectl get myapps.mycompany.com

# Describe CRD
kubectl describe crd myapps.mycompany.com


```

  

## 🗒️ YAML format example with explaining if needed

```YAML

apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: myapps.mycompany.com
spec:
  group: mycompany.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                replicas:
                  type: integer
                image:
                  type: string
  scope: Namespaced
  names:
    plural: myapps
    singular: myapp
    kind: MyApp
    shortNames:
      - ma


```

  

## List of tasks / Execution
-  Design your custom domain object (e.g., BackupTask, MLJob)
-  Write a CRD YAML defining it
-  Apply it to the cluster
-  Create a sample instance of the CR
-  (Optional) Write a controller or use `kubebuilder`/`operator-sdk`

  
🏷️ Tags:
#crd #object #custom #controller #resource #template