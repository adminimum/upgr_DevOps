## 📌 Definition

- What it is:
  In Docker, `CMD` and `ENTRYPOINT` define what runs inside a container by default. `CMD` sets default arguments, while `ENTRYPOINT` specifies the executable. Additionally, you can override them at runtime using `docker run <image> <command> <args>`.

- How useful it is:
  They control the main process of a container and let you make containers flexible or fixed in behavior depending on how you design them.

- How to implement:
  In a `Dockerfile`, use either:
  `CMD ["arg1", "arg2"]` (default parameters).
  `ENTRYPOINT ["executable", "param1"]` (fixed entry point).
  Combine both, where `ENTRYPOINT` is fixed and `CMD` provides default but override-able args.

- Simple analogy:
  Think of `ENTRYPOINT` as the program (like `python`), and `CMD` as its default input (like `app.py`). You can replace the input when you run the container, but the program remains the same.

- Problem it solves:
  It ensures containers start consistently with the right program while still giving flexibility to override commands without rebuilding images.

- My thoughts:
  It's a simple feature that let us predefine way to run container and if it's needed we can replace some of the arguments.
  
- In Kubernetes:
  CMD is overwritten as a spec.containers.args: [] form, and ENTRYPOINT is overwritten as a spec.containers.command: [] syntax. So chose carrifuly.

## 🔗 Related Topics

- [[]]

  

## 🛠 Commands / Syntax

```bash

# Run container overriding CMD
docker run my-image echo "Hello World"

# Run container overriding both ENTRYPOINT and CMD
docker run --entrypoint /bin/bash my-image -c "echo Hello"

# Inspect entrypoint and cmd of an image
docker inspect --format='{{.Config.Entrypoint}} {{.Config.Cmd}}' my-image


```

  

## 🗒️ YAML format example with explaining

```YAML

  apiVersion: v1
kind: Pod
metadata:
  name: cmd-args-example
spec:
  containers:
  - name: demo
    image: ubuntu:20.04
    command: ["echo"]         # Equivalent to ENTRYPOINT, overrides default command
    args: ["Hello", "World"]  # Equivalent to CMD, passes arguments


```

## List of tasks / Execution

- Write a Dockerfile using `CMD` only.
- Write a Dockerfile using `ENTRYPOINT` + `CMD`.
- Run a container overriding `CMD` arguments.
- Run a container overriding `ENTRYPOINT`.
- Test the same behavior in Kubernetes with `command` and `args`.

  

🏷️ Tags: #cmd #docker #command #entrypoint #params