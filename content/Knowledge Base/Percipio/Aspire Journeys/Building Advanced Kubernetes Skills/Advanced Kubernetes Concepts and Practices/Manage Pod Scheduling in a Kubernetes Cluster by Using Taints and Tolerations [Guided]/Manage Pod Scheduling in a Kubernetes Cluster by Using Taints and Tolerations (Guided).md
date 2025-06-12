# Manage Pod Scheduling in a Kubernetes Cluster by Using Taints and Tolerations (Guided)

## 1
To apply a taint to a node in your Kubernetes cluster, follow these steps:

### Step 1: Display the Nodes in the Cluster
1. **SSH into `k8s-master1`** using MobaXterm.
   - Use the **administrator** credentials (`Passw0rd!`) when prompted.
   - In MobaXterm, double-click the `k8s-master1` session, and when asked for the password, enter `Passw0rd!`.

2. Once logged into `k8s-master1`, **display the nodes in the cluster** by running the following command:

   ```bash
   kubectl get nodes
   ```

   This will show all the nodes in the cluster, and you'll see the status of each node (e.g., **Ready** or **NotReady**).

### Step 2: Apply the Taint to the `k8s-worker3` Node
3. Now, apply the **taint** to the `k8s-worker3` node by running the following `kubectl taint` command:

   ```bash
   kubectl taint node k8s-worker3 memory=large:NoSchedule
   ```

   - **Taint**: `memory=large:NoSchedule` ensures that **no new pods** will be scheduled on `k8s-worker3` unless they **tolerate** this taint.
   - **memory=large** is a key-value pair. The key here is "memory" and the value is "large", indicating the resource feature.
   - **NoSchedule** is the effect that will prevent pods that don't have a matching toleration from being scheduled on this node.

### Step 3: Verify the Taint on `k8s-worker3`
4. To **verify the taint** has been applied correctly, run the following command:

   ```bash
   kubectl describe node k8s-worker3 | grep Taints
   ```

   Alternatively, you can run:

   ```bash
   kubectl describe node k8s-worker3
   ```

   This command will display all the details of the `k8s-worker3` node, including the taints. The relevant section will look like this:

   ```
   Taints:             memory=large:NoSchedule
   ```

   This indicates that the taint `memory=large:NoSchedule` has been applied to the `k8s-worker3` node.

### Taint Effects
- **NoSchedule**: Prevents new pods from being scheduled on this node unless they tolerate the taint.
- **PreferNoSchedule**: Tries to avoid scheduling new pods on this node unless they tolerate the taint.
- **NoExecute**: Evicts existing pods that do not tolerate the taint, and prevents new pods from being scheduled.

### Summary
- You've applied a taint to the `k8s-worker3` node to prevent new pods from being scheduled on it unless they have a matching toleration.
- You verified the taint using `kubectl describe node`.

Let me know if you need further clarification or assistance!

## 2
### Steps to Download the YAML File, Create the Deployment, and Check Pod Distribution:

#### Step 1: Download the `web.deployment.yaml` File

1. **SSH into the `k8s-master1` node** via MobaXterm if you haven't already.

2. Use the `wget` command to download the `web.deployment.yaml` file. Run the following command:

   ```bash
   wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/web.deployment.yaml
   ```

   This will download the file to your current directory on the `k8s-master1` node.

#### Step 2: Create the Deployment from the YAML File

3. Now, use the `kubectl create` command to create a **Deployment** in your Kubernetes cluster by referencing the downloaded YAML file. Run the following command:

   ```bash
   kubectl create -f web.deployment.yaml
   ```

   - The `-f` flag tells `kubectl` to apply the configuration file specified (`web.deployment.yaml`).
   - The Deployment defined in the file will create a **webserver** Deployment with six replica pods running an NGINX web server.

#### Step 3: Display the Pods and Their Node Distribution

4. To see where the pods from the `webserver` Deployment are running, use the following command:

   ```bash
   kubectl get pods -o wide
   ```

   - The `-o wide` flag will show additional information, such as the node each pod is running on.
   
   Example output:
   
   ```
   NAME                         READY   STATUS    RESTARTS   AGE   IP            NODE        NOMINATED NODE   READINESS GATES
   webserver-6df9f84c57-7nxlw    1/1     Running   0          5m    10.244.0.10   k8s-worker1   <none>           <none>
   webserver-6df9f84c57-2pm3f    1/1     Running   0          5m    10.244.0.11   k8s-worker2   <none>           <none>
   webserver-6df9f84c57-8b2wp    1/1     Running   0          5m    10.244.0.12   k8s-worker2   <none>           <none>
   webserver-6df9f84c57-5pckf    1/1     Running   0          5m    10.244.0.13   k8s-worker1   <none>           <none>
   webserver-6df9f84c57-4bp7t    1/1     Running   0          5m    10.244.0.14   k8s-worker2   <none>           <none>
   webserver-6df9f84c57-jq5nw    1/1     Running   0          5m    10.244.0.15   k8s-worker1   <none>           <none>
   ```

   - You will see that the `webserver` pods are running on **k8s-worker1** and **k8s-worker2**.
   - **k8s-worker3** will not have any of these pods because it **repels** the `webserver` pods. The pods do not have a **toleration** for the taint `memory=large:NoSchedule` applied to `k8s-worker3`.

#### Step 4: Understand Why the Pods Don't Run on `k8s-worker3`

5. As described, `k8s-worker3` has the taint `memory=large:NoSchedule`. The **webserver** pods created by the deployment do not have a **toleration** for this taint, so they will not be scheduled on `k8s-worker3`.

   To allow the `webserver` pods to run on `k8s-worker3`, you would need to add a toleration to the pods in the deployment definition. But, since the question only asks for you to see the distribution, the pods will not be running on `k8s-worker3` unless the toleration is added.

---

### Summary
- You downloaded the `web.deployment.yaml` file.
- You created a Deployment from that file which launched six NGINX webserver pods.
- You verified the pods' node distribution using `kubectl get pods -o wide`.
- The pods are running on `k8s-worker1` and `k8s-worker2`, not on `k8s-worker3`, because `k8s-worker3` has a taint (`memory=large:NoSchedule`) that prevents the pods from being scheduled there.

Let me know if you need further assistance!

## 3
### Steps to Download the YAML File, Display Tolerations, Create the Deployment, and Check Pod Distribution:

#### Step 1: Download the `db.deployment.yaml` File

1. **SSH into the `k8s-master1` node** via MobaXterm, if you haven't already.

2. Use the `wget` command to download the `db.deployment.yaml` file. Run the following command:

   ```bash
   wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/db.deployment.yaml
   ```

   This will download the file to your current directory on the `k8s-master1` node.

#### Step 2: Display the Tolerations in the `db.deployment.yaml` File

3. Once the file is downloaded, use the `cat` command to display its contents and check for tolerations.

   ```bash
   cat db.deployment.yaml
   ```

   In the output, look for the `tolerations` section. This section will define the tolerations the pods in the `db` Deployment need to run on tainted nodes (like `k8s-worker3`). The `tolerations` in the `db.deployment.yaml` file should look something like this:

   ```yaml
   tolerations:
   - key: "memory"
     operator: "Equal"
     value: "large"
     effect: "NoSchedule"
   ```

   - This toleration matches the taint `memory=large:NoSchedule` applied to the `k8s-worker3` node.

#### Step 3: Create the `db` Deployment

4. Now, use the `kubectl create` command to create the **Deployment** using the `db.deployment.yaml` file:

   ```bash
   kubectl create -f db.deployment.yaml
   ```

   This command will create a Deployment defined in the `db.deployment.yaml` file. The Deployment will include replica pods that can tolerate the taint on `k8s-worker3`.

#### Step 4: Display the Pods and Their Node Distribution

5. To see where the pods from the `db` Deployment are running, use the following command:

   ```bash
   kubectl get pods -o wide
   ```

   - The `-o wide` flag will show additional information, such as the node each pod is running on.

   Example output might look like this:

   ```
   NAME                          READY   STATUS    RESTARTS   AGE   IP            NODE        NOMINATED NODE   READINESS GATES
   db-deployment-7bc7c7f9c8-9fkw7 1/1     Running   0          3m    10.244.1.10   k8s-worker1   <none>           <none>
   db-deployment-7bc7c7f9c8-5bdl2 1/1     Running   0          3m    10.244.1.11   k8s-worker2   <none>           <none>
   db-deployment-7bc7c7f9c8-2b5gk 1/1     Running   0          3m    10.244.1.12   k8s-worker3   <none>           <none>
   ```

   - You will see the `db-deployment` pods running across the nodes, including `k8s-worker3`, because the pods have a **toleration** that matches the taint on `k8s-worker3`.
   - Since the pods can tolerate the taint `memory=large:NoSchedule`, they may run on any node that has the matching taint or no taint at all.

#### Explanation of Taint and Toleration

- **Taint**: A taint on a node (like `memory=large:NoSchedule` on `k8s-worker3`) prevents pods without the matching **toleration** from being scheduled on that node.
  
- **Toleration**: The toleration in the `db.deployment.yaml` allows the `db` pods to run on nodes with the taint `memory=large:NoSchedule`.

- A **taint** does not force a pod to run on a specific node, it just blocks pods from running on the node unless the pod has a **matching toleration**.

---

### Summary
- You downloaded the `db.deployment.yaml` file.
- You checked the **tolerations** in the file to confirm it matches the taint on `k8s-worker3`.
- You created the `db` Deployment using `kubectl create -f db.deployment.yaml`.
- You verified the pod distribution across the nodes using `kubectl get pods -o wide`.
- The `db` Deployment pods can run on `k8s-worker3` because they tolerate its taint.

Let me know if you need further assistance!

## 4
### Steps to Evict a Pod from `k8s-worker2` Node:

#### Step 1: Apply the Taint to the `k8s-worker2` Node

1. **SSH into the `k8s-master1` node** (if not already connected).
2. **Apply the taint** `diskType=ssd:NoExecute` to the `k8s-worker2` node using the following `kubectl taint` command:

   ```bash
   kubectl taint nodes k8s-worker2 diskType=ssd:NoExecute
   ```

   This taint will prevent any pods from running on `k8s-worker2` unless the pods have a toleration that matches this taint. Additionally, any pods that are already running on `k8s-worker2` and do not have the matching toleration will be evicted immediately due to the `NoExecute` effect.

#### Step 2: Verify the Taint on `k8s-worker2`

3. To check that the taint has been applied to `k8s-worker2`, run the following command:

   ```bash
   kubectl describe node k8s-worker2 | grep Taints
   ```

   You should see the following output, indicating that the taint has been successfully applied:

   ```bash
   Taints:             diskType=ssd:NoExecute
   ```

   This confirms that the node `k8s-worker2` now has a taint that will prevent pods without the appropriate toleration from running on it.

#### Step 3: Display the Nodes and Pod Distribution

4. To see the effect of the taint on the pods, display the nodes where the pods are running using the following command:

   ```bash
   kubectl get pods -o wide
   ```

   - Any pods that were previously running on `k8s-worker2` will be **evicted** and will no longer appear as running on that node.
   - The pods that do not have the toleration for the `diskType=ssd:NoExecute` taint will have been rescheduled on other nodes (or will be pending if no suitable node is available).

   Example output:

   ```bash
   NAME                          READY   STATUS    RESTARTS   AGE   IP            NODE
   db-deployment-7bc7c7f9c8-9fkw7 1/1     Running   0          5m    10.244.1.10   k8s-worker1
   db-deployment-7bc7c7f9c8-5bdl2 1/1     Running   0          5m    10.244.1.11   k8s-worker3
   db-deployment-7bc7c7f9c8-2b5gk 1/1     Evicted   0          5m    10.244.1.12   k8s-worker2
   ```

   In this example, the pod `db-deployment-7bc7c7f9c8-2b5gk` was running on `k8s-worker2` but has been evicted due to the new taint. It has been moved to another node or removed from the cluster if no suitable nodes exist.

#### Step 4: Confirm Eviction

5. If you see any `Evicted` pods, it means those pods did not have the appropriate toleration for the taint applied to `k8s-worker2`. These pods will be re-scheduled according to the pod's toleration configuration or may stay in the evicted state if no appropriate node is available.

#### Explanation of `NoExecute` Taint Effect

- The `NoExecute` effect of a taint not only prevents new pods from being scheduled onto the node but also **evicts** any existing pods that are already running on that node and do not have a matching toleration.
- The **toleration** for `diskType=ssd:NoExecute` is required for any pod to stay on `k8s-worker2` after the taint is applied.

---

### Summary of Steps:
1. **Applied the taint** `diskType=ssd:NoExecute` to `k8s-worker2`.
2. **Verified** that the taint is applied using `kubectl describe`.
3. **Checked** the node and pod distribution with `kubectl get pods -o wide`, confirming that pods without the toleration on `k8s-worker2` were evicted.
4. **Understood** that the `NoExecute` taint causes both the prevention of new pods and eviction of running pods that don't match the taint's toleration.

Let me know if you need more assistance!

## 5
### Steps to Remove a Taint from `k8s-master1` Node and Scale a Deployment:

#### Step 1: Display the Current Taints on `k8s-master1`

1. To view the current taints applied to `k8s-master1`, use the following command:

   ```bash
   kubectl describe node k8s-master1 | grep Taints
   ```

2. You should see the output showing the default taint on the `k8s-master1` node, which typically looks like this:

   ```bash
   Taints:             node-role.kubernetes.io/master:NoSchedule
   ```

   This taint is preventing any pods from being scheduled on `k8s-master1`, except for the control plane processes.

#### Step 2: Remove the Taint from `k8s-master1`

3. To remove the taint that is preventing pods from being scheduled on `k8s-master1`, run the following command:

   ```bash
   kubectl taint node k8s-master1 node-role.kubernetes.io/master:NoSchedule-
   ```

   The `-` at the end of the taint command removes the taint from the node.

4. After removing the taint, the `kubectl describe node k8s-master1` command should no longer show the taint under the "Taints" section, and the node will be available for scheduling pods.

   The output should no longer list the taint:

   ```bash
   Taints:             <empty>
   ```

   This confirms that the taint has been successfully removed from `k8s-master1`.

#### Step 3: Scale the `db` Deployment to 12 Replicas

5. Now that `k8s-master1` is available for scheduling, scale the `db` Deployment to 12 replicas. Use the `kubectl scale` command with the `--replicas` flag:

   ```bash
   kubectl scale deployment db --replicas=12
   ```

   This command will increase the number of replicas for the `db` Deployment to 12.

#### Step 4: Display the Nodes Where Pods Are Running

6. To see where the pods from the `db` Deployment are running after scaling, run the following command:

   ```bash
   kubectl get pods -o wide
   ```

   You will see the newly scaled pods running on the available nodes, including potentially `k8s-master1` now that the taint has been removed.

   Example output might look like this:

   ```bash
   NAME                                READY   STATUS    RESTARTS   AGE   IP            NODE
   db-deployment-7bc7c7f9c8-2fdlv      1/1     Running   0          2m    10.244.1.10   k8s-worker1
   db-deployment-7bc7c7f9c8-9h3kd      1/1     Running   0          2m    10.244.1.11   k8s-worker2
   db-deployment-7bc7c7f9c8-6ckpw      1/1     Running   0          2m    10.244.1.12   k8s-master1
   db-deployment-7bc7c7f9c8-98bkj      1/1     Running   0          2m    10.244.1.13   k8s-master1
   ...
   ```

   After removing the taint, you'll see that some pods may now be scheduled on `k8s-master1`, in addition to the worker nodes.

### Summary of Actions:
1. **Removed the taint** `node-role.kubernetes.io/master:NoSchedule` from `k8s-master1` to allow pods to be scheduled on the master node.
2. **Scaled** the `db` Deployment to 12 replicas, which will now be scheduled across available nodes, including `k8s-master1`.
3. **Verified** the pod distribution with `kubectl get pods -o wide`.

Let me know if you need further clarification!
