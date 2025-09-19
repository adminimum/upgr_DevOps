  ![Certs](certif.png)

![TLSINKUBE](tlskube.jpg)
## 📌 Definition

- What it is:
  TLS in Kubernetes secures communication between components (API server, kubelets, etcd, controllers) and between workloads (Pods, Services, Ingress). It uses X.509 certificates for encryption and authentication.

- How useful it is:
	- Ensures API requests and cluster communication are encrypted.
	- Verifies identity of clients/servers via certificates.
	- Protects sensitive cluster data in transit.

- How to implement:
	- Certificates are issued (self-signed by Kubernetes CA or external CA).
	- Kubernetes components (API server, kubelet, etcd) are configured with cert/key pairs.
	- For workloads, Secrets or cert-manager are used to provide TLS certs to Pods/Ingress.

- Simple analogy:
  It’s like requiring an ID badge to enter every building inside a secure campus. The badge (cert) proves who you are, and doors only open for valid holders.

- Problem it solves:
  Prevents man-in-the-middle attacks, impersonation of services, and eavesdropping on sensitive cluster communications.

- Attributes:
	- Certificate Authority (CA) inside cluster.
	- Component certs (API server, kubelet, controller-manager, scheduler, etcd).
	- Expiry and rotation policies (certs usually last 1 year by default).
	- Client certificates for authentication (`kubectl` uses `~/.kube/config`).

- My thoughts:
  This system of certificates storing and using certs let us be calm that nothing can engage into a network communication process between nodes, services.

  

## 🔗 Related Topics

- [[TLS Basics]]

  

## 🛠 Commands / Syntax

```bash

# View cluster certificates expiry
kubeadm certs check-expiration

# Renew all control plane certificates
sudo kubeadm certs renew all

# Generate a new certificate and key (example)
openssl req -newkey rsa:2048 -nodes -keyout apiserver.key -out apiserver.csr -subj "/CN=kube-apiserver"

# Approve a CSR in Kubernetes (if a component requests new certs)
kubectl certificate approve <csr-name>


```

  

## 🗒️ YAML format example with explaining

```YAML
apiVersion: v1
kind: Secret
metadata:
  name: tls-secret
  namespace: default
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded-cert>   # Public certificate
  tls.key: <base64-encoded-key>   # Private key

  

```

  

## List of tasks / Execution
-  Check current cluster certificates with `kubeadm certs check-expiration`.
-  Renew or rotate expiring certificates.
-  Store app TLS certs as Kubernetes Secrets.
-  Configure Ingress with TLS Secret for HTTPS.
-  Consider automating cert issuance with **cert-manager**.

  

🏷️ Tags:
#certs #kubersecurity #tls #key #generate #ssl #openssl #renew