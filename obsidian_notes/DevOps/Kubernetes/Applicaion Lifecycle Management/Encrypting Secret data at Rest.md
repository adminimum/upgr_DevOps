## 🔐 What it is (short)

- Kubernetes can **encrypt Secrets in etcd** so they aren’t stored as plaintext.
    
- Done by the **API server** using an **EncryptionConfiguration** (AES-CBC/AES-GCM) or a **KMS provider**.
    
- Pods still read Secrets normally; encryption is transparent.
    

---

## ⚙️ Quick steps (kubeadm/control-plane node)

```
# 1) Generate a 32-byte key for AES (base64) head -c 32 /dev/urandom | base64  # 2) Create the encryption config on the control plane sudo vi /etc/kubernetes/encryption-config.yaml```


```# /etc/kubernetes/encryption-config.yaml apiVersion: apiserver.config.k8s.io/v1 kind: EncryptionConfiguration resources: - resources: ["secrets"]   providers:   - aescbc:       keys:       - name: key1         # paste the base64 string from step 1 here         secret: <BASE64_32_BYTES>   - identity: {}   # fallback (keeps ability to read old, unencrypted data)```

```
```# 3) Point kube-apiserver to this file and mount it (kubeadm clusters) sudo vi /etc/kubernetes/manifests/kube-scheduler.yaml   # <-- ignore; wrong file sudo vi /etc/kubernetes/manifests/kube-apiserver.yaml   # <-- edit this one  # Add/ensure this flag under command: # - --encryption-provider-config=/etc/kubernetes/encryption-config.yaml  # And ensure a hostPath volume + volumeMount exist for /etc/kubernetes/encryption-config.yaml # Kubelet will auto-restart the API server.  # 4) Re-encrypt existing Secrets (rewrite them so they’re stored encrypted) kubectl get secrets --all-namespaces -o json | kubectl replace -f -  # 5) (Optional) Verify in etcd (should NOT show plaintext; look for k8s:enc:) # Requires etcdctl and proper certs; command varies by distro.```

---

## 🔁 Key rotation (short)

1. Add a **new key** at the top of `providers.aescbc.keys`.
    
2. Restart API server (if needed).
    
3. Re-encrypt:
    

`kubectl get secrets --all-namespaces -o json | kubectl replace -f -`

4. Remove the **old key**.
    

---

## 🔑 KMS (recommended in prod)

Use an external KMS plugin (Vault, AWS KMS, Azure Key Vault, GCP KMS) instead of raw keys:

```apiVersion: apiserver.config.k8s.io/v1 kind: EncryptionConfiguration resources: - resources: ["secrets"]   providers:   - kms:       apiVersion: v2       name: kms-plugin       endpoint: unix:///var/run/kmsplugin/socket       cachesize: 1000       timeout: 3s   - identity: {}```

> You must deploy the KMS plugin (DaemonSet/Pod) that exposes the socket above.

---

## 📝 Notes

- **Base64 ≠ encryption**: Secrets in manifests are base64, but at rest they’re encrypted only if you enable this feature.
    
- You can also encrypt other resources (e.g., `configmaps`) by adding them to `resources`.
    
- Changes affect **storage in etcd only**; API behavior for clients stays the same.