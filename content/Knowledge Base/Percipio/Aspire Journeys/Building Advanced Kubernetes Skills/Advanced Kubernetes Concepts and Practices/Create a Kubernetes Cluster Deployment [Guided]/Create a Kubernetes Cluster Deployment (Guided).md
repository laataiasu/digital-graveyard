---
date: 1970-01-01
---

# Create a Kubernetes Cluster Deployment (Guided)

## 1
To complete the task, you will perform a series of steps to create, manage, and inspect a ReplicaSet in a Kubernetes cluster. Below are the commands and instructions based on the provided steps:

### 1. **Display the contents of the `rs.yaml` file**:
You are asked to view the contents of the `rs.yaml` file to examine the ReplicaSet configuration. To do so, use the `cat` command in the terminal:

```bash
cat rs.yaml
```

This command will print the contents of the `rs.yaml` file, which defines a ReplicaSet named `rs` with a pod running the `nginx` Docker container, and specifies 4 replicas.

### 2. **Review the ReplicaSet definition**:
From the output of the previous command, verify that the `rs.yaml` file defines the following fields:

- `apiVersion`: Defines the version of the API used (likely `apps/v1`).
- `kind`: Specifies the object type (in this case, `ReplicaSet`).
- `metadata`: Contains information like the name of the ReplicaSet (`rs`).
- `spec`: Defines the specifications of the ReplicaSet, including the number of replicas (4) and the pod template (which includes the `nginx` container).

### 3. **Print the contents to a file**:
To save the output to a file named `rs-review.txt`, run the following command:

```bash
cat rs.yaml > rs-review.txt
```

### 4. **Create the ReplicaSet**:
Next, you need to create the ReplicaSet by applying the `rs.yaml` file using `kubectl apply`. This will create the resources defined in the `rs.yaml` file:

```bash
kubectl apply -f rs.yaml
```

This will create the ReplicaSet in the Kubernetes cluster.

### 5. **Print the output to a file**:
To capture the output from the previous command in a file named `rs-replica-create.txt`, use this command:

```bash
kubectl apply -f rs.yaml > rs-replica-create.txt
```

### 6. **Display the ReplicaSets running in the cluster**:
To list all the ReplicaSets currently running in your cluster, use the `kubectl get replicasets` command:

```bash
kubectl get replicasets
```

This will show details about the ReplicaSets, including the one you just created (`rs`).

### 7. **Print the ReplicaSets report to a file**:
To save the output of the `kubectl get replicasets` command to a file named `replicasets-report.txt`, run:

```bash
kubectl get replicasets > replicasets-report.txt
```

### 8. **Display the pods running in the cluster**:
To list the pods running in the cluster, use the `kubectl get pods` command:

```bash
kubectl get pods
```

Identify one of the pod names from the list. Each pod created by the ReplicaSet will have a unique name, with a suffix that distinguishes them from each other.

### 9. **Delete a pod**:
To delete one of the pods (replace `<pod-name>` with the actual pod name from the previous step), run:

```bash
kubectl delete pod <pod-name>
```

### 10. **Verify the pod has been replaced**:
Since the ReplicaSet is configured to maintain 4 replicas, Kubernetes will automatically create a new pod to replace the one that was deleted. To verify this, run the `kubectl get pods` command again:

```bash
kubectl get pods
```

This should show a new pod with a different name but the same specifications as the deleted one.

### 11. **Print the final output to a file**:
Finally, save the updated list of pods to a file named `replicasets-renew-report.txt`:

```bash
kubectl get pods > replicasets-renew-report.txt
```

---

### Summary of Key Commands:
1. **View the contents of the `rs.yaml` file**:
   ```bash
   cat rs.yaml
   ```
2. **Print to `rs-review.txt`**:
   ```bash
   cat rs.yaml > rs-review.txt
   ```
3. **Create the ReplicaSet**:
   ```bash
   kubectl apply -f rs.yaml
   ```
4. **Print output to `rs-replica-create.txt`**:
   ```bash
   kubectl apply -f rs.yaml > rs-replica-create.txt
   ```
5. **List ReplicaSets**:
   ```bash
   kubectl get replicasets
   ```
6. **Print ReplicaSets to `replicasets-report.txt`**:
   ```bash
   kubectl get replicasets > replicasets-report.txt
   ```
7. **List Pods**:
   ```bash
   kubectl get pods
   ```
8. **Delete a pod**:
   ```bash
   kubectl delete pod <pod-name>
   ```
9. **Verify the pod replacement**:
   ```bash
   kubectl get pods
   ```
10. **Print final pod list to `replicasets-renew-report.txt`**:
    ```bash
    kubectl get pods > replicasets-renew-report.txt
    ```

By following these steps, you will have created the ReplicaSet, managed its pods, and saved the relevant outputs to the specified text files.

## 2
To complete this task, you'll follow a series of steps similar to the previous ReplicaSet task, but this time you will be working with a Deployment. Below are the instructions and commands to help you create and manage a Deployment using the `webservers.yaml` file.

### 1. **Display the contents of the `webservers.yaml` file**:
Use the `cat` command to display the contents of the `webservers.yaml` file, which defines a Deployment that includes a ReplicaSet.

```bash
cat webservers.yaml
```

### 2. **Review the Deployment definition**:
The `webservers.yaml` file should contain similar fields to the ReplicaSet file, but with the addition of a Deployment definition. A Deployment manages the creation and scaling of ReplicaSets. It will also define the desired state for the number of pods, container specifications, etc.

- **apiVersion**: Defines the Kubernetes API version (likely `apps/v1`).
- **kind**: Should be `Deployment`.
- **metadata**: Contains the name of the Deployment (likely `webservers`).
- **spec**: Defines the specifications, such as the number of replicas and the pod template (including container specifications like `nginx`).

### 3. **Print the contents to a file**:
To save the output of the `cat` command to a file named `webservers-review.txt`, run:

```bash
cat webservers.yaml > webservers-review.txt
```

### 4. **Create the Deployment**:
Next, you will create the Deployment using the `kubectl apply` command. This will create a ReplicaSet and the associated pods as defined in the `webservers.yaml` file.

```bash
kubectl apply -f webservers.yaml
```

### 5. **Print the output to a file**:
To capture the output of the command in a file named `webservers-deployment-create.txt`, run:

```bash
kubectl apply -f webservers.yaml > webservers-deployment-create.txt
```

### 6. **Display the pods running in the cluster**:
After creating the Deployment, you can view the status of the pods by using the `kubectl get pods` command. Pods in the process of being created may show a status of `ContainerCreating`.

```bash
kubectl get pods
```

### 7. **Print the pods report to a file**:
To save the output of the pods' status to a file named `webservers-pods-report.txt`, use:

```bash
kubectl get pods > webservers-pods-report.txt
```

If the status of any pods is `ContainerCreating`, wait a moment and run the command again to check when the pod reaches the `Running` status.

### 8. **Display the Deployments running in the cluster**:
To view the list of all deployments in the cluster, use:

```bash
kubectl get deployments
```

This should list the `webservers` Deployment you just created.

### 9. **Display the ReplicaSets running in the cluster**:
Since the Deployment automatically creates a ReplicaSet, you can display the ReplicaSets with the following command:

```bash
kubectl get replicasets
```

This should include a ReplicaSet created by the `webservers` Deployment.

### 10. **Print the ReplicaSets report to a file**:
To save the output of the `kubectl get replicasets` command to a file named `webservers-replicasets-report.txt`, run:

```bash
kubectl get replicasets > webservers-replicasets-report.txt
```

---

### Summary of Key Commands:
1. **View the contents of the `webservers.yaml` file**:
   ```bash
   cat webservers.yaml
   ```
2. **Print to `webservers-review.txt`**:
   ```bash
   cat webservers.yaml > webservers-review.txt
   ```
3. **Create the Deployment**:
   ```bash
   kubectl apply -f webservers.yaml
   ```
4. **Print output to `webservers-deployment-create.txt`**:
   ```bash
   kubectl apply -f webservers.yaml > webservers-deployment-create.txt
   ```
5. **List Pods**:
   ```bash
   kubectl get pods
   ```
6. **Print Pods report to `webservers-pods-report.txt`**:
   ```bash
   kubectl get pods > webservers-pods-report.txt
   ```
7. **List Deployments**:
   ```bash
   kubectl get deployments
   ```
8. **List ReplicaSets**:
   ```bash
   kubectl get replicasets
   ```
9. **Print ReplicaSets to `webservers-replicasets-report.txt`**:
   ```bash
   kubectl get replicasets > webservers-replicasets-report.txt
   ```

By following these steps, you will create the `webservers` Deployment, manage its pods, and save the relevant output to the specified text files.

## 3
To follow through with the task, you will perform a series of commands to update the `webservers` Deployment to use an `httpd` image instead of `nginx`, manage its rollout, scale the replicas, and gather information about the deployment. Here’s a step-by-step guide:

### 1. **Update the `webservers` Deployment to use an `httpd` image**:
You can update the `webservers` Deployment using the `kubectl set` command to specify a new container image. In this case, replace the `nginx` image with the `httpd` image.

```bash
kubectl set image deployment/webservers nginx=httpd
```

In this command:
- `nginx=httpd`: This updates the `nginx` container to use the `httpd` image instead.

### 2. **Retrieve the rollout status of the Deployment update**:
After updating the deployment, you can track the status of the update using the `kubectl rollout status` command.

```bash
kubectl rollout status deployment/webservers
```

This command will show the rollout progress and indicate whether the update was successful.

### 3. **Print the rollout status to a file**:
To save the output of the rollout status to a file named `deployment-rollout-status.txt`, use:

```bash
kubectl rollout status deployment/webservers > deployment-rollout-status.txt
```

### 4. **Retrieve the running configuration of the `webservers` Deployment**:
You can get detailed information about the current state of the `webservers` Deployment with the `kubectl describe` command. This will show you the configuration and status of the deployment, including any updates made.

```bash
kubectl describe deployment/webservers
```

### 5. **Print the configuration details to a file**:
To save the output of the `kubectl describe` command to a file named `deployment-updated-report.txt`, run:

```bash
kubectl describe deployment/webservers > deployment-updated-report.txt
```

### 6. **Increase the number of pod replicas in the `webservers` Deployment**:
To scale the `webservers` Deployment to have 4 replicas, use the `kubectl scale` command with the `--replicas=4` option:

```bash
kubectl scale deployment/webservers --replicas=4
```

This command will change the number of pods managed by the `webservers` Deployment to 4.

### 7. **Print the scaling report to a file**:
To save the scaling output to a file named `deployment-scale-report.txt`, use:

```bash
kubectl scale deployment/webservers --replicas=4 > deployment-scale-report.txt
```

### 8. **Display the pods running in the cluster**:
To see the status of the pods, including the ones created by the `webservers` Deployment, use:

```bash
kubectl get pods
```

This will list all the pods, including the newly scaled pods.

### 9. **Display the ReplicaSets running in the cluster**:
To view the ReplicaSets in the cluster (including the new and old ReplicaSets created during the update), use:

```bash
kubectl get replicasets
```

You should see two ReplicaSets: one representing the old version of the Deployment (with 0 replicas) and another representing the updated version with 4 replicas.

### 10. **Retrieve event information about the `webservers` Deployment**:
To gather information about the events, including the scaling up of the new ReplicaSet and the scaling down of the old ReplicaSet, use:

```bash
kubectl describe deployment/webservers
```

This will display the events related to the Deployment, such as pod creation and termination.

### 11. **Retrieve information about the strategy type of the `webservers` Deployment update**:
To view the strategy type used for the update (typically `RollingUpdate`), you can use the `kubectl describe` command combined with `grep` to filter the output:

```bash
kubectl describe deployment/webservers | grep -i strategy
```

This command filters the output for the strategy type (which may show `RollingUpdate` or `Recreate`).

### 12. **Print the strategy type to a file**:
To save the strategy type to a file named `deployment-strategy-type.txt`, use:

```bash
kubectl describe deployment/webservers | grep -i strategy > deployment-strategy-type.txt
```

### Summary of Key Commands:
1. **Update the Deployment image**:
   ```bash
   kubectl set image deployment/webservers nginx=httpd
   ```
2. **Get rollout status**:
   ```bash
   kubectl rollout status deployment/webservers
   ```
3. **Save rollout status to file**:
   ```bash
   kubectl rollout status deployment/webservers > deployment-rollout-status.txt
   ```
4. **Describe the Deployment**:
   ```bash
   kubectl describe deployment/webservers
   ```
5. **Save Deployment details to file**:
   ```bash
   kubectl describe deployment/webservers > deployment-updated-report.txt
   ```
6. **Scale the Deployment**:
   ```bash
   kubectl scale deployment/webservers --replicas=4
   ```
7. **Save scale report to file**:
   ```bash
   kubectl scale deployment/webservers --replicas=4 > deployment-scale-report.txt
   ```
8. **Get Pods**:
   ```bash
   kubectl get pods
   ```
9. **Get ReplicaSets**:
   ```bash
   kubectl get replicasets
   ```
10. **Describe the Deployment (events)**:
    ```bash
    kubectl describe deployment/webservers
    ```
11. **Get strategy type**:
    ```bash
    kubectl describe deployment/webservers | grep -i strategy
    ```
12. **Save strategy type to file**:
    ```bash
    kubectl describe deployment/webservers | grep -i strategy > deployment-strategy-type.txt
    ```

By following these steps, you will have updated the `webservers` Deployment, scaled its pods, and gathered the necessary information about its rollout, configuration, and strategy.

## 4
To roll back the webserver's deployment and verify the success of the rollback, here are the steps you can follow:

### 1. Rollback the Deployment
To rollback the `webservers` deployment to the previous version, run the following command:

```bash
kubectl rollout undo deployment webservers
```

This command will undo the most recent deployment change, reverting it to the previous version of the deployment.

### 2. Display the ReplicaSets
To display the ReplicaSets that are running in your cluster, use the following command:

```bash
kubectl get replicasets
```

This command will show all the ReplicaSets in your cluster, along with their current states and the associated deployments.

### 3. Display the Pods
To display the pods running in your cluster, use this command:

```bash
kubectl get pods
```

This will list all the pods running in the cluster, along with their statuses.

### 4. Verify the Success of the Rollback
To verify that the rollback was successful, check the details of the `webservers` deployment. Specifically, you want to check which image is being used by the deployment. Use the following command:

```bash
kubectl describe deployment webservers | grep "Image"
```

This will retrieve the image information from the `webservers` deployment and confirm that the rollback has reverted the image to the previous version.

### 5. Save the Output to a File
If you want to save the output to a file named `deployment-image.txt`, you can redirect the output to a file like this:

```bash
kubectl describe deployment webservers | grep "Image" > deployment-image.txt
```

This command will write the image details from the `webservers` deployment to the `deployment-image.txt` file.

### Summary
- **Rollback Deployment**: `kubectl rollout undo deployment webservers`
- **Get ReplicaSets**: `kubectl get replicasets`
- **Get Pods**: `kubectl get pods`
- **Verify Rollback**: `kubectl describe deployment webservers | grep "Image"`
- **Save Output**: `kubectl describe deployment webservers | grep "Image" > deployment-image.txt`

These steps will allow you to roll back the deployment, check the ReplicaSets and Pods, and verify the rollback success by inspecting the image being used in the deployment.

## 5
To delete the `webservers` deployment and gather information about the status of the pods and deployments in your Kubernetes cluster, here are the detailed steps:

### 1. Delete the `webservers` Deployment
To delete the `webservers` deployment, use the `kubectl delete` command:

```bash
kubectl delete deployment webservers
```

This command will delete the `webservers` deployment from the cluster. Once the deployment is deleted, the ReplicaSet that was associated with it will also be removed, and any pods that were part of the deployment will be terminated.

### 2. Display the Pods
After the deployment is deleted, you can check the status of the remaining pods in the cluster:

```bash
kubectl get pods
```

If you see that any pod has a **Terminating** status, it means that the pod is in the process of being removed. In such cases, you should run the `kubectl get pods` command again to check whether the pod has been fully terminated:

```bash
kubectl get pods
```

If a pod is still in the terminating state after the first check, you can continue running this command to monitor the status until it completes the termination process.

### 3. Save the Pod Information to a File
To save the output of the `kubectl get pods` command to a file named `pods-delete-report.txt`, run the following command:

```bash
kubectl get pods > pods-delete-report.txt
```

This will save the current status of all pods in the cluster, including the terminated ones, to the file `pods-delete-report.txt`.

### 4. Display the Deployments
To display the deployments still running in the cluster, use this command:

```bash
kubectl get deployments
```

This will show all deployments currently running in the cluster. Since the `webservers` deployment was deleted, it should no longer appear in the list.

### 5. Save the Deployment Information to a File
To save the output of the `kubectl get deployments` command to a file named `deployments-delete-report.txt`, run the following command:

```bash
kubectl get deployments > deployments-delete-report.txt
```

This will write the list of current deployments (which should not include `webservers` anymore) to the `deployments-delete-report.txt` file.

### Summary of Commands:
1. **Delete the Deployment**:  
   ```bash
   kubectl delete deployment webservers
   ```

2. **Get Pods**:  
   ```bash
   kubectl get pods
   ```

3. **Save Pod Info**:  
   ```bash
   kubectl get pods > pods-delete-report.txt
   ```

4. **Get Deployments**:  
   ```bash
   kubectl get deployments
   ```

5. **Save Deployment Info**:  
   ```bash
   kubectl get deployments > deployments-delete-report.txt
   ```

These steps will help you delete the deployment, monitor the pods' termination status, and save the output for further review.