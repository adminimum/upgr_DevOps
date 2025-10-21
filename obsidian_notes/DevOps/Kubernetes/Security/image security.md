## 📌 Definition

- What it is:
  Image security in Kubernetes refers to the practices and mechanisms used to ensure that container images used in pods are safe, verified, and free from vulnerabilities or malicious code.

- How useful it is:
  Securing container images is essential to prevent supply-chain attacks, reduce vulnerabilities, and ensure compliance and integrity in your Kubernetes workloads

- Main details:
	- Images should be scanned for known vulnerabilities (CVEs).
	- Use only **trusted sources** or **private registries**.
	- Implement **ImagePullPolicies** and **Admission Controllers**.
	- Enable **runtime security** (e.g. seccomp, AppArmor).
	- Verify **image signatures** (e.g. Cosign + Sigstore).
	- Avoid using `latest` tags and favor **immutable tags**.

- How to implement:
	- Use scanners like **Trivy**, **Clair**, **Anchore**, or **Snyk** in your CI/CD pipeline.
	- Enable **Notary** or **Cosign** for signature verification.
	- Use **Kubernetes PodSecurityPolicies** or **OPA Gatekeeper** to enforce image rules.
	- Limit image pull access via **RBAC** and **network policies**.
	- Run containers as **non-root** users whenever possible.

- Simple analogy:
  Just like you wouldn’t install random software on your computer, you shouldn't deploy random or unverified images to your cluster — they might contain malware or open doors for attackers.

- Problem it solves:
	- Prevents unauthorized or malicious containers from running.
	- Reduces exposure to known vulnerabilities.
	- Increases control and traceability over workloads.
	- Helps meet compliance and audit standards.

- Attributes:
	- CVE scanning
	- Signature verification
	- Least privilege
	- Policy enforcement
	- Registry access control

- My thoughts:
  It's the way to verify that images in your deployments and pods are valid or secured.
  The best way is to create secret for private repository and use this secret in your yaml manifests to pull images from private registry. 

## 🛠 Commands / Syntax

```bash
# Scan an image with Trivy
trivy image nginx:1.21

# Verify image signature using Cosign
cosign verify ghcr.io/your-org/your-image

# Pull from private registry with credentials
kubectl create secret docker-registry regcred \
  --docker-server=your-registry.io \
  --docker-username=your-user \
  --docker-password=your-pass \
  --docker-email=your-email

# Apply image policy with Kyverno or Gatekeeper (example template)

```

  

## 🗒️ YAML format example with explaining if needed

```YAML

# Example: Pod using a verified image and non-root user
apiVersion: v1
kind: Pod
metadata:
  name: secure-nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.21.6
    securityContext:
      runAsUser: 1000
      runAsNonRoot: true
      readOnlyRootFilesystem: true
    imagePullPolicy: IfNotPresent
  imagePullSecrets:
  - name: regcred


```

  

## List of tasks / Execution
-  Integrate image scanning in CI/CD (Trivy or Snyk)
-  Set up Cosign for image signing/verification
-  Enforce pull from trusted registries onl
-  Create AdmissionPolicy (OPA / Kyverno)
-  Remove all uses of `latest` tag
-  Enforce runAsNonRoot for all workloads

🏷️ Tags:
#image #security #imagehub #docker #private #pull