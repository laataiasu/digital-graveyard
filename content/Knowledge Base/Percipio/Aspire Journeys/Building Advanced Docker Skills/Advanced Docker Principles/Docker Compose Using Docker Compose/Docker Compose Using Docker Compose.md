---
date: 2001-01-01
---

# Docker Compose Using Docker Compose

## 1.
### Docker and Docker Compose Installation Requirements

#### Supported Platforms for Docker Compose
Docker Compose is available on multiple platforms:
- **Windows** (Windows 10, Windows Server 2016)
- **Mac OS**
- **64-bit Linux**

Docker Compose requires **Docker Engine** to function, so ensure Docker Engine is installed locally or remotely before using Compose.

#### Installation on Desktop Systems
- **Docker Desktop for Mac and Windows**: Docker Compose is included in these installations.
- **Linux**: You must first install Docker Engine, then Docker Compose.

#### Alternative Installation Methods for Docker Compose
- **Using pip**: Install via Python package manager (`pip`).
- **Docker Container**: Install Docker Compose as a separate Docker container.

It is recommended to follow the installation method provided on the official Docker website to avoid troubleshooting issues.

---

### Docker Desktop Installation Requirements

#### Docker Desktop on Windows
Docker Desktop is available for:
- **Windows 10 (64-bit)**: Pro, Enterprise, or Education editions.
- **Windows 10 Home**.

##### System Requirements for Docker Desktop on Windows:
- **Hyper-V and Containers** features must be enabled.
- **Hyper-V Requirements**:
  - 64-bit CPU with **Second Level Address Translation (SLAT)**.
  - **4 GB RAM** minimum.
  - **Hardware virtualization** enabled in BIOS.

If these requirements aren't met, Docker Desktop may fail to install or perform poorly.

#### Docker Desktop on Mac
Docker Desktop is supported on:
- **Mac hardware**: 2010 or newer models.
- **Intel processor**.
- **Mac OS version**: 10.14 (Mojave) or later. Docker supports the current and previous two macOS releases.
- **Memory Requirements**: At least **4 GB RAM**.

##### Compatibility Notes:
- **VirtualBox**: If using VirtualBox, versions prior to **4.3.30** must be removed or upgraded, as they are incompatible with Docker Desktop.

#### Docker Desktop Components
The Docker Desktop installation includes:
- **Docker Engine**: Server with a long-running daemon (`docker-d`).
- **Docker CLI**: Command-line interface for interacting with Docker.
- **Docker Compose**: Tool for defining and running multi-container applications.
- **Notary**: Tool for managing trusted content.
- **Kubernetes**: Container orchestration tool.
- **Credential Helper**: Stores Docker credentials securely.

## 2.
### Docker Compose Fundamentals

#### What is Docker Compose?
Docker Compose is a tool for defining and managing multi-container applications. It uses a YAML file (`docker-compose.yml`) to configure application services and automate their creation.

Think of Docker Compose as an automated workflow for managing multiple containers, making it ideal for development, testing, CI/CD workflows, and staging environments.

#### Key Features of Docker Compose
- **Multiple Isolated Environments**: Create isolated environments on a single host.
- **Volume Data Persistence**: Retain volume data when containers are recreated.
- **Selective Container Recreation**: Only recreate containers that have changed, optimizing performance.
- **Environment Variables**: Use variables to configure different environments easily.
- **Container Orchestration**: Manage containers that work together and communicate within a defined environment.

#### Advantages of Docker Compose
- **Isolated Environments**: Run multiple isolated environments on a single host using project names to prevent conflicts between services.
- **Centralized Management**: Bring up or tear down an entire environment with a single command (`docker-compose up` / `docker-compose down`), simplifying deployment and portability.
- **Repeatable Testing**: Run unit and end-to-end tests in isolated environments that closely mimic production conditions.
- **Quick Deployment**: Easily create and destroy environments, particularly useful for testing, CI workflows, and staging.

#### Common Use Cases for Docker Compose
1. **Development Environments**: Compose provides an easy way to define environments that can run on any machine with Docker, eliminating configuration and hardware issues. It creates isolated environments that mirror production setups for accurate testing.
   
2. **Automated Testing**: Compose is perfect for continuous integration (CI) workflows. It enables the creation and destruction of testing environments that are similar to production, ensuring tests run in consistent, isolated conditions.

3. **Single Host, Multi-Container Deployment**: Originally designed for development and testing, Docker Compose is now used to deploy a range of containers on a single host system.

4. **Simplified Dependencies**: Docker Compose manages dependencies like databases, queues, and caches. It creates all necessary containers with a single command, making it ideal for testing and staging environments.

---

### Docker Compose Workflow

#### docker-compose.yml File
To deploy containers, Docker Compose uses a configuration file called `docker-compose.yml`. This file contains multiple sections, each representing a container, and defines the services they form when combined.

For example, a `docker-compose.yml` file might include:
- **Web**: Configuration for the web server.
- **DB**: Configuration for the database.

Each section within the YAML file defines specific components for the container, such as the image to use, environment variables, ports, and volumes.

#### Key Benefits in CI/CD and Development
- **Automated Testing**: Use Docker Compose to spin up dedicated environments for each test run.
- **Consistency**: Ensure environments in development, testing, and production are as similar as possible.
- **Efficiency**: Quickly create and tear down environments, speeding up testing and deployment cycles.

Docker Compose streamlines container management, making it an essential tool for development teams automating workflows and building reliable, repeatable environments.

## 3.
### Docker Compose Best Practices

#### 1. **Avoid Repetition with YAML Templates**
If your first container has many options that are repeated in other service definitions, create a **YAML template** for the first service and reuse it for others. This reduces duplication and makes maintenance easier.

#### 2. **Use an Init Process to Prevent Zombie Processes**
Include an **init process** in your containers to avoid the "PID 1 zombie reaping problem." Zombie processes occur when child processes terminate but aren't properly cleaned up by their parent, leading to resource consumption. The init process helps reaps zombie processes and prevents the kernel process table from filling up, allowing new processes to be created.

#### 3. **Use DNS Names for Container Communication**
Instead of manually creating a network and assigning IPs, you can rely on the **service name** as a DNS hostname. This allows containers to communicate with each other without the need for explicit network definitions.

#### 4. **Update Containers with Minimal Downtime**
To quickly update containers (e.g., swap images), modify your `docker-compose.yml` file and run:
```bash
docker-compose up -d
```
This command downloads the updated image and recreates the container with minimal downtime. If a full rebuild is needed, use:
```bash
docker-compose up -d --build
```

#### 5. **Manage Environment-Specific Variables**
For environments with slight configuration differences, use a **template Docker Compose file** and replace variables based on the environment. You can use a `.env` file to store environment-specific variables, which will be substituted in the `docker-compose.yml` file.

#### 6. **Use a Single Docker Compose File for All Environments**
While Docker recommends separate Compose files for development and production, maintaining a single file is often safer. It reduces errors caused by manually syncing changes between files and ensures consistency across environments. Explicitly specify the image version to avoid issues with the default `latest` tag.

#### 7. **Version Control Your Docker Compose File**
Store your `docker-compose.yml` file **alongside your application code** in version control. This ensures that changes to the application (like new services or port changes) are always reflected in the Compose configuration. **Never include secrets** in your Compose file or source control.

#### 8. **Use Load Balancers in Development**
In production, multiple instances of a service often require load balancing. It's good practice to also use load balancers in your **development environment**, even though you may only have one instance locally. Keeping port numbers consistent for each service across environments helps manage load balancing and network configurations.

#### 9. **Centralize Environment Variables**
Instead of relying on `.env` files, it's often better to define **environment variables** explicitly in the service definitions within the `docker-compose.yml` file. This centralizes configuration and avoids the potential issues of misconfigured or outdated `.env` files.

#### 10. **Define Named Volumes for Portability**
Define **named volumes** at the top of your `docker-compose.yml` file to make it easier to manage persistent data storage. Named volumes allow for easier swapping of storage solutions during deployment or development (e.g., using local storage during development, and networked storage in production).

#### 11. **Follow a Clear Naming Convention**
Use a **naming convention** that makes it easy to trace each container to its corresponding code base. The container name should indicate the Git repository, branch, and Dockerfile used, which helps maintain consistency and traceability.

#### 12. **Ensure Accurate Exit Codes**
Monitor **exit codes** for each service to determine if containers start successfully or encounter errors. Accurate exit codes are crucial for debugging and identifying issues in your logs. Misleading exit codes can cause difficulty in troubleshooting and impact system reliability.

#### 13. **Test Changes in Isolated Environments**
Compose provides a quick, repeatable way to create isolated environments for testing. This is invaluable for **automated testing** in CI/CD pipelines, where you can ensure that your app behaves as expected in environments that closely mimic production.

By adhering to these best practices, you can make your Docker Compose workflow more efficient, maintainable, and reliable—whether for development, testing, or production environments.

## 4.
### Steps to Define, Build, and Run a Docker Compose Project

#### 1. **Defining Your Project**
To start a Docker Compose project, you need to define the services your application will use, such as databases and web servers. Here's how to define a project step by step:

1. **Create a Directory for Your Project**
   - Create an empty directory where your project files will reside:
     ```bash
     mkdir MyProject
     cd MyProject
     ```

2. **Create the `docker-compose.yml` File**
   - In this directory, create the `docker-compose.yml` file, which will contain all the configuration for your services.
   
   Example for a **WordPress** setup with **MySQL**:

   ```yaml
   version: '3.3'

   services:
     db:
       image: mysql:5.7
       volumes:
         - db_data:/var/lib/mysql
       restart: always
       environment:
         MYSQL_ROOT_PASSWORD: somewordpress
         MYSQL_DATABASE: wordpress
         MYSQL_USER: wordpress
         MYSQL_PASSWORD: wordpress

     wordpress:
       depends_on:
         - db
       image: wordpress:latest
       ports:
         - "8000:80"
       restart: always
       environment:
         WORDPRESS_DB_HOST: db:3306
         WORDPRESS_DB_USER: wordpress
         WORDPRESS_DB_PASSWORD: wordpress
         WORDPRESS_DB_NAME: wordpress
       volumes:
         - db_data:/var/lib/mysql

   volumes:
     db_data:
   ```

   **Explanation of Key Sections:**
   - **`version:`**: Specifies the Docker Compose version.
   - **`services:`**: Defines the containers you need.
     - **`db:`**: Configures the MySQL database service.
     - **`wordpress:`**: Configures the WordPress service, which depends on the database.
   - **`volumes:`**: Defines shared storage for persistent data (e.g., MySQL data).

#### 2. **Building the Project**
After defining the `docker-compose.yml` file, you need to build the project by pulling the necessary images and creating the containers.

1. **Run `docker-compose up`**
   - Run the following command in the directory where the `docker-compose.yml` file is located:
     ```bash
     docker-compose up -d
     ```
   - The `-d` flag stands for *detached mode*, meaning it runs the containers in the background.

2. **What Happens Next?**
   - Docker Compose will:
     - Create a network for your services (e.g., `my_wordpress_default`).
     - Pull the images (`mysql:5.7` and `wordpress:latest`) from Docker Hub.
     - Create and start the containers (e.g., `my_wordpress_db_1` and `my_wordpress_wordpress_1`).
   
   **Sample Output**:
   ```
   Creating network "my_wordpress_default" with the default driver
   Pulling db (mysql:5.7)...
   Pulling wordpress (wordpress:latest)...
   Creating my_wordpress_db_1  ... done
   Creating my_wordpress_wordpress_1 ... done
   ```

3. **Access Your Application**
   - After the containers are up and running, you can access your WordPress application.
   - If you're using Docker Desktop for Mac or Windows, go to `http://localhost:8000` in your web browser.
   - If using Docker Machine, get the IP address with:
     ```bash
     docker-machine ip MACHINE_VM
     ```
     Then access `http://<machine-ip>:8000`.

#### 3. **Shutting Down and Cleaning Up**
Once you're done with the containers, it's important to clean up resources to avoid consuming unnecessary memory and disk space.

1. **Stop and Remove Containers (Without Deleting Volumes)**
   - To stop the containers and remove them while keeping your database intact, use:
     ```bash
     docker-compose down
     ```

2. **Stop and Remove Containers, Volumes, and Networks**
   - If you want to completely remove everything, including volumes (which contain persistent data), use:
     ```bash
     docker-compose down --volumes
     ```

3. **Why Clean Up?**
   - Containers and volumes consume system resources. Keeping unnecessary containers running, especially with Docker Desktop (which uses significant memory), can slow down your machine. Regularly cleaning up helps prevent resource overload.

By following these steps, you can easily define, build, and run a Docker Compose project, ensuring that your environment is set up correctly and cleaned up when no longer needed.

## 5.
### Docker Compose CLI Features Overview

The **Docker Compose CLI** is a powerful tool for managing multi-container Docker applications. It builds upon the core **Docker CLI** and provides specific commands and flags for handling complex setups. Here's a breakdown of key features and usage of the **docker-compose** command.

---

### **Docker CLI and Docker Compose**
Docker Compose is an additional command-line tool that enhances the Docker CLI. While Docker CLI directly interacts with the Docker daemon, Docker Compose provides an abstraction layer to manage multi-container applications, such as web services, databases, and caches, using a `docker-compose.yml` configuration file.

#### **Basic Command Structure**:
```bash
docker-compose [OPTIONS] COMMAND [ARGS...]
```
- **OPTIONS**: Flags or parameters for the command.
- **COMMAND**: The action you want to perform (e.g., `up`, `down`, `build`).
- **ARGS**: Additional arguments, such as service names or paths.

---

### **Common Docker Compose Flags**

These flags modify the behavior of the `docker-compose` command:

- `-f` or `--file`: Specifies one or more Compose files. If not specified, Docker Compose searches for `docker-compose.yml` in the current directory.
  
  Example:
  ```bash
  docker-compose -f custom-compose.yml up
  ```

- `-p` or `--project-name`: Sets the project name. If not specified, it defaults to the name of the current directory.
  
  Example:
  ```bash
  docker-compose -p my_project up
  ```

- `--profile`: Activates specific profiles for the project. Profiles allow you to group services by type (e.g., `frontend`, `backend`) and start only the services related to a profile.
  
  Example:
  ```bash
  docker-compose --profile frontend up
  ```

- `--verbose`: Enables verbose output, giving more detailed logs.
  
- `--log-level`: Sets the logging level (e.g., `DEBUG`, `INFO`, `ERROR`).

- `--no-ansi`: Disables colored output and ANSI escape sequences.

- `-v` or `--version`: Displays the Docker Compose version.
  
- `-H` or `--host`: Specifies the Docker daemon socket to connect to (useful when managing remote Docker hosts).

---

### **Docker Compose Commands**

The **docker-compose** CLI provides a rich set of commands to manage the lifecycle of multi-container applications. Here are some of the most commonly used commands:

1. **`up`**: Creates and starts containers from the configuration in the `docker-compose.yml` file.
   ```bash
   docker-compose up
   ```
   - Add `-d` to run containers in detached mode (in the background).

2. **`down`**: Stops and removes all containers, networks, and volumes defined in the Compose file.
   ```bash
   docker-compose down
   ```

3. **`build`**: Builds or rebuilds services defined in the Compose file.
   ```bash
   docker-compose build
   ```

4. **`logs`**: Views the logs of the containers.
   ```bash
   docker-compose logs
   ```

5. **`ps`**: Lists the running containers and their details.
   ```bash
   docker-compose ps
   ```

6. **`exec`**: Executes a command inside a running container.
   ```bash
   docker-compose exec <service_name> <command>
   ```

7. **`stop`**: Stops running containers without removing them.
   ```bash
   docker-compose stop
   ```

8. **`restart`**: Restarts the containers for a service.
   ```bash
   docker-compose restart <service_name>
   ```

9. **`rm`**: Removes stopped containers.
   ```bash
   docker-compose rm
   ```

10. **`scale`**: Scales the number of containers for a specific service.
    ```bash
    docker-compose scale <service_name>=<num_containers>
    ```

---

### **Working with Multiple Compose Files**

Docker Compose allows you to specify multiple configuration files using the `-f` flag. This is useful when you want to split the configuration into different environments (e.g., `development`, `production`, `staging`).

For example, consider the following command:
```bash
docker-compose -f docker-compose.yml -f docker-compose.override.yml up
```
- **`docker-compose.yml`**: The base configuration file.
- **`docker-compose.override.yml`**: Additional settings or overrides (e.g., for development purposes).

Compose processes the files in order. If a setting is defined in both files, the later file will override the earlier one.

---

### **Using Profiles**

**Profiles** allow you to group and manage services for different environments. For example, you could define a `frontend` profile for UI services and a `backend` profile for API services. With profiles, you can start only the services you need for a particular environment or scenario.

To specify a profile, use the `--profile` flag:
```bash
docker-compose --profile frontend up
```
This will start only the services associated with the `frontend` profile.

---

### **Environment Variables**

You can specify Compose configurations using environment variables, making your setups more dynamic. These can be used for things like file paths, project names, or service-specific configuration.

Example: 
```bash
export COMPOSE_FILE=docker-compose.yml:docker-compose.prod.yml
docker-compose up
```

Alternatively, you can set the project name via an environment variable:
```bash
export COMPOSE_PROJECT_NAME=my_project
docker-compose up
```

---

### **Practical Example**

Let's walk through a practical example of using the Docker Compose CLI:

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
1. **-f**: Specifies two Compose files:
   - `docker-compose.yml`: The base configuration.
   - `docker-compose.prod.yml`: Overrides for the production environment.
   
2. **up -d**: Starts the containers in detached mode.

In this example, the `docker-compose.prod.yml` file could include settings like different environment variables, port numbers, or volume configurations for a production environment.

---

### **Conclusion**

The Docker Compose CLI enhances the power of Docker by making it easier to manage multi-container applications. It allows for flexible configuration with flags, profiles, and environment variables, and provides a suite of commands for building, running, and managing your services.

Key takeaways:
- Use the `-f` flag to specify configuration files.
- Leverage profiles to manage different environments.
- Manage services with commands like `up`, `down`, `logs`, and `exec`.
- Customize behavior with flags like `-p`, `--verbose`, `--profile`, and others. 

By understanding and utilizing the Docker Compose CLI effectively, you can streamline your workflows and improve the management of Dockerized applications.

## 6.
### Building a Simple Python Web Application Using Docker Compose

In this video, we walk through the steps of creating a basic Python web application with Flask and Redis using Docker Compose. The application will include a simple hit counter feature that uses Redis caching to store the number of times the page has been accessed.

Here's a detailed breakdown of the steps involved:

---

### **Step 1: Set Up the Docker Compose File**

We'll start by defining the services required for the application in the `docker-compose.yml` file.

1. **Version and Services**
   - We'll set the version of Docker Compose to `3.9`:
     ```yaml
     version: "3.9"
     ```
   
2. **Web Service**  
   This is where we define the application server:
   ```yaml
   services:
     web:
       build: .
       ports:
         - "5000:5000"
       depends_on:
         - redis
     redis:
       image: "redis:alpine"
   ```
   - **Web Service**: 
     - We specify that the web service will build from a Dockerfile in the current directory using `build: .`.
     - We map port 5000 from the container to port 5000 on the host.
     - It depends on the `redis` service, meaning Redis must be up before the web app starts.
   - **Redis Service**:
     - We use the official Redis image (`redis:alpine`) to set up the Redis service.
  
3. **Next Step**: Create the `Dockerfile` to define how the web app is built.

---

### **Step 2: Create the Dockerfile**

This Dockerfile defines the environment in which the Python web app will run.

1. **Base Image and Setup**
   ```dockerfile
   FROM python:3.7-alpine
   WORKDIR /code
   ENV FLASK_APP=app.py
   ENV FLASK_RUN_HOST=0.0.0.0
   ```
   - The Docker image is based on `python:3.7-alpine` for a lightweight Python environment.
   - The working directory inside the container is set to `/code`.
   - We define environment variables for Flask:
     - `FLASK_APP` is set to `app.py`, the entry point for the Flask app.
     - `FLASK_RUN_HOST` is set to `0.0.0.0`, which allows Flask to listen on all available network interfaces.
   
2. **Install Dependencies**:
   ```dockerfile
   RUN apk add --no-cache gcc musl-dev linux-headers
   ```
   - We use `apk`, the Alpine package manager, to install necessary dependencies for Python packages that require compilation (e.g., Redis client).

3. **Copy and Install Python Dependencies**:
   ```dockerfile
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   ```
   - We copy the `requirements.txt` file into the container and then install the Python dependencies.

4. **Expose Port**:
   ```dockerfile
   EXPOSE 5000
   ```
   - We expose port 5000 so that Flask can serve the app on that port.

5. **Copy Project Files**:
   ```dockerfile
   COPY . .
   ```
   - Copies the current directory (your application code) into the container's working directory.

6. **Define the Default Command**:
   ```dockerfile
   CMD ["flask", "run"]
   ```
   - The default command to run the Flask application is `flask run`, which starts the server when the container runs.

---

### **Step 3: Create the `requirements.txt` File**

The `requirements.txt` file lists the Python dependencies for our application:

```txt
flask
redis
```
- **Flask**: The web framework we'll use to build the application.
- **Redis**: The Redis client for Python to interact with Redis.

---

### **Step 4: Create the Flask Application (`app.py`)**

Now we define the Python application that will run inside the container.

```python
import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello World! I have been seen {count} times.'

if __name__ == '__main__':
    app.run()
```

- **Imports**:
  - `redis`: For connecting to the Redis cache.
  - `flask`: For building the web application.
  
- **App Setup**:
  - A `Flask` app is created.
  - A connection to Redis is established using the `redis.Redis` object, where the `host` is set to `redis` (the name of the Redis service in the `docker-compose.yml`) and the `port` is `6379` (the default Redis port).
  
- **Hit Count Logic**:
  - The function `get_hit_count()` increments a `hits` counter stored in Redis every time the page is visited.
  - If the Redis server is temporarily unavailable, it retries 5 times with a delay of 0.5 seconds.

- **Route**:
  - The route `/` returns a message with the number of times the page has been visited, using the value from the Redis counter.

---

### **Step 5: Build and Run the Application with Docker Compose**

Now that all files are in place, you can build and run the application using Docker Compose.

1. **Build and Start the Containers**:
   ```bash
   docker-compose up -d
   ```
   - The `-d` flag runs the containers in detached mode, meaning they run in the background.

2. **Check Running Containers**:
   ```bash
   docker ps
   ```
   - This command shows the running containers. You should see two services: `python_web_1` and `python_redis_1`.

3. **Access the Application**:
   - Open your browser and go to [http://localhost:5000](http://localhost:5000).
   - You should see a message: `Hello World! I have been seen X times.` where `X` increments each time you refresh the page.

---

### **Conclusion**

You’ve now created a simple Python web application using Flask and Redis, containerized it with Docker, and managed it using Docker Compose. The application uses Redis as a cache to store a hit counter that increments with each page refresh.

This setup is very flexible and can be expanded with more services, environments, and complex application logic. Docker Compose makes it easy to manage all these components as a single, cohesive unit.

## 7. 
### Building a Simple PHP Web Application with Apache Using Docker Compose

In this video, we'll walk through how to set up a simple PHP web application running on an Apache web server, all managed using Docker Compose. This setup involves creating a Docker Compose file, a Dockerfile for building the PHP application, and a basic `index.php` file to display a "Hello World" message.

---

### **Step 1: Project Directory Structure**

We'll begin by setting up the project directory structure. Your directory will look like this:

```
/project-root
  ├── docker-compose.yml
  └── /app
      └── Dockerfile
      └── index.php
```

---

### **Step 2: Create the `docker-compose.yml` File**

The `docker-compose.yml` file defines how the services (containers) will be set up, including which image to build, the ports to expose, and volumes to mount.

1. **Define Version and Services**

   Create a file named `docker-compose.yml` in the root of your project directory. Then, start by defining the version and services:
   
   ```yaml
   version: "3.7"

   services:
     web:
       build: ./app
       ports:
         - "8000:80"
       volumes:
         - ./app:/var/www/html
   ```

   - **Version**: Specifies the version of the Docker Compose file format (in this case, `3.7`).
   - **Services**: Defines the containers that Docker Compose will run.
   - **web**: The service for the PHP web application.
     - **build**: This tells Docker Compose to build the `web` service from the `./app` directory, which contains the `Dockerfile`.
     - **ports**: Maps port 8000 on your local machine to port 80 in the container, so the app will be accessible via `localhost:8000`.
     - **volumes**: Mounts the local `./app` directory to the container's `/var/www/html` directory, which is where Apache serves the PHP files.

---

### **Step 3: Create the `Dockerfile` in the `app` Directory**

The `Dockerfile` defines how the PHP container is built. We’ll use the `php:7.2-apache` image, which combines PHP with the Apache web server.

1. **Create the Dockerfile**

   In the `app` folder, create a file named `Dockerfile`. Add the following content:
   
   ```dockerfile
   FROM php:7.2-apache
   ```

   This command tells Docker to pull the `php:7.2-apache` image from Docker Hub, which includes PHP 7.2 and Apache.

---

### **Step 4: Create the PHP Application (index.php)**

Now we need to create a simple PHP application that will display "Hello World" when accessed through the web browser.

1. **Create the `index.php` File**

   In the `app` folder, create a file named `index.php`. Add the following PHP code:
   
   ```php
   <?php
   echo "<h1>Hello World</h1>";
   ?>
   ```

   This script simply outputs a header (`<h1>`) with the text "Hello World".

---

### **Step 5: Build and Run the Application with Docker Compose**

Now that everything is set up, we can use Docker Compose to build and start the containers.

1. **Open a Terminal and Run Docker Compose**

   In the root directory of your project (where the `docker-compose.yml` file is located), open a terminal and run the following command:
   
   ```bash
   docker-compose up -d
   ```

   - The `-d` flag runs the containers in detached mode, meaning they will run in the background.
   - Docker Compose will read the `docker-compose.yml` file, build the `web` service using the `Dockerfile` in the `app` folder, and start the container.

2. **Check the Running Containers**

   After Docker Compose finishes, run the following command to ensure the containers are running:
   
   ```bash
   docker ps
   ```

   This will list all running containers. You should see a container for the web service named something like `php_web_1`.

---

### **Step 6: Access the Application in the Browser**

Now that the container is running, open your web browser and navigate to:

```
http://localhost:8000
```

You should see the following message displayed in your browser:

```
Hello World
```

This confirms that your PHP application is running successfully on the Apache web server, hosted inside a Docker container.

---

### **Step 7: Summary**

Here’s a recap of what we’ve done:

- **docker-compose.yml**: Defined the services for the application, including how to build the PHP web app from the `app` folder, map ports, and set up volume mounts.
- **Dockerfile**: Defined how the PHP application will be built using the `php:7.2-apache` image from Docker Hub.
- **index.php**: Created a simple PHP script that displays "Hello World".
- **docker-compose up**: Built and ran the application using Docker Compose.

This setup can be extended with additional PHP files, Apache configurations, and services like databases, caching, etc., to build a more complex web application.

## 8.
### Building a Django Application with PostgreSQL Using Docker Compose

In this tutorial, we'll walk through how to set up a Django web application with a PostgreSQL database, all managed using Docker Compose. We'll create a Python web application and connect it to a PostgreSQL database, leveraging Docker to manage both services. Below are the steps for setting this up:

---

### **Step 1: Create the Project Structure**

Your project directory should look something like this:

```
/DJANGO
  ├── docker-compose.yml
  ├── Dockerfile
  ├── requirements.txt
  └── /django
      └── (Django project files will be created here)
```

---

### **Step 2: Create the `Dockerfile`**

The `Dockerfile` defines the Docker image for your Django application, including the necessary dependencies.

1. **Create the `Dockerfile`** in the root of your project folder:

   ```dockerfile
   # Use the official Python 3 image as a base
   FROM python:3

   # Set environment variables to ensure Python output is sent straight to terminal (not buffered)
   ENV PYTHONUNBUFFERED=1

   # Set the working directory to /code in the container
   WORKDIR /code

   # Copy the requirements.txt file to the container
   COPY requirements.txt /code/

   # Install the required dependencies inside the container
   RUN pip install -r requirements.txt

   # Copy everything from the current directory to the /code directory in the container
   COPY . /code/
   ```

   - **FROM python:3**: Uses the official Python 3 image as the base.
   - **ENV PYTHONUNBUFFERED=1**: Disables buffering of Python output, which is helpful for Docker logs.
   - **WORKDIR /code**: Sets the working directory inside the container to `/code`.
   - **COPY requirements.txt /code/**: Copies the `requirements.txt` file into the container.
   - **RUN pip install -r requirements.txt**: Installs the dependencies specified in `requirements.txt`.
   - **COPY . /code/**: Copies the rest of the project files into the `/code` directory inside the container.

---

### **Step 3: Create the `requirements.txt` File**

The `requirements.txt` file lists the Python packages that your Django application needs to run. For our case, we need Django and psycopg2 (the PostgreSQL adapter for Python).

1. **Create `requirements.txt`** with the following content:

   ```
   Django>=3.0,<4.0
   psycopg2-binary>=2.8
   ```

   - **Django>=3.0,<4.0**: Installs a version of Django between 3.0 and 4.0.
   - **psycopg2-binary>=2.8**: Installs the PostgreSQL adapter for Python.

---

### **Step 4: Create the `docker-compose.yml` File**

Now we will create a `docker-compose.yml` file to define the services for our application (the Django web server and the PostgreSQL database).

1. **Create `docker-compose.yml`** in the root of your project:

   ```yaml
   version: "3.9"

   services:
     db:
       image: postgres:13
       volumes:
         - ./data/db:/var/lib/postgresql/data
       environment:
         POSTGRES_DB: postgres
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: postgres

     web:
       build: .
       command: python manage.py runserver 0.0.0.0:8000
       volumes:
         - .:/code
       ports:
         - "8000:8000"
       depends_on:
         - db
   ```

   - **version**: Specifies the version of the Docker Compose file format (3.9).
   - **services**: Defines the two services, `db` and `web`.
   
   **db service**:
   - **image**: Uses the official `postgres:13` image from Docker Hub.
   - **volumes**: Mounts a volume for persistent PostgreSQL data storage (`./data/db` on the host maps to `/var/lib/postgresql/data` in the container).
   - **environment**: Sets the environment variables for PostgreSQL (`POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`).
   
   **web service**:
   - **build**: Builds the Django web service from the current directory (where the `Dockerfile` is located).
   - **command**: Runs Django's development server on all network interfaces (`0.0.0.0`) and binds it to port 8000.
   - **volumes**: Mounts the current directory (`.`) to the `/code` directory in the container, allowing live code updates.
   - **ports**: Maps port 8000 on the host to port 8000 in the container.
   - **depends_on**: Specifies that the `web` service depends on the `db` service, ensuring that the database is ready before the web service starts.

---

### **Step 5: Create the Django Project**

We will now use Docker Compose to run a command that sets up a new Django project.

1. **Run the Django Project Setup** using the following command:

   Open a terminal and run the following command to create a new Django project:

   ```bash
   docker-compose run web django-admin startproject django .
   ```

   - This will generate a new Django project named `django` in the current directory (`.`).
   - `docker-compose run web` runs the Django command (`django-admin startproject`) inside the web service container.

   After the command runs, the `django` folder will contain the standard Django project structure:

   ```
   django/
     ├── manage.py
     ├── django/
       ├── __init__.py
       ├── settings.py
       ├── urls.py
       ├── wsgi.py
       └── asgi.py
   ```

---

### **Step 6: Configure the Database Connection in Django**

Now, let's configure Django to use PostgreSQL as the database.

1. **Edit `settings.py`** to configure the database connection:

   In the `django/django/settings.py` file, scroll down to the `DATABASES` section and replace the default SQLite configuration with the PostgreSQL configuration:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'postgres',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': 'db',
           'PORT': '5432',
       }
   }
   ```

   - **ENGINE**: Specifies the PostgreSQL database backend.
   - **NAME**: The database name (`postgres` as set in the `docker-compose.yml` file).
   - **USER** and **PASSWORD**: The username and password for the database (`postgres` as set in `docker-compose.yml`).
   - **HOST**: Refers to the name of the database service (`db`), which Docker will resolve to the container running PostgreSQL.
   - **PORT**: The default PostgreSQL port (`5432`).

---

### **Step 7: Run the Application**

Now that everything is configured, we can start our application with Docker Compose.

1. **Start the services**:

   Run the following command to start both the `db` and `web` services:

   ```bash
   docker-compose up -d
   ```

   This will build the images, create the containers, and start the services. The `-d` flag runs the containers in detached mode.

2. **Apply the migrations**:

   Once the services are up, run the following command to apply the database migrations:

   ```bash
   docker-compose run web python manage.py migrate
   ```

3. **Access the Application**:

   Now, open your browser and go to `http://localhost:8000`. You should see the Django welcome page confirming that the installation was successful.

   ```
   The install worked successfully! Congratulations!
   ```

---

### **Step 8: Summary**

Here’s a summary of the steps we’ve taken:

1. **Dockerfile**: Defined how to build the Docker image for our Django app.
2. **requirements.txt**: Listed the required Python packages (Django and psycopg2).
3. **docker-compose.yml**: Defined two services: `db` for PostgreSQL and `web` for the Django app.
4. **Django Project**: Created a Django project using Docker Compose and configured it to use PostgreSQL.
5. **Run the Application**: Started the services with `docker-compose up -d` and accessed the Django app in the browser.

Now, you have a Django application running with a PostgreSQL database, all within Docker containers!

## 9.
### Building a Python Flask Application with Docker Compose

In this tutorial, we'll walk through how to set up a simple Python Flask application using Docker Compose. The setup involves creating a `docker-compose.yml` file, setting up a Dockerfile to define how the Flask app will be built, and creating the required Python files (such as `requirements.txt` and `app.py`) for the Flask application itself.

---

### **Step 1: Set up the Project Structure**

Your project directory will look like this:

```
/FlaskApp
  ├── docker-compose.yml
  ├── /app
      ├── Dockerfile
      ├── requirements.txt
      └── app.py
```

### **Step 2: Create the `docker-compose.yml` File**

The `docker-compose.yml` file will define the services for the Flask application (in this case, just a `web` service that runs the Flask app).

1. **Create the `docker-compose.yml` file** in the root of the project folder:

   ```yaml
   version: "3.7"

   services:
     web:
       build: ./app
       ports:
         - "5000:5000"
   ```

   - **version**: Specifies the version of Docker Compose.
   - **services**: Defines the services in the application. Here, we have only one service: `web`.
   - **build**: Specifies the directory where the `Dockerfile` for the `web` service is located (in the `./app` directory).
   - **ports**: Maps port 5000 on the host to port 5000 on the container so we can access the app in the browser.

---

### **Step 3: Create the Dockerfile for the Flask App**

The Dockerfile will define how the Docker image for the Flask app is built.

1. **Create the `Dockerfile` inside the `app` directory**:

   ```dockerfile
   # Use the official Python 3.7 Alpine image as the base image
   FROM python:3.7-alpine

   # Set the working directory inside the container to /app
   WORKDIR /app

   # Copy the requirements.txt file into the container
   COPY requirements.txt /app/

   # Install the Python dependencies
   RUN pip3 install --no-cache-dir -r requirements.txt

   # Copy the rest of the application code into the container
   COPY . /app/

   # Set the entry point to run the app with Python
   ENTRYPOINT ["python3", "app.py"]
   ```

   - **FROM python:3.7-alpine**: Uses a lightweight version of Python 3.7 as the base image.
   - **WORKDIR /app**: Sets the working directory for the app inside the container to `/app`.
   - **COPY requirements.txt /app/**: Copies the `requirements.txt` file into the container.
   - **RUN pip3 install -r requirements.txt**: Installs all the dependencies listed in `requirements.txt`.
   - **COPY . /app/**: Copies the entire `app` folder into the `/app` directory inside the container.
   - **ENTRYPOINT ["python3", "app.py"]**: Defines the command to run when the container starts. In this case, it will start the Flask app by running `app.py`.

---

### **Step 4: Set up the `requirements.txt` File**

The `requirements.txt` file specifies the Python packages needed to run the Flask application.

1. **Create the `requirements.txt` file** in the `app` directory:

   ```txt
   flask
   ```

   - This file only contains Flask as the dependency since we’re building a simple Flask app.

---

### **Step 5: Create the Flask Application (app.py)**

Now, we’ll create a simple Python Flask application that will serve a "Hello World" message.

1. **Create the `app.py` file** in the `app` directory:

   ```python
   from flask import Flask

   # Initialize the Flask application
   app = Flask(__name__)

   # Define a route for the root ("/") URL
   @app.route('/')
   def hello():
       return "Hello World!"

   # Run the Flask app on all interfaces (0.0.0.0) so it can be accessed externally
   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
   ```

   - **Flask(__name__)**: Initializes the Flask application.
   - **@app.route('/')**: Defines a route for the root URL (`/`) that calls the `hello` function when accessed.
   - **app.run(host="0.0.0.0", port=5000)**: Runs the Flask app on all network interfaces (`0.0.0.0`) so it’s accessible on port 5000 from outside the container.

---

### **Step 6: Build and Run the Application Using Docker Compose**

Now that all the necessary files are set up, we can use Docker Compose to build the Flask app and run it inside a Docker container.

1. **Open the terminal** in the root directory of the project (where `docker-compose.yml` is located).
   
2. **Run the following command** to build the image and start the container:

   ```bash
   docker-compose up -d
   ```

   - This command will:
     - Build the Flask app image based on the `Dockerfile` inside the `./app` directory.
     - Start the container in detached mode (`-d`).

3. **Access the Flask application**:

   Open your web browser and go to `http://localhost:5000`. You should see:

   ```
   Hello World!
   ```

   This confirms that the Flask app is up and running inside the Docker container.

---

### **Step 7: Summary and Recap**

Here’s a quick summary of what we’ve done:

1. **`docker-compose.yml`**: Defined the services (in this case, just the `web` service for the Flask app).
2. **`Dockerfile`**: Configured how the Docker image should be built for the Flask app, including installing dependencies and setting the entry point to run the Flask application.
3. **`requirements.txt`**: Listed the Flask dependency.
4. **`app.py`**: Created a simple Flask application that returns "Hello World!" when accessed at the root URL (`/`).
5. **Run the app**: Used `docker-compose up -d` to build the app, start the container, and run the Flask app.
6. **Access the app**: Accessed the app in the browser at `http://localhost:5000`.

Now, you have a fully working Flask application running in a Docker container, all managed with Docker Compose!

## 10.

### Setting Up a WordPress Application with Docker Compose

In this tutorial, we will go through the process of setting up a WordPress application using Docker Compose. Docker Compose allows us to define and run multi-container Docker applications. In this case, we'll set up two containers: one for the MySQL database and one for the WordPress site itself. By using Docker Compose, we can easily manage these containers and connect them to each other.

---

### **Step 1: Set Up the Project Structure**

Here’s what your project directory will look like:

```
/WORDPRESS
  └── docker-compose.yml
```

### **Step 2: Create the `docker-compose.yml` File**

First, let’s define our services (WordPress and MySQL) in the `docker-compose.yml` file.

1. **Create a new file** named `docker-compose.yml` inside the `WORDPRESS` directory.
2. **Add the following content** to the `docker-compose.yml` file:

```yaml
version: "3.9"

services:
  db:
    image: mysql:5.7
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress

volumes:
  db_data:
```

### **Explanation of the `docker-compose.yml` File:**

- **`version: "3.9"`**: Specifies the version of Docker Compose to use.
- **`services`**: This section defines the two services we are using:
  
  - **`db`** (MySQL):
    - **`image: mysql:5.7`**: We’re using the official MySQL 5.7 image from Docker Hub.
    - **`volumes`**: This maps a volume called `db_data` to the container's data directory `/var/lib/mysql`. It allows data to persist across container restarts.
    - **`restart: always`**: Ensures that the MySQL container always restarts unless explicitly stopped.
    - **`environment`**: These are environment variables needed to set up MySQL:
      - `MYSQL_ROOT_PASSWORD`: Root password for MySQL.
      - `MYSQL_DATABASE`: The name of the database (WordPress will use this).
      - `MYSQL_USER` and `MYSQL_PASSWORD`: Credentials for connecting WordPress to MySQL.
  
  - **`wordpress`**:
    - **`depends_on: db`**: This ensures that the WordPress service waits for the `db` service to be ready before starting.
    - **`image: wordpress:latest`**: Pulls the latest WordPress image from Docker Hub.
    - **`ports`**: Maps port 8000 on the host machine to port 80 on the WordPress container, so we can access WordPress on `http://localhost:8000`.
    - **`restart: always`**: Ensures the WordPress container always restarts unless explicitly stopped.
    - **`environment`**: These environment variables are needed for WordPress to connect to the MySQL database:
      - `WORDPRESS_DB_HOST`: Host and port where the database is located (`db:3306`).
      - `WORDPRESS_DB_USER`, `WORDPRESS_DB_PASSWORD`, and `WORDPRESS_DB_NAME`: These values match the ones set up for the MySQL container.

- **`volumes`**: This section defines the `db_data` volume to persist the MySQL database data across container restarts.

---

### **Step 3: Start the Containers Using Docker Compose**

1. **Open a terminal** in the `WORDPRESS` directory (where the `docker-compose.yml` file is located).
   
2. **Run the following command** to start up the services in detached mode:

   ```bash
   docker-compose up -d
   ```

   - **`up`**: Tells Docker Compose to create and start the services defined in the `docker-compose.yml` file.
   - **`-d`**: Runs the containers in detached mode (in the background).

3. **Verify the services are running**:

   After running the `docker-compose up -d` command, Docker Compose will create the containers and set up the network. You should see something like this:

   ```
   Creating network "wordpress_default" with the default driver
   Creating volume "wordpress_db_data" with default driver
   Creating wordpress_db_1 ... done
   Creating wordpress_wordpress_1 ... done
   ```

   This means the WordPress and MySQL containers are now up and running.

---

### **Step 4: Access the WordPress Application**

1. Open your web browser and navigate to:

   ```
   http://localhost:8000
   ```

2. **WordPress Setup**:
   - You should see the WordPress installation screen. Select your language (e.g., English).
   - Click **"Continue"**.

3. **Configure WordPress**:
   - **Site Title**: You can name your site "WordPress".
   - **Username**: Choose a username (e.g., `admin`).
   - **Password**: Use the password provided in the setup (or you can choose your own).
   - **Email**: Enter a valid email address (e.g., `me@me.com`).
   
4. Click **"Install WordPress"** to complete the installation.

---

### **Step 5: Log in to WordPress**

Once the installation is complete, you can log in to your new WordPress site:

1. Click **"Log In"**.
2. Use the **username** and **password** you created during the setup process.
3. You will be logged into your WordPress admin dashboard, and you can start customizing your site!

---

### **Step 6: Recap**

Here’s a quick recap of the steps involved:

1. **Create `docker-compose.yml`**: We defined two services (`db` for MySQL and `wordpress` for the WordPress application) with the necessary configurations and environment variables.
2. **Start the containers**: We used `docker-compose up -d` to start the services in detached mode.
3. **Access WordPress**: We visited `http://localhost:8000` to complete the WordPress installation.
4. **Log in**: After the installation, we logged into the WordPress admin dashboard and started managing our new site.

By using Docker Compose, we have successfully set up WordPress and MySQL in isolated containers, which makes it easy to run WordPress locally in a clean, reproducible environment.
