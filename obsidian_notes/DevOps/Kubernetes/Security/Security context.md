## 📌 Definition

- What it is:
  `securityContext` in Kubernetes defines the **security settings** (permissions, user IDs, capabilities, privilege levels) for a **pod or container**. It controls how containers run and what they’re allowed to do.

- How useful it is:
  It helps enforce the **principle of least privilege**, improves cluster security, and protects against container escapes or privilege escalation.

- Main details:
	- Can be set at **Pod level** or **Container level**.
	- Defines settings like:
	    - `runAsUser`, `runAsGroup`, `runAsNonRoot`
	    - `privileged` (should be false)
	    - `allowPrivilegeEscalation`
	    - `readOnlyRootFilesystem`
	    - Linux capabilities (e.g. `capAdd`, `capDrop`)
	- Works together with PodSecurityStandards (baseline, restricted).

- How to implement:
  Add a `securityContext` block in your pod or container spec, setting rules that define what the process inside the container can or cannot do.

- Simple analogy:
  Like setting **user permissions and safety locks** for each program on your computer — you decide who runs it, what files it can touch, and whether it can act as an administrator.

- Problem it solves:
  Prevents containers from running as root or gaining unwanted privileges, reducing the risk of attacks or misconfigurations

- Attributes:
	- Least privilege
	- Non-root execution
	- Capability control
	- Filesystem protection

- My thoughts:
  This is just an option to run container or pod as non-root user. Wether add or remove modules of system.

## 🛠 Commands / Syntax

```bash

# View pod security context
kubectl get pod mypod -o yaml | grep securityContext -A 10

# Apply a YAML with security context
kubectl apply -f secure-pod.yaml


```

  

## 🗒️ YAML format example with explaining if needed

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsUser: 1000          # Run as non-root user ID
    fsGroup: 2000            # Group ID for mounted volumes
  containers:
  - name: app
    image: nginx:1.21
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      runAsNonRoot: true
      capabilities:
        drop: ["ALL"]

  

```

  

## List of tasks / Execution
-  Enforce `runAsNonRoot` for all workloads
-  Disable privilege escalation in all containers
-  Use read-only file systems
-  Drop unnecessary capabilities

  
🏷️ Tags:
#non-root #security #context #user #group #runas