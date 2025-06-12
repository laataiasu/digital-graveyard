# Install Kubernetes Cluster Components (Guided)

## 1
Here’s a step-by-step breakdown to guide you through the tasks outlined:

### 1. Open MobaXterm Desktop Application
Launch the MobaXterm application on your computer.

### 2. Establish a New SSH Session
- **Connect to `k8s-master1`:**
  1. Click on the "Session" button in MobaXterm.
  2. Choose **SSH** as the session type.
  3. For **Remote host**, enter the IP address or hostname of `k8s-master1`.
  4. Set **Username** to `administrator` (or your admin username).
  5. When prompted, enter the password: `Passw0rd!`.
  6. When asked to save the password, choose **No**.
  7. After connecting, ensure you’re logged in to `k8s-master1`.

- **Connect to `k8s-worker1` and `k8s-worker2`:**
  1. Repeat the same process for both `k8s-worker1` and `k8s-worker2`, entering the same password `Passw0rd!` for each.

### 3. Use MobaXterm Tabbed User Interface
- You can use **multiple tabs** in MobaXterm for easy switching between SSH sessions. For instance, one tab can be connected to `k8s-master1`, another to `k8s-worker1`, and a third to `k8s-worker2`.

### 4. Determine the IPv4 Address of `k8s-worker1` and `k8s-worker2`
- **On `k8s-worker1`:**
  1. Execute the following command to get the IP address:
     ```bash
     ip addr show ens32
     ```
  2. Look for the `inet` line under `ens32` to find the IPv4 address (e.g., `192.168.x.x`).
  3. Record this IP address in the `k8s-worker1 IPv4 Address` text box.

- **On `k8s-worker2`:**
  1. Execute the same command on `k8s-worker2`:
     ```bash
     ip addr show ens32
     ```
  2. Note the IPv4 address and record it in the `k8s-worker2 IPv4 Address` text box.

### 5. Verify Network Connectivity with `ping`
- **On `k8s-master1`:**
  1. To check the network connectivity to `k8s-worker1`, run:
     ```bash
     ping <k8s-worker1-IP>
     ```
  2. To check the network connectivity to `k8s-worker2`, run:
     ```bash
     ping <k8s-worker2-IP>
     ```
  3. Confirm that the nodes can ping each other without issues.

### 6. Check Number of Virtual Processors (vCPUs)
- **On `k8s-master1`:**
  1. To check the number of vCPUs, run:
     ```bash
     lscpu
     ```
  2. Record the number of CPUs listed under `CPU(s)`.

  3. To save this output to a file:
     ```bash
     lscpu > ~/cpu-report.txt
     ```

### 7. Check RAM Availability
- **On `k8s-master1`:**
  1. To check RAM usage, run:
     ```bash
     free -h
     ```
  2. Confirm that the system has at least 2 GB (2000000 KB) of RAM.
  3. Save the output to a file:
     ```bash
     free -h > ~/ram-report.txt
     ```

- **On `k8s-worker1` and `k8s-worker2`:**
  1. Run the same `free -h` command on both `k8s-worker1` and `k8s-worker2` to ensure they have at least 1 GB (1000000 KB) of RAM.
  2. Save the output to `~/ram-report.txt` on both nodes.

### 8. Check Internet Connectivity with `curl`
- **On `k8s-master1`:**
  1. Test internet connectivity to `https://kubernetes.io` using the following command:
     ```bash
     curl -I https://kubernetes.io
     ```
  2. Ensure the command returns a successful HTTP response (e.g., `HTTP/1.1 200 OK`).
  3. Save the output to a file:
     ```bash
     curl -I https://kubernetes.io > ~/network-report.txt
     ```

- **On `k8s-worker1` and `k8s-worker2`:**
  1. Repeat the same `curl` command on both `k8s-worker1` and `k8s-worker2`.
  2. Save the output to the same `~/network-report.txt` file on both nodes.

### Summary of Commands:

- **Determine IPv4 address:**
  ```bash
  ip addr show ens32
  ```

- **Ping another node:**
  ```bash
  ping <node-IP>
  ```

- **Check CPU info:**
  ```bash
  lscpu
  ```

- **Save CPU info to a file:**
  ```bash
  lscpu > ~/cpu-report.txt
  ```

- **Check RAM info:**
  ```bash
  free -h
  ```

- **Save RAM info to a file:**
  ```bash
  free -h > ~/ram-report.txt
  ```

- **Check internet connectivity:**
  ```bash
  curl -I https://kubernetes.io
  ```

- **Save network info to a file:**
  ```bash
  curl -I https://kubernetes.io > ~/network-report.txt
  ```

By following these steps, you’ll complete the setup and verification process for your Kubernetes nodes (`k8s-master1`, `k8s-worker1`, `k8s-worker2`).

## 2
Here's an expanded set of instructions for the tasks involving the `apt-get` update, Docker installation, and service management on `k8s-master1`, `k8s-worker1`, and `k8s-worker2`:

---

### 1. **Update the APT Software Package Index**

The APT package manager is used in Debian-based distributions (such as Ubuntu) to manage software packages. Running `apt-get update` fetches the latest list of available packages from the configured repositories, ensuring that your system can install the latest available versions of software.

**Steps:**

- Open a terminal on **k8s-master1** (or any of the other nodes if required).
- To update the package index, run the following command:
  
  ```bash
  sudo apt-get update
  ```

- The terminal will prompt you to enter the **sudo password** for administrative privileges. Enter `Passw0rd!` when prompted. 

  > **Note:** You will be asked for the sudo password only the first time you use `sudo` in the session. Afterward, you can run other sudo commands without re-entering the password for a short time.

- Once the command finishes running, the APT package index on your system will be up-to-date.

Repeat this process on **k8s-worker1** and **k8s-worker2**.

---

### 2. **Install Docker on k8s-master1, k8s-worker1, and k8s-worker2**

Docker is a container runtime that allows you to run and manage containers on your system. Kubernetes relies on a container runtime to manage the containers that run your applications.

**Steps:**

- On **k8s-master1**, install Docker by running the following command:

  ```bash
  sudo apt-get install docker.io
  ```

- Once the command executes successfully, Docker will be installed on the system.

- Repeat this command on **k8s-worker1** and **k8s-worker2** to install Docker on those nodes as well.

---

### 3. **Verify the State of the Docker Service**

After installing Docker, the Docker service is likely not running yet. Use the `systemctl` command to check the status of the Docker service.

**Steps:**

- On **k8s-master1**, check the Docker service status:

  ```bash
  sudo systemctl status docker
  ```

  This will show whether the Docker service is running or inactive. The output will indicate the state of the service.

---

### 4. **Enable the Docker Service**

To ensure Docker starts automatically when the system boots up, you need to enable the service.

**Steps:**

- On **k8s-master1**, run the following command to enable the Docker service:

  ```bash
  sudo systemctl enable docker
  ```

  This command ensures that Docker will start automatically on boot.

---

### 5. **Start the Docker Service**

After enabling Docker, you must start the service to begin running it on the current system.

**Steps:**

- On **k8s-master1**, start the Docker service by running:

  ```bash
  sudo systemctl start docker
  ```

- You can verify if Docker is running by checking the service status again:

  ```bash
  sudo systemctl status docker
  ```

  The status should now show that Docker is active and running.

Repeat the process of enabling and starting Docker on **k8s-worker1** and **k8s-worker2**.

---

### 6. **Configure Docker to Use Systemd Cgroup (for Kubernetes)**

Kubernetes requires Docker to be configured with the `systemd` cgroup driver for proper functioning. This configuration must be done in the `/etc/docker/daemon.json` file.

**Steps:**

- On **k8s-master1**, open the Docker configuration file:

  ```bash
  sudo nano /etc/docker/daemon.json
  ```

  If the file does not exist, you can create it.

- Add the following configuration to specify the `systemd` cgroup driver:

  ```json
  {
    "exec-opts": ["native.cgroupdriver=systemd"]
  }
  ```

  This ensures Docker uses the `systemd` cgroup driver, which is required for Kubernetes.

- Save the file and exit the text editor (`CTRL+X`, then `Y`, and press `Enter`).

---

### 7. **Restart Docker to Apply Configuration**

After updating the Docker configuration, restart the Docker service for the changes to take effect.

**Steps:**

- On **k8s-master1**, restart Docker by running:

  ```bash
  sudo systemctl restart docker
  ```

- You can verify that Docker is using the correct configuration by checking the Docker service status:

  ```bash
  sudo systemctl status docker
  ```

Repeat the steps to configure Docker with `systemd` and restart the Docker service on **k8s-worker1** and **k8s-worker2**.

---

### Final Verification

Finally, verify that Docker is properly installed and running on all nodes (`k8s-master1`, `k8s-worker1`, `k8s-worker2`) by running:

```bash
sudo systemctl status docker
```

Make sure that Docker is in the "active (running)" state and configured to use the `systemd` cgroup driver.

---

These steps should complete the installation and configuration of Docker on your Kubernetes nodes, ensuring that Docker is running correctly and configured with the appropriate cgroup settings for Kubernetes.

## 3
To perform the tasks outlined in your question on `k8s-master1`, `k8s-worker1`, and `k8s-worker2`, here's a detailed breakdown of the steps you need to take:

### 1. **Create the `/etc/apt/keyrings` Directory on k8s-master1**
   This step ensures that the keyrings directory exists, where the GPG keys for the Kubernetes repository will be stored.
   
   ```bash
   sudo mkdir -p -m 755 /etc/apt/keyrings
   ```

### 2. **Download and Convert the Kubernetes GPG Signing Key on k8s-master1**
   Use `curl` to download the GPG key, then convert it to a usable format with `gpg -dearmor` and save it to the `/etc/apt/keyrings/kubernetes-apt-keyring.gpg` file.

   ```bash
   curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   ```

   When prompted for a password, enter `Passw0rd!`.

### 3. **Add the Kubernetes v1.30 Software Repository on k8s-master1**
   Add the Kubernetes v1.30 repository to the `kubernetes.list` file in `/etc/apt/sources.list.d/` to ensure that Kubernetes packages can be installed. Use the `echo` and `tee` command to append the repository URL to the list.

   ```bash
   echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
   ```

### 4. **Update the APT Package Index on k8s-master1**
   Run the `apt-get update` command to update the list of available packages from the new Kubernetes repository.

   ```bash
   sudo apt-get update
   ```

### 5. **Install Kubernetes Components on k8s-master1**
   Install the specific version (v1.30) of `kubeadm`, `kubelet`, and `kubectl` using `apt-get`.

   ```bash
   sudo apt-get install -y kubeadm=1.30.* kubelet=1.30.* kubectl=1.30.*
   ```

   If you encounter the error `E: Could not get lock /var/lib/dpkg/lock-frontend`, it means another package installation is in progress. Wait a few minutes and try again.

### 6. **Mark the Kubernetes Components as Held on k8s-master1**
   Use the `apt-mark` command to prevent automatic updates to the `kubeadm`, `kubelet`, and `kubectl` packages on `k8s-master1`.

   ```bash
   sudo apt-mark hold kubeadm kubelet kubectl
   ```

### 7. **Repeat Steps on k8s-worker1 and k8s-worker2**
   Now, you need to repeat the following steps on both `k8s-worker1` and `k8s-worker2`:

   - **Create the `/etc/apt/keyrings` Directory**
     ```bash
     sudo mkdir -p -m 755 /etc/apt/keyrings
     ```

   - **Download and Convert the Kubernetes GPG Signing Key**
     ```bash
     curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
     ```

   - **Add the Kubernetes Repository**
     ```bash
     echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
     ```

   - **Update the APT Package Index**
     ```bash
     sudo apt-get update
     ```

   - **Install Kubernetes Components**
     ```bash
     sudo apt-get install -y kubeadm=1.30.* kubelet=1.30.* kubectl=1.30.*
     ```

   - **Mark the Kubernetes Components as Held**
     ```bash
     sudo apt-mark hold kubeadm kubelet kubectl
     ```

### Summary of Key Commands:
- **Create keyrings directory:**
  ```bash
  sudo mkdir -p -m 755 /etc/apt/keyrings
  ```
- **Download and convert GPG key:**
  ```bash
  curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
  ```
- **Add the Kubernetes repository:**
  ```bash
  echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
  ```
- **Update package index:**
  ```bash
  sudo apt-get update
  ```
- **Install Kubernetes components:**
  ```bash
  sudo apt-get install -y kubeadm=1.30.* kubelet=1.30.* kubectl=1.30.*
  ```
- **Mark packages as held:**
  ```bash
  sudo apt-mark hold kubeadm kubelet kubectl
  ```

By following these steps, you will configure Kubernetes on all three nodes (`k8s-master1`, `k8s-worker1`, and `k8s-worker2`) to use the specified version of the Kubernetes components and hold them at that version to prevent accidental upgrades.

## 4
To disable swap on your system by editing the `/etc/fstab` file, follow these steps:

### Steps to Edit `/etc/fstab` and Disable Swap:

1. **Open the `/etc/fstab` file in the Nano text editor:**
   Run the following command to open the file in `nano`:
   ```bash
   sudo nano /etc/fstab
   ```

2. **Locate the Swap Configuration:**
   - Scroll down to the last line of the file using the arrow keys.
   - The swap file configuration will typically look something like:
     ```
     /swapfile none swap sw 0 0
     ```

3. **Comment Out the Swap Line:**
   - To disable swap, you need to comment out this line by adding a `#` at the beginning of it.
   - The line should now look like:
     ```bash
     #/swapfile none swap sw 0 0
     ```

4. **Save and Exit Nano:**
   - After commenting out the line, press `Ctrl + X` to exit the editor.
   - When prompted to save changes, press `Y` to confirm.
   - Then press `Enter` to confirm the filename (`/etc/fstab`).

### Example of the `/etc/fstab` File After Edit:
```bash
# /swapfile none swap sw 0 0
```

This action will prevent the system from enabling swap during the boot process.

### Additional Step (Optional):
If you want to immediately disable swap without rebooting, you can turn off swap with the following command:
```bash
sudo swapoff -a
```

This will disable swap until the next system reboot, and after the `/etc/fstab` modification, it won't be enabled again on reboot.

That's it! You have successfully edited the `/etc/fstab` file to disable swap.

## 5
To verify that the Kubernetes and Docker component software packages have been installed on the virtual machines, you can use the `dpkg` command to check for installed packages. Additionally, you'll redirect the output of the command to a file (`~/install-report.txt`) for easier review. Here's a detailed explanation of the steps:

### 1. **Verify Kubernetes and Docker Installation**

First, you will verify if Docker and Kubernetes components are installed using the `dpkg` and `grep` commands.

#### **Check for Docker Installation:**
You can check if Docker is installed on the system using the following command:

```bash
dpkg --get-selections | grep docker
```

This will list all installed Docker-related packages. The `dpkg --get-selections` command lists all packages, and the `grep docker` part filters for any entries containing "docker".

#### **Check for Kubernetes Installation:**
Similarly, you can check for installed Kubernetes components (like `kubeadm`, `kubelet`, `kubectl`) by running:

```bash
dpkg --get-selections | grep kube
```

This will list any installed Kubernetes packages.

### 2. **Redirect Output to a File**

To save the results of these checks to a file (e.g., `~/install-report.txt`), you can redirect the output to that file. Here's how you can do this:

#### **Save Docker Package Information:**

```bash
dpkg --get-selections | grep docker > ~/install-report.txt
```

This command will:

- Check for Docker-related packages installed on the system.
- Save the output of the `dpkg` command to the file `install-report.txt` located in your home directory (`~`).

#### **Check for Kubernetes Package Information:**

Similarly, you can append the Kubernetes package details to the same file:

```bash
dpkg --get-selections | grep kube >> ~/install-report.txt
```

Here, `>>` appends the output to the existing `install-report.txt` file. If you use a single `>` (like the previous command), it will overwrite the file.

### 3. **View the Report**

After running these commands, the `install-report.txt` file will contain the list of installed Docker and Kubernetes packages. To view the contents of the file, you can use the `cat` command:

```bash
cat ~/install-report.txt
```

### Example of Commands and Outputs:

#### **1. Check for Docker Installation:**
```bash
dpkg --get-selections | grep docker > ~/install-report.txt
```
This could produce output similar to:
```
docker-ce                        install
docker-ce-cli                    install
docker-ce-rootless-extras        install
```

#### **2. Check for Kubernetes Installation:**
```bash
dpkg --get-selections | grep kube >> ~/install-report.txt
```
This could produce output like:
```
kubeadm                          install
kubelet                          install
kubectl                          install
```

### Final Report:

The `install-report.txt` will contain something like this:

```
docker-ce                        install
docker-ce-cli                    install
docker-ce-rootless-extras        install
kubeadm                          install
kubelet                          install
kubectl                          install
```

### Summary of Steps:

1. **Verify Docker installation**:
   ```bash
   dpkg --get-selections | grep docker
   ```

2. **Verify Kubernetes installation**:
   ```bash
   dpkg --get-selections | grep kube
   ```

3. **Save Docker installation report**:
   ```bash
   dpkg --get-selections | grep docker > ~/install-report.txt
   ```

4. **Save Kubernetes installation report (optional)**:
   ```bash
   dpkg --get-selections | grep kube >> ~/install-report.txt
   ```

5. **View the contents of the report**:
   ```bash
   cat ~/install-report.txt
   ```

This ensures you have an installation report of Docker and Kubernetes packages for reference or troubleshooting.