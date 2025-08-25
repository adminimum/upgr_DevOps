![Architecture](images/architecture.webp)

## 📌 Definition

- What it is: **Control plane manages, worker nodes run workloads.**

- How useful it is: Kubernetes architecture is effective because its clear separation of control and worker planes, modular component design, and built-in mechanisms for scalability and fault tolerance allow applications to run reliably, flexibly, and efficiently across clusters of any size

- How to implement: Implementation is always the same from cluster to cluster. It cannot be run with another architecture type.

- Simple analogy: You can use another container orchestrators as you wish.

- Problem it solves: Modular approach provides vital effectiveness for communication through the whole cluster network between all the nodes.

  

## 🛠 Commands / Syntax

### Azure
```bash

# Run cluster in Azure
az aks create \
  --resource-group myResourceGroup \
  --name myAKSCluster \
  --node-count 3 \
  --enable-addons monitoring \
  --generate-ssh-keys

az aks get-credentials --resource-group myResourceGroup --name myAKSCluster

```

### GCP
```bash

# Run cluster in GCP
gcloud config set compute/zone us-central1-a

gcloud container clusters create my-gke-cluster \
  --num-nodes=3 \
  --machine-type=e2-medium

gcloud container clusters get-credentials my-gke-cluster


```


### AWS
```bash

# Run cluster in AWS
aws eks create-cluster \
  --name my-cluster \
  --role-arn arn:aws:iam::<account-id>:role/EKSClusterRole \
  --resources-vpc-config subnetIds=subnet-abc123,subnet-def456,securityGroupIds=sg-0123456789abcdef

aws eks wait cluster-active --name my-cluster

aws eks update-kubeconfig --name my-cluster --region us-east-1

aws eks create-nodegroup \
  --cluster-name my-cluster \
  --nodegroup-name my-nodes \
  --subnets subnet-abc123 subnet-def456 \
  --node-role arn:aws:iam::<account-id>:role/EKSNodeRole \
  --scaling-config minSize=1,maxSize=3,desiredSize=2


```

## 🔗 Related Topics

- [[CRI Container runtime interface]]
- [[ETCD]]
- [[Kube-Api Server]]
- [[Kube-Controller-Manager]]
- [[Kube-sheduler]]

## List of tasks / Execution

- [X]   Manually up healthy kubernetes cluster from 3 bare vm

- [] Run Kubernetes cluster as a service in GCP, check "kubectl describe nodes ..." 