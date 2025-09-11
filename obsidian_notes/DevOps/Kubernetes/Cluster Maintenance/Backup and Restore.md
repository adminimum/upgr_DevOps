
## 📌 Definition

- What it is:
  Backup and restore in Kubernetes refers to saving and recovering both cluster state (etcd, manifests, configs) and workloads (Persistent Volumes, Deployments, Secrets, ConfigMaps).

- How useful it is:
  Prevents data loss, enables disaster recovery, and allows migration or rollback

- How to implement:
  Can be done by backing up etcd, using tools like Velero, or storage provider snapshots.

- Simple analogy:
  Like creating a "save point" in a video game—you can return to a working state if something breaks.

- Problem it solves:
  Protects against node failures, accidental deletions, or cluster corruption

- My thoughts:
  It's possibility to restore all data what can be lost during maintenance on the cluster.

  

## 🔗 Related Topics

- [[]]

  

## 🛠 Commands / Syntax

```
kubectl get all -A -o yaml > all_resources_in_one_file.yaml
```
### Etcd backup (control plane node)
```
# Save snapshot
ETCDCTL_API=3 etcdctl snapshot save snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Verify snapshot
ETCDCTL_API=3 etcdctl snapshot status snapshot.db

```

### Etcd restore
```
ETCDCTL_API=3 etcdctl snapshot restore snapshot.db \
  --data-dir /var/lib/etcd-from-backup

# Update kube-apiserver manifest to use restored etcd data-dir
sudo vim /etc/kubernetes/manifests/etcd.yaml
# Replace --data-dir path with /var/lib/etcd-from-backup

# Stop api server

# Change etcd service to indicate path to recovery directory of etcd 
Update --data-dir to use new target location
 --data-dir=/var/lib/etcd-from-backup

 Update new initial-cluster-token to specify new cluster
 --initial-cluster-token=etcd-cluster-1

 Update volumes and volume mounts to point to new path
      volumeMounts:
          - mountPath: /var/lib/etcd-from-backup
            name: etcd-data
          - mountPath: /etc/kubernetes/pki/etcd
            name: etcd-certs
   hostNetwork: true
   priorityClassName: system-cluster-critical
   volumes:
   - hostPath:
       path: /var/lib/etcd-from-backup
       type: DirectoryOrCreate
     name: etcd-data
   - hostPath:
       path: /etc/kubernetes/pki/etcd
       type: DirectoryOrCreate
     name: etcd-certs
```

### Velero backup tool
```
# Install Velero CLI
velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.7.0 \
  --bucket my-backup-bucket --secret-file ./credentials-velero

# Backup all namespaces
velero backup create my-backup --include-namespaces=* 

# Restore backup
velero restore create --from-backup my-backup

```

## 🗒️ YAML format example with explaining

```YAML

  # Velero Backup custom resource example
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: my-backup
spec:
  includedNamespaces:
    - default
    - kube-system
  ttl: 24h0m0s  # backup expiry time


```

  

## List of tasks / Execution
-  Decide backup strategy: etcd-only or full workloads.
-  Install Velero (or another backup tool) for automated backups.
-  Schedule periodic backups.
-  Test restore process on staging.
-  Document disaster recovery procedure.

  

🏷️ Tags:
#snapshot #restore #backup #cluster #safety