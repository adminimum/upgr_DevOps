![Pod](pod.svg)
## 📌 Definition

- What it is:
  The smallest deployable unit in Kubernetes. A Pod is an abstraction that represents one or more tightly coupled containers that share the same network namespace and storage volumes

- How useful it is:
  Pods allow you to run applications in containers but manage them with Kubernetes features like scaling, self-healing, and networking. They provide the foundation for deploying and running workloads in Kubernetes.

- How to implement:
  You typically define a Pod in a YAML manifest (`pod.yaml`) and create it using `kubectl apply -f pod.yaml`. Example:
  ```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx

  ```

- Simple analogy:
  Think of a **Pod as a small tent** at a festival. Inside the tent (Pod), you may have one person (container) or a small group of people (multiple containers) sharing the same space, electricity, and supplies (network and storage).

- Problem it solves:
  Running raw containers directly doesn’t provide orchestration features like networking, scaling, or lifecycle management. Pods solve this by being the Kubernetes wrapper around containers, allowing them to be scheduled, networked, and managed seamlessly.

- My thoughts:
  Pod is the smallest part of the Kubernetes. It allows to start simple container app with shared resources between them. But it also provides a bunch of different security, safety, advantages.
  

## 🔗 Related Topics

- [[]]

## 🛠 Commands / Syntax

```bash
# List all Pods in the current namespace
kubectl get pods

# List all Pods across all namespaces
kubectl get pods -A

# Describe detailed information about a Pod
kubectl describe pod <pod-name>

# Get logs from a Pod (default container)
kubectl logs <pod-name>

# Get logs from a specific container inside a Pod
kubectl logs <pod-name> -c <container-name>

# Start an interactive shell session inside a Pod
kubectl exec -it <pod-name> -- /bin/bash

# Create a Pod from a YAML file
kubectl apply -f pod.yaml

# Delete a specific Pod
kubectl delete pod <pod-name>

# Delete all Pods in the current namespace
kubectl delete pods --all

# Watch Pods in real-time as they change
kubectl get pods -w

```


## 🗒️ YAML format example with explaining

```YAML
apiVersion: v1                # API version of Kubernetes object
kind: Pod                     # Object type (Pod)
metadata:                      # Metadata about the Pod
  name: my-pod                 # Name of the Pod (must be unique in namespace)
  namespace: default           # Namespace where Pod runs
  labels:                      # Key-value pairs to organize and select Pods
    app: myapp
    tier: backend
  annotations:                 # Extra metadata (non-identifying, e.g. hints, docs)
    description: "Example pod with all fields"
  finalizers:                  # Prevent deletion until conditions are met
    - example.com/finalizer
  ownerReferences:             # Reference to parent object (e.g., Deployment)
    - apiVersion: apps/v1
      kind: ReplicaSet
      name: my-replicaset
      uid: 12345

spec:                          # Pod specification (desired state)
  restartPolicy: Always        # Pod restart behavior: Always, OnFailure, Never
  serviceAccountName: default  # Service account used for API access
  nodeName: node1              # Force scheduling on a specific node
  nodeSelector:                # Match labels on nodes
    disktype: ssd
  affinity:                    # Rules for pod scheduling
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
    podAffinity: {}            # Affinity to other pods
    podAntiAffinity: {}        # Avoid placing with specific pods
  tolerations:                 # Allow scheduling on tainted nodes
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoSchedule"
  hostNetwork: false           # If true, use host's network
  dnsPolicy: ClusterFirst      # DNS policy: Default, ClusterFirst, None, etc.
  dnsConfig:                   # Customize DNS
    nameservers:
      - 8.8.8.8
    searches:
      - mydomain.local
    options:
      - name: ndots
        value: "2"
  terminationGracePeriodSeconds: 30  # Seconds to wait before force kill

  securityContext:             # Security settings for the Pod
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
    seLinuxOptions:
      level: "s0:c123,c456"
    supplementalGroups: [4000]

  volumes:                     # Volumes accessible to containers
  - name: my-volume
    emptyDir: {}               # Ephemeral storage
  - name: config-volume
    configMap:
      name: my-config
  - name: secret-volume
    secret:
      secretName: my-secret

  initContainers:              # Containers run before main containers
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'echo Init container started']
    volumeMounts:
    - name: my-volume
      mountPath: /data

  containers:                  # List of main containers in the Pod
  - name: myapp-container
    image: nginx:1.21           # Container image
    imagePullPolicy: IfNotPresent  # Always / IfNotPresent / Never
    command: ["/bin/sh","-c"]   # Override entrypoint
    args: ["echo Hello World"]  # Arguments for command
    ports:                      # Exposed container ports
    - name: http
      containerPort: 80
      protocol: TCP
    env:                        # Environment variables
    - name: ENV_VAR
      value: "value"
    - name: CONFIG_VALUE
      valueFrom:
        configMapKeyRef:
          name: my-config
          key: setting
    resources:                  # Resource requests and limits
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "500m"
        memory: "512Mi"
    volumeMounts:               # Mount volumes to container path
    - name: my-volume
      mountPath: /usr/share/nginx/html
    readinessProbe:             # Probe for readiness
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 10
    livenessProbe:              # Probe for liveness
      tcpSocket:
        port: 80
      initialDelaySeconds: 15
      periodSeconds: 20
    startupProbe:               # Probe for startup success
      exec:
        command: ["cat", "/tmp/healthy"]
      failureThreshold: 30
      periodSeconds: 10
    lifecycle:                  # Lifecycle hooks
      postStart:
        exec:
          command: ["sh", "-c", "echo PostStart Hook"]
      preStop:
        exec:
          command: ["sh", "-c", "echo PreStop Hook"]

  hostAliases:                  # Custom /etc/hosts entries
  - ip: "127.0.0.1"
    hostnames:
    - "custom.local"

status: {}                      # Current status (set by Kubernetes, not user)
  

```

## List of tasks / Execution

- [] Create a pod with all the possible information set in a yaml config.
- [X] Finish demo practice topic Pod


🏷️ Tags: #pod #config #app #logic #container #yaml