sudo apt update && sudo apt upgrade -y
sudo apt install -y curl apt-transport-https ca-certificates gnupg lsb-release software-properties-common


// sudo hostnamectl set-hostname k8s-worker-1
// sudo hostnamectl set-hostname k8s-worker-2

sudo swapoff -a
sudo sed -i '/ swap / s/^/#/' /etc/fstab


cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
overlay
EOF

sudo modprobe br_netfilter
sudo modprobe overlay


cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

sudo sysctl --system


sudo apt install -y containerd

# Настроим конфиг:
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml > /dev/null

# Включим SystemdCgroup (очень важно):
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# Перезапуск:
sudo systemctl restart containerd
sudo systemctl enable containerd


sudo mkdir -p /usr/share/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/kubernetes-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl


kubeadm version
kubelet --version
containerd --version


# Example   kubeadm init command
kubeadm join 10.240.0.11:6443 --token dalk8k.v27z2vbubg65yyay \
	--discovery-token-ca-cert-hash sha256:c2a603531a7efd7735b35d962ab75852bd6609ace83391e86df2e3e6cf3b445a