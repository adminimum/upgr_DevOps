![Helm](helm.svg)

## 📌 Description

**Helm** is the package manager for Kubernetes. It bundles Kubernetes manifests into reusable, versioned packages called **Charts**, making it easy to install, upgrade, and rollback complex applications.

## 🛠 Usage / Where

- Deploy third-party apps (Prometheus, Nginx, cert-manager) with a single command.
- Manage environment-specific config via `values.yaml` overrides.
- Version-control application deployments and roll back when needed.
- Share internal app configs across teams as private charts.

## ⚡ Advantages

- One command installs an entire stack (chart + dependencies).
- `values.yaml` separates config from templates — easy to customize per environment.
- Built-in rollback: `helm rollback <release>`.
- Large public registry: [Artifact Hub](https://artifacthub.io).

## ⚠️ Limitations

- Charts can become complex and hard to debug.
- Templating syntax (Go templates) has a learning curve.
- Doesn't replace GitOps tools — pairs with ArgoCD/Flux for full lifecycle.

## 🧰 Key Concepts

| Concept | Description |
|---|---|
| **Chart** | Package of Kubernetes manifests + templates |
| **Release** | A deployed instance of a chart |
| **Repository** | Registry of charts (Artifact Hub, private) |
| **values.yaml** | Default config values for a chart |
| **Hooks** | Run jobs at specific points in the lifecycle |

## 🛠 Commands / Syntax

```bash
# Add a repo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Search for a chart
helm search repo nginx

# Install a chart
helm install my-release bitnami/nginx

# Install with custom values
helm install my-release bitnami/nginx -f custom-values.yaml

# List releases
helm list -A

# Upgrade a release
helm upgrade my-release bitnami/nginx --set replicaCount=3

# Rollback
helm rollback my-release 1

# Uninstall
helm uninstall my-release

# Template (dry-run, see rendered manifests)
helm template my-release bitnami/nginx
```

## 🔗 Documentation

- [Helm Docs](https://helm.sh/docs/)
- [Artifact Hub](https://artifacthub.io)

🏷️ Tags: #helm #package-manager #charts #kubernetes #deployment #k8s
