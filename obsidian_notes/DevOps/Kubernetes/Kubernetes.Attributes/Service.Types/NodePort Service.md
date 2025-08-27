![NodePort](nodeport.png) 
### 📌 **Description**

- A **NodePort Service** exposes your application on a static port (the _NodePort_) on **every node** in your cluster.
- Traffic sent to `<NodeIP>:<NodePort>` will be forwarded to your **Service**, which then routes it to a **Pod**.
- The `NodePort` range is **30000–32767** by default.

### 📌 **When to Choose NodePort**

✅ Use NodePort if you:
- Want to **expose a Service externally** without a cloud LoadBalancer.
- Are running on **bare-metal clusters** or **local setups** (e.g., Minikube, kubeadm).
- Need a **quick, simple way** to access your app from outside.
    
⚠️ But:
- You must **manually manage external access** (e.g., DNS, IPs).
- Limited port range may cause conflicts.
- For production, **LoadBalancer** is usually preferred.

```YAML
apiVersion: v1
kind: Service
metadata:
  name: my-app-nodeport
  labels:
    app: my-app
spec:
  type: NodePort  # Expose service on each node’s IP at a static port
  selector:
    app: my-app   # Match Pods with this label
  ports:
    - protocol: TCP
      port: 80          # Port inside cluster (Service port)
      targetPort: 8080  # Pod container port
      nodePort: 30080   # External port (must be in 30000–32767 range)

```

#NodePort