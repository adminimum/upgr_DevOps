```bash

# 1. Check api manifest and locations of all certificates
cat /etc/kubernetes/manifests/kub-apiserver.yaml

# 2. Check each cert by command to get output of them. Then check expiration and SAN (Subject Alternative Name), organization 
openssl x509 -in /...crt -text -noout

# 3. check logs of etcd
journalctl -u etcd.service -l

# 4. If not works 3 check logs directly from container by using cri tools

crictl ps -a

# 4 command to check all certs in cluster
kubectl certificate approve --kubeconfig admin.kubeconfig $(kubectl get csr --kubeconfig admin.kubeconfig -o json | jq -r '.items | .[]  | select(.spec.username == "system:node:node02") | .metadata.name')

```