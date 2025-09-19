![TLS](tls-dia.png)
## 📌 Definition

- What it is:
  TLS (Transport Layer Security) is a cryptographic protocol that ensures secure communication over a network using encryption, authentication, and integrity checks.

- How useful it is:
	- Protects data in transit from eavesdropping (confidentiality).
	- Verifies that communication is with the intended party (authentication).
	- Prevents data tampering or alteration (integrity).

- How to implement:
	-  Generate a private key and a certificate signing request (CSR).
	- Sign the CSR with a trusted Certificate Authority (CA) or self-sign for testing.
	- Deploy the certificate and private key to your server/application.
	- Configure the server to use TLS (e.g., Nginx, Apache, custom app).

- Simple analogy:
  TLS is like sealing a letter in a locked envelope that only the recipient has the key to open. The stamp and signature on the envelope (certificate) prove it really came from the sender.

- Problem it solves:
  Without TLS, attackers can intercept (sniff), modify (man-in-the-middle), or impersonate (spoof) communication.

- How Cert and Key works:
	- **Private Key (.key):** Secret file used to encrypt/sign data. Must never be shared.
	- **Public Certificate (.crt/.pem):** Contains public key + identity info. Shared openly to let others verify your server.
	- **Handshake:** Client verifies server cert → negotiates a session key → communication encrypted with session key.

- Attributes:
	- Subject (CN – Common Name, SAN – Subject Alternative Name)
	- Issuer (CA that signed it)
	- Validity period (Not Before / Not After dates)
	- Public Key
	- Signature Algorithm

- How to sign:
	- **Self-signed:** Cert is signed with its own key (good for testing).
	- **CA-signed:** Cert is signed by trusted authority (e.g., Let’s Encrypt, DigiCert).
	- **Intermediate CA:** Chains trust from root CA → intermediate CA → end-entity cert.

- My thoughts:
  This is a system of encrypting and decrypting information. First - generating pub and priv keys. Then you should sign them as you as a server. Then you send session key to the server or vice versa encrypted with server's public key, validating that it's real server that you need. Then server decrypt this key with its private key, validate your cert and establish private connection with session key.

## 🔗 Related Topics

- [[]]

  

## 🛠 Commands / Syntax / Gen Keys or Certs

```bash

# Generate private key
openssl genrsa -out server.key 2048

# Generate CSR (Certificate Signing Request)
openssl req -new -key server.key -out server.csr -subj "/CN=mydomain.com"

# Self-sign CSR (valid 365 days)
openssl x509 -req -in server.csr -signkey server.key -out server.crt -days 365

# Inspect certificate
openssl x509 -in server.crt -text -noout

# Verify certificate matches private key
openssl x509 -noout -modulus -in server.crt | openssl md5
openssl rsa -noout -modulus -in server.key | openssl md5


```

  

## 🗒️ YAML format example with explaining
Not TLS native, but if used in config files (like web servers, apps, or Kubernetes), you’ll often see

```YAML

  
tls:
  certificate: /etc/ssl/certs/server.crt   # Public certificate file
  privateKey: /etc/ssl/private/server.key  # Private key file
  caCertificate: /etc/ssl/certs/ca.crt     # (Optional) CA cert for verifying peers

```

  

## List of tasks / Execution
-  Generate private key and CSR.
-  Get certificate signed (CA or self-signed).
-  Install cert+key on server.
-  Configure app/web server to use TLS.
-  Test with `openssl s_client -connect host:443`.

  

🏷️ Tags: #TLS #cert #CA #key #secure #ssl #pki 