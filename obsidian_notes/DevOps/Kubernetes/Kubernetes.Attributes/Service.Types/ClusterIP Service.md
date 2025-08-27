![ClusterIP-Service](ClusterIP-Service.png)  

## 🔹 Description:
- Best for internal communication between microservices (e.g., frontend → backend, backend → database).
- Pods may change IPs dynamically, but Service ensures a **stable DNS name + virtual IP**.
- Traffic is automatically load-balanced across all healthy Pods behind the Service.

## 🔹 When to choose ClusterIP:
- ✅ Internal-only communication.
- ✅ Backend services (databases, internal APIs, cache).
- ❌ Not suitable when you need **external access** from outside the cluster.

```YAML
apiVersion: v1
kind: Service
metadata:
  name: my-clusterip-service   # Name of the service
  labels:
    app: myapp                 # Labels to identify the service
spec:
  type: ClusterIP              # Service type (default)
  selector:                    # Selects Pods by labels
    app: myapp
  ports:
    - port: 80                 # Port on the service (ClusterIP)
      targetPort: 8080         # Port on the Pods
      protocol: TCP            # Protocol (TCP/UDP)

```


#ClusterIP