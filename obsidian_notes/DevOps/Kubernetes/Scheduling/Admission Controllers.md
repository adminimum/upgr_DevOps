# 🗓️ Scheduling Type: Admission Controllers


## 📌 Description

- Admission controllers are plugins in the Kubernetes API server that **intercept requests** before they are persisted in etcd.
- They can **validate** or **mutate** objects (e.g., enforce security policies, add default values, deny requests).
- Two types:
    - **Mutating admission controllers** → modify requests (e.g., add labels, inject sidecars).
    - **Validating admission controllers** → approve or reject requests based on policies.

## ⚙️ Implementation

- Enabled/disabled via API server flags:
    `kube-apiserver --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount`
    
- Common controllers:
    - `NamespaceLifecycle` → prevents deleting default namespaces.
    - `LimitRanger` → enforces resource limits on pods.
    - `MutatingAdmissionWebhook` & `ValidatingAdmissionWebhook` → extend functionality with webhooks.

## ✅ Advantages

- Ensures **policy enforcement** and **security** at the API level.
- Provides **automation** by injecting defaults (e.g., sidecars, resource limits).
- Reduces misconfigurations before they hit the cluster.
- Extensible via **custom admission webhooks**.

## 📋 YAML

```YAML
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: validate-pods
webhooks:
  - name: pod-policy.example.com
    rules:
      - apiGroups: [""]
        apiVersions: ["v1"]
        operations: ["CREATE"]
        resources: ["pods"]
    clientConfig:
      service:
        namespace: default
        name: pod-validator
        path: /validate
      caBundle: <CA_BUNDLE>
    admissionReviewVersions: ["v1"]
    sideEffects: None

```

### 🔖 Tags
`#security` `#kubernetes` `#admission` `#webhooks` `#validation`