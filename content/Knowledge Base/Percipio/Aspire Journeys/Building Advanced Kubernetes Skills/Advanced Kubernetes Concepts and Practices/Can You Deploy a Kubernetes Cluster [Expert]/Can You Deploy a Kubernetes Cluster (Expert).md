---
date: 2001-01-01
---

# Can You Deploy a Kubernetes Cluster

## 1
To complete the steps in your challenge lab, follow these instructions:

1. **Establish an SSH session:**

   First, you need to establish an SSH connection to the master node (`k8s-master1`) using MobaXterm as the administrator. This will allow you to run Kubernetes commands on the master node.

   - Open MobaXterm and start a new SSH session.
   - Use the credentials for `k8s-master1` (Ubuntu VM), with the password `Passw0rd!`.

2. **Retrieve a list of the cluster nodes:**

   After logging into the `k8s-master1` virtual machine, run the following command to list the cluster nodes:
   ```bash
   kubectl get nodes > nodes
   ```
   This command will list all the nodes in your Kubernetes cluster and save the output to a file named `nodes` in the current working directory.

3. **Retrieve a list of all running pods:**

   To get a list of all running pods in all namespaces, use this command:
   ```bash
   kubectl get pods --all-namespaces > getallpods
   ```
   This will retrieve all the pods across every namespace in the Kubernetes cluster and save the output to a file called `getallpods`.

4. **Retrieve the running configuration of the `etcd-k8s-master1` pod:**

   To get the running configuration of the `etcd-k8s-master1` pod, which is located in the `kube-system` namespace, use the following command:
   ```bash
   kubectl get pod etcd-k8s-master1 -n kube-system -o yaml > getetcd
   ```
   This command fetches the configuration of the `etcd-k8s-master1` pod in YAML format and saves it to a file named `getetcd`.

5. **Determine the number of pods running in all namespaces:**

   To determine how many pods are running across all namespaces in the cluster, use the following command:
   ```bash
   kubectl get pods --all-namespaces --no-headers | wc -l
   ```
   This command counts the number of running pods in the entire cluster. It does this by listing the pods across all namespaces (without headers) and piping the output into the `wc -l` command to count the number of lines, which corresponds to the number of pods.

### Summary of Commands:

```bash
# List cluster nodes and save output to 'nodes' file
kubectl get nodes > nodes

# List all pods in all namespaces and save output to 'getallpods' file
kubectl get pods --all-namespaces > getallpods

# Get the etcd-k8s-master1 pod configuration in yaml format and save to 'getetcd'
kubectl get pod etcd-k8s-master1 -n kube-system -o yaml > getetcd

# Count the number of pods running across all namespaces
kubectl get pods --all-namespaces --no-headers | wc -l
```

Once you've executed these commands, you will have completed the tasks specified in the challenge lab.

# Total number of pods across all namespaces
kubectl get pods --all-namespaces --no-headers | wc -l

# Total number of namespaces in the cluster
kubectl get namespaces --no-headers | wc -l

# Total number of pods running on the k8s-master1 node
kubectl get pods --all-namespaces -o wide | grep k8s-master1 | wc -l


## 2
Here’s how you can create and manage the resources in a Kubernetes cluster, based on your requirements:

### 1. **Create a Pod named `pod1` with an `nginx` Docker container image:**

To create a pod named `pod1` with an `nginx` image, create a YAML file `pod1.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  containers:
  - name: nginx-container
    image: nginx
```

Apply the YAML file to create the pod:
```bash
kubectl apply -f pod1.yaml
```

### 2. **Create a Pod named `pod2` with an `httpd` Docker container image and label `os=alpine`:**

Create a YAML file `pod2.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod2
  labels:
    os: alpine
spec:
  containers:
  - name: httpd-container
    image: httpd
```

Apply the YAML file to create the pod:
```bash
kubectl apply -f pod2.yaml
```

### 3. **Ensure you are in the `/home/administrator` directory:**

If you are working on a local environment or server, ensure that you are in the `/home/administrator` directory:
```bash
cd /home/administrator
```

### 4. **Display the contents of the `rs.yaml` ReplicaSet definition file:**

The contents of a sample `rs.yaml` file for creating a ReplicaSet might look like this:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-replicaset
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
        image: nginx
```

### 5. **Create a ReplicaSet using the `rs.yaml` file:**

To create a ReplicaSet from the `rs.yaml` file, apply it with the following command:
```bash
kubectl apply -f rs.yaml
```

### 6. **Display the contents of the `webservers.yaml` Deployment definition file:**

A sample `webservers.yaml` Deployment definition file could look like this:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webservers
spec:
  replicas: 2
  selector:
    matchLabels:
      app: webserver
  template:
    metadata:
      labels:
        app: webserver
    spec:
      containers:
      - name: nginx
        image: nginx
```

### 7. **Create a Deployment using the `webservers.yaml` file:**

To create a Deployment from the `webservers.yaml` file, use the following command:
```bash
kubectl apply -f webservers.yaml
```

### 8. **Create a Deployment definition file named `database.yaml` for a deployment named `database` that contains a `redis` Docker container image:**

Create a file `database.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: database
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis
```

### 9. **Create the Deployment using the `database.yaml` file:**

Apply the `database.yaml` file to create the deployment:

```bash
kubectl apply -f database.yaml
```

### 10. **Check Your Work:**

- **Determine the number of pods running in the default namespace:**
  
  To determine the number of pods running in the default namespace, use:
  ```bash
  kubectl get pods --namespace=default
  ```
  Then count the number of pods listed in the output.

- **Determine the number of ReplicaSets running in the default namespace:**
  
  To determine the number of ReplicaSets in the default namespace, use:
  ```bash
  kubectl get replicasets --namespace=default
  ```
  Then count the number of ReplicaSets listed in the output.

--- 

### Summary:
- You have created various resources (pods, ReplicaSets, and Deployments) using YAML files.
- You can use `kubectl get pods` and `kubectl get replicasets` to verify the resources created and count the number of running pods and ReplicaSets.

## 3
Here’s how to organize the resources in your Kubernetes cluster based on your requirements:

### 1. **Create a namespace named `finance`:**

You can create the `finance` namespace using the following command:
```bash
kubectl create namespace finance
```

### 2. **Create a pod named `pod3` in the `finance` namespace with a `redis` Docker container image and a label `app=accounting`:**

Create a `pod3.yaml` file with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod3
  namespace: finance
  labels:
    app: accounting
spec:
  containers:
  - name: redis-container
    image: redis
```

Then, apply the file to create the pod in the `finance` namespace:
```bash
kubectl apply -f pod3.yaml
```

### 3. **Create a ReplicaSet in the `finance` namespace using the `rs.yaml` ReplicaSet definition file:**

Assuming you already have the `rs.yaml` file, which contains the following content:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: finance-replicaset
  namespace: finance
spec:
  replicas: 3
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis
```

Apply the `rs.yaml` file to create the ReplicaSet in the `finance` namespace:
```bash
kubectl apply -f rs.yaml
```

### 4. **Create a namespace named `marketing`:**

You can create the `marketing` namespace using the following command:
```bash
kubectl create namespace marketing
```

### 5. **Create a Deployment named `intranet` in the `marketing` namespace with an `httpd` Docker container image:**

Create a `intranet.yaml` file with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: intranet
  namespace: marketing
spec:
  replicas: 2
  selector:
    matchLabels:
      app: intranet
  template:
    metadata:
      labels:
        app: intranet
    spec:
      containers:
      - name: httpd
        image: httpd
```

Then, apply the file to create the Deployment in the `marketing` namespace:
```bash
kubectl apply -f intranet.yaml
```

### 6. **Check Your Work:**

- **Determine the number of pods running in the `finance` namespace:**

To determine the number of pods running in the `finance` namespace, use:
```bash
kubectl get pods --namespace=finance
```
Then count the number of pods listed in the output.

- **Determine the number of namespaces defined in the cluster:**

To determine the number of namespaces defined in the cluster, use:
```bash
kubectl get namespaces
```
Then count the number of namespaces listed in the output.

- **Determine the number of pods running in the `marketing` namespace:**

To determine the number of pods running in the `marketing` namespace, use:
```bash
kubectl get pods --namespace=marketing
```
Then count the number of pods listed in the output.

- **Determine the number of ReplicaSets running in the `marketing` namespace:**

To determine the number of ReplicaSets running in the `marketing` namespace, use:
```bash
kubectl get replicasets --namespace=marketing
```
Then count the number of ReplicaSets listed in the output.

---

### Summary:
- You’ve organized resources into two namespaces: `finance` and `marketing`.
- The required pods, ReplicaSets, and Deployments are created using appropriate YAML files.
- You can verify the resources using `kubectl get pods`, `kubectl get namespaces`, and `kubectl get replicasets` to check the number of resources in each namespace.

## 4
Here’s how you can update your cluster resources and check your work based on your requirements:

### 1. **Update the `intranet` deployment in the `marketing` namespace to use the `nginx` image instead of the `httpd` image:**

To update the `intranet` Deployment, you can either modify the `intranet.yaml` file manually and reapply it or use the `kubectl set image` command to directly update the Deployment.

#### Option 1: Modify the `intranet.yaml` file:
- Find the `intranet.yaml` file and update the `httpd` image to `nginx`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: intranet
  namespace: marketing
spec:
  replicas: 2
  selector:
    matchLabels:
      app: intranet
  template:
    metadata:
      labels:
        app: intranet
    spec:
      containers:
      - name: nginx
        image: nginx  # updated from httpd to nginx
```

Then, apply the updated file:
```bash
kubectl apply -f intranet.yaml
```

#### Option 2: Use `kubectl set image`:
Alternatively, you can use the following command to update the image of the `intranet` deployment:

```bash
kubectl set image deployment/intranet nginx=nginx --namespace=marketing
```

### 2. **Scale the `webservers` Deployment in the default namespace to 4 replicas:**

To scale the `webservers` Deployment, you can use the following command to increase the number of replicas to 4:

```bash
kubectl scale deployment webservers --replicas=4 --namespace=default
```

### 3. **Scale the `rs` ReplicaSet in the default namespace to 2 replicas:**

To scale the `rs` ReplicaSet, use the following command to decrease the number of replicas to 2:

```bash
kubectl scale replicaset rs --replicas=2 --namespace=default
```

### 4. **Check Your Work:**

- **Determine the total number of ReplicaSets in the `marketing` namespace:**

To check the number of ReplicaSets in the `marketing` namespace, use:

```bash
kubectl get replicasets --namespace=marketing
```

Count the number of ReplicaSets listed in the output. Record the total.

---

### Summary:

- **Deployment Update:** You updated the `intranet` Deployment to use the `nginx` image instead of `httpd` either by modifying the YAML file or using `kubectl set image`.
- **Scaling Resources:** You scaled the `webservers` Deployment to 4 replicas and the `rs` ReplicaSet to 2 replicas.
- **Verification:** You can verify the total number of ReplicaSets in the `marketing` namespace using `kubectl get replicasets --namespace=marketing`.

## 5
To **roll back the `intranet` Deployment** in the `marketing` namespace to its previous version, you can use the `kubectl rollout undo` command. Here’s how you can do that:

### 1. **Rollback the `intranet` Deployment in the `marketing` namespace to its previous version:**

Run the following command to roll back the `intranet` deployment:

```bash
kubectl rollout undo deployment/intranet --namespace=marketing
```

This will revert the `intranet` deployment to the previous version before the update (which had the `httpd` image).

### 2. **Check Your Work:**

After performing the rollback, you need to verify that the correct container image is now running in the `intranet` deployment.

- **Determine the container image that is running in the `intranet` Deployment:**

Use the following command to check the details of the `intranet` Deployment, specifically the container image:

```bash
kubectl describe deployment intranet --namespace=marketing
```

Look for the `Containers` section in the output to find the image that is running. It should now be the previous image that was used (which was `httpd` if you rolled back to the version before the `nginx` update).

---

### Summary:

- **Rollback Command:** You used `kubectl rollout undo` to roll back the `intranet` Deployment.
- **Verification:** You checked the running container image by using `kubectl describe deployment intranet --namespace=marketing` and verified the container image in the Deployment details.
