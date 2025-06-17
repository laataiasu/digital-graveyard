---
date: 1970-01-01
---

# Can You Manage Pod Scheduling in a Kubernetes Cluster [Advanced]

## 1
To create a DaemonSet in a Kubernetes cluster, you will need to follow these steps:

### 1. SSH into the `k8s-master1` node
You will be working directly on the `k8s-master1` node using the `kubectl` command. First, SSH into the node using the following information:

- Host: `k8s-master1`
- Username: `administrator`
- Password: `Passw0rd!`

You can use an SSH client like MobaXterm to establish the connection.

### 2. Download the DaemonSet YAML Definition
You need to download the `logger.daemonset.yaml` file from the provided URL using the `wget` command.

In your terminal, use the following command to download the YAML file:

```bash
wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/logger.daemonset.yaml
```

This will fetch the `logger.daemonset.yaml` file into your current directory.

### 3. Review the YAML File (Optional)
Before creating the DaemonSet, you can optionally review the contents of the file to ensure it is correct. You can do this by running:

```bash
cat logger.daemonset.yaml
```

This file will define the specifications for the DaemonSet you will create.

### 4. Create the DaemonSet
Now that you have the YAML file, you can use the `kubectl` command to create the DaemonSet in your Kubernetes cluster. Run the following command:

```bash
kubectl create -f logger.daemonset.yaml
```

This command will create the DaemonSet resource in your cluster using the definitions in the `logger.daemonset.yaml` file.

### 5. Verify the DaemonSet is Created
To confirm that the DaemonSet has been successfully created and is running, use the following command:

```bash
kubectl get daemonsets
```

This will list all DaemonSets running in the cluster. You should see `logger` in the list of DaemonSets.

### 6. Check the Pods Created by the DaemonSet
To verify that the DaemonSet has created the expected pods on each node, you can run:

```bash
kubectl get pods -l name=logger
```

This will list all pods created by the `logger` DaemonSet.

### Summary of Commands:

1. SSH into `k8s-master1`.
2. Download the YAML file:
   ```bash
   wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/logger.daemonset.yaml
   ```
3. Create the DaemonSet:
   ```bash
   kubectl create -f logger.daemonset.yaml
   ```
4. Verify the DaemonSet:
   ```bash
   kubectl get daemonsets
   ```
5. (Optional) Verify the pods:
   ```bash
   kubectl get pods -l name=logger
   ```

By following these steps, you will successfully create and verify the DaemonSet in your Kubernetes cluster.

## 2
To schedule pods using `nodeSelector` and address the issue of the database replica pods being in a pending state, follow these steps:

### Step 1: Download the `ssd.deployment.yaml` file
Start by downloading the `ssd.deployment.yaml` file, which contains the Deployment definition, including the `nodeSelector` configuration. To do this, use the following `wget` command:

```bash
wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/ssd.deployment.yaml
```

### Step 2: Review the `ssd.deployment.yaml` file
Once the file is downloaded, review its contents to understand the `nodeSelector` configuration. The `nodeSelector` ensures that the pods are scheduled only on nodes with the specified label.

To view the file's contents, use:

```bash
cat ssd.deployment.yaml
```

Look for a section like the following inside the file:

```yaml
spec:
  template:
    spec:
      nodeSelector:
        diskType: ssd
```

This `nodeSelector` is specifying that the pods should be scheduled only on nodes labeled with `diskType=ssd`.

### Step 3: Create the Deployment
Create the Deployment by applying the `ssd.deployment.yaml` file using `kubectl`:

```bash
kubectl apply -f ssd.deployment.yaml
```

This will create the deployment and attempt to schedule the pods according to the `nodeSelector` configuration.

### Step 4: Display the Running Pods
To verify the status of the pods that have been scheduled, run:

```bash
kubectl get pods
```

This will display the list of pods. If any of the database replica pods are in a **pending** state, you may need to address the issue of insufficient resources or node labeling.

### Step 5: Investigate Why Database Replica Pods are in a Pending State
If the database replica pods are still in a **pending** state, one of the following reasons might be the cause:

1. **Insufficient RAM**: The cluster nodes may not have enough resources (RAM) to schedule the pods.
2. **NodeSelector Issue**: The pods are likely not scheduled because the `nodeSelector` specifies that they should run only on nodes with the `diskType=ssd` label, and no nodes are labeled with this key-value pair.
3. **No Matching Nodes**: The cluster nodes might not have the correct label (`diskType=ssd`) as required by the `nodeSelector`.

### Step 6: Add the `diskType=ssd` Label to a Node
If the issue is that no nodes have the required label, you need to add the `diskType=ssd` label to a node (e.g., `k8s-worker3`). You can add the label with the following command:

```bash
kubectl label nodes k8s-worker3 diskType=ssd
```

This will add the `diskType=ssd` label to the `k8s-worker3` node, which will allow the pods with the `nodeSelector: diskType=ssd` to be scheduled on it.

### Step 7: Verify the Pods Again
After adding the label, you can verify if the pods are scheduled correctly by running:

```bash
kubectl get pods
```

This will show if the pods are now in the **Running** state or still in the **Pending** state.

### Summary of Steps:

1. **Download the Deployment definition**:
   ```bash
   wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/ssd.deployment.yaml
   ```

2. **Review the `nodeSelector`**:
   ```bash
   cat ssd.deployment.yaml
   ```

3. **Create the Deployment**:
   ```bash
   kubectl apply -f ssd.deployment.yaml
   ```

4. **Check the status of the pods**:
   ```bash
   kubectl get pods
   ```

5. **Add the label to `k8s-worker3` node**:
   ```bash
   kubectl label nodes k8s-worker3 diskType=ssd
   ```

6. **Verify the pods again**:
   ```bash
   kubectl get pods
   ```

By following these steps, the pods should now be scheduled correctly based on the `nodeSelector`, and the database replica pods should no longer be in the **Pending** state.

## 3
To schedule a pod using **node affinity** and resolve the issue of the `nginx` pod being in the **Pending** state, follow these steps:

### Step 1: Download the `required.affinity.pod.yaml` file
You need to first download the pod definition file, which includes the node affinity configuration. Use the following command to download the file:

```bash
wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/required.affinity.pod.yaml
```

### Step 2: Display the Contents of the YAML File
After downloading the file, you should inspect its contents to understand how node affinity is being configured. You can display the content using:

```bash
cat required.affinity.pod.yaml
```

Inside the YAML file, look for the `affinity` section, which specifies the **node affinity** rules. It will look something like this:

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: zone
            operator: In
            values:
            - west
```

In this example, the pod will only be scheduled on nodes that have the label `zone=west`.

### Step 3: Create the Pod
Now, you can create the pod named `nginx` using the `kubectl apply` command with the downloaded YAML file:

```bash
kubectl apply -f required.affinity.pod.yaml
```

This will create the pod according to the configuration, which includes node affinity.

### Step 4: Display the Pods in the Cluster
To see the status of the pod and other pods running in the cluster, use the following command:

```bash
kubectl get pods
```

If the pod is in a **Pending** state, you will need to investigate further.

### Step 5: Investigate Why the Pod is in the Pending State
If the pod is still in the **Pending** state, the most likely reason is that there are no nodes with the label `zone=west`. The **node affinity** configuration specifies that the pod should only be scheduled on nodes that have this label, but if no nodes have it, the pod cannot be scheduled and will remain pending.

### Step 6: Update the `k8s-worker3` Node
To resolve this issue, you need to add the `zone=west` label to the `k8s-worker3` node. You can do this using the following command:

```bash
kubectl label nodes k8s-worker3 zone=west
```

This will label the `k8s-worker3` node with `zone=west`, which should satisfy the **node affinity** requirement for the pod.

### Step 7: Verify the Pod's Status Again
After labeling the node, check the status of the pods again:

```bash
kubectl get pods
```

This should show that the `nginx` pod has been scheduled and is now running if the labeling was successful.

### Summary of Steps:

1. **Download the YAML file**:
   ```bash
   wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/required.affinity.pod.yaml
   ```

2. **Display the contents of the YAML file**:
   ```bash
   cat required.affinity.pod.yaml
   ```

3. **Create the pod**:
   ```bash
   kubectl apply -f required.affinity.pod.yaml
   ```

4. **Check the pod status**:
   ```bash
   kubectl get pods
   ```

5. **Add the label to `k8s-worker3` node**:
   ```bash
   kubectl label nodes k8s-worker3 zone=west
   ```

6. **Verify the pod's status again**:
   ```bash
   kubectl get pods
   ```

### Conclusion
The pod was in the **Pending** state because no node matched the affinity rule (`zone=west`). Once the `k8s-worker3` node was labeled with `zone=west`, the pod should be scheduled and run properly.
