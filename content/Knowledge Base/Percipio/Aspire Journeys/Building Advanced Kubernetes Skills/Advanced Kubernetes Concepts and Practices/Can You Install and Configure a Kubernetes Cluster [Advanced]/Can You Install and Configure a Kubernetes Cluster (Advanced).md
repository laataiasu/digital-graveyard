---
date: 1970-01-01T00:00:00Z
---

# Can You Install and Configure a Kubernetes Cluster [Advanced]

## 1
To install Docker on your Ubuntu-based `k8s-master1`, `k8s-worker1`, and `k8s-worker2` virtual machines and configure it for use with Kubernetes, follow the steps below.

### Step 1: Open MobaXterm and Establish SSH Sessions
1. Open the MobaXterm desktop application.
2. Start new SSH sessions to the following virtual machines using the credentials provided:
   - **k8s-master1**
   - **k8s-worker1**
   - **k8s-worker2**

   Use `Passw0rd!` as the password when prompted.

### Step 2: Update APT Package Index
For each virtual machine (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`), update the APT software package index:

```bash
sudo apt-get update
```

### Step 3: Install Docker on Each Machine
After updating the package index, install Docker using the following command on all three virtual machines:

```bash
sudo apt-get install docker.io -y
```

### Step 4: Enable Docker Service
Next, enable the Docker service on all three virtual machines to start automatically on boot:

```bash
sudo systemctl enable docker
```

### Step 5: Start Docker Service
Start the Docker service on all virtual machines:

```bash
sudo systemctl start docker
```

### Step 6: Configure Docker to Use `systemd` Cgroup Driver
Kubernetes expects Docker to use the `systemd` cgroup driver. To configure Docker to use this driver, follow these steps:

1. Create and edit the Docker daemon configuration file `/etc/docker/daemon.json`:

```bash
sudo nano /etc/docker/daemon.json
```

2. Add the following contents to the file:

```json
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}
```

3. Save and close the file.

### Step 7: Restart Docker Service
Restart the Docker service on all virtual machines to apply the changes:

```bash
sudo systemctl restart docker
```

### Step 8: Verify Docker Installation
Finally, verify that Docker is installed and running correctly on each machine:

```bash
sudo docker --version
sudo systemctl status docker
```

Repeat these steps for each machine: `k8s-master1`, `k8s-worker1`, and `k8s-worker2`.

Once Docker is installed and properly configured, your machines will be ready for Kubernetes to use Docker as the container runtime.

## 2
To install Kubernetes on the three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`), follow the steps outlined below. These instructions are based on the hints you provided.

### Step 1: Create the `/etc/apt/keyrings` Directory

Run the following command on all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`) to create the `/etc/apt/keyrings` directory:

```bash
sudo mkdir -p -m 755 /etc/apt/keyrings
```

### Step 2: Download the Kubernetes Repository Signing Key and Save It

1. Use `curl` to download the Kubernetes repository signing key from the specified URL and convert it to a GPG key using `gpg --dearmor`. This will save the key to `/etc/apt/keyrings/kubernetes-apt-keyring.gpg`.

Run the following command on all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`):

```bash
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

### Step 3: Add Kubernetes v1.30 Software Repository to APT

1. Create a new `.list` file for the Kubernetes repository in the `/etc/apt/sources.list.d/` directory.
   
Run the following command on all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`):

```bash
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

### Step 4: Update the APT Package Index

Update the APT package index so that the Kubernetes packages can be installed.

Run the following command on all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`):

```bash
sudo apt-get update
```

### Step 5: Install Kubernetes Components (kubeadm, kubelet, kubectl)

Now, install the necessary Kubernetes components: `kubeadm`, `kubelet`, and `kubectl`.

Run the following command on all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`):

```bash
sudo apt-get install -y kubeadm kubelet kubectl
```

If you encounter the error `E: Could not get lock /var/lib/dpkg/lock-frontend`, wait a few moments for the system to finish other package management tasks and then try the command again.

### Step 6: Mark the Kubernetes Components as Held

Mark the installed packages (`kubeadm`, `kubelet`, and `kubectl`) as "held" to prevent them from being upgraded automatically.

Run the following command on all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`):

```bash
sudo apt-mark hold kubeadm kubelet kubectl
```

This ensures that the packages remain at the current version and are not accidentally upgraded when you run `apt-get upgrade` in the future.

### Summary of Commands

For each node (`k8s-master1`, `k8s-worker1`, `k8s-worker2`), run the following commands:

```bash
# Step 1: Create the keyring directory
sudo mkdir -p -m 755 /etc/apt/keyrings

# Step 2: Download and save the GPG key
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# Step 3: Add Kubernetes repository
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list

# Step 4: Update APT package index
sudo apt-get update

# Step 5: Install Kubernetes components
sudo apt-get install -y kubeadm kubelet kubectl

# Step 6: Mark the components as held
sudo apt-mark hold kubeadm kubelet kubectl
```

After completing these steps, your nodes will have the necessary Kubernetes components installed and held at the desired version.

## 3
To initialize the Kubernetes cluster and configure the nodes, follow these detailed steps based on the hints you provided. We'll disable swap, initialize the cluster control plane on the master node (`k8s-master1`), and gather the necessary token information for joining the worker nodes.

### Step 1: Disable Swap on All Nodes

Kubernetes requires that swap be disabled to ensure optimal performance. You need to disable swap on all nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`).

To disable swap temporarily, run the following command on each node:

```bash
sudo swapoff -a
```

To disable swap permanently (so it doesn't turn on after a reboot), edit the `/etc/fstab` file:

1. Open `/etc/fstab` for editing:

```bash
sudo nano /etc/fstab
```

2. Find the line that mentions `swap` (it will look something like this):

```
/swapfile none swap sw 0 0
```

3. Comment out the swap line by adding a `#` at the beginning of the line:

```
#/swapfile none swap sw 0 0
```

4. Save the file and exit (`CTRL + O` to save, `CTRL + X` to exit).

### Step 2: Initialize the Kubernetes Cluster on the Master Node

Next, you need to initialize the Kubernetes cluster control plane on the master node (`k8s-master1`) using the `kubeadm` tool.

1. Run the following command on `k8s-master1` to initialize the Kubernetes cluster with the `flannel` overlay network plug-in and a specific Pod network CIDR (`10.244.0.0/16`):

```bash
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

This process may take some time. Please be patient.

### Step 3: Configure kubectl for the Master Node

After the initialization is complete, you'll need to configure `kubectl` (the Kubernetes command-line tool) to access the cluster from `k8s-master1`.

Run the following commands on `k8s-master1`:

1. Create the `.kube` directory:

```bash
mkdir -p $HOME/.kube
```

2. Copy the Kubernetes configuration file to the `.kube` directory:

```bash
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
```

3. Change the ownership of the configuration file to your user:

```bash
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### Step 4: Install the Flannel Network Plugin

To enable networking between the pods in the cluster, you need to deploy the Flannel network plugin. Run the following command on `k8s-master1`:

```bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

This will install Flannel on the Kubernetes cluster, enabling pod communication across nodes.

### Step 5: Gather the Join Token Information

After the cluster is initialized, `kubeadm init` will provide a join command along with a token that the worker nodes will need to join the cluster. The output will look like this:

```
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Then you need to run the following on each worker node:
  kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>

Please note that the join command will be provided only once, so save it to a file for later use.
```

1. **Copy the last two lines** of the output (the `kubeadm join` command and its token) to a text file on your local machine or in Notepad.

2. This token will be used to join the worker nodes (`k8s-worker1` and `k8s-worker2`) to the cluster.

### Step 6: Join the Worker Nodes to the Cluster

Now, you can use the join command on each worker node (`k8s-worker1` and `k8s-worker2`). Run the following command on each worker node:

```bash
sudo kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

- Replace `<master-ip>` with the IP address of the master node (`k8s-master1`).
- Replace `<master-port>` with the port (usually `6443`).
- Replace `<token>` and `<hash>` with the values provided in the `kubeadm init` output.

After the worker nodes have successfully joined the cluster, you can check the status of the nodes from `k8s-master1`:

```bash
kubectl get nodes
```

This should show all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`) as `Ready`.

### Summary of Commands

On all nodes (`k8s-master1`, `k8s-worker1`, `k8s-worker2`):

1. Disable swap temporarily:

```bash
sudo swapoff -a
```

2. Disable swap permanently by editing `/etc/fstab`.

On `k8s-master1` (only):

1. Initialize the Kubernetes cluster with Flannel as the network plugin:

```bash
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

2. Configure `kubectl`:

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

3. Install Flannel network plugin:

```bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

4. Copy the `kubeadm join` command (with token) from the `kubeadm init` output to a text file.

On `k8s-worker1` and `k8s-worker2`:

1. Join the cluster using the `kubeadm join` command provided:

```bash
sudo kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

Finally, verify the nodes are joined successfully by running `kubectl get nodes` on `k8s-master1`.

## 4
To configure cluster admin privileges on the `k8s-master1` node, you need to set up the `kubectl` configuration file (`config`) for the administrator user. Here's how you can do that step by step:

### Step 1: Ensure You Are in the `/home/administrator` Directory

Make sure you are in the correct directory before proceeding:

```bash
cd /home/administrator
```

### Step 2: Create a Hidden Directory for Kubernetes Config

Now, create a hidden directory named `.kube` in the administrator's home directory. You can do this with the following command:

```bash
mkdir -p /home/administrator/.kube
```

This will create the `.kube` directory where Kubernetes configurations will be stored.

### Step 3: Copy the Kubernetes Admin Configuration File

Next, copy the `/etc/kubernetes/admin.conf` file to `/home/administrator/.kube/config`. The `admin.conf` file contains the necessary configuration for the `kubectl` command to interact with the Kubernetes cluster.

Run this command:

```bash
sudo cp /etc/kubernetes/admin.conf /home/administrator/.kube/config
```

### Step 4: Change Ownership of the Config File

After copying the `admin.conf` file, you need to change the ownership of the file to the `administrator` user. This ensures that the administrator user has the necessary permissions to access and modify the file.

Run the following command:

```bash
sudo chown administrator:administrator /home/administrator/.kube/config
```

This command changes the owner and group of the `config` file to `administrator`.

### Step 5: Verify Permissions and Access

At this point, the administrator user should have full access to the Kubernetes configuration. You can verify that everything is working correctly by running the following command as the `administrator` user:

```bash
kubectl get nodes
```

This should show the nodes in the cluster, confirming that the configuration has been correctly set up and the user has cluster admin privileges.

### Summary of Commands

To summarize the steps:

1. Navigate to the administrator's home directory:

```bash
cd /home/administrator
```

2. Create the hidden `.kube` directory:

```bash
mkdir -p /home/administrator/.kube
```

3. Copy the Kubernetes admin config to the `.kube` directory:

```bash
sudo cp /etc/kubernetes/admin.conf /home/administrator/.kube/config
```

4. Change ownership of the config file to the administrator:

```bash
sudo chown administrator:administrator /home/administrator/.kube/config
```

After completing these steps, the `administrator` user will have the necessary permissions to interact with the Kubernetes cluster using `kubectl`.

## 5
To join the worker nodes (`k8s-worker1` and `k8s-worker2`) to the Kubernetes cluster, follow the steps below:

### Step 1: Open an Interactive Subshell as the Root User

First, you need to open an interactive subshell as the root user on both worker nodes (`k8s-worker1` and `k8s-worker2`).

1. On `k8s-worker1`, run the following command:

```bash
sudo -i
```

When prompted for the password, enter `Passw0rd!`.

2. Repeat the same command on `k8s-worker2`:

```bash
sudo -i
```

Enter `Passw0rd!` when prompted.

### Step 2: Join the Worker Node to the Cluster

Next, use the `kubeadm join` command, which you previously copied from the output of the `kubeadm init` command on the master node. This command contains a token and a certificate hash that is needed to securely join the worker nodes to the cluster.

Run the following command on `k8s-worker1` (substitute `<master-ip>`, `<master-port>`, `<token>`, and `<hash>` with the actual values from the `kubeadm init` output):

```bash
kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

Repeat the same `kubeadm join` command on `k8s-worker2` to join the second worker node to the cluster.

### Step 3: Wait for Worker Nodes to Join the Cluster

Once you run the `kubeadm join` command on both worker nodes, the joining process will take a few minutes. Wait for the worker nodes to finish joining the cluster. You can check the status by running the following command on `k8s-master1`:

```bash
kubectl get nodes
```

After a few minutes, you should see `k8s-worker1` and `k8s-worker2` appear as `Ready` in the list of nodes.

### Step 4: Exit the Root Subshell

Once both worker nodes have joined the cluster and are showing as `Ready`, exit the root subshell on both worker nodes.

To exit the root subshell, simply type:

```bash
exit
```

### Summary of Commands:

1. On `k8s-worker1` and `k8s-worker2`, enter the interactive root subshell:

```bash
sudo -i
```

2. Join the worker nodes to the cluster using the `kubeadm join` command (on both nodes):

```bash
kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

3. After both worker nodes have joined the cluster, check the status on `k8s-master1`:

```bash
kubectl get nodes
```

4. Exit the root subshell on each worker node:

```bash
exit
```

After following these steps, both `k8s-worker1` and `k8s-worker2` will be successfully joined to the Kubernetes cluster.