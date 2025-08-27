![Services](services.gif)
## 📌 Definition

- What it is:
  A **Service** in Kubernetes is an abstraction that defines a stable way to access a group of Pods. Since Pods are ephemeral (they can be restarted, rescheduled, or replaced), a Service provides a **permanent IP address and DNS name** to ensure reliable communication between components inside or outside the cluster.

- Types:
  Kubernetes supports different **Service types**, depending on how you want to expose your application:
	1. **ClusterIP** (default) – Exposes the Service on an internal IP inside the cluster. Accessible only within the cluster.
	2. **NodePort** – Exposes the Service on a static port on each Node’s IP. External traffic can access the Service via `<NodeIP>:<NodePort>`.
	3. **LoadBalancer** – Provisions an external load balancer (cloud provider dependent) and exposes the Service to the internet.
	4. **ExternalName** – Maps a Service to an external DNS name (no proxying, just DNS CNAME).

- How useful it is:
	- Provides **stable network identity** for Pods that may frequently change.
	- Enables **load balancing** between multiple Pods.
	- Separates **frontend** and **backend** services clearly.
	- Allows **internal and external** access management depending on Service type.

- How to implement:
	You create a **YAML manifest** that defines:
	- `selector`: Which Pods the Service targets (labels).
	- `ports`: Port mapping (port inside Service, targetPort inside Pod, optional NodePort).
	- `type`: Service exposure type (`ClusterIP`, `NodePort`, `LoadBalancer`, `ExternalName`).
	Then apply it with: "kubectl apply -f ..."

- Simple analogy:
  Imagine a **restaurant kitchen (Pods)**. Chefs may come and go, but the **waiter (Service)** always takes your order and knows which chef is available. Customers don’t care which chef is cooking—**they just order through the waiter**.

- Problem it solves:
	- **Pods are ephemeral**: their IPs change when restarted, making direct communication unreliable.
	- Services solve this by providing:
	    - **Stable endpoint** (IP and DNS).
	    - **Load balancing** across Pod replicas.
	    - **Controlled external access** when needed.

- My thoughts:
  The main goal of services on my perspective is to make network connectivity between services by dns note (ClusterIP), expose port for the application throughout port of the nodes (NodePort), Load balancing traffic to the apps entities(Load Balancer) 

## 🔗 Related Topics

- [[NodePort Service]]
- [[ClusterIP Service]]
- [[Load Balancer Service]]

  

## 🛠 Commands / Syntax

```bash
# 1. List all services
kubectl get svc

# 2. Describe a service (see details like endpoints, selectors)
kubectl describe svc <service-name>

# 3. Expose a deployment as a service
kubectl expose deployment <deployment-name> --type=NodePort --port=80 --target-port=8080

# 4. Access service logs and debug networking
kubectl get endpoints <service-name>

# 5. Delete a service
kubectl delete svc <service-name>


```

  

## 🗒️ YAML format example with explaining

```YAML

  apiVersion: v1
kind: Service
metadata:
  name: my-service                   # Name of the Service
  namespace: default                 # Namespace (default if not specified)
  labels:                            # Labels for identifying the service
    app: my-app
  annotations:                       # Annotations (metadata, not used for selection)
    description: "My sample service"

spec:
  type: ClusterIP                    # Service type: ClusterIP | NodePort | LoadBalancer | ExternalName
  clusterIP: None                    # Optional: set None for headless service
  externalName: example.com          # Used only for ExternalName type
  sessionAffinity: None              # None | ClientIP (stick requests from same client)
  selector:                          # Pod labels to match
    app: my-app
  ports:                             # Define ports for the service
    - name: http
      protocol: TCP                  # Protocol: TCP | UDP | SCTP
      port: 80                       # Port exposed by the Service
      targetPort: 8080               # Pod port that receives traffic
      nodePort: 30080                # Required for NodePort (range: 30000-32767)
  externalIPs:                       # Optional: IPs outside cluster that route to Service
    - 192.168.1.100
  loadBalancerIP: 34.68.194.10       # Optional: Cloud provider assigned LoadBalancer IP
  loadBalancerSourceRanges:          # Restrict LB access to specific CIDRs
    - 203.0.113.0/24
  ipFamilyPolicy: SingleStack        # SingleStack | PreferDualStack | RequireDualStack
  ipFamilies:                        # Specify IPv4/IPv6
    - IPv4
  publishNotReadyAddresses: false    # If true, service routes to not-ready pods too
  topologyKeys:                      # Prefer traffic routing by topology
    - "kubernetes.io/hostname"
    - "topology.kubernetes.io/zone"
status:                              # Status (populated by K8s automatically)
  loadBalancer:                      # Info about LoadBalancer (if type=LoadBalancer)
    ingress:
      - ip: 203.0.113.25


```

  

## List of tasks / Execution

- [] Create deployment with web app, then create service node port for exposing port out of the nodes
  

🏷️ Tags: #service #port #app #selector #dns #loadbalancer #ip