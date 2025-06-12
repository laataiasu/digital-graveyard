# Application Containers

## 1. Application Containers

### Application Containers

**Definition**: An application container is a logical isolation boundary where an application runs with all its required components stored within the container. Unlike traditional installations, these components are encapsulated within the container, requiring only a compatible host operating system to run.

**Microservices Architecture**: Applications can be modularized into multiple containers, each serving a specific function, known as microservices. For example:
- One container may handle user content uploads.
- Another may manage the web interface.
- A third could be responsible for printing functions.

Containers can communicate over a network, regardless of whether they run on the same host.

**Deployment**: In larger environments, containerized applications may be deployed in a Kubernetes cluster. 

**Benefits of Microservices**:
- Allows for easier updates and testing without affecting the entire application.
- Promotes application component decoupling, enabling independent operation of various components.

**Usage with Message Queues**: Developers often use containers with message queues to facilitate communication between components, ensuring messages are queued for components that may be temporarily offline.

### Application Container Structure

- **Host Operating System**: The application container runs on a host OS, which can be Linux, Windows, or others. The important factor is having a container engine like Docker installed.

- **Docker Engine**: A common container engine that manages resources and runs application containers.

- **Container Images**: A dormant state of the application container, containing all necessary software and settings. When activated, it becomes a running container.

**Contents of an Application Container**:
- Scripts and executable binaries
- App-specific libraries (e.g., `.so` for Linux, `.DLL` for Windows)
- Configuration files
- Runtime environments (e.g., command prompts, web server stacks)

### Differences from Virtual Machines

Application containers do not include a full operating system; they share the host OS kernel, allowing for lightweight and rapid deployment compared to virtual machines.

### Benefits of Application Containers

- **Portability**: Containers are self-contained and can be easily moved across different hosts with compatible container engines.
- **Speed**: Containers start quickly since they leverage the already running host OS.
- **Isolation**: Changes made in one container do not impact others, enhancing uptime and user experience.

## 2. Installing Docker on Linux

**Steps**:
1. Run the command: `sudo apt install docker.io`
2. Confirm installation by running: `sudo docker`
3. Check Docker service status: `sudo service docker status`
4. To list local images: `sudo docker images`

**Pulling and Running a Container**:
- Search for a container image (e.g., Alpine) on Docker Hub.
- Pull the image with: `sudo docker pull alpine`
- Run the container interactively: `sudo docker run -it alpine`
- To exit the container, type `exit`.

**Viewing Running Containers**:
- To check currently running containers: `sudo docker ps`
- To see all containers, including those that have exited: `sudo docker ps -a`

This covers the basics of application containers, their structure, benefits, and the installation and operation of Docker on a Linux host.

## 3. Docker CLI Basics

- To check installed commands, use:
  ```
  sudo docker
  ```

- **Removing Images**: 
  - Command: 
    ```
    sudo docker rmi <IMAGE_NAME>
    ```
  - Use `--help` for options:
    ```
    sudo docker rmi --help
    ```
  - Options include:
    - `-f` or `--force`: Force removal without confirmation.
    - `--no-prune`: Do not delete untagged parents.

- **Check Docker Version**: 
  ```
  sudo docker version
  ```

- **List Local Images**: 
  - Command:
    ```
    sudo docker images
    ```
  - Without `sudo`, you may receive permission denied errors.

- **Pulling Images**: 
  - Command to pull an image from Docker Hub:
    ```
    sudo docker pull <IMAGE_NAME>
    ```
  - Example:
    ```
    sudo docker pull caddy
    ```

- **Running Containers**: 
  - Command to run a container:
    ```
    sudo docker run -p 80:80 caddy
    ```
  - Use `Ctrl+C` to stop it.

- **Listing Running Containers**:
  - Show currently running:
    ```
    sudo docker ps
    ```
  - Show all containers (including stopped):
    ```
    sudo docker ps -a
    ```

- **Docker Overlay Network**:
  - Used to create a distributed network between Docker hosts, typically with Docker Swarm.
  - Allows inter-host communication without needing hosts to be on the same subnet.

## 4. Setting Up Docker Swarm

1. **Initialize Swarm**:
   - Command on manager node:
     ```
     sudo docker swarm init
     ```

2. **Join Worker Nodes**:
   - Copy the join command provided after initialization and add `sudo`:
     ```
     sudo docker swarm join --token <TOKEN> <MANAGER_IP>:2377
     ```

3. **Open Required Ports**:
   - Ensure the following ports are open:
     - TCP port 2377
     - TCP and UDP ports 7946
     - UDP port 4789

4. **List Swarm Nodes**:
   - Command:
     ```
     sudo docker node ls
     ```

5. **List Docker Networks**:
   - Command:
     ```
     sudo docker network ls
     ```

6. **Create Docker Service**:
   - Command to create a service:
     ```
     sudo docker service create --name caddy -p 80:80 caddy
     ```

7. **Check Service Status**:
   - Command:
     ```
     sudo docker service ps caddy
     ```

8. **Verify Web App**:
   - Use `curl` to check the web page:
     ```
     curl 127.0.0.1:80
     ```

9. **Inspect Overlay Network**:
   - Command:
     ```
     sudo docker network inspect ingress
     ```

- Default overlay networks are generally suitable unless custom configurations are necessary.

## 5. Docker Hub Overview

- Sign up for a free account at [Docker Hub](https://hub.docker.com) to access a wider range of container images and create your own repositories.

- **Searching for Images**:
  - Use the search function to find images. For example, searching for "mysql" will show the official MySQL image.

- **Pulling Images**:
  - To pull the MySQL container image, run:
    ```
    sudo docker pull mysql
    ```

- **Checking Docker Status**:
  - Verify Docker is running:
    ```
    sudo service docker status
    ```
  - List existing images:
    ```
    sudo docker images
    ```

- **Running Containers**:
  - To start a MySQL container with a root password, use:
    ```
    sudo docker run --name mysqltest1 -e MYSQL_ROOT_PASSWORD=Pa$$w0rdABC123 mysql:latest
    ```
  - This command creates a container named `mysqltest1` with the specified root password.

- **Listing Running Containers**:
  - Check running containers:
    ```
    sudo docker ps
    ```

- **Stopping Containers**:
  - To stop a running container:
    ```
    sudo docker stop mysqltest1
    ```

- **Running in Detached Mode**:
  - To run an Alpine container in detached mode:
    ```
    sudo docker run -itd alpine
    ```

- **Interacting with Containers**:
  - To execute a command inside a running container:
    ```
    sudo docker exec -it <CONTAINER_NAME> /bin/sh
    ```
  - Replace `<CONTAINER_NAME>` with the actual name (e.g., `naughty_allen`) to access the shell of the container.

## 6. Creating and Using a Cloud-based Container Registry

### Creating a Cloud-Based Container Registry in Azure

1. **Sign in to Azure Portal**:
   - Go to the Microsoft Azure portal.

2. **Create a Container Registry**:
   - Click on **Create a resource** and search for **Azure Container Registry**.
   - Select **Container Registry** and click **Create**.

3. **Basic Configuration**:
   - In the **Basics** section:
     - Choose a **Resource group** (e.g., `stdcontainerregistry172`).
     - Enter a **Registry name** (e.g., `stdcontainerregistry172`).
     - Select **Location** (e.g., East US).
     - Note: The registry will have the `.azurecr.io` suffix.

4. **Networking and Encryption**:
   - Click **Next** for Networking. For Standard SKU, you may see limited options.
   - Skip adding tags and proceed to **Review + create**.
   - Click **Create** to deploy the registry.

5. **Accessing the Registry**:
   - Once the deployment is complete, click **Go to resource** to view the properties of your new container registry.

6. **Prepare to Push Images**:
   - Click on **Quick start** in the left pane for step-by-step instructions.
   - Ensure Docker is installed on your local machine. Check with:
     ```bash
     sudo service docker status
     ```

7. **Login to the Container Registry**:
   - Enable the Admin user under **Access keys**.
   - Copy the login server URI (e.g., `stdcontainerregistry172.azurecr.io`).
   - Run the Docker login command:
     ```bash
     sudo docker login stdcontainerregistry172.azurecr.io
     ```
   - Use the registry name as the username and one of the passwords provided.

8. **Tag and Push a Docker Image**:
   - List your local images:
     ```bash
     sudo docker images
     ```
   - Tag the image you want to push (e.g., `alpine`):
     ```bash
     sudo docker tag alpine stdcontainerregistry172.azurecr.io/my-alpine
     ```
   - Push the tagged image to your Azure Container Registry:
     ```bash
     sudo docker push stdcontainerregistry172.azurecr.io/my-alpine
     ```

9. **Verify the Push**:
   - Return to the Azure portal and navigate to **Repositories** under your container registry.
   - You should see `my-alpine` listed with its latest version.

## 7. Dockerfiles

Managing Docker application containers involves working with Dockerfiles, which are text files used to build Docker container images. A Dockerfile specifies the directives and values necessary to create a new container image, which contains all the application files and settings.

**Key Points:**

- **Dockerfile Naming**: The file must be named `Dockerfile` (case-sensitive, no spaces).

- **Docker CLI**: Use the Docker command line interface (CLI), installed with Docker Engine, to manage containers and images. In Linux, you may need `sudo` for elevated permissions.

- **Basic Syntax**:
  - Use `docker build -f <path to Dockerfile>` to specify the Dockerfile to build from.
  - The Dockerfile can use a backslash (`\`) as an escape character to split long lines for readability.

**Common Directives**:
- **FROM**: Defines the base image for the new container (e.g., `FROM ubuntu:latest`).
- **COPY**: Copies files or directories from the host into the container image.
- **ADD**: Similar to COPY but can also pull files from URLs.
- **RUN**: Executes commands during the image build process (e.g., `RUN apt-get update`).
- **CMD**: Specifies the default command to run when the container starts.

**.dockerignore File**:
- Used to specify files and directories to exclude from the Docker image.
- Syntax includes:
  - Comments with `#`.
  - Wildcards (`*` for multiple characters, `?` for a single character).
  - Inversion with `!` to exclude patterns.

**Building and Running a Container**:
1. Create a Dockerfile in the current directory with appropriate directives.
2. Build the image using:
   ```
   docker build -t <image_name>:<tag> .
   ```
   For example, `docker build -t mycontainerimage:1.0 .`
3. Run the container with:
   ```
   docker run -p <host_port>:<container_port> <image_name>:<tag>
   ```
   For example, `docker run -p 5000:5000 mycontainerimage:1.0`.

**Example Dockerfile**:
```dockerfile
FROM ubuntu:latest
MAINTAINER example@example.com

# Install dependencies
RUN apt-get update && apt-get install -y python

# Copy application files
COPY hello.py /home/hello.py

# Set the default command
CMD ["python", "/home/hello.py"]
```

**Sample Commands**:
- To check available images: 
  ```
  docker images
  ```
- To list running containers: 
  ```
  docker ps
  ```
- To stop a running container: 
  ```
  docker stop <container_id>
  ```

This concise format provides essential information about Dockerfiles and their usage, making it easier to understand and apply.

## 8. Kubernetes Container Orchestration

### What is Kubernetes?
Kubernetes is essentially a cluster of nodes (virtual machines) designed to support containerized applications. These applications can range from web apps to data analytics engines. The advantages of Kubernetes include:

- **Flexibility**: Deploy on-premises or as a managed service in the cloud.
- **Simplified Management**: Cloud deployments simplify installation and configuration.

### Key Features of Kubernetes
1. **Container Management**: Facilitates deployment through units called **pods**.
2. **Autoscaling**: Automatically adjusts the number of worker nodes based on demand (e.g., increased data feeds).
3. **Load Balancing**: Distributes incoming traffic to ensure applications are responsive.
4. **Desired State Management**: Ensures a specified number of nodes are always running, launching replacements when failures occur (autohealing).
5. **Zero Downtime Updates**: Allows software updates without taking the entire application offline.

### Deploying Kubernetes
#### Setting Up a Cluster
Kubernetes deployment starts with creating a cluster. This can be done through command-line tools or graphical interfaces, particularly in cloud environments.

##### Example: Creating a Kubernetes Cluster on Azure
1. **Access Azure Portal**: 
   - Search for and select **Azure Kubernetes Service (AKS)**.
   
2. **Configuration Steps**:
   - Choose a **Resource Group** and **Cluster Name** (e.g., `mykubernetescluster172`).
   - Select the **Region** for deployment (e.g., East US).
   - Configure the **Node Size** and **Autoscaling** options.

3. **Creating the Cluster**: 
   - Click **Review + create** to validate and then **Create**.

#### Understanding Kubernetes Pods
A **pod** is a basic deployable unit in Kubernetes. It can run one or more containers from specified images. Pods can be defined and deployed using a YAML configuration file.

- **Kubelet**: This process on worker nodes manages communication between nodes and the cluster service node.

#### Deploying Applications
After creating a cluster, you can deploy applications using:
```bash
kubectl apply -f <filename>.yml
```

### Video Tutorial: Deploying a Cloud-based Kubernetes Cluster
#### Overview
In the video, Dan Lachance demonstrates how to deploy a Kubernetes cluster in the cloud, emphasizing the ease of using managed services.

#### Steps Covered in the Video
1. **Create a Resource**: Navigate to create a Kubernetes service in Azure.
2. **Configuration**: Set the cluster name, region, and node settings.
3. **Validation**: Review and create the cluster.

#### Using Cloud Shell
- The Azure portal includes a **Cloud Shell** for executing commands.
- Commands like `az aks create` and `kubectl get nodes` allow you to manage your Kubernetes environment.

### Conclusion
Kubernetes is a powerful tool for orchestrating containerized applications. Its features, such as autoscaling, load balancing, and zero-downtime updates, make it essential for modern application deployment and management.

## 9. Managing Kubernetes With kubectl

In this demonstration, we'll explore basic Kubernetes management using the `kubectl` command.

1. **Check Existing Kubernetes Clusters**  
   Access the Azure portal and navigate to the "All resources" view. Search for resources containing "Kubernetes." This will display any existing Kubernetes clusters, such as `myakscluster178` and `mykubernetescluster172`, along with supporting resources like Managed Identity and Load Balancers.

2. **Connect to a Kubernetes Cluster**  
   Click on a Kubernetes cluster (e.g., `mykubernetescluster172`). Use the "Connect" button to open Cloud Shell. This provides access to Azure command line tools and preinstalled Kubernetes management tools.

3. **Authenticate with Azure Kubernetes Service (AKS)**  
   In Cloud Shell, run the following command to authenticate:
   ```
   az aks get-credentials --resource-group hq --name myakscluster178
   ```
   This sets the current context for your cluster.

4. **List Nodes in the Cluster**  
   Clear the screen and list the nodes using:
   ```
   kubectl get nodes
   ```

5. **Create a Deployment Configuration**  
   Use the nano text editor to create a deployment file:
   ```
   nano app1.yaml
   ```
   Define the deployment configuration:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: pod1
   spec:
     containers:
       - name: app1
         image: caddy:latest
   ```
   Save and exit the editor (Ctrl+X, then confirm save).

6. **Apply the Deployment Configuration**  
   Deploy the configuration to your Kubernetes cluster:
   ```
   kubectl apply -f app1.yaml
   ```
   Confirm that `pod1` has been created.

7. **Verify the Pod Status**  
   Check the status of all pods:
   ```
   kubectl get pods --all-namespaces
   ```

8. **Show Pod Labels**  
   To see labels associated with the pods, run:
   ```
   kubectl get pods --show-labels
   ```

9. **Copy Files to a Running Pod**  
   To copy a file into the running pod, use:
   ```
   kubectl cp ./file1.txt pod1:/ -c app1
   ```

This process illustrates how to manage Kubernetes clusters effectively using `kubectl` commands for deploying and interacting with containerized applications.