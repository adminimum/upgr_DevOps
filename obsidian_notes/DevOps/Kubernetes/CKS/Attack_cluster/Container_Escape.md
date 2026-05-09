# Container Escape

Container escape means **breaking out of the container boundary to gain access to the host node**. Once on the node, the attacker controls all pods running there and can reach the kubelet.

---

## ⚠️ Escape Vectors

### 1. Privileged Container
- `privileged: true` gives the container **all Linux capabilities + access to all host devices**.
- Attacker mounts the host filesystem and chroots into it.

```bash
# Inside a privileged container
mount /dev/sda1 /mnt
chroot /mnt
# Now you're on the host
```

### 2. hostPath Volume Mount
- Mounts a host directory directly into the container.
- If `/` or `/etc` is mounted, attacker reads/writes host files.

```yaml
# Dangerous pod spec
volumes:
  - name: host-root
    hostPath:
      path: /
volumeMounts:
  - mountPath: /host
    name: host-root
```

```bash
# Attacker reads host's sensitive files
cat /host/etc/shadow
cat /host/var/lib/kubelet/pods/<pod>/volumes/kubernetes.io~secret/token
```

### 3. hostPID / hostNetwork / hostIPC
- `hostPID: true` — attacker sees all host processes, can inject into them.
- `hostNetwork: true` — attacker sees host network interfaces, can sniff traffic.
- `hostIPC: true` — attacker shares host IPC namespace, can access shared memory.

```bash
# With hostPID, attacker can nsenter into host namespace
nsenter -t 1 -m -u -i -n -p -- /bin/bash
# Now running in host namespaces
```

### 4. Dangerous Capabilities
- `CAP_SYS_ADMIN` — nearly root, can mount filesystems, change namespaces.
- `CAP_NET_ADMIN` — manipulate host network interfaces.
- `CAP_SYS_PTRACE` — trace/inject into other processes.

### 5. Writable Container Filesystem + Kernel Exploit
- If container runs with unconfined seccomp and no AppArmor, a kernel CVE can escape the container.

---

## 🛡 Defenses (CKS exam focus)

| Attack | Defense |
|---|---|
| Privileged container | `privileged: false`, PodSecurityAdmission `restricted` |
| hostPath | Disallow via OPA/Gatekeeper policy or PSA |
| hostPID/hostNetwork | `hostPID: false`, `hostNetwork: false` in pod spec |
| Dangerous caps | `drop: [ALL]`, only `add` what's needed |
| Kernel exploit | Seccomp profile, AppArmor profile, keep kernel patched |

---

## 🔗 Related

- [[The_Attack]]
- [[API Server Attacks]]
- [[Lateral Movement]]

🏷️ Tags: #cks #attack #container-escape #privileged #hostpath #capabilities #seccomp #apparmor
