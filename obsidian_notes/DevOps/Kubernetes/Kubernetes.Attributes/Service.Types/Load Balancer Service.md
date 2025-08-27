![Load Balancer](load_balancer.png) 

### 📌 **Description**
- A **LoadBalancer Service** exposes your application to the **outside world** by creating a cloud provider’s load balancer (e.g., AWS ELB, GCP Load Balancer, Azure LB).
- It routes external traffic to the Service and then to the correct Pods.
- Each cloud provider automatically assigns a **public IP** to the LoadBalancer.
- Best suited for apps that **must be publicly accessible**.

### 📌 **When to Choose NodePort**
- Use when you need to **expose an app to the internet**.
- Ideal for **production workloads** (e.g., APIs, web apps).
- When deploying on **cloud environments** that support external load balancers.
- Avoid if running only inside a private cluster (better use ClusterIP or NodePort).

```YAML
apiVersion: v1
kind: Service
metadata:
  name: my-loadbalancer-service  # Name of the service
  labels:
    app: my-app
spec:
  type: LoadBalancer              # Service type is LoadBalancer
  selector:
    app: my-app                   # Pods to forward traffic to
  ports:
    - protocol: TCP               # Protocol (TCP/UDP)
      port: 80                    # Port exposed externally (LoadBalancer)
      targetPort: 8080            # Pod container port
      nodePort: 30080             # Optional, NodePort allocated (within 30000–32767)

```

#loadbalancer 