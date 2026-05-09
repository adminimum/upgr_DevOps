![storage.png](storage.png)

## 📌 Definition

- **What it is:**  
    Kubernetes **Storage** refers to the set of APIs and mechanisms that allow Pods to persist, share, and manage **data volumes**, even if containers die or move.
    
- **How useful it is:**  
    Containers are **ephemeral** (temporary), but applications often need to **persist data** (e.g. databases, logs, uploads). Kubernetes provides persistent storage that survives Pod restarts, reschedules, and even cluster changes.

## 🔗 Related Topics

- [[Container Storage Interface]]
- [[Volumes]]
- [[persistant volumes]]
- [[persistent volume claims]]
- [[storage class]]