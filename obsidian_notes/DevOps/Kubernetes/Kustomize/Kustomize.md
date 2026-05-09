![Kustomize](kustomize.png)

## 📌 Description

**Kustomize** is a built-in Kubernetes tool for customizing raw YAML manifests **without templates**. It uses a layered overlay approach — a base config + environment-specific patches — keeping manifests plain and readable.

## 🛠 Usage / Where

- Manage dev/staging/prod config differences without duplicating YAML.
- Patch existing manifests (e.g. change image tag, replica count) per environment.
- Built into `kubectl` — no extra install needed (`kubectl apply -k`).
- Works well alongside GitOps (ArgoCD, Flux support Kustomize natively).

## ⚡ Advantages

- No templating language — pure YAML overlays.
- Native `kubectl` integration.
- Easier to review changes — diffs are readable YAML patches.
- Great for multi-environment setups (base + overlays).

## ⚠️ Limitations

- Less powerful than Helm for packaging and sharing apps publicly.
- No built-in rollback mechanism.
- Complex patch strategies can get hard to follow.

## 🧰 Key Concepts

| Concept | Description |
|---|---|
| **Base** | The common/shared manifests |
| **Overlay** | Environment-specific patches on top of base |
| **kustomization.yaml** | Entry point — declares resources, patches, generators |
| **Patch** | Strategic merge or JSON6902 patch |
| **namePrefix / nameSuffix** | Add prefix/suffix to all resource names |

## 📋 Example Structure

```
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
└── overlays/
    ├── dev/
    │   └── kustomization.yaml   # patches for dev
    └── prod/
        └── kustomization.yaml   # patches for prod
```

## 🛠 Commands / Syntax

```bash
# Apply with kustomize
kubectl apply -k ./overlays/prod

# Preview rendered output
kubectl kustomize ./overlays/prod

# Build (same as kustomize, outputs to stdout)
kustomize build ./overlays/dev
```

```yaml
# kustomization.yaml example
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - ../../base

patches:
  - path: replica-patch.yaml

images:
  - name: my-app
    newTag: v2.1.0
```

## 🔗 Documentation

- [Kustomize Docs](https://kustomize.io/)
- [kubectl kustomize reference](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)

🏷️ Tags: #kustomize #configuration #overlays #yaml #kubernetes #gitops #k8s
