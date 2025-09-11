![Auth](authentic.png)
## 📌 Definition

- What it is:
  Authentication in Kubernetes is the process of confirming the identity of a user, service, or component before they can interact with the Kubernetes API server

- How useful it is:
  It provides the **first security layer** for clusters, making sure that only verified identities can even attempt to perform actions.

- How to implement:
	- Configure API server with supported authentication methods.
	- Use certificates, bearer tokens, or external identity providers (OIDC, LDAP).
	- Applications authenticate via **Service Accounts** (automatically mounted in Pods).

- Simple analogy:
	  Think of Kubernetes authentication as the **ID check at the entrance of a secure building**: if you don’t prove who you are, you won’t even reach the security gates

- Problem it solves:
	  Prevents unknown or unauthorized entities from directly communicating with the API, thereby avoiding cluster compromise.
	  
- Types:
	1. **Static authentication** (basic, for testing)
	    - Username/password file
	    - Static bearer tokens
	2. **Certificates** (x509 client certificates)
	3. **Service Accounts** (JWT tokens for Pods)
	4. **Authentication plugins** (Webhook, OIDC, LDAP, IAM providers)

- Best Approach:
	- For **users**: OIDC (via SSO/identity provider like Google, Keycloak, Azure AD).    
	- For **applications inside cluster**: Service Accounts with RBAC.
	- Avoid static tokens/passwords except for testing.

- My thoughts:
  This is just the secure way to communicate with cluster. Prevent all unexpected accesses for unauthurorized users. 

## 🔗 Related Topics

- [[]]


## 🛠 Commands / Syntax

```bash

# View current user identity from kubeconfig
kubectl config view --minify -o jsonpath='{.users[0].name}'

# Create a service account
kubectl create serviceaccount my-app-sa

# Bind service account to a role
kubectl create clusterrolebinding my-app-sa-binding \
  --clusterrole=view \
  --serviceaccount=default:my-app-sa

# Use client certificate for authentication
kubectl --client-certificate=client.crt --client-key=client.key get pods

```

  

## 🗒️ YAML format example with explaining

```YAML
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-app-sa
  namespace: default
  

```

  

## List of tasks / Execution
-  Choose authentication mechanism for **users** (OIDC, LDAP, certs).
-  Enable API server flags for chosen mechanism (`--oidc-issuer-url`, `--client-ca-file`).
-  Create and assign **Service Accounts** for applications.
-  Bind identities to RBAC roles for authorization.
-  Test authentication flows with `kubectl` or application pods.

  

🏷️ Tags:
#Auth #authentication #certificate #login #user #admin #password