
## 📌 Definition

- What it is:
  The **Certificates API** (`certificates.k8s.io`) is Kubernetes’ built-in mechanism for requesting, approving/denying, and retrieving **X.509 certificates** via **CertificateSigningRequest (CSR)** objects. CSRs are signed by a configured signer (usually the Kubernetes controller manager) and returned to the CSR’s `status.certificate`.

- How useful it is:
  Lets you issue **client** or **server** certs _inside_ the cluster with RBAC-gated approval, auditability, and automatic kubelet rotation—no external CA scripting needed

- How to implement:
  Create a key + CSR → post a **CSR object** → an approver sets `Approved` (or `Denied`) → the signer issues a cert (respecting `signerName` & `usages`) → read the signed cert from the CSR → store it (e.g., in a `Secret`).

- Simple analogy:
  Think of a CSR object as a ticket at a help desk: you submit the request (CSR), a manager approves it, and the system prints your badge (certificate) onto the ticket

- Problem it solves:
  Safe, RBAC-controlled certificate issuance for workloads, kubelets, and components—without baking long-lived keys into images or running custom CA scripts.

- Attributes:
	- Resource: `CertificateSigningRequest` (cluster-scoped).
	- Key fields: `spec.request` (PEM CSR, base64), `spec.usages`, `spec.signerName`, `status.certificate`.
	- Approval: conditions `Approved`/`Denied`.
	- Common signers:
	    - `kubernetes.io/kube-apiserver-client`
	    - `kubernetes.io/kube-apiserver-client-kubelet`
	    - `kubernetes.io/kubelet-serving`
	    - `kubernetes.io/legacy-unknown` (generic; often used by custom signers)
	- Security: the API server overwrites `spec.username/groups` of the CSR to the **requesting user**, so RBAC on approvals is critical.

- My thoughts:
  It's a possibility to create credentials for managing your cluster (key, cert) pair. You should create key, then cert request by openssl command. Then crate yaml object cert.sing.req and after that you should approve it by kubectl. Get containing info and send it to user.


## 🛠 Commands / Syntax

```bash
# 0) Generate a private key and CSR (client cert example)
openssl genrsa -out app.key 2048
openssl req -new -key app.key -subj "/CN=app-user/O=app-group" -out app.csr

# 1) Create CSR object (see YAML below)
kubectl apply -f app-csr.yaml

# 2) List pending CSRs
kubectl get csr

# 3) Describe one CSR (see requester, usages, signer, conditions)
kubectl describe csr app-csr

# 4) Approve (needs RBAC like 'certificatesigningrequests/approval')
kubectl certificate approve app-csr
#   or deny
# kubectl certificate deny app-csr

# 5) Fetch the issued certificate (PEM) to a file
kubectl get csr app-csr -o jsonpath='{.status.certificate}' | base64 -d > app.crt

# 6) (Optional) Wrap into a TLS Secret for pods/ingress
kubectl create secret tls app-tls --cert=app.crt --key=app.key -n myns

# 7) Server cert (kubelet-serving style) requires SANs in the CSR:
#    Generate with SANs using OpenSSL config:
# openssl req -new -key server.key -subj "/CN=my-svc.myns.svc" \
#   -reqexts v3_req -config <(cat /etc/ssl/openssl.cnf \
#   <(printf "\n[v3_req]\nsubjectAltName=DNS:my-svc.myns.svc,IP:10.0.0.10")) \
#   -out server.csr
# then create CSR with signerName: kubernetes.io/kubelet-serving and usages=server auth

# 8) One-liner to see all issued cert NotAfter dates from CSRs
kubectl get csr -o json | jq -r '
  .items[] | select(.status.certificate) |
  .metadata.name as $n |
  (.status.certificate | @base64d) as $pem |
  "=== \($n) ===\n" + $pem' | awk 'BEGIN{RS="=== "; ORS=""} {if(NR>1){print "=== "$0 | "openssl x509 -noout -enddate -dates -subject"}}' | bash


```

  

## 🗒️ YAML format example with explaining

```YAML
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: app-csr
spec:
  # Base64 of the PEM-formatted CSR (cat app.csr | base64 -w0)
  request: {{BASE64_OF_app.csr}}
  signerName: kubernetes.io/legacy-unknown
  # For client certificates:
  usages:
    - client auth
  # ExpirationSeconds is optional; signer may ignore or cap it
  # expirationSeconds: 31536000
  
  
  LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZqQ0NBVDRDQVFBd0VURVBNQTBHQTFVRUF3d0dZV3R6YUdGNU1JSUJJakFOQmdrcWhraUc5dzBCQVFFRgpBQU9DQVE4QU1JSUJDZ0tDQVFFQTA0N0JNVm9OTmdOZzFmb1hBTmUrV2xTK2gwdFF1RkxwUXhTYTZrNU1aem9vCk9uOXlrK2tWYTJIM2U0RlJsSWVTc2dMak51b1V6dDBKUnh1RFAvY2FqOTYrb2tKWFp3REQyWHJ6M0hlSWtDeE4KVUszUzVsZkR5NXVvd1Z3Q3BYNjVRaitueXNNYUJvQzZZZGtvcisvbHBBZEZidFpQUCswZlhYekM5N3JiVkM3TQpQSnhaZHZBbHZUdCtVZTBKK3ExblhFV1JvMHlGSlB2NS9IQkhTOThEYjF0WHVTZUl3NFJvdDF3T3FmaC9pK1B3CmErVGNXVWFUQ04rOTQ2d3M5NTRVYzBuSzFIcmYzN29ucEwxZUJiN0dIOXZrS2FHMnZzRlVCMnh5NWFaSFBPS28KeXBaTnJMbzNaNk5rL2RsTnkzSnNhUkhxYyt0L1VkVHdkd1hpL3RUOU93SURBUUFCb0FBd0RRWUpLb1pJaHZjTgpBUUVMQlFBRGdnRUJBSll4eUhOT2hKWVpIazJNR1hZdjZGcDIwU2R2WmFLZ2ttZkZLbVZxV1N6Q3J1MGhkRnhSClJHck81bzdJQ0JyNitJZThWWWUySzFsQk5vR05KYmFMcDJneE9RVGo4UXdEU3FnVVJXVWt0MDd5MnZNSGVJRzYKc1NuSysyVDhJaHB0bHhyRHdyMDRtWmg2ZVBVOWFScVp2WHd1L2VkTm1BL0NsOFphZlc2Y2VSY2RQR0UvNkVXOQp0Sm9kanMrdmJXTXhaUStZY3VQZm42TDBBcmdISkFIV1BwNXh0VTJhcm1wOFhqc3laRmdneWpHcWE0ZHg3QnJICnpqWm83OS94dG81VXJjQ2U1bXh5MmUrLzVaUXNSQlRmRkYveU1qa3FsSEQvNGlwdGxzVm9MOFZLZmN1eVhkd0QKTFRFN1RvVkV2T1lBYm5YT1hVWlJZZU1IdkZDUkVLbkd3YTA9Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=

```

  

## List of tasks / Execution
- Generate key + CSR for the identity you need (client/server); include **SANs for server** CSRs.
    
- Create CSR object with correct `signerName` and `usages`.
    
- Have an approver (human or controller) **approve** it (RBAC needed).
    
- Retrieve `status.certificate`, store it securely (often wrap in a `Secret`).
    
- Configure your app/component to use `cert/key` and CA trust.
    
- Set up **renewal** (cron/controller or cert-manager) before expiry.
  

🏷️ Tags:
#cert #key #api #user #access #approve #certificatesigningrequest