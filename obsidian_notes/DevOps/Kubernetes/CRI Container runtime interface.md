
  
![CRE](images/cre.png)
## 📌 Definition

- What it is: it’s the software that actually runs containers on a host. **Docker or Containerd**. But Docker works through **dockershim** with Kubernetes, because it's not support CRI (imagespec, runtimespec)

- CLIs: docker - **specifically for Docker CRE**, nerdctl - **Likewise docker command, created for containerd, convenient in use** , crictl - **Used by kubelet inside Kubernetes, working with each CRI**, ctr - **Create especially for containerd as default cli tool, better for debugging**

- How useful it is: "nerdctl" useful for working manually, "ctr" or "crictl" best way for debagging. But all container CLI tools are incredibly useful when you need to work with containers before implementing CRI in Kubernetes. 

- How to implement: Download as package on host where there is one of the CRI engines. Automatically in the Kubernetes. 

- Simple analogy: docker cli, ctr, crictl, nerdctl - all analogies for themself 

- Problem it solves: Tools for working with containers when it necessary to perform some actions on containers manually. 

  

## 🛠 Commands / Syntax

```bash

# ctr 

ctr images list
ctr images pull docker.io/library/nginx:latest
ctr images rm docker.io/library/nginx:latest
ctr containers list
ctr run -t --rm docker.io/library/nginx:latest mynginx
ctr tasks list
ctr tasks start mynginx
ctr tasks stop mynginx
ctr exec -t mynginx /bin/bash

# nerdctl
nerdctl images
nerdctl pull nginx:latest
nerdctl rmi nginx:latest
nerdctl ps -a
nerdctl run -it --rm nginx:latest /bin/bash
nerdctl start <container_id>
nerdctl stop <container_id>
nerdctl exec -it <container_id> /bin/bash
nerdctl logs <container_id>

#crictl
crictl ps -a
crictl inspect <container_id>
crictl stop <container_id>
crictl rm <container_id>
crictl images
crictl pull nginx:latest
crictl rmi nginx:latest
crictl runp <pod-config.json>
crictl exec -it <container_id> /bin/sh



```

## 🔗 Related Topics

- [[]]

## List of tasks / Execution

- [] Run nginx container with opened ports via nerdctl, ctr, crictl

- [] Try to go into container through these all CLIs 