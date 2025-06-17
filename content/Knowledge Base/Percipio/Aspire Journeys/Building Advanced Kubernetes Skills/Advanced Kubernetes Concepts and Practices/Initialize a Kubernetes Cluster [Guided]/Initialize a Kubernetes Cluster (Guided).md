---
date: 1970-01-01
---

# Initialize a Kubernetes Cluster (Guided)

## 1
To establish the Kubernetes control plane and initialize the cluster on `k8s-master1` using `kubeadm`, follow the steps outlined below:

### Step 1: Launch MobaXterm and Open a New SSH Session
1. **Open MobaXterm** on your machine.
2. In the **User sessions** section of MobaXterm, double-click on `k8s-master1` to start an SSH session.
3. When prompted for a password, enter **`Passw0rd!`** and press **Enter**.
   - Note that you won't see the password as you type.
4. When asked whether to save the password, select **No**.

Repeat this process for the `k8s-worker1` and `k8s-worker2` virtual machines.

### Step 2: Initialize the Kubernetes Control Plane on `k8s-master1`
Now that you're logged into `k8s-master1`, you can initialize the Kubernetes control plane using `kubeadm`:

1. Run the following command to initialize the Kubernetes control plane with Flannel overlay network settings:

   ```bash
   sudo kubeadm init --pod-network-cidr=10.244.0.0/16
   ```

2. **Enter the sudo password** (`Passw0rd!`) when prompted and press **Enter**.

### Step 3: Wait for Initialization to Complete
- The initialization process will take some time as it performs pre-flight checks, generates certificates, and creates manifest files.
- Once the initialization is complete, you'll see **bootstrap token** information on the terminal. **Keep this information handy**, as you'll need it to join the worker nodes (`k8s-worker1` and `k8s-worker2`) to the cluster.

### Step 4: Note Important Commands
- The initialization process will output commands that you need to run on the worker nodes to join them to the cluster. You may also see instructions for setting up the Kubernetes kubeconfig file on the master node to manage the cluster.

### Next Steps
After the cluster has been initialized, you'll need to install the Flannel network plugin and join the worker nodes to the cluster. Follow the instructions displayed after the `kubeadm init` command completes.

Let me know if you need further assistance!

## 2

To successfully join `k8s-worker1` and `k8s-worker2` to the Kubernetes cluster, follow these detailed steps:

### Step 1: Copy the Bootstrap Token from `k8s-master1`
1. **Locate the Bootstrap Token**: After initializing the cluster on `k8s-master1`, the last two lines of the output will contain the bootstrap token and join command. The output will look something like this:
   ```
   kubeadm join k8s-master1:6443 --token <your_token> --discovery-token-ca-cert-hash sha256:<hash>
   ```
   
2. **Select and Copy the Token**: In MobaXterm, select the last two lines of the output that contain the `kubeadm join` command with the token. This copy action is implicit as you highlight the text.

3. **Open Notepad**: On your local machine, open **Notepad**.

4. **Paste the Token Information**: Right-click in Notepad and select **Paste**, or use `Ctrl+V` to paste the copied token information.

5. **Save the File**: Save the file as `token.txt` on your **Desktop** for later use.

### Step 2: Join `k8s-worker1` to the Cluster
1. **SSH into `k8s-worker1`**: Open an SSH session to the `k8s-worker1` virtual machine in MobaXterm.

2. **Enter Root User Shell**: Run the following command to open an interactive root shell:
   ```bash
   sudo -i
   ```
   Enter the password **`Passw0rd!`** when prompted.

3. **Paste the Bootstrap Token**: In the terminal, right-click to paste the `kubeadm join` command you copied from `k8s-master1` (which includes the token). The command will look similar to this:
   ```bash
   kubeadm join k8s-master1:6443 --token <your_token> --discovery-token-ca-cert-hash sha256:<hash>
   ```
   
4. **Confirm the Join**: You will see a confirmation message indicating that `k8s-worker1` has successfully joined the Kubernetes cluster. The message should look like:
   ```
   This node has joined the cluster:
     * The cluster control plane has been updated with this node
     * The node is now a part of the cluster
   ```

5. **Exit the Root Shell**: After successfully joining the cluster, type `exit` to leave the root subshell and return to the regular user prompt.

### Step 3: Join `k8s-worker2` to the Cluster
1. **SSH into `k8s-worker2`**: Open a new SSH session to the `k8s-worker2` virtual machine.

2. **Enter Root User Shell**: Run the following command to enter an interactive root shell:
   ```bash
   sudo -i
   ```
   Again, enter **`Passw0rd!`** when prompted.

3. **Paste the Bootstrap Token**: Paste the same `kubeadm join` command (with the token) into the terminal by right-clicking to paste.

4. **Confirm the Join**: After pasting the join command, you should see the same success message indicating that `k8s-worker2` has successfully joined the Kubernetes cluster.

5. **Exit the Root Shell**: Once `k8s-worker2` has joined the cluster, type `exit` to exit the root subshell.

### Step 4: Verify Cluster Nodes
1. **Return to `k8s-master1`**: Switch back to your SSH session on `k8s-master1`.

2. **Verify Node Status**: Run the following `kubectl` command to confirm that all worker nodes have successfully joined the cluster:
   ```bash
   kubectl get nodes
   ```
   You should see `k8s-master1`, `k8s-worker1`, and `k8s-worker2` listed as nodes in the cluster.

### Final Notes:
- **All cluster operations** can now be performed from `k8s-master1`.
- You have successfully initialized the Kubernetes cluster on the master node and added the worker nodes (`k8s-worker1` and `k8s-worker2`) to the cluster.

Let me know if you need further help!

## 3
To configure the Kubernetes CLI (`kubectl`) on `k8s-master1` so that the administrator can manage the cluster, follow these detailed steps:

### Step 1: Change to the Home Directory
1. First, ensure that you are in the **home directory** of the administrator by running the following command:

   ```bash
   cd ~
   ```

   The `~` symbol refers to the current user's home directory, ensuring you are in the correct location.

### Step 2: Create a Hidden Directory for Kubernetes Configuration
2. Create a **hidden directory** named `.kube` in the administrator's home directory. This directory will store the Kubernetes configuration files, including the kubeconfig file used by `kubectl`:

   ```bash
   mkdir -p $HOME/.kube
   ```

   - The `-p` flag ensures that the command will create the `.kube` directory if it doesn't already exist.

### Step 3: Copy the Kubernetes Admin Configuration File
3. Copy the `/etc/kubernetes/admin.conf` file to the newly created `.kube/config` file in the home directory:

   ```bash
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   ```

   - The `-i` flag ensures you are prompted for confirmation before overwriting the file, though in most cases, this should not be necessary.
   - You will be prompted to enter **`Passw0rd!`** as the sudo password. Enter the password and press **Enter**.

### Step 4: Change Ownership of the Configuration File
4. Now, change the **ownership** of the `.kube/config` file to the administrator user to allow non-root access for `kubectl` commands:

   ```bash
   sudo chown administrator:administrator $HOME/.kube/config
   ```

   - This command sets both the **user** and **group** ownership of the configuration file to `administrator`. This allows the `administrator` user to read and write to the file.

### Step 5: Verify the Configuration
5. After completing these steps, you can use `kubectl` as the administrator to interact with the Kubernetes cluster. For example, you can run:

   ```bash
   kubectl get nodes
   ```

   This command should return a list of nodes in the cluster, including `k8s-master1`, `k8s-worker1`, and `k8s-worker2`.

### Summary
- You have set up the **Kubernetes configuration** file (`admin.conf`) for the administrator user, allowing `kubectl` commands to be run as a non-root user.
- The configuration file is now located in `~/.kube/config`, and the correct file ownership has been set.

Let me know if you need further assistance!

## 4
To install the Flannel overlay network and ensure that your Kubernetes cluster nodes are in a **Ready** state, follow these steps:

### Step 1: Display the Current Cluster Nodes
1. On `k8s-master1`, display the current status of the cluster nodes using the `kubectl get nodes` command:

   ```bash
   kubectl get nodes
   ```

2. You should see that the nodes are in a **NotReady** state because the network plugin is not installed. The output will look something like this:
   
   ```
   NAME           STATUS     ROLES    AGE    VERSION
   k8s-master1    NotReady   master   10m    v1.26.0
   k8s-worker1    NotReady   <none>   10m    v1.26.0
   k8s-worker2    NotReady   <none>   10m    v1.26.0
   ```

   The status **NotReady** is expected since the network plugin is missing.

### Step 2: Install the Flannel Network Plugin
3. To install the **Flannel overlay network**, use the following command to apply the Flannel YAML configuration:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
   ```

   This command downloads and applies the Flannel network configuration from the Flannel GitHub repository. It will create the necessary resources, such as Pods, ConfigMaps, and other configurations required for Flannel to operate as the network plugin.

### Step 3: Wait for the Network Plugin to Be Installed
4. The installation of Flannel may take some time. Once the Flannel network is applied, Kubernetes will begin deploying the necessary pods to the cluster.

5. After a few moments, you can check the status of the nodes again by running:

   ```bash
   kubectl get nodes
   ```

6. The status of the nodes should now change to **Ready**, indicating that the Flannel network has been successfully installed and that the nodes are now fully operational:

   ```
   NAME           STATUS   ROLES    AGE    VERSION
   k8s-master1    Ready    master   20m    v1.26.0
   k8s-worker1    Ready    <none>   20m    v1.26.0
   k8s-worker2    Ready    <none>   20m    v1.26.0
   ```

### Summary
- By installing the **Flannel network plugin**, the overlay network for your Kubernetes cluster is set up, allowing the nodes to communicate with each other.
- After installing Flannel, the status of the nodes should change to **Ready**, meaning your Kubernetes cluster is now fully functional and the network is in place.

Let me know if you need further assistance!
