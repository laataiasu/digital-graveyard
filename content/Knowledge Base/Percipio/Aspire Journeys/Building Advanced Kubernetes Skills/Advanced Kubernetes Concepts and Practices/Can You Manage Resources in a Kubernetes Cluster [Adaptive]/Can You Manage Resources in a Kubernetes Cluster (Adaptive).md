---
date: 1970-01-01
---

# Can You Manage Resources in a Kubernetes Cluster (Adaptive)

## 1
Here are the steps you need to follow to complete the task of creating a ReplicaSet in a Kubernetes namespace `dev`:

### 1. SSH into the Master Node
- Open the MobaXterm desktop application.
- SSH into the `k8s-master1` node using the credentials provided.
  - Host: `k8s-master1`
  - Username: `administrator`
  - Password: `Passw0rd!`
  
### 2. Create the `dev` Namespace
Once logged into the `k8s-master1` node, create the `dev` namespace using the following `kubectl` command:

```bash
kubectl create namespace dev
```

### 3. Display the Namespaces in the Cluster
To verify that the `dev` namespace was created successfully, use the following command:

```bash
kubectl get namespaces
```

This should show the `dev` namespace among other namespaces.

### 4. Display the Contents of the `rs.yaml` File
Next, you need to review the contents of the `rs.yaml` file, which contains the ReplicaSet definition. Use the `cat` command to display it:

```bash
cat rs.yaml
```

![alt text](Knowledge%20Base/Percipio/Aspire%20Journeys/Building%20Advanced%20Kubernetes%20Skills/Advanced%20Kubernetes%20Concepts%20and%20Practices/Can%20You%20Manage%20Resources%20in%20a%20Kubernetes%20Cluster%20[Adaptive]/image.png)

Make sure you review the file and understand its structure. It typically contains a ReplicaSet definition with configurations like the `replicas`, `selector`, and `template` for the pods.

### 5. Create the ReplicaSet in the `dev` Namespace
To create the ReplicaSet defined in `rs.yaml` within the `dev` namespace, run the following `kubectl` command:

```bash
kubectl apply -f rs.yaml -n dev
```

This will create the ReplicaSet named `rs` in the `dev` namespace.

### 6. Display the Status of the ReplicaSets in the `dev` Namespace
To check the status of the ReplicaSets in the `dev` namespace, use the following command:

```bash
kubectl get replicasets -n dev
```

This will show the ReplicaSets running in the `dev` namespace and their statuses.

### 7. Display the Pods Running in the Cluster
To display all the pods running in the cluster (across all namespaces), use the following command:

```bash
kubectl get pods --all-namespaces
```

Alternatively, if you only want to display the pods in the `dev` namespace, use:

```bash
kubectl get pods -n dev
```

This will list the pods associated with the ReplicaSet you created in the `dev` namespace.

### Summary of Commands:

```bash
kubectl create namespace dev
kubectl get namespaces
cat rs.yaml
kubectl apply -f rs.yaml -n dev
kubectl get replicasets -n dev
kubectl get pods --all-namespaces
# Or, if you want pods in the dev namespace only:
kubectl get pods -n dev
```

By following these steps, you'll have created the namespace, deployed the ReplicaSet, and verified its status in the `dev` namespace.

## 2
Here’s a step-by-step guide to create a Deployment in a Kubernetes namespace `intranet`:

### 1. Create the `intranet` Namespace
First, create the `intranet` namespace using the following `kubectl` command:

```bash
kubectl create namespace intranet
```

### 2. Display the Namespaces in the Cluster
To verify that the `intranet` namespace was created successfully, run the following command:

```bash
kubectl get namespaces
```

This will display a list of namespaces in your cluster, and you should see `intranet` among them.

### 3. Display the Contents of the `webservers.yaml` File
Next, review the contents of the `webservers.yaml` file. This file contains the Deployment definition for the `webservers`. Use the `cat` command to display it:

```bash
cat webservers.yaml
```

![alt text](Knowledge%20Base/Percipio/Aspire%20Journeys/Building%20Advanced%20Kubernetes%20Skills/Advanced%20Kubernetes%20Concepts%20and%20Practices/Can%20You%20Manage%20Resources%20in%20a%20Kubernetes%20Cluster%20[Adaptive]/image-1.png)

The file should define a Deployment with information such as the number of replicas, the container image, ports, and other settings for the `webservers` Deployment.

### 4. Create the Deployment in the `intranet` Namespace
To create the Deployment defined in `webservers.yaml` within the `intranet` namespace, use the following command:

```bash
kubectl apply -f webservers.yaml -n intranet
```

This will create the `webservers` Deployment in the `intranet` namespace.

### 5. Display the Deployments in the `intranet` Namespace
To check the status of the Deployments in the `intranet` namespace, use the following command:

```bash
kubectl get deployments -n intranet
```

This will list the Deployments running in the `intranet` namespace.

### 6. Display the ReplicaSets in the `intranet` Namespace
Every Deployment manages one or more ReplicaSets. To check the ReplicaSets in the `intranet` namespace, run:

```bash
kubectl get replicasets -n intranet
```

This will show the ReplicaSets associated with the `webservers` Deployment.

### 7. Display the Pods in the `intranet` Namespace
Finally, to list the pods created by the Deployment in the `intranet` namespace, use the following command:

```bash
kubectl get pods -n intranet
```

This will display all the pods that are running under the `intranet` namespace, which should correspond to the `webservers` Deployment.

### Summary of Commands:

```bash
kubectl create namespace intranet
kubectl get namespaces
cat webservers.yaml
kubectl apply -f webservers.yaml -n intranet
kubectl get deployments -n intranet
kubectl get replicasets -n intranet
kubectl get pods -n intranet
```

By following these steps, you'll successfully create the `intranet` namespace, deploy the `webservers` Deployment, and verify the status of the associated resources (Deployments, ReplicaSets, and Pods) in the `intranet` namespace.

## 3

Let's walk through each step for updating and managing the Deployment in the `intranet` namespace using `kubectl` commands.

### 1. **Update the webservers Deployment to use an httpd image instead of nginx**

To update the container image in the webservers Deployment, run the following command:

```bash
kubectl set image deployment/webservers nginx=httpd -n intranet
```

This command updates the `nginx` container in the `webservers` Deployment to use the `httpd` container image in the `intranet` namespace.

### 2. **Display the name of the container image in the webservers Deployment**

To display the container image of the webservers Deployment, use this command:

```bash
kubectl get deployment webservers -n intranet -o=jsonpath='{.spec.template.spec.containers[*].image}'
```

This command will return the name of the image currently being used in the `webservers` Deployment in the `intranet` namespace.

### 3. **Display the ReplicaSets in the intranet namespace**

To view the ReplicaSets in the `intranet` namespace, use:

```bash
kubectl get replicasets -n intranet
```

This will list all the ReplicaSets in the `intranet` namespace.

### 4. **Scale the webservers Deployment to 6 replicas**

To scale the `webservers` Deployment to 6 replicas, run:

```bash
kubectl scale deployment/webservers --replicas=6 -n intranet
```

This command will adjust the number of replicas for the `webservers` Deployment to 6 in the `intranet` namespace.

### 5. **Display the pods running in the intranet namespace**

To display the pods running in the `intranet` namespace, use:

```bash
kubectl get pods -n intranet
```

This will list all the pods currently running in the `intranet` namespace.

### Check your work:

1. **Verify that the image has been updated**: After running the `kubectl set image` command, confirm the image change by using the command for displaying the container image (`kubectl get deployment webservers -n intranet -o=jsonpath='{.spec.template.spec.containers[*].image}'`).

2. **Verify that the Deployment is scaled to 6 replicas**: Use the `kubectl get deployment webservers -n intranet` command to check the `replicas` field, which should now show 6.

By following these steps, you will have successfully updated the image, scaled the deployment, and listed the necessary resources in the `intranet` namespace.

### Summary of Commands:

```bash
kubectl set image deployment/webservers webservers=httpd:latest -n intranet
kubectl describe deployment webservers -n intranet
kubectl get replicasets -n intranet
kubectl scale deployment webservers --replicas=6 -n intranet
kubectl get pods -n intranet
```

These commands will update the container image in the `webservers` Deployment, display the current container image, check the ReplicaSets, scale the Deployment to 6 replicas, and show the pods running in the `intranet` namespace.

## 4
To roll back the `webservers` Deployment to its previous state, follow these steps:

### 1. Roll Back the `webservers` Deployment to the Previous State

To roll back the `webservers` Deployment in the `intranet` namespace to the previous state (before it was updated to use the `httpd` image), use the following `kubectl` command:

```bash
kubectl rollout undo deployment/webservers -n intranet
```

This command will undo the most recent update to the `webservers` Deployment, effectively rolling it back to the previous configuration, which should be using the `nginx` image.

### 2. Verify the Success of the Rollback by Retrieving the Container Image

To verify that the rollback was successful and that the `webservers` Deployment is now using the `nginx` image, describe the Deployment and check the container image. Use the following command:

```bash
kubectl describe deployment webservers -n intranet
```

Under the `Containers` section, you should see the container image as `nginx` (or the specific version you were using before the rollback).

### 3. Display the ReplicaSets in the `intranet` Namespace

After the rollback, the Deployment will manage a new ReplicaSet, so you can check the ReplicaSets in the `intranet` namespace to confirm:

```bash
kubectl get replicasets -n intranet
```

This will show the ReplicaSets, and you should see one associated with the previous configuration (likely using the `nginx` image).

### 4. Display the Pods in the `intranet` Namespace

Finally, to confirm that the pods have been rolled back and are now using the `nginx` image, check the status of the pods in the `intranet` namespace:

```bash
kubectl get pods -n intranet
```

The pods should reflect the updated configuration (using `nginx`).

### Summary of Commands:

```bash
kubectl rollout undo deployment/webservers -n intranet
kubectl describe deployment webservers -n intranet
kubectl get replicasets -n intranet
kubectl get pods -n intranet
```

These commands will roll back the `webservers` Deployment to its previous state, verify the container image change, display the updated ReplicaSets, and show the pods running in the `intranet` namespace.

## 5
To delete the namespaces `intranet` and `dev`, follow these steps:

### 1. Delete the `intranet` Namespace

To delete the `intranet` namespace, use the following `kubectl` command:

```bash
kubectl delete namespace intranet
```

This will delete the `intranet` namespace along with all resources (like Deployments, ReplicaSets, Pods) within it.

### 2. Delete the `dev` Namespace

Similarly, to delete the `dev` namespace, use the following command:

```bash
kubectl delete namespace dev
```

This will delete the `dev` namespace and all of its associated resources.

### 3. Display the Namespaces in the Cluster

To confirm that both namespaces have been deleted, use the following command to display the remaining namespaces:

```bash
kubectl get namespaces
```

This will list all namespaces currently in the cluster. After the deletion, the `intranet` and `dev` namespaces should no longer appear.

### Summary of Commands:

```bash
kubectl delete namespace intranet
kubectl delete namespace dev
kubectl get namespaces
```

These commands will delete the `intranet` and `dev` namespaces, and then show the remaining namespaces in the cluster.