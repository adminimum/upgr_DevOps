
## 📌 Definition

- What it is:
  Creating X.509 certificates (and their private keys + CA chain) for Kubernetes components and workloads, then surfacing them to pods (typically via Secrets) so traffic is **encrypted** (TLS) and optionally **authenticated** (mTLS).

- How useful it is:
		- Encrypts data in transit (ingress, service-to-service, webhooks).
		- Proves identity (servers to clients; clients to servers with mTLS).
		- Enables browsers/trust stores to accept your endpoints without warnings.
		- Satisfies compliance (PCI/HIPAA/SOC2 “encryption in transit”).

- How to implement:
	1. **Manual**: `openssl` → create CA, sign CSRs → store as `kubernetes.io/tls` Secrets.
	2. **K8s CSR API**: submit `CertificateSigningRequest` → cluster CA or external approver signs.
	3. **cert-manager** (recommended): declarative `Certificate` + `Issuer/ClusterIssuer` → auto-provision/rotate (self-signed, internal CA, or ACME/Let’s Encrypt).

- Simple analogy:
	Think of a **passport** (certificate) issued by a **government** (CA). Servers show passports; clients verify the government’s signature. With **mTLS**, both sides show passports.
	
- Problem it solves:
	Authenticity (who am I talking to?), confidentiality (no eavesdropping), integrity (no tampering), and _automation of renewals_.
	
- Attributes:
	CN/SANs, key type/size (RSA-2048/3072 or ECDSA P-256), validity/rotation, key usage (serverAuth/clientAuth), CA chain, revocation strategy (usually rotate/replace in K8s), storage (Secrets).
	
- My thoughts:
	It's the most difficult topic I've ever met about k8s, but the main idea of the certificates in cluster is that they need to provide secure connection between all communicating object. Moreover there should be one main cert+key group, that sign all the other certs to prove they are correct and secure.
  

## 🔗 Related Topics

- [[TLS in kubernetes]]

## 🛠 List of actions

```bash
## 🧩 Certificate Creation Checklist

1. **Create PKI directories**  
    `/etc/kubernetes/pki` and `/etc/kubernetes/pki/etcd`
    
2. **Create cluster CA (root CA)**
    
    - Generate `ca.key` and `ca.crt`
        
    - Stored in `/etc/kubernetes/pki/`
        
3. **Create kube-apiserver server certificate**
    
    - SANs: cluster DNS + control-plane IPs + Service IP (10.96.0.1)
        
    - Files: `apiserver.key`, `apiserver.crt`
        
    - Signed by cluster CA
        
4. **Create apiserver–kubelet client certificate**
    
    - CN: `kube-apiserver-kubelet-client`, O: `system:masters`
        
    - Files: `apiserver-kubelet-client.key`, `.crt`
        
    - Signed by cluster CA
        
5. **Create controller-manager client certificate**
    
    - CN: `system:kube-controller-manager`
        
    - Files: `controller-manager.key`, `.crt`
        
6. **Create scheduler client certificate**
    
    - CN: `system:kube-scheduler`
        
    - Files: `scheduler.key`, `.crt`
        
7. **Create kube-proxy client certificate**
    
    - CN: `system:kube-proxy`
        
    - Files: `kube-proxy.key`, `.crt`
        
8. **Create front-proxy CA**
    
    - Files: `front-proxy-ca.key`, `.crt`
        
    - Stored in `/etc/kubernetes/pki/`
        
9. **Create front-proxy client certificate**
    
    - CN: `front-proxy-client`
        
    - Files: `front-proxy-client.key`, `.crt`
        
    - Signed by front-proxy CA
        
10. **Create Service Account keypair**
    
    - Files: `sa.key`, `sa.pub`
        
    - RSA 2048 bits
        
11. **Create etcd CA**
    
    - Files: `/etc/kubernetes/pki/etcd/ca.key`, `.crt`
        
12. **Create etcd server certificate (per control-plane node)**
    
    - CN = hostname
        
    - Files: `server.key`, `.crt`
        
    - Signed by etcd CA
        
13. **Create etcd peer certificate (per control-plane node)**
    
    - CN = hostname
        
    - Files: `peer.key`, `.crt`
        
    - Signed by etcd CA
        
14. **Create etcd healthcheck client certificate**
    
    - CN: `kube-etcd-healthcheck-client`
        
    - Files: `healthcheck-client.key`, `.crt`
        
    - Signed by etcd CA
        
15. **Create apiserver–etcd client certificate**
    
    - CN: `kube-apiserver-etcd-client`
        
    - Files: `apiserver-etcd-client.key`, `.crt`
        
    - Signed by etcd CA
        
16. **Create kubelet client certificate (per node)**
    
    - CN: `system:node:<node-name>`, O: `system:nodes`
        
    - Files: `/var/lib/kubelet/pki/kubelet-client.key`, `.crt`
        
17. **Create admin client certificate**
    
    - CN: `kubernetes-admin`, O: `system:masters`
        
    - Files: `admin.key`, `.crt`
        
18. **Set permissions**
    
    - `.key` → `chmod 600`
        
    - `.crt` → `chmod 644`
        
19. **Verify structure**
```

  

## 🗒️ directory tree

```YAML
/etc/kubernetes/pki/
  ├── ca.{crt,key}
  ├── apiserver.{crt,key}
  ├── apiserver-kubelet-client.{crt,key}
  ├── controller-manager.{crt,key}
  ├── scheduler.{crt,key}
  ├── kube-proxy.{crt,key}
  ├── front-proxy-ca.{crt,key}
  ├── front-proxy-client.{crt,key}
  ├── sa.{key,pub}
  └── etcd/
      ├── ca.{crt,key}
      ├── server.{crt,key}
      ├── peer.{crt,key}
      ├── healthcheck-client.{crt,key}
      └── apiserver-etcd-client.{crt,key}
  

```

  

## List of tasks / Execution

- Renew all  the certificates in cluster

  

🏷️ Tags: 
#tls #certificate #key #security #dif10 #signing