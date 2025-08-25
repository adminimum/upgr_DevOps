![Api server](api-server.png)
## 📌 Definition

- What it is: Main central component of cluster that connect all elements of architecture. Provide door for managing cluster and communication between services and systems of the cluster

- How useful it is: 
	1. It’s the **only way** to talk to the cluster.
	2. Ensures **security**, **validation**, and **consistency** of requests
	3. Without it → cluster can’t be managed.

- How to implement:
	1.  Runs as a **pod (kube-apiserver)** on the **control plane node(s)**
	2. Exposes a **REST API** (HTTP/JSON)
	3. Talks to **etcd** (the database) to store and retrieve cluster state

- Simple analogy:
	Think of it like a **bank teller / receptionist**:
	1.  You don’t go directly to the bank vault (etcd).
	2. You go to the **teller (kube-api server)**, ask for something, and they:
			a. check your **identity (auth)**,
			b. make sure your **request makes sense (validation)**,
			c. then pass it to the **system (controllers, etcd)**.

- Problem it solves:
	1. **Single, consistent entry point** for the whole cluster.
	2. Prevents chaos: without it, everyone would poke etcd or nodes directly → unsafe and uncoordinated
	3. Makes Kubernetes **extensible and secure**

  

## 🔗 Related Topics


## 🛠 Commands / Syntax

```bash

# Check health of api server
kubectl get --raw='/healthz'

# List all available api resources
kubectl api-resources

# Check available api version
kubectl api-versions

# Direct request to api server
kubectl get --raw='/api/v1/namespaces/default/pods'

# Check api server config info
kubectl cluster-info

```

  

## List of tasks / Execution

- [] Write script that shows all necessary information about resources in a particular namespace by direct api requests.