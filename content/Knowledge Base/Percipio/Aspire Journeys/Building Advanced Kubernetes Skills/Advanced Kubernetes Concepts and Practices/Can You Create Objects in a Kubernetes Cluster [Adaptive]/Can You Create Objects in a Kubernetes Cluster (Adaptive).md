---
date: 2001-01-01
---

# Can You Create Objects in a Kubernetes Cluster (Adaptive)

## 1
To complete the tasks you've outlined, you'll need to interact with the Kubernetes cluster using the `kubectl` command. Here’s how you can do it step-by-step:

### 1. SSH into the `k8s-master1` Virtual Machine
First, you need to SSH into the `k8s-master1` node (the master node of your Kubernetes cluster).

- Open MobaXterm and connect to the `k8s-master1` virtual machine.
- When prompted for a password, use `Passw0rd!`.
- Do **not** save the password when prompted.

Once logged in, you'll be at the command prompt.

### 2. Create a Pod Named `pod1` with an Nginx Container

To create a pod named `pod1` with the Nginx Docker container image, use the following `kubectl` command:

```bash
kubectl run pod1 --image=nginx
```

This command will create a pod named `pod1` with an Nginx container. By default, Kubernetes will try to pull the `nginx` image from Docker Hub, so make sure your Kubernetes master node has internet access.

### 3. Create a Pod Named `pod2` with an HTTPD Container and a Label

To create a pod named `pod2` containing an HTTPD Docker container image, and a label `app=webapp`, you can run the following command:

```bash
kubectl run pod2 --image=httpd --labels="app=webapp"
```

This command creates a pod named `pod2` with an HTTPD container and applies the label `app=webapp` to the pod.

### 4. Display the Status of Running Pods

After creating the pods, you can check the status of all the running pods in your cluster using the following command:

```bash
kubectl get pods
```

This will show you a list of all pods and their current statuses, such as whether they are running, pending, or in an error state.

### Summary of Commands

Here’s a summary of the commands:

1. SSH into `k8s-master1`.
2. Create the Nginx pod:
   ```bash
   kubectl run pod1 --image=nginx
   ```
3. Create the HTTPD pod with the label:
   ```bash
   kubectl run pod2 --image=httpd --labels="app=webapp"
   ```
4. Check the pod status:
   ```bash
   kubectl get pods
   ```

Once you've run these commands, the pods should be created, and you can verify their status by listing them with `kubectl get pods`.

## 2
To complete the tasks you've outlined, you'll need to interact with Kubernetes using the `kubectl` command. Here's how to do it step-by-step:

### 1. Create an Application Deployment Named `database` with Redis Container

To create a deployment named `database` that contains the Redis Docker container image, use the following `kubectl` command:

```bash
kubectl create deployment database --image=redis
```

This command creates a deployment named `database` with Redis as the container image. By default, Kubernetes will create one replica of the Redis container in the deployment.

### 2. Scale the Deployment to 4 Replicas

To scale the `database` deployment to have 4 replicas (pods), use the following `kubectl` command:

```bash
kubectl scale deployment database --replicas=4
```

This command will change the number of pods created by the `database` deployment to 4.

### 3. Display the Deployments Running in the Cluster

To view the deployments running in the cluster, use the following `kubectl` command:

```bash
kubectl get deployments
```

This will show you a list of all the deployments currently running in your Kubernetes cluster.

### 4. Display the Pods Running in the Cluster

To view the pods running in the cluster, use the following `kubectl` command:

```bash
kubectl get pods
```

This command will list all the pods, including those created by the `database` deployment. Since you've scaled the deployment to 4 replicas, you should see 4 pods associated with the `database` deployment.

### Summary of Commands

Here’s a summary of the commands you'll need to run:

1. Create the Redis deployment:
   ```bash
   kubectl create deployment database --image=redis
   ```
2. Scale the deployment to 4 replicas:
   ```bash
   kubectl scale deployment database --replicas=4
   ```
3. View the deployments:
   ```bash
   kubectl get deployments
   ```
4. View the pods:
   ```bash
   kubectl get pods
   ```

Once you've executed these commands, you will have successfully created the `database` deployment, scaled it to 4 replicas, and displayed the running deployments and pods in your cluster.

## 3
To complete the tasks, you will need to generate a pod definition file (`pod3.yaml`), use it to create a pod, and then retrieve the status of the pod using the `kubectl` command. Here are the steps:

### 1. Generate a Pod Definition File (`pod3.yaml`)

To generate a YAML definition file for a pod named `pod3` that contains an Nginx Docker container, use the following `kubectl` command:

```bash
kubectl run pod3 --image=nginx --dry-run=client -o yaml > pod3.yaml
```

Here’s a breakdown of the command:
- `kubectl run pod3`: This creates a pod named `pod3`.
- `--image=nginx`: This specifies that the container will use the `nginx` Docker image.
- `--dry-run=client`: This ensures that the pod is not actually created but the output is generated as a YAML definition.
- `-o yaml`: This outputs the pod definition in YAML format.
- `> pod3.yaml`: This redirects the output to a file named `pod3.yaml`.

### 2. Create the Pod from the `pod3.yaml` File

Once the `pod3.yaml` file is generated, you can use it to create the pod. Run the following command to create the pod:

```bash
kubectl apply -f pod3.yaml
```

This will create the pod named `pod3` using the definition in the `pod3.yaml` file.

### 3. Retrieve the Status of `pod3`

To check the status of `pod3`, use the following command:

```bash
kubectl get pod pod3
```

This will display the current status of the `pod3` pod, such as whether it's running, pending, or has encountered an error.

### Summary of Commands

Here’s a summary of the commands:

1. Generate the `pod3.yaml` definition file:
   ```bash
   kubectl run pod3 --image=nginx --dry-run=client -o yaml > pod3.yaml
   ```
2. Create the pod using the `pod3.yaml` file:
   ```bash
   kubectl apply -f pod3.yaml
   ```
3. Retrieve the status of `pod3`:
   ```bash
   kubectl get pod pod3
   ```

By following these steps, you will generate the pod definition, create the pod from the YAML file, and check its status.

## 4
To complete the tasks you have outlined, follow these steps to generate the deployment definition file, create the deployment, and scale the number of replicas:

### 1. Generate a Deployment Definition File (`intranet.yaml`)

To generate a YAML definition file for a deployment named `intranet` that uses an HTTPD Docker container image, run the following `kubectl` command:

```bash
kubectl create deployment intranet --image=httpd --dry-run=client -o yaml > intranet.yaml
```

Here’s an explanation of the command:
- `kubectl create deployment intranet`: This creates a deployment named `intranet`.
- `--image=httpd`: This specifies the `httpd` Docker image for the containers in the deployment.
- `--dry-run=client`: This simulates the creation of the deployment and prevents it from being created immediately.
- `-o yaml`: This outputs the deployment definition in YAML format.
- `> intranet.yaml`: This redirects the output to a file named `intranet.yaml`.

### 2. Create the Deployment Using the `intranet.yaml` File

Once the `intranet.yaml` file is generated, you can use it to create the deployment. Run the following command:

```bash
kubectl apply -f intranet.yaml
```

This command will create a deployment named `intranet` based on the YAML file you just generated.

### 3. Increase the Number of Replicas for the `intranet` Deployment

To scale the `intranet` deployment to 6 replicas, use the following `kubectl` command:

```bash
kubectl scale deployment intranet --replicas=6
```

This command will update the deployment to have 6 replicas (pods) instead of the default 1 replica.

### Summary of Commands

Here’s a summary of the commands:

1. Generate the `intranet.yaml` definition file:
   ```bash
   kubectl create deployment intranet --image=httpd --dry-run=client -o yaml > intranet.yaml
   ```
2. Create the deployment from the `intranet.yaml` file:
   ```bash
   kubectl apply -f intranet.yaml
   ```
3. Scale the `intranet` deployment to 6 replicas:
   ```bash
   kubectl scale deployment intranet --replicas=6
   ```

By following these steps, you will generate the deployment definition, create the deployment from the YAML file, and scale it to 6 replicas.
