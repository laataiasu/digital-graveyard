---
date: 1970-01-01
---

# Kubernetes Pods, Deployments, Services, Namespaces, & DaemonSets

## Pods: The Atoms of Kubernetes

### Kubernetes Pods

#### What is a Pod?
- **Pod**: The smallest unit of scheduling in Kubernetes.
- A **pod** can contain one or more containers.
- Pods are a shared execution environment that includes:
  - Shared **storage** (volumes).
  - Shared **network resources** (IP address, ports).
  - **Execution specifications** for the containers (how to run them).
  
#### Pod with a Single Container
- A pod can run just one container (this is the most common use case).
- In this case, the pod essentially wraps the single container.

#### Pod with Multiple Containers
- A pod can also contain multiple containers that are tightly coupled and need to share resources (e.g., storage or network).
- These containers are complementary and run together to form a single unit of service.
- Containers in a pod:
  - Are scheduled to run on the same physical or virtual machine.
  - Share the same **network namespace** and **storage**.
  
#### Container Runtimes
- Kubernetes supports multiple container runtimes.
- **Docker** is the most commonly used runtime.
- Other runtimes must adhere to the **Container Runtime Interface (CRI)**.
- In Kubernetes, pods are similar to groups of Docker containers with shared namespaces and filesystem volumes.

#### Pod Execution Environment
- Pods are based on **Linux namespaces** and **cgroups**:
  - **Namespaces** provide isolation for networking, processes, and more.
  - **Cgroups** limit and isolate resource usage (CPU, memory, etc.) for processes.
  
- Pods ensure containers are:
  - **Co-located**: Run on the same node.
  - **Co-scheduled**: Managed together.

#### Init Containers
- **Init containers** are special containers in a pod that run before any app containers.
- They are used for initialization tasks (e.g., setting up configuration, loading data).

#### Ephemeral Containers
- **Ephemeral containers** are temporary containers used for debugging purposes.
  
#### Pod Lifecycle and Scheduling
- Pods are **transient** and **disposable**.
- A pod is scheduled to a node until it completes or is deleted due to a resource issue or node failure.
- When a pod fails or is evicted:
  - A **controller** will create a replacement pod and schedule it on a healthy node.

#### Pod Templates and Controllers
- **Pod Template**: A specification used to create pods.
- **Controllers** like **Deployments**, **Jobs**, and **DaemonSets** use pod templates to manage pods.
- Controllers don’t update existing pods but instead create new ones with updated pod templates when changes are made.

#### Direct Pod Management
- While typically pods are managed indirectly via controllers, you can update some fields of a running pod directly (with limitations).
  - **Immutable fields**: Some fields like the pod name or namespace cannot be changed after creation.
  
#### Volumes and Shared Storage
- Pods can have **shared storage volumes** that are accessible by all containers within the pod.
- Volumes ensure **data persistence** even if a container is restarted.
  
#### Networking in Pods
- Each pod has a unique **IP address**.
- Containers within the same pod share the same network namespace:
  - They share the **IP address** and **ports**.
  - They can communicate with each other using **localhost** or **IPC** (Inter-Process Communication).
  
- Pods communicate externally using **IP networking**. For example, containers in different pods communicate using the pod’s IP address.

#### Privileged Containers
- Containers can be run in **privileged mode** by setting the `privileged` flag in the container’s security context.
- This allows containers to perform **system-level operations**, such as accessing hardware.

#### Static Pods
- **Static Pods** are managed outside the Kubernetes API server.
- They are primarily used for running components like the self-hosted control plane.
- Each static pod is tied to a **specific node** and managed by the **kubelet**.
- The kubelet is responsible for restarting static pods if they fail.

## The Life of a Pod

### Life of a Pod

#### Pod Lifecycle Overview
- **Pods are ephemeral**: They are short-lived or transient entities.
  - They **do not self-heal**: If a pod fails or is evicted (due to resource issues or node maintenance), it is **deleted** and **not rescheduled**.
  - If a pod fails or is deleted, a **new pod** will be created to replace it.
  
#### Pod Assignment and Deletion
- When a pod is created, it is assigned a **unique ID (UID)** and scheduled to a node.
  - The pod stays on that node until it is **terminated** or **deleted**.
- **Objects within a pod**, such as volumes, have the same lifetime as the pod.
  - If the pod is deleted, the associated objects (e.g., volumes) are also deleted.
  - If the pod is recreated, new objects (e.g., volumes) are created as well.

#### Pod Status and Phases
Each pod has a **PodStatus** object, which includes a **phase field** that describes the pod's state. The phase provides a high-level summary of the pod's lifecycle but does not capture all details about the container or pod state.

##### Possible Pod Phases:
1. **Pending**: 
   - The pod has been accepted by the cluster (stored in etcd).
   - At least one container has not been set up or is still being downloaded.
   - The pod may be waiting to be scheduled or for images to download.
   
2. **Running**:
   - The pod has been successfully scheduled to a node.
   - All containers in the pod are running and created by the kubelet.

3. **Succeeded**:
   - All containers in the pod have successfully terminated.
   - No containers will be restarted.

4. **Failed**:
   - All containers in the pod have terminated, but at least one container failed.

5. **Unknown**:
   - The API server cannot determine the state of the pod (typically due to communication issues with the kubelet).

#### Container States within Pods
Each container within a pod has its own state. The container state can be tracked independently of the pod's state.

##### Possible Container States:
1. **Waiting**:
   - The container is waiting to complete startup operations, such as downloading images.
   - A `reason` field provides details about why the container is waiting.

2. **Running**:
   - The container is up and running without issues.
   - The `kubectl` output includes the timestamp of when the container started running.

3. **Terminated**:
   - The container has either completed its execution or failed.
   - The `kubectl` output includes the reason for termination, the exit code, and start/finish times.

#### Restart Policy for Pods
Each pod has a **restart policy** that dictates how Kubernetes responds when containers exit.

- **Always**: Kubernetes will always attempt to restart a container after it exits, regardless of success or failure.
- **OnFailure**: Kubernetes will attempt to restart the container only if it exits with a failure (non-zero exit code).
- **Never**: Kubernetes will not restart a container once it has exited, regardless of the exit code.

##### Use Cases for Restart Policies:
- **OnFailure** or **Never**: Used for pods running batch processes that are expected to terminate after completing their tasks.
- **Always**: Used for pods running services, like web servers, where the container should always be restarted, even if it fails.

#### Pod Conditions
A pod's **PodStatus** includes several **PodConditions** that track the pod's readiness at various stages.

##### Pod Condition Types:
1. **PodScheduled**: The pod has been successfully scheduled to a node.
2. **ContainersReady**: All containers in the pod are ready.
3. **Initialized**: All init containers have started successfully.
4. **Ready**: The pod is ready to serve requests.

Each condition includes:
- **Type**: The name of the condition (e.g., `PodScheduled`).
- **Status**: The condition's status (`True`, `False`, or `Unknown`).
- **LastProbeTime**: The timestamp of the last condition probe.
- **LastTransitionTime**: The timestamp of the last status change for the condition.
- **Message**: A description of the last status transition.

## Allocating Resources

### Allocating and Restricting Resources for Containers

In Kubernetes, you can specify resource **requests** and **limits** for containers within a pod. The most commonly specified resources are **CPU** and **memory**.

#### Key Concepts:
- **Resource Request**: Specifies the minimum amount of a resource (like CPU or memory) that a container must have to run. Kubernetes guarantees this amount when scheduling the pod.
- **Resource Limit**: Specifies the maximum amount of a resource that a container can consume. Kubernetes ensures that containers do not exceed this limit.

### Step-by-Step Demo

1. **Set Up Aliases**:
   - Create an alias for `kubectl` to shorten the command:
     ```bash
     alias k=kubectl
     ```
   - Create another alias for clearing the terminal:
     ```bash
     alias c=clear
     ```

2. **Create a Namespace**:
   To isolate demo resources, create a new namespace:
   ```bash
   k create namespace demo
   ```

3. **Create a Pod with Resource Requests and Limits**:
   Open a text editor and create the following YAML manifest for a pod called `demo-ram`. This pod uses the `polinux/stress` image and sets both memory **requests** and **limits**.

   **YAML Manifest: `demo-ram.yaml`**:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: demo-ram
     namespace: demo
   spec:
     containers:
     - name: demo-ram
       image: polinux/stress
       resources:
         limits:
           memory: "250Mi"
         requests:
           memory: "50Mi"
       command: ["stress"]
       args:
         - "--vm"
         - "1"
         - "--vm-bytes"
         - "100M"
         - "--vm-hang"
         - "0"
   ```

4. **Apply the Pod YAML**:
   Apply the manifest to create the pod:
   ```bash
   k apply -f demo-ram.yaml
   ```

5. **Verify Pod Creation**:
   Check the pod status:
   ```bash
   k get po --namespace=demo
   ```
   If successful, the pod will be in the **Running** state.

6. **Check Pod Resource Usage**:
   To inspect resource usage, access the node where the pod is running (e.g., `worker2`). Use Docker to see the stats for the container:
   ```bash
   sudo docker ps
   sudo docker stats <container_id>
   ```

   In the stats output, you should see that the memory usage is around **100Mi**, which is within the allocated limits.

7. **Modify the Pod to Exceed Memory Limit**:
   Edit the pod YAML to request more memory than allowed by the limit (e.g., 400Mi). Update the `args` section in the YAML to request 400Mi:
   ```yaml
   args:
     - "--vm"
     - "1"
     - "--vm-bytes"
     - "400M"
     - "--vm-hang"
     - "0"
   ```

8. **Apply the Updated Pod**:
   Apply the updated YAML:
   ```bash
   k apply -f demo-ram.yaml
   ```

9. **Monitor Pod Status**:
   Get the pod status again:
   ```bash
   k get po demo-ram --namespace=demo
   ```

   The pod will show a **CrashLoopBackOff** status because it attempted to exceed the memory limit.

   - The pod will eventually be **OOMKilled** (out of memory killed) because it requested more memory than allowed.

10. **Delete the Pod**:
    Delete the pod:
    ```bash
    k delete po demo-ram --namespace=demo
    ```

### CPU Resource Allocation

1. **Create a Pod with CPU Limits**:
   Create another YAML manifest for a pod called `demo-cpu` using the `vish/stress` image. This pod requests more CPU than the node can provide.

   **YAML Manifest: `demo-cpu.yaml`**:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: demo-cpu
     namespace: demo
   spec:
     containers:
     - name: demo-cpu
       image: vish/stress
       resources:
         limits:
           cpu: "1.0"
         requests:
           cpu: "4.5"
       args:
         - "--cpu"
         - "4"
   ```

2. **Apply the CPU Pod YAML**:
   Apply the new pod configuration:
   ```bash
   k apply -f demo-cpu.yaml
   ```

3. **Verify Pod Creation**:
   Check the pod's status:
   ```bash
   k get po demo-cpu --namespace=demo
   ```
   The pod will be **Running**.

4. **Inspect Resource Usage on Worker Node**:
   Access the worker node (`worker1`) where the pod is running and check the CPU usage with Docker stats:
   ```bash
   sudo docker ps
   sudo docker stats <container_id>
   ```

   You should see that the CPU usage is capped at **1.0 CPU unit** despite requesting **4.5 CPU units**. Kubernetes throttles the container to respect the `cpu: "1.0"` limit.

5. **Clean Up**:
   Once you're done, delete the `demo` namespace to clean up all resources:
   ```bash
   k delete namespace demo
   ```

### Summary of Resource Requests and Limits:
- **Requests** guarantee the minimum resources required for a container.
- **Limits** define the maximum resources a container can use.
- **CPU Limits** are enforced by throttling the container, while **memory limits** can lead to termination (OOMKilled) if exceeded.
- Containers are scheduled based on resource requests, and Kubernetes ensures that containers do not exceed their resource limits.

This demo illustrates how Kubernetes can control and manage the resources allocated to containers, ensuring both performance and stability within a cluster.

## Kubernetes Namespaces

### Kubernetes Namespaces Overview

In Kubernetes, **namespaces** provide a way to partition a single physical cluster into multiple virtual clusters, allowing you to isolate resources and manage large-scale environments more effectively. They are useful in scenarios where you have many users, teams, or projects that need to share the same cluster but require isolation for resource management, security, and access control.

Here’s a breakdown of Kubernetes namespaces:

---

### **What are Kubernetes Namespaces?**

- **Logical Partitioning**: Namespaces are essentially **logical partitions** within a Kubernetes cluster. They allow you to isolate and organize resources like pods, services, and deployments within a single cluster.
- **Resource Scope**: Each resource in Kubernetes (such as a pod, service, or deployment) belongs to exactly one namespace. Resource names must be unique within a namespace, but they don’t have to be unique across namespaces.
- **No Nesting**: Namespaces cannot be nested. That is, you can't have a namespace within another namespace.
- **Isolation**: Namespaces are primarily used to isolate groups of resources within a cluster, especially when dealing with many teams or projects. However, namespaces are **not** a strict security boundary; they don’t provide full isolation in terms of security unless additional configurations like **NetworkPolicies** or **RBAC (Role-Based Access Control)** are applied.

### **When to Use Multiple Namespaces**

Namespaces are ideal in the following scenarios:

1. **Multiple Teams or Projects**: If your cluster is shared by many teams or projects, namespaces help to ensure each team or project can work within its own space without affecting others.
2. **Large Scale Environments**: In large environments with many users or a complex architecture, namespaces provide logical segmentation.
3. **Multi-Tenancy**: If you're supporting multiple tenants or user groups within a single Kubernetes cluster, namespaces allow each tenant to have its own isolated space for resources.

However, namespaces **should not** be used to differentiate similar resources that only slightly differ, such as different software versions. In such cases, it's better to use **labels** and **selectors** within a single namespace to manage those resources.

---

### **System Namespaces vs User-Created Namespaces**

Kubernetes automatically creates several system namespaces when a cluster is first set up. These are critical for the internal operation of Kubernetes and should not be modified or deleted by users:

1. **`default`**:
   - This is the default namespace for resources that don’t have any other namespace specified. If you create a resource without specifying a namespace, it will go into the `default` namespace.

2. **`kube-system`**:
   - This namespace is used by Kubernetes for **system-related resources**. These include things like core Kubernetes components (e.g., `kube-dns`, `kube-proxy`, etc.) and infrastructure-related resources.
   - It’s reserved for Kubernetes internal services and should not be used by users.

3. **`kube-public`**:
   - This namespace is **publicly readable**. It can be accessed by all users, including unauthenticated users.
   - It's typically used for resources that should be visible to all users in the cluster, such as public information or shared configuration.

4. **`kube-node-lease`**:
   - This namespace is used for **node heartbeat monitoring**. Kubernetes uses it to track node health and determine whether nodes are healthy or have failed.
   - It’s primarily for internal Kubernetes use and isn’t meant for user-created resources.

### **Creating and Managing Namespaces**

To manage namespaces in Kubernetes, you use the `kubectl` command. Here are some common commands:

1. **List all namespaces**:
   ```bash
   kubectl get namespaces
   ```
   This command will show you a list of all the namespaces in your cluster.

2. **Create a new namespace**:
   You can create a new namespace by applying a YAML manifest or directly using the `kubectl` command:
   ```bash
   kubectl create namespace <namespace-name>
   ```
   For example:
   ```bash
   kubectl create namespace dev
   ```

3. **Apply resources to a specific namespace**:
   When you create resources, you can specify the namespace using the `--namespace` flag or by including it in your YAML manifest.

   Example:
   ```bash
   kubectl apply -f <resource-file>.yaml --namespace=dev
   ```

4. **Switch namespaces**:
   To work within a specific namespace, you can set the default namespace for your `kubectl` context:
   ```bash
   kubectl config set-context --current --namespace=dev
   ```
   This sets the namespace for the current context, so you don't need to specify the `--namespace` flag in every command.

5. **Delete a namespace**:
   To delete a namespace and all resources within it:
   ```bash
   kubectl delete namespace <namespace-name>
   ```

---

### **Best Practices for Namespaces**

- **Avoid Overusing Namespaces**: Don’t create namespaces for every small difference between resources (like different versions of the same app). Instead, use **labels** to differentiate between such resources within the same namespace.
  
- **Security Considerations**: While namespaces provide logical isolation, they do not guarantee full security. To enforce security policies within namespaces, use **Role-Based Access Control (RBAC)** and **NetworkPolicies** to restrict access.

- **Use Namespaces for Environment Separation**: A common practice is to use namespaces for separating environments, such as:
   - `dev` for development resources.
   - `staging` for staging environments.
   - `prod` for production resources.

- **Resource Quotas**: You can apply **ResourceQuotas** to namespaces to limit the amount of resources (such as CPU, memory, or storage) that can be consumed within a namespace. This helps avoid resource contention between teams.

---

### **Example: Creating a Namespace and Using It**

1. **Create a New Namespace**:
   ```bash
   kubectl create namespace team-a
   ```

2. **Apply a Deployment to the New Namespace**:
   ```bash
   kubectl apply -f deployment.yaml --namespace=team-a
   ```

3. **List Resources in a Namespace**:
   To list the pods in the `team-a` namespace:
   ```bash
   kubectl get pods --namespace=team-a
   ```

4. **Set Context to a Namespace**:
   You can switch to a specific namespace context for easier management:
   ```bash
   kubectl config set-context --current --namespace=team-a
   ```

---

### **Conclusion**

Kubernetes namespaces are a powerful way to partition and organize resources within a cluster, particularly in multi-team or multi-project environments. They provide a way to logically separate resources, ensuring that users or teams don’t interfere with each other’s resources. However, namespaces should not be overused, and you should prefer using labels for managing slightly different resources within a single namespace. 

By understanding and applying namespaces effectively, you can improve the scalability, security, and management of your Kubernetes clusters.

## Demonstrating Kubernetes Policies

### Kubernetes Limit Range Policy Demo Overview

In this demo, we'll explore how **Kubernetes LimitRanges** are used to enforce resource constraints on containers within a specific namespace. This is important because, by default, Kubernetes doesn't impose any restrictions on resource consumption, which could lead to resource contention and inefficient usage of the cluster. A **LimitRange** allows cluster administrators to set limits on resources like CPU, memory, and storage to ensure that containers don't consume more resources than they should, and to enforce default values when no resource limits are specified.

### **LimitRange in Kubernetes**

A **LimitRange** is a policy that defines the minimum and maximum values for resources like memory and CPU that containers and pods can request and consume in a particular namespace. This is enforced on a namespace level, meaning each namespace can have its own resource constraints.

---

### **Key Concepts**

1. **LimitRange Object**: A LimitRange is an object that defines resource limits and requests for containers within a namespace. It ensures that no container within the namespace can exceed the specified limits or fall below the defined minimums.
   
2. **Default Values**: If a container does not specify its resource limits and requests, Kubernetes will apply the default values defined in the LimitRange for that namespace.

3. **Resource Constraints**: LimitRanges can be applied to different resource types like:
   - Memory
   - CPU
   - Storage

4. **Namespace Scope**: A LimitRange object is applied to a specific namespace, meaning all the resources in that namespace will be subject to the defined limits.

---

### **Demo Walkthrough**

Here’s how we create and apply a LimitRange in Kubernetes, followed by creating a pod to test the resource limits:

#### 1. **Create a Namespace**
First, we create a namespace to isolate the resources for this demo. This is done using the following command:

```bash
k create ns demo
```

We use the short name `k` as an alias for `kubectl`. Then, we describe the namespace to verify it was created successfully.

```bash
k describe ns demo
```

Initially, there is **no LimitRange** in the namespace, which is what we expect.

#### 2. **Create the LimitRange Object**
Next, we create the **LimitRange** object. A YAML file defines this LimitRange and sets a **minimum** and **maximum** memory limit for containers in the `demo` namespace.

Here is an example of the YAML file (`demo-lr.yaml`):

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: demo-lr
  namespace: demo
spec:
  limits:
  - type: Container
    max:
      memory: "750Mi"
    min:
      memory: "250Mi"
```

- The `max` value specifies that containers cannot consume more than `750Mi` of memory.
- The `min` value specifies that containers must request at least `250Mi` of memory.
- The `type: Container` means that these limits are applied to individual containers within pods in the namespace.

We apply the LimitRange using the following command:

```bash
k apply -f demo-lr.yaml
```

#### 3. **Verify the LimitRange**
We can verify the LimitRange has been applied successfully by describing the `demo` namespace again:

```bash
k describe ns demo
```

You’ll see the **minimum** and **maximum** memory constraints listed, along with default values for memory (`750Mi`).

- **Default Request** and **Default Limit**: If containers don’t specify their own memory limits, Kubernetes will apply the default values (750Mi) as specified in the LimitRange.

#### 4. **Create a Pod Without Memory Limits**
Now, we create a pod that doesn’t specify its own resource requests or limits. The following YAML (`demo-pod.yaml`) defines a simple pod but does **not** specify the memory requests or limits:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
  namespace: demo
spec:
  containers:
  - name: demo-container
    image: nginx
```

We apply the pod:

```bash
k apply -f demo-pod.yaml
```

After creating the pod, we retrieve detailed information about the pod to verify the resource limits are applied:

```bash
k get po demo-pod -n demo -o yaml
```

In the output, you will see that Kubernetes has automatically applied the **default resource request** and **limit** (750Mi) to the pod's container since no explicit values were set in the YAML.

#### 5. **Create a Pod with Custom Memory Limits**
Next, we modify the `demo-pod.yaml` to specify custom memory limits and requests. This is done by uncommenting the `limits` and `requests` sections in the YAML file:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
  namespace: demo
spec:
  containers:
  - name: demo-container
    image: nginx
    resources:
      requests:
        memory: "300Mi"
      limits:
        memory: "500Mi"
```

We apply the updated pod:

```bash
k apply -f demo-pod.yaml
```

Now, when we get the pod’s details, we see that the memory request is `300Mi` and the memory limit is `500Mi`. These values are **within the range** specified in the LimitRange (between 250Mi and 750Mi).

#### 6. **Test Pod Creation with Invalid Memory Limits**
Finally, let's try creating a pod with memory limits that exceed the maximum defined in the LimitRange. We update the `demo-pod.yaml` to set the memory limit to `800Mi` (which is above the `750Mi` limit):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
  namespace: demo
spec:
  containers:
  - name: demo-container
    image: nginx
    resources:
      requests:
        memory: "300Mi"
      limits:
        memory: "800Mi"
```

We attempt to apply the pod:

```bash
k apply -f demo-pod.yaml
```

This time, Kubernetes will reject the pod creation with an error:

```
Error from server (Forbidden): error when creating "demo-pod.yaml": pods "demo-pod" is forbidden: memory limit exceeds limit range
```

This error occurs because the memory limit exceeds the maximum value (`750Mi`) specified in the LimitRange.

#### 7. **Cleanup**
Finally, we delete the pod and the LimitRange object to clean up the resources:

```bash
k delete po demo-pod -n demo
k delete limitrange demo-lr -n demo
```

---

### **Conclusion**

In this demo, we explored **Kubernetes LimitRange** objects, which are used to enforce resource constraints like memory and CPU on containers within a namespace. By defining these limits, administrators can ensure that containers within the namespace consume resources within the desired ranges. This is important for managing resource usage in multi-tenant environments, preventing any one container from consuming excessive resources and affecting the performance of other containers.

Key takeaways:
- **LimitRange** is a policy to set min/max resource values for containers in a namespace.
- If no specific resources are set for a container, the defaults from the LimitRange are applied.
- Containers can be constrained by memory and CPU requests/limits based on the policies defined in LimitRange.
- Kubernetes enforces these limits and rejects containers that exceed the specified limits.

## Pod Redundancy with ReplicaSets

### **Kubernetes ReplicaSets Overview**

In this video, we explore **Kubernetes ReplicaSets**, a type of controller that ensures a specified number of identical pods are running and available at all times. We'll dive into its purpose, how it works, and its relationship with other controllers like **Deployments**.

### **What is a ReplicaSet?**

A **ReplicaSet** is a Kubernetes controller that ensures that a defined number of replica pods are always running. If a pod managed by a ReplicaSet fails, the ReplicaSet will automatically create a new pod to replace it, maintaining the desired state. 

ReplicaSets are often used with **Deployments**, which provide additional features like **self-healing** and **scalability**, but it's important to note that **ReplicaSets themselves only manage the replicas of pods**.

---

### **ReplicaSet's Purpose**

- **Maintain a Stable Set of Pods**: The ReplicaSet's primary goal is to make sure the exact number of pods (replicas) are running at all times. If a pod fails or is deleted, the ReplicaSet will create a new one to replace it.
- **Pod Selector**: Each ReplicaSet has a **pod selector** that defines which pods it manages. This selector uses **labels** to match the pods it is responsible for. Only the pods that match this selector are part of the ReplicaSet.

---

### **How Does a ReplicaSet Work?**

1. **Pod Template**: The ReplicaSet has a **pod template** field in its manifest. This template specifies the **specifications** for the pods that the ReplicaSet will manage.
   
2. **Replicas**: The `replicas` field in the manifest defines how many pods should be running at any given time. The ReplicaSet ensures that exactly this number of pods are always running.

3. **Managing Pods**: 
    - If a pod is deleted or becomes unhealthy, the ReplicaSet detects this and creates a new pod to maintain the specified number of replicas.
    - The ReplicaSet creates new pods based on the pod template provided in its specification.

4. **OwnerReference**: Each pod created by the ReplicaSet has an `ownerReferences` field, which ties the pod back to the ReplicaSet. This allows Kubernetes to track the relationship between the ReplicaSet and its pods.

5. **Acquiring Pods**: If a pod doesn't have an `ownerReference` or if it doesn't belong to any controller, and it matches the ReplicaSet's selector, the ReplicaSet can "acquire" this pod. This is important to avoid unintentional interactions with other controllers, like Deployments, that may use ReplicaSets.

---

### **ReplicaSet and Deployments**

While **ReplicaSets** can be used on their own, they are commonly **managed by Deployments**. **Deployments** provide more advanced features, like **rolling updates** and **rollback capabilities**, which makes them preferable for most use cases.

- **Deployments manage ReplicaSets**: A Deployment creates and manages a ReplicaSet. The ReplicaSet ensures the correct number of pod replicas, while the Deployment handles the deployment strategies and updates to those replicas.

- **Self-healing**: If a pod goes down, the ReplicaSet automatically replaces it, ensuring that the application continues running without manual intervention.

- **Scalability**: The `replicas` field in a ReplicaSet manifest allows you to scale the application up or down. If you need more instances of the pod, you can change the `replicas` field to a higher number.

---

### **Key Features of a ReplicaSet**

- **Pod Selector**: A ReplicaSet uses a label selector to manage the pods it controls. This selector ensures that only the pods that match the labels are part of the ReplicaSet.
- **Pod Template**: The ReplicaSet’s pod template specifies the pod’s configuration (e.g., container images, environment variables, etc.).
- **Replicas**: The number of identical pods that the ReplicaSet should ensure are running.
- **OwnerReference**: Each pod in the ReplicaSet has an owner reference, linking it back to the ReplicaSet, ensuring proper management of the pods.

---

### **ReplicaSet Manifest Structure**

Here is an example of a **ReplicaSet manifest**:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: nginx
        image: nginx:latest
```

- **apiVersion**: The API version used for ReplicaSets is `apps/v1` because ReplicaSets are part of the **apps** API group.
- **kind**: The kind is `ReplicaSet`, which defines this as a ReplicaSet object.
- **metadata**: This section includes the name of the ReplicaSet.
- **spec**:
  - `replicas`: The number of replicas (3 in this case).
  - `selector`: The label selector used to identify the pods managed by this ReplicaSet. In this example, the ReplicaSet will manage all pods with the label `app: my-app`.
  - `template`: The pod template, which defines the pod configuration (e.g., container image, labels, etc.).

---

### **ReplicaSet's Relationship with Other Kubernetes Controllers**

- **Deployment vs. ReplicaSet**: While **Deployments** use **ReplicaSets** to manage the application pods, a ReplicaSet can also be used independently if you don’t require the additional features provided by a Deployment.
  
- **Pod vs. ReplicaSet**: A **Pod** is a single instance of a container, while a **ReplicaSet** is responsible for managing a group of pods, ensuring that the right number of identical pods are running at all times.
  
- **StatefulSet**: Unlike ReplicaSets, **StatefulSets** are used for managing stateful applications, such as databases. They manage the deployment and scaling of a set of Pods, and provide guarantees about the ordering and uniqueness of the Pods.

---

### **Best Practices with ReplicaSets**

- **Use Deployments for most cases**: In most cases, you will interact with Deployments rather than ReplicaSets directly. Deployments give you more control over updating your application without downtime.
  
- **Avoid direct use of ReplicaSets unless necessary**: You may interact directly with ReplicaSets when you need a custom update strategy or when working with legacy systems.
  
- **Avoid orphaned pods**: Ensure that pods do not have selectors matching those of any ReplicaSet unless you intend for the ReplicaSet to manage them. This helps to prevent unintentional management of pods by multiple controllers.

---

### **Conclusion**

**ReplicaSets** are crucial components of Kubernetes that ensure a specified number of identical pods are running at all times. While ReplicaSets can be used independently, they are often managed by **Deployments** for easier management of scaling, updating, and rollback. Understanding how ReplicaSets work, their relationship with other controllers, and how to define them in a manifest will help you manage the availability and stability of applications in a Kubernetes environment.

**Key Takeaways:**
- A ReplicaSet ensures that the specified number of pods are running.
- It is often managed by a Deployment but can be used on its own.
- The ReplicaSet uses a **label selector** to identify and manage its pods.
- Pods within a ReplicaSet are automatically recreated if deleted or fail.

## DaemonSets - Ensuring a Pod is Running per-Node

### **Kubernetes DaemonSets Overview**

In this video, we explore **Kubernetes DaemonSets**, a type of controller in Kubernetes that ensures a specific pod is running on all nodes within a cluster. DaemonSets are typically used for tasks like logging, monitoring, and storage on every node in the cluster. We’ll walk through the concept of DaemonSets, their use cases, manifest structure, and update mechanisms.

---

### **What is a DaemonSet?**

A **DaemonSet** is a controller in Kubernetes that ensures a particular pod is **running on every node** in a cluster. When nodes are added to the cluster, the DaemonSet ensures the pod is created on the new node. If nodes are removed, the DaemonSet automatically cleans up the associated pods.

#### Key Features of DaemonSets:
- **Pod Replication Across Nodes**: Ensures that one pod runs on every node.
- **Automatic Scaling**: When new nodes are added, the DaemonSet controller creates pods on them. Similarly, it removes pods when nodes are deleted.
- **Garbage Collection**: If a DaemonSet is deleted, all the pods created by it are also deleted.

---

### **Common Use Cases for DaemonSets**

DaemonSets are typically used for managing tasks that need to be run on every node in the cluster, including:

1. **Log Collection**: Running a logging daemon (e.g., Fluentd or Logstash) on each node to collect logs.
2. **Monitoring**: Running a node monitoring daemon (e.g., Prometheus node exporter) on each node to collect performance metrics.
3. **Cluster Storage**: Running a storage daemon (e.g., Ceph or GlusterFS) to manage distributed storage across the cluster.

While basic cases typically involve one DaemonSet per daemon type, more complex configurations may involve multiple DaemonSets for a single daemon, differentiated by specific flags or configurations.

---

### **Communication Methods with DaemonSet Pods**

DaemonSet pods can be accessed in various ways depending on the use case and how you configure them:

1. **Push-based Communication**: The DaemonSet pods themselves may push updates to another service, with no direct clients.
2. **NodeIP and Known Port**: You can expose the DaemonSet pods via **host ports**, which can be accessed using the node’s IP address and port number.
3. **DNS-based Communication**: A **headless service** (without a cluster IP) can be used with the same pod selector, allowing communication with DaemonSet pods through DNS.
4. **Service-based Communication**: A standard **Kubernetes Service** can be created with the same pod selector, allowing communication with the DaemonSet pods. However, this doesn’t allow targeting specific nodes, only accessing any pod within the DaemonSet.

---

### **DaemonSet YAML Manifest Structure**

Like all Kubernetes API objects, DaemonSets are defined using a **YAML manifest**. Here's the general structure of a DaemonSet manifest:

1. **apiVersion**: Specifies the version of the DaemonSet API (usually `apps/v1`).
2. **kind**: Always set to `DaemonSet` to indicate the type of resource.
3. **metadata**: Contains metadata about the DaemonSet, including its name. The name must be a valid **DNS subdomain** name.
4. **spec**: This section defines the specifications of the DaemonSet, including the **selector** and the **pod template**.

#### Basic Example of a DaemonSet YAML Manifest

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
    spec:
      containers:
        - name: fluentd
          image: fluent/fluentd:v1.12-1
          ports:
            - containerPort: 24224
```

- **apiVersion**: `apps/v1` — The API version for DaemonSets.
- **kind**: `DaemonSet` — Specifies this resource is a DaemonSet.
- **metadata**: Contains metadata, including the name of the DaemonSet.
- **spec.selector**: This selector ensures that the DaemonSet matches pods with the label `app: log-collector`.
- **spec.template**: The pod template that specifies the containers to run in each pod. Here, Fluentd is specified as the container image to collect logs.

---

### **DaemonSet Pod Template**

The **pod template** within the DaemonSet is essentially a standard Kubernetes pod specification. Some important points to note:

- **Pod Selector**: The pod template must include labels that match the selector, ensuring the DaemonSet can correctly manage its pods.
- **RestartPolicy**: The `RestartPolicy` for DaemonSet pods must always be `Always`, or it can be omitted because `Always` is the default for Kubernetes pods.

---

### **DaemonSet Scheduling**

Normally, Kubernetes schedules pods to nodes based on the **scheduler**. However, for DaemonSets, the **DaemonSet controller** handles scheduling pods onto nodes, not the Kubernetes scheduler. Some DaemonSet-specific scheduling options include:

- **Node Selector**: You can specify a **node selector** in the pod template’s `spec` to ensure that DaemonSet pods only run on nodes that match the selector.
- **Node Affinity**: For more complex scheduling requirements, DaemonSets can use **node affinity** to determine where pods should be scheduled.
- **Taints and Tolerations**: You can also use taints and tolerations to control which nodes the DaemonSet pods can run on.

---

### **Updating a DaemonSet**

#### 1. **Node Label Changes**
If node labels change, the DaemonSet automatically adds pods to matching nodes and deletes pods from nodes that no longer match the labels.

#### 2. **Rolling Updates**
DaemonSets support **rolling updates**, which update pods in a controlled, incremental manner. You can update the DaemonSet’s pod template (e.g., by changing the container image), and Kubernetes will update the pods in a rolling manner to ensure that the application remains available.

```bash
kubectl set image daemonset/log-collector fluentd=fluent/fluentd:v1.12-2
```

This command updates the Fluentd image in the DaemonSet, and Kubernetes will replace pods with the new version one by one.

---

### **Deleting a DaemonSet**

When you delete a DaemonSet, by default, the **pods managed by the DaemonSet are also deleted**. However, you can use the `--cascade=false` flag with `kubectl delete` to prevent automatic deletion of the pods.

```bash
kubectl delete daemonset log-collector --cascade=false
```

This would delete the DaemonSet but leave the pods running on the nodes.

---

### **Advanced DaemonSet Considerations**

1. **Match Expressions**: In the `.spec.selector` section, **match expressions** can be used for more complex pod selection. These expressions allow specifying key-value pairs and operators for better control over pod selection.
   
2. **Multiple DaemonSets for Different Configurations**: In some cases, you might have multiple DaemonSets for a single daemon type, such as running the same logging daemon with different configurations on different nodes.

3. **DaemonSet vs. Deployment**: While **Deployments** are generally used for stateless applications where you want to scale pods, **DaemonSets** are used for system daemons that need to run on every node.

---

### **Conclusion**

**DaemonSets** in Kubernetes are an essential tool for managing pods that must run on every node in the cluster, such as logging, monitoring, and storage daemons. By automatically managing the creation, scaling, and deletion of these pods across all nodes, DaemonSets simplify operations for workloads that need to run across the entire cluster. Understanding how to configure, update, and manage DaemonSets will help ensure the stability and consistency of critical infrastructure services in Kubernetes. 

**Key Takeaways:**
- DaemonSets are used to run a pod on every node in a Kubernetes cluster.
- They are ideal for system daemons such as log collectors, monitoring agents, and storage services.
- DaemonSets ensure that pods are scheduled on the appropriate nodes, and that they are updated and garbage collected as nodes are added or removed.

## Kubernetes Deployments

### **Kubernetes Deployments Overview**

In this video, we explore **Kubernetes Deployments**, a powerful feature for managing **pod replicas** and **ReplicaSets** with declarative updates. A Deployment is used to define a desired state for a set of pods, and the **Deployment Controller** ensures the cluster maintains that state by making any necessary changes to meet the defined specification.

---

### **What is a Kubernetes Deployment?**

A **Deployment** in Kubernetes is an API object used to manage and control the rollout and scaling of **ReplicaSets** and the **pods** they contain. With a Deployment, you specify the desired state for the application, and the Deployment Controller automatically makes the necessary changes to the system to match that desired state.

#### Key Features of Deployments:
- **Declarative Updates**: You define the desired state, and Kubernetes handles the rest (i.e., ensuring the correct number of replicas are running).
- **Rolling Updates**: Kubernetes supports zero-downtime rolling updates, which means new versions of applications can be deployed without affecting availability.
- **Rollback**: If an update causes issues, you can roll back to a previous stable version of the deployment.
- **Scaling**: Deployments make it easy to scale the number of pods up or down to handle varying levels of load.

---

### **Use Cases for Kubernetes Deployments**

Here are some typical use cases for Deployments in Kubernetes:

1. **Rollout of ReplicaSets**: You can use a deployment to create a new ReplicaSet, and Kubernetes will ensure the desired number of pods are running as defined in the Deployment.
2. **Rollbacks**: If a new deployment introduces issues or becomes unstable, you can easily roll back to a previous revision.
3. **Scaling**: You can scale the number of replicas to accommodate more traffic, by simply changing the `replicas` field in the Deployment specification.
4. **Pod Template Updates**: Deployments allow you to update the pod template specification, declaring a new desired state for the pods.
5. **Cleaning Up Older ReplicaSets**: Deployments ensure that old ReplicaSets that are no longer needed are automatically cleaned up.

---

### **Deployment Manifest Breakdown**

Let’s look at an example **Deployment YAML manifest** for an NGINX web server:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.19.0
          ports:
            - containerPort: 80
```

#### Key Fields in the Manifest:
1. **apiVersion**: Specifies the API version. Here, it's `apps/v1`, which is the version for deployment objects.
2. **kind**: Specifies the type of object, which is `Deployment` in this case.
3. **metadata**: Contains metadata about the Deployment, including its name (`nginx-deployment`).
4. **spec.replicas**: Specifies the number of replicas (pods) that should be running for this deployment. In this case, we want 3 replicas.
5. **spec.selector**: Defines the label selector used to match the pods managed by this deployment. In this case, we’re selecting pods with the label `app=nginx`.
6. **spec.template**: The pod template that defines the structure of the pods that will be created. The `template.spec` field defines the containers to run in each pod, their images, and ports.

---

### **Deployment Example Steps**

Here’s a practical guide to creating and managing a deployment with the example manifest:

1. **Create the Deployment**:
   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```

2. **Check Deployment Status**:
   Use the following command to check the status of your deployment:
   ```bash
   kubectl get deployments
   ```

   You can also use the `-o wide` flag to get more detailed information:
   ```bash
   kubectl get deployments -o wide
   ```

3. **Watch for Changes**:
   If you want to monitor changes as they happen, use the `-w` flag to watch the deployment in real-time:
   ```bash
   kubectl get deployments -w
   ```

4. **Rollout Status**:
   To check if a rollout is successful or still in progress, use:
   ```bash
   kubectl rollout status deployment/nginx-deployment
   ```

5. **View the ReplicaSet**:
   Each time a Deployment creates a new ReplicaSet, you can view the ReplicaSet using:
   ```bash
   kubectl get rs
   ```

   This will list all ReplicaSets in the namespace, showing their desired state and current status.

6. **Check Pod Labels**:
   To see all the labels attached to the pods created by the Deployment:
   ```bash
   kubectl get pods --show-labels
   ```

---

### **Zero-Downtime Rolling Updates**

One of the main benefits of using Deployments is the ability to perform **zero-downtime rolling updates**. When you update a Deployment (e.g., by changing the container image), Kubernetes will gradually update the pods to ensure there is no downtime.

#### Rolling Update Process:
1. **New ReplicaSet**: A new ReplicaSet is created based on the updated pod template.
2. **Scaling**: The new ReplicaSet is scaled up while the old ReplicaSet is scaled down.
3. **Gradual Transition**: Kubernetes incrementally replaces old pods with new ones, ensuring that some replicas are always running, which minimizes downtime.

---

### **Handling Updates with `kubectl`**

To manage and track updates to a Deployment, Kubernetes provides several commands:

1. **Record Command**: The `kubectl rollout` command allows you to record the rollout for introspection later:
   ```bash
   kubectl rollout history deployment/nginx-deployment
   ```

2. **Status Command**: You can watch the rollout status with:
   ```bash
   kubectl rollout status deployment/nginx-deployment
   ```

3. **Pause and Resume**: Sometimes, you may need to pause the deployment to fix an issue before continuing. You can pause a deployment and then resume it:
   ```bash
   kubectl rollout pause deployment/nginx-deployment
   kubectl rollout resume deployment/nginx-deployment
   ```

---

### **Label Selector Updates (Not Recommended)**

While Kubernetes supports updating the **label selectors** for a Deployment, this is **not recommended** unless absolutely necessary, as it can lead to orphaning old ReplicaSets. 

#### Label Selector Updates:
- If you update the **matchLabels** field in the `spec.selector` of a Deployment, Kubernetes will no longer consider existing ReplicaSets that were created with the old selector.
- If labels are **added**, this requires corresponding updates in the pod template, otherwise a validation error will occur.
- If labels are **removed**, Kubernetes will not create a new ReplicaSet but will remove the label from existing pods and ReplicaSets.

---

### **Rollback to a Previous Version**

If a Deployment becomes unstable after an update, you can easily **roll back** to a previous stable version.

#### Rollback Command:
To roll back a deployment to a previous revision:
```bash
kubectl rollout undo deployment/nginx-deployment
```

This will roll back to the previous stable state, and you can also specify a revision if you want to roll back to a specific version.

---

### **Scaling Deployments**

Deployments can also be **scaled** using the `kubectl scale` command. This allows you to adjust the number of pod replicas based on your application's needs.

#### Scaling Command:
```bash
kubectl scale deployment/nginx-deployment --replicas=5
```

This will scale the deployment to 5 replicas. Additionally, **horizontal pod autoscaling** can be used to automatically scale the deployment based on CPU usage.

---

### **Conclusion**

Kubernetes **Deployments** are an essential resource for managing applications in Kubernetes. They provide a simple way to define and manage the desired state for a set of pods, including rolling updates, rollbacks, and scaling. By using Deployments, you can ensure that your applications are always running in the desired state, with minimal downtime and automatic scaling. With the ability to manage the rollout process, track changes, and perform rollbacks, Deployments are a powerful tool for maintaining production-ready applications in Kubernetes.

## Exploring Deployments in Action

### **Kubernetes Deployment Demo Breakdown**

In this demo, we walk through the process of creating and managing a **Kubernetes Deployment**. The deployment will be performed in a **demo namespace**, and the steps include scaling the deployment, monitoring pod creation and termination, and replacing a pod. Let's break down the steps performed during the demo:

---

### **Step 1: Create a Namespace**
The demo begins by creating a namespace (`demo`) to isolate the deployment resources from the rest of the cluster.

```bash
k create ns demo
```

This ensures that the deployment and any related resources (e.g., pods, ReplicaSets) are confined to the `demo` namespace.

---

### **Step 2: Prepare the Deployment Manifest**

The deployment manifest (`demo-deploy.yaml`) is structured as follows:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  namespace: demo
  labels:
    app: nginx
spec:
  replicas: 10
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.19.0
        ports:
        - containerPort: 80
```

- **apiVersion**: `apps/v1` (used for deployments).
- **kind**: `Deployment`.
- **metadata**: Contains the name (`nginx-deploy`), the namespace (`demo`), and labels (`app: nginx`).
- **spec**: 
  - **replicas**: The desired number of pod replicas (set to 10 initially).
  - **selector**: The label selector used to find matching pods. In this case, it targets pods with the label `app: nginx`.
  - **template**: The pod template specifying the container's configuration (NGINX image and port 80).

---

### **Step 3: Apply the Deployment**

The deployment is created by applying the `demo-deploy.yaml` file:

```bash
k apply -f demo-deploy.yaml
```

Once the deployment is applied, Kubernetes will create 10 pods as per the specified replica count.

---

### **Step 4: Monitor the Deployment**

You can check the status of the deployment:

```bash
k get deploy -n demo
```

This shows the **nginx-deploy** deployment in the `demo` namespace with:
- 10 pods **READY**
- 10 pods **UP-TO-DATE**
- 10 pods **AVAILABLE**
- The age of the deployment (a few seconds).

---

### **Step 5: View ReplicaSets**

To check the ReplicaSet created by the deployment, run:

```bash
k get rs -n demo
```

The ReplicaSet is automatically created by the deployment, and the name will include the deployment name (e.g., `nginx-deploy-<UID>`). The output indicates:
- The desired number of pods (10).
- The current number of pods (10).
- The number of pods that are ready (10).

---

### **Step 6: Monitor Pods with `watch`**

To see the running pods and their status in real-time, use:

```bash
k get po -n demo -o wide -w
```

This command will list all 10 running pods, with 5 on each of the two nodes. The `-w` flag watches the pods, so any changes (like pod creation or termination) will be displayed live.

---

### **Step 7: Scale the Deployment Down**

The replica count is reduced from 10 to 3 in the `demo-deploy.yaml` file:

```yaml
replicas: 3
```

After saving the file, the deployment is updated with:

```bash
k apply -f demo-deploy.yaml
```

Once applied, Kubernetes immediately starts terminating 7 of the 10 pods (since we reduced the replica count). The system scales down the deployment to 3 pods. This change is reflected in the watch session.

---

### **Step 8: Verify Pod Status After Scaling**

After scaling down, you can verify the pod status:

```bash
k get po -n demo -o wide
```

This shows that only 3 pods are now running. You can confirm that the scale-down operation completed successfully.

---

### **Step 9: Delete a Pod and Watch the Replacement**

Next, a pod is deleted manually using:

```bash
k delete po <pod-name> -n demo
```

For example, to delete a pod named `nginx-deploy-75c7f965d8-7s2hf`, the command is:

```bash
k delete po nginx-deploy-75c7f965d8-7s2hf -n demo
```

Kubernetes will immediately replace the deleted pod with a new one. The `-w` flag is used again to monitor this in real-time.

---

### **Step 10: Scale the Deployment Up**

The replica count is updated again, this time increasing the number of replicas from 3 to 4 in the `demo-deploy.yaml` file:

```yaml
replicas: 4
```

After saving the file, apply the changes with:

```bash
k apply -f demo-deploy.yaml
```

Kubernetes scales the deployment up, adding another pod. The new pod will be scheduled on one of the nodes (in this case, likely `worker2` to balance the load).

---

### **Step 11: Verify Pod Distribution After Scaling Up**

Finally, verify the pod distribution after scaling up:

```bash
k get po -n demo -o wide
```

This shows that there are now 2 pods running on **worker1** and 2 pods running on **worker2** (or as per the available nodes in the cluster).

---

### **Conclusion**

In this demo, we covered the entire process of creating and managing a Kubernetes deployment, including:

1. Creating a namespace to isolate the demo resources.
2. Defining a deployment manifest with NGINX as the container.
3. Applying the deployment, monitoring the pod and ReplicaSet status.
4. Scaling the deployment up and down.
5. Deleting and replacing pods.
6. Verifying changes in real-time using the `-w` flag.

By using **Kubernetes Deployments**, we can easily scale applications, manage pods, and ensure zero-downtime updates across multiple nodes in the cluster.

## Kubernetes Services

### **Kubernetes Services Overview**

In this video, we delve into **Kubernetes Services**, which are crucial for managing how different parts of your application (pods) communicate with each other within a Kubernetes cluster. Here's a breakdown of the key concepts discussed:

---

### **Why Do We Need Kubernetes Services?**

- **Pods are ephemeral**: Kubernetes pods are designed to be temporary and dynamic. When a pod dies and is recreated (for instance, by a ReplicaSet), it gets a new IP address. Therefore, directly connecting to pods via their IPs is not reliable.

- **Need for Service Abstraction**: Services provide a stable, logical abstraction layer for a group of pods, making it possible for other components to interact with them, regardless of their individual IP addresses or lifecycles. This decouples services (such as frontend applications) from the pods providing backend workloads.

- **Service Discovery**: Kubernetes uses an internal DNS and environment variables to allow services to discover each other dynamically. When a service is created, its name is automatically registered in the DNS, making it discoverable by other pods.

---

### **What is a Kubernetes Service?**

A **Kubernetes Service** is an abstraction that defines how to access a set of pods. It acts as a stable endpoint for these pods, allowing other applications or services to connect to them, without worrying about the changing pod IP addresses.

- **Selector-based Services**: A service is often configured to target a set of pods using labels. For example, if a service targets all pods with the label `app=nginx`, it will route traffic to those pods.
  
- **Service Discovery**: Kubernetes supports service discovery via DNS and environment variables. Every pod knows about the internal DNS and can resolve services by their name.

---

### **Key Concepts in Kubernetes Services**

1. **Service as a REST Object**: Like other Kubernetes resources, a service is defined using a YAML manifest and applied via `kubectl`.

2. **Service Name**: The service name must be a valid DNS label (max 63 characters, lowercase alphanumeric characters and dashes).

3. **Ports**:
   - **Port**: The port that clients use to communicate with the service.
   - **TargetPort**: The port on the container that the service should forward traffic to.

   For example, if a service exposes port 80, but the container behind it listens on port 9000, the service will route traffic from port 80 to port 9000 on the container.

---

### **Advanced Service Concepts**

1. **Services Without Selectors**:
   - Sometimes, a service might not have selectors, such as when you need to point to an external service or a database that isn't running as a pod inside the cluster.
   - In this case, the service does not automatically create an associated endpoints object, and you can manually define the service's destination (e.g., an external database or a different Kubernetes cluster).

2. **Multiple Ports**: You can define multiple ports for a service (e.g., one for HTTP and another for HTTPS). When doing this, each port must have a unique name to avoid ambiguity.

3. **Headless Services**: A **headless service** is a service without a cluster IP. It doesn’t involve load balancing and directly exposes the individual pods behind the service.
   - Headless services can be used to expose applications like databases that require direct access to individual pods rather than being load balanced.

4. **DNS for Service Discovery**:
   - If a service has selectors, Kubernetes will create DNS A records pointing to the individual pod IPs.
   - For services without selectors, Kubernetes may create CNAME records (pointing to an external service) or A records pointing to the endpoints of the service.

---

### **Service Types**

Kubernetes allows several types of services, each suited for different use cases:

1. **ClusterIP (Default)**: 
   - Exposes the service on an internal IP within the cluster. It is only accessible from within the Kubernetes cluster. This is the default service type.
   
2. **NodePort**:
   - Exposes the service on a static port on each node's IP address. It allows access from outside the cluster by specifying the node IP and the NodePort.
   - Kubernetes automatically creates a **ClusterIP** service when you create a NodePort service, and the NodePort routes traffic to the ClusterIP.

3. **LoadBalancer**:
   - Typically used in cloud environments, a LoadBalancer service exposes the service externally by creating a cloud provider’s load balancer. It automatically creates both a NodePort and a ClusterIP service.
   - Traffic coming to the cloud load balancer is forwarded to the backend services in the cluster.

4. **ExternalName**:
   - An **ExternalName** service does not create a proxy for the service. Instead, it maps the service to an external DNS name, allowing Kubernetes to return a CNAME record.
   - This type of service is useful when you want Kubernetes to connect to services outside the cluster.

---

### **Service Discovery Methods**

1. **Environment Variables**:
   - When a pod starts, the Kubernetes **kubelet** injects environment variables corresponding to each active service in the cluster.
   - If a pod tries to access a service, it can use the service's DNS name (if DNS is configured) or access the service via environment variables that contain the cluster IP and port.

2. **DNS**:
   - Kubernetes uses **CoreDNS** (or another DNS service) to handle service discovery. Whenever a new service is created, CoreDNS generates DNS records for the service.
   - Pods use DNS to resolve service names like `my-service.my-namespace.svc.cluster.local`.

---

### **Example YAML for a Kubernetes Service**

Here is a simple service YAML that illustrates some of the concepts discussed:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app  # Selects pods with this label
  ports:
    - protocol: TCP
      port: 80       # Port exposed by the service
      targetPort: 9000  # Port on the container
  type: ClusterIP  # Default service type
```

### **Conclusion**

- **Kubernetes Services** are essential for abstracting and managing network access to a set of pods in a cluster.
- Services provide stable endpoints for communication between different components (e.g., frontend and backend).
- Kubernetes supports multiple service types, including `ClusterIP`, `NodePort`, `LoadBalancer`, and `ExternalName`, for various access needs.
- Service discovery in Kubernetes is automatically handled via DNS and environment variables, making it easier for pods to discover and connect to other services in the cluster.

Kubernetes services ensure that communication between components is seamless, even as pods are created and destroyed, providing a robust infrastructure for deploying scalable, cloud-native applications.

## Exploring Services in Action

### **Kubernetes Service Demo Breakdown**

In this demo, you walked through the steps of creating a **Kubernetes Service** to expose a pod running in the cluster, and accessed it externally using a **NodePort**. Below is a breakdown of the key steps and concepts you covered:

---

### **1. Creating the Namespace**

First, you created a new namespace to isolate resources for this demo:

```bash
k create ns demo
```

This helps avoid any conflicts with other resources in the cluster by keeping your demo resources in their own isolated space.

---

### **2. Creating the Pod**

Next, you created a **Pod** using the `demo-pod.yaml` manifest. This pod uses the official **nginx** Docker image (version 1.19.0) and runs in the `demo` namespace. Here’s the basic idea behind the pod:

- **Pod Definition**: The pod runs an Nginx container, which will serve content on port 80.

---

### **3. Accessing the Pod's Shell**

Once the pod was created, you accessed its shell using the following command:

```bash
k exec -it nginx-pod -n demo -- /bin/sh
```

This gives you an interactive shell inside the container running in the pod.

- The `-i` flag keeps the session open.
- The `-t` flag allocates a pseudo-TTY (for terminal interaction).
- The `--` separates the command from its arguments (in this case, `/bin/sh`).

You then verified the pod’s hostname with `hostname` and customized the Nginx homepage by creating a new `index.html` with a custom message using `EOF` markers.

---

### **4. Creating the Service (NodePort)**

You created the **Service** with the following YAML (`demo-svc.yaml`), which defines a **NodePort** service to expose the pod externally:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-svc
  namespace: demo
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80         # Internal service port
      targetPort: 80    # Container port where nginx listens
      nodePort: 31000   # Expose externally on port 31000
```

- **`type: NodePort`**: Exposes the service on every node’s IP at a static port (in this case, `31000`).
- **`selector`**: Ensures the service only routes traffic to pods with the label `app=nginx`.
- **`port`**: The internal port within the cluster where the service will be accessible.
- **`targetPort`**: The port within the container (nginx) that the service will forward requests to.
- **`nodePort`**: Specifies the external port (31000) on which the service will be accessible from outside the cluster.

After applying this YAML (`k apply -f demo-svc.yaml`), the service is created and available.

---

### **5. Finding the Node IP and Testing the Service**

To access the service from outside the cluster, you needed to find the **Node IP** of the worker node where your pod was running. You used:

```bash
k get po -n demo -o wide
```

This showed that the pod is running on `Kubernetes worker1`, so you proceeded to find the node IP:

```bash
k get no -o wide
```

This gave you the IP address of the node (`192.168.100.132`), which you combined with the `nodePort` (`31000`).

- The service was now available externally at `http://192.168.100.132:31000`.

You pasted this into a browser and confirmed that you could access the custom message served by Nginx, which displayed the message **"K8s Rules!"**.

---

### **Conclusion**

- **Creating a Kubernetes Service** using a `NodePort` exposes a set of pods (in this case, running an Nginx container) externally to the cluster, making it accessible via the node’s IP address and a specific port.
- **NodePort** is ideal for quick access to services for development or testing purposes, although in production, you'd often use a **LoadBalancer** service for better management of external traffic.
  
This demo covered the fundamental steps of creating a service, using `kubectl` to create the resources, and verifying the service’s functionality via external access.


## Identifying Ingress: Manage External Traffic

### **Kubernetes Ingress Demo Breakdown**

In this demo, you walk through the steps of setting up an **Ingress** in a Kubernetes cluster to manage external traffic to multiple services. You use **Minikube** to create the cluster, **Nginx Ingress Controller** as the ingress controller, and then define an **Ingress Object** to route traffic to different backend services based on the URL path. Let's break down the key steps.

---

### **1. Enabling the Ingress Controller in Minikube**

To begin, you enabled the **Ingress Controller** in Minikube using the following command:

```bash
minikube addons enable ingress
```

- **Ingress Controller**: This is a component that listens for incoming HTTP(S) traffic and routes it to the appropriate backend service based on the rules you define in your Ingress resources. In this case, the **Nginx Ingress Controller** is used.
- **Minikube Add-ons**: Minikube includes the Nginx Ingress Controller as an add-on, which can be enabled with a single command.

Once enabled, you checked the status of the Ingress Controller:

```bash
k get po -A -l app.kubernetes.io/name=ingress-nginx
```

This confirms the controller is running and ready to manage external traffic.

---

### **2. Creating Two Backend Services**

Next, you created two backend services (`app1` and `app2`) using the **`app-svc.yaml`** file.

#### **Pod Definitions**:

- **App1**: A pod running the **hashicorp/http-echo** container, which simply echoes a custom message. It listens on port `5678`.
- **App2**: A similar pod that echoes a different message, also listening on port `5678`.

#### **Services**:

- **app1-svc**: A service that targets `app=app1` pods, exposing port `5678`.
- **app2-svc**: A service targeting `app=app2` pods, exposing port `5678`.

After applying the YAML file using:

```bash
k apply -f app-svc.yaml
```

You confirmed that both services were created correctly with:

```bash
k get svc -o wide
```

---

### **3. Creating the Ingress Resource**

Now, you created the **Ingress Resource** using the **`ing-rule.yaml`** file, which defines the routing rules.

#### **Key Sections of the Ingress Object**:

- **`apiVersion: networking.k8s.io/v1`**: This is the stable API version for Ingress, replacing the deprecated `extensions/v1beta1`.
- **Rules**:
  - **Host**: The host is set to `domain.local`. This is a placeholder for the domain name that will route traffic to your services. (We will handle DNS resolution in a later step).
  - **Paths**:
    - **/path1** routes to `app1-svc`.
    - **/path2** routes to `app2-svc`.

Here's the relevant part of the **Ingress YAML**:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: simple-ingress
spec:
  rules:
  - host: domain.local
    http:
      paths:
      - path: /path1
        pathType: Prefix
        backend:
          service:
            name: app1-svc
            port:
              number: 5678
      - path: /path2
        pathType: Prefix
        backend:
          service:
            name: app2-svc
            port:
              number: 5678
```

You created the ingress with:

```bash
k apply -f ing-rule.yaml
```

---

### **4. Verifying Ingress Status and Getting the IP**

Once the Ingress resource was created, you checked its status with:

```bash
k get ing -o wide -w
```

The `-w` flag allows you to watch changes, and you observed that initially, there was no address assigned. After a few moments, the address appeared, which is the **Minikube IP**:

```bash
minikube ip
```

You used this IP (`172.17.20.26`) to configure your local machine's **hosts file** so that `domain.local` resolves to this IP. This was done by adding the following line to the `hosts` file:

```plaintext
172.17.20.26 domain.local
```

This allows you to use `domain.local` in your browser or curl requests.

---

### **5. Testing the Ingress with `curl`**

Finally, you tested the Ingress routing by sending HTTP requests to `domain.local`.

- **Testing `/path1`**:

```bash
curl -kL http://domain.local/path1
```

This correctly returned the response from `app1` (i.e., **"greetings from app1"**).

- **Testing `/path2`**:

```bash
curl -kL http://domain.local/path2
```

This returned the response from `app2` (i.e., **"greetings from app2"**).

This shows that the Ingress is correctly routing traffic based on the URL path to the appropriate backend service.

---

### **Conclusion**

By following these steps, you've successfully:

1. Enabled the **Ingress Controller** in Minikube.
2. Created two backend services (`app1-svc` and `app2-svc`), each serving a different message.
3. Defined an **Ingress Resource** to route traffic based on URL paths (`/path1` to `app1-svc` and `/path2` to `app2-svc`).
4. Verified the Ingress functionality by setting up the `domain.local` hostname and testing it via `curl`.

This setup illustrates how Kubernetes Ingress can help manage and route external traffic to different services within a cluster, providing a convenient way to expose multiple services over a single external IP address.