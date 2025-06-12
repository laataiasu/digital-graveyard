# Performance Troubleshooting

## 2
### Performance Engineering

**Definition**  
Performance engineering is a discipline focused on the non-functional requirements of software, including metrics like:

- **Throughput**: The amount of network traffic the software can handle.
- **Latency**: The speed of response of the software.
- **Memory usage**: The amount of memory consumed by the software.

Other metrics may also be relevant to performance engineering, but these three are easily measurable through performance tests.

---

### Performance Testing vs. Performance Engineering

**Performance Testing**  
Performance testing is part of performance engineering but is not the same thing. It involves writing tests to ensure that the application meets non-functional requirements, typically conducted after the application is built but before deployment. Common examples include:

- Verifying the software can handle a specified throughput.
- Checking for memory leaks.
  
**Performance Engineering**  
Performance engineering integrates performance considerations throughout the software lifecycle—from design to deployment. Unlike performance testing, which happens at the end, performance engineering ensures that speed, scalability, and other performance factors are part of the development process, not an afterthought. 

Performance tests are executed regularly during the software lifecycle, ensuring performance is continuously monitored and optimized.

---

### Business Impact of Performance Engineering

The goal of performance engineering is to **increase business revenue**. Well-performing systems contribute to this by:

- Enhancing customer satisfaction.
- Ensuring applications run efficiently, leading to higher conversion rates (e.g., in e-commerce).

Poor performance can lead to:

- **Lost revenue**: Slow software may drive customers to competitors.
- **Increased costs**: Performance failures lead to costly fixes and delays.

In engineering terms, performance engineering aims to:

- Eliminate system failures.
- Avoid delays in deployment.
- Minimize system modifications and ongoing maintenance.

A stable, performant system reduces operational overhead and minimizes the risk of expensive fixes.

---

### Identifying and Preventing Future Issues

Performance engineering also helps to **anticipate potential issues**, such as system scalability limits or bottlenecks, before they affect production. Efficient software reduces the load on servers, allowing existing resources to handle more traffic.

---

### Phases of Performance Engineering

1. **Elaboration Phase**  
   - Break down use cases and derive performance testing scenarios.
   - Identify business-critical scenarios that bring the most value.
   - Set clear rules and deliverables.

2. **Construction Phase**  
   - Identify the right tools for performance analysis.
   - Select subject-matter experts to manage the tools.
   - Automate performance tests, including unit testing, load testing, and database testing.
   - Set up performance tests in a staging environment and train the team on using the tools.

3. **Transition Phase**  
   - Deploy the application to production.
   - Set up the production environment according to performance requirements.
   - Implement performance monitoring tools that generate regular automated reports.
   - Address performance issues identified through reports.

---

### Stakeholder Collaboration

Performance engineering requires ongoing collaboration among various stakeholders:

- **Performance Engineer**: Drives and orchestrates the performance engineering process.
- **Software Developer**: Designs with performance in mind and integrates unit testing.
- **Business Analyst**: Collects business requirements that form the basis for performance requirements.
- **DevTester**: Integrates performance testing into development cycles.

Collaboration ensures that performance is not isolated but embedded throughout the software lifecycle.

---

This structure emphasizes the key concepts and practical aspects of performance engineering, focusing on the importance of integrating performance considerations from the start of the development process to ensure better software quality, customer satisfaction, and business success.

## 3
### Effective Performance Engineering Techniques

#### 1. **Tier-Based Engineering Transactions**
   - **Tier Definition**: Applications typically have multiple tiers (or layers) of functionality, such as:
     - **Web Tier**: Handles static pages.
     - **Database Tier**: Handles data retrieval or manipulation.
   - **Why Tiering Helps**: Breaking down transactions by tier helps isolate the source of performance issues. For example, if a web-tier transaction fails, you don’t need to check database connections.

   **Action**: Identify the tier of each transaction during performance testing to narrow down potential issues.

---

#### 2. **Benchmark Tests**
   - **What is a Benchmark Test?**: A benchmark test has predefined standard variable settings. All subsequent tests are compared against this baseline.
   - **Testing Approach**: Only vary one variable at a time while keeping others constant to identify the root cause of performance issues.
     - Example: To test the impact of CPU type on latency, only vary the CPU, not the number of concurrent users, to identify which factor affects performance.

---

#### 3. **Monitoring and Resource Utilization**
   - **Comprehensive Monitoring**: Monitor both software transactions and hardware resources (CPU, memory, disk space).
   - **Underutilized Resources**: Identify underused resources, as they represent wasted capacity. For example, if the CPU usage is only 5%, consider lowering the server’s CPU capacity to save costs.
   - **Rule of Thumb**: All tests should be repeatable. Run each test at least **three times** to ensure consistency and validity of results.

---

#### 4. **Consistency and Repeatability**
   - **Importance of Repeatability**: Performance tests must show consistent results over multiple runs to be valid.
     - **Action**: Run each test at least three times. If results vary significantly, investigate the underlying cause.
   - **Complete Data Set**: Wait for all tests to complete before analyzing results. Analyzing partial data can lead to incorrect conclusions.

---

#### 5. **Automation in Performance Engineering**
   - **Automation is Key**: Automating tests frees up performance engineers to focus on analyzing results rather than manually running tests.
   - **Benefit**: With proper automation, you can run tests more efficiently, allowing for deeper analysis and faster identification of performance issues.

---

#### 6. **Simplified Load Testing**
   - **Single-User Load Test**: Start with tests using just one user to establish how the system behaves under minimal load.
   - **Ghost Tests**: Monitor the system when no users are active to establish baseline hardware performance (i.e., CPU, memory, disk space).
   - **Ramp Up Concurrent Users**: Gradually increase the number of users in subsequent tests to understand how the system scales.

   **Action**: Ensure that each test runs long enough to gather **at least three results** for meaningful analysis. As a rule, run load tests for a minimum of **30 minutes**, excluding any warm-up periods for the system.

---

#### 7. **Spotting Anomalies**
   - **Visualizing Results**: Anomalies are often easier to identify when test results are visualized in charts.
   - **Action**: Use charts to compare expected results with actual outcomes. Anomalies will often stand out, allowing for quicker identification and investigation.

---

#### 8. **Granularity in Measurement**
   - **Granularity Impact**: The granularity of the data can significantly affect the insights you gain. For example, viewing data every hour can hide important trends that might appear if the granularity is set to 5 minutes.
   - **Action**: Be mindful of the granularity when analyzing results. Adjust it as needed to uncover critical details and trends that would otherwise be missed.
     - **Tip**: Some visualization tools automatically set granularity to suboptimal levels, so ensure it is explicitly configured to suit your analysis.

---

### Summary of Key Points:
- **Identify tiers** of transactions to isolate issues (web, database, etc.).
- **Use benchmark tests** with one variable change to trace performance issues.
- **Monitor hardware resources** for underutilization and optimize costs.
- **Repeat tests** at least three times to ensure consistency in results.
- **Automate tests** to focus more on analysis rather than manual testing.
- Start with **single-user and ghost tests** before ramping up load tests.
- **Visualize results** to spot anomalies quickly.
- Pay attention to **granularity** in measurements to reveal important trends.

By following these techniques, you can effectively isolate and address performance issues while ensuring reproducible, accurate results.

## 4
### Docker Performance Engineering Considerations

#### 1. **CPU Performance in Docker Containers**
   - **Default Behavior**: By default, Docker containers have access to all of the CPU capacity on their host system.
   - **Potential Issue**: If multiple containers share the same host, one container may consume most of the CPU resources, potentially starving others and causing performance degradation.
   - **Solution**: You can configure **CPU constraints** by setting limits on how much CPU each container can use. This helps prevent resource contention and ensures fair distribution of CPU resources among containers.

---

#### 2. **Memory Usage in Docker Containers**
   - **Memory Sharing**: Multiple containers on the same host share the host’s memory. However, Docker doesn't enforce strict memory limits by default, which could lead to memory starvation.
   - **Memory Limits**:
     - **Hard Memory Limit**: Enforces a strict upper limit on the amount of memory a container can use.
     - **Soft Memory Limit**: Allows containers to use more memory than the soft limit unless the host runs low on memory, at which point the container may be restricted.
   - **Performance Consideration**: As a performance engineer, you should determine the appropriate memory limit configuration based on your container workload to avoid memory-related performance issues, such as unexpected process termination due to memory exhaustion.

---

#### 3. **Disk Storage Considerations**
   - **Storage Options**: Docker provides two primary options for managing persistent data storage:
     - **Volumes**: Docker-managed storage on the host. Volumes are the preferred method for storing persistent data because they offer better performance with less overhead and latency.
     - **Bind Mounts**: Mounts a directory from the host system into the container. This can sometimes lead to higher overhead and latency compared to volumes.
   - **Performance Impact**: While volumes are the best choice for data storage, both volumes and bind mounts introduce some overhead due to disk I/O operations. Proper configuration is important to minimize this overhead.

---

#### 4. **Networking Options and Performance**
   - **Bridging**: A network bridge is a software solution that manages network traffic among containers on the same host. Bridging has minimal overhead but restricts communication to only within the host.
   - **NAT (Network Address Translation)**: NAT networking allows containers to communicate with external networks, including the internet. However, NAT introduces performance overhead because of the additional network translation steps.
   - **Performance Consideration**: As a performance engineer, decide whether containers need external network access. If not, using bridging will be more efficient, as it avoids the extra overhead of NAT.

---

#### 5. **Optimizing Docker Images**
   - **Dockerfile**: The Docker image is defined by a `Dockerfile`, which specifies build commands, installation instructions, environment variables, and networking requirements.
   - **Build Context**: The context for building the Docker image consists of all the necessary files. However, the larger the build context, the longer it takes to build the image. 
     - **Optimization**: Use a `.dockerignore` file to exclude unnecessary files from the build context, reducing build time and the final image size.
   - **Command to Check Image Size**: Run `docker images` to see a list of all Docker images on your system, including the size of each image.

---

#### 6. **Docker Stats for Performance Monitoring**
   - **docker stats**: This command provides real-time statistics for running containers, including:
     - **CPU Usage**: Percentage of the host CPU being used by each container.
     - **Memory Usage**: Amount of memory and percentage of host memory used by each container.
     - **Network Traffic**: Amount of data being sent and received by each container.
     - **Disk Usage**: The amount of disk space used by the container.
     - **Thread Count**: The number of threads used by each container.
   - **Real-Time Analysis**: `docker stats` continually updates the performance statistics, enabling you to analyze container performance in real time. By default, it shows stats for all containers, but you can specify individual containers for focused monitoring.

---

### Summary of Key Considerations:
1. **CPU Constraints**: Limit the CPU resources available to containers to avoid resource contention.
2. **Memory Limits**: Use hard or soft memory limits to prevent memory starvation and container crashes.
3. **Disk Storage**: Use volumes for more predictable performance when storing persistent data.
4. **Networking**: Choose between bridging (minimal overhead) or NAT networking (external communication, higher overhead).
5. **Image Optimization**: Reduce build context size with `.dockerignore` and check image sizes using `docker images`.
6. **Monitoring with `docker stats`**: Continuously monitor CPU, memory, network, and disk usage for performance tuning.

By considering these Docker-specific performance factors, you can optimize your containerized applications and ensure they run efficiently on your infrastructure.

## 5
### Managing Host Resources with Docker Containers

When running Docker containers, it's crucial to manage and limit the resources (CPU and memory) they use to prevent resource hogging and ensure other containers on the same host aren't negatively affected. By default, Docker containers have unrestricted access to the host's CPU and RAM, which is fine for isolated or small workloads, but in production environments, resource limits must be set for efficient operation.

---

### 1. **Memory Management**

#### a. **Hard Memory Limit**
   - To set a **hard memory limit** for a container, use the `--memory` flag. This restricts the container to a specified amount of RAM, and Docker will kill the container if it exceeds this limit.
   - **Example**:
     ```bash
     docker run -it --memory="500m" ubuntu
     ```
     This command sets a 500 MB memory limit for the container.
   - **Memory Units**: You can specify the limit in bytes, kilobytes (`k`), megabytes (`m`), or gigabytes (`g`). For example:
     - `50m` means 50 megabytes.
     - `2g` means 2 gigabytes.

#### b. **Swap Memory**
   - Swap memory allows data that doesn't fit in physical RAM to be moved to disk storage. While convenient, **swap memory** is much slower than regular RAM and should be avoided for performance-sensitive applications.
   - The `--memory-swap` flag allows you to set the total amount of memory, including both RAM and swap.
   - **Example**:
     ```bash
     docker run -it --memory="4g" --memory-swap="5g" ubuntu
     ```
     This example sets a hard memory limit of 4 GB and allows 1 GB of swap memory (totaling 5 GB).
   - **Important**: If `--memory-swap` is set, you must also set a memory limit with `--memory`.

#### c. **Soft Memory Limits**
   - **Soft limits** do not kill the container if exceeded. They only reserve a minimum amount of memory for the container, which it can use if needed but can exceed if other containers are not using memory.
   - The `--memory-reservation` flag is used to set a **soft memory limit**.
   - **Example**:
     ```bash
     docker run -it --memory="2g" --memory-reservation="1g" ubuntu
     ```
     Here, the container has a **hard memory limit of 2 GB** but a **soft memory reservation of 1 GB**. If the host is running low on memory, 1 GB will be reserved for this container, but it can use more memory if available.

---

### 2. **CPU Management**

#### a. **Hard CPU Limit**
   - You can specify a **hard CPU limit** using the `--cpus` flag. This defines the number of CPU cores the container can use.
   - **Example**:
     ```bash
     docker run -it --cpus="1.5" ubuntu
     ```
     This allows the container to use **1.5 CPU cores** on a host with 2 CPU cores. If you only have 1 CPU, the container will use 100% of the available CPU capacity.

#### b. **CPU Shares (Soft Limit)**
   - The `--cpu-shares` flag defines the **relative weight** of CPU access when CPU capacity is limited. It doesn't limit the actual CPU usage but defines the priority of CPU access when resources are scarce.
   - **Example**:
     ```bash
     docker run -it --cpu-shares="700" ubuntu
     ```
     The default CPU share is `1024`, so setting it to `700` means this container gets less CPU time compared to a container with the default `1024` share when there is competition for CPU resources.

#### c. **CPU Quota and Period**
   - The `--cpu-period` and `--cpu-quota` flags control the **CPU scheduling period** and **quota** for containers.
   - These flags are most useful for managing containers' CPU time in environments with limited CPU resources. However, they are more complex to use compared to `--cpus`.
     - `--cpu-period`: Specifies the length of the CPU scheduling period (default is 100,000 microseconds).
     - `--cpu-quota`: Specifies how much CPU time is allocated during the period.
   - **Example** (not commonly used as `--cpus` is simpler):
     ```bash
     docker run -it --cpu-period="100000" --cpu-quota="50000" ubuntu
     ```
     This configuration allocates **50% of a CPU core** during each scheduling period.

#### d. **Specifying CPU Cores**
   - You can assign containers to specific **CPU cores** using the `--cpuset-cpus` flag.
   - **Example**:
     ```bash
     docker run -it --cpuset-cpus="0,2" ubuntu
     ```
     This command gives the container access to **CPU cores 0 and 2**, ignoring others.

---

### Summary of Resource Management Flags:

- **Memory**:
  - `--memory`: Set a hard memory limit for the container.
  - `--memory-swap`: Define total memory (RAM + swap) for the container.
  - `--memory-reservation`: Set a soft memory limit to reserve a minimum amount of memory.

- **CPU**:
  - `--cpus`: Set a hard CPU limit (fraction of a CPU core).
  - `--cpu-shares`: Set relative CPU weight (soft limit, works when CPU is under contention).
  - `--cpu-period` and `--cpu-quota`: Control CPU time allocation (more complex, less common).
  - `--cpuset-cpus`: Assign specific CPU cores to the container.

By configuring these resource limits, you can ensure that your containers are efficient, prevent resource contention, and maintain stable performance across your host system.

## 6
### Common Performance Issues with Docker

In this video, we dive into several common performance issues that can arise when using Docker containers and how to address them. While containers offer flexibility and scalability, their performance can be impacted by various factors ranging from container size to network inefficiencies. Below, we’ll walk through key issues and solutions.

---

### 1. **Container Size**

**Issue:**
- The **size of a Docker container** can significantly affect its performance. Larger containers take more time to **spin up** (start), **migrate**, and **deploy**. This can be especially problematic in environments where containers are frequently started or moved, such as in **continuous integration/continuous deployment (CI/CD)** pipelines.

**Solution:**
- **Minimize Container Size**: Aim to reduce the size of your containers by:
  - Using **minimal base images**. For example, use `alpine` instead of heavier distributions like `ubuntu` when possible.
  - Removing unnecessary files and dependencies from the image.
  - Leveraging multi-stage builds to separate the build environment from the runtime environment.
  
  By reducing the size, you’ll improve container startup times, make deployments faster, and improve the overall efficiency of your containerized environment.

---

### 2. **Resource Usage and Host Load**

**Issue:**
- **Resource contention** becomes a significant problem when multiple containers run on the same host. Containers can **overwhelm host resources** like **IO**, **memory**, and **CPU**, leading to performance degradation for all containers running on that host.

**Solution:**
- **Monitor Host Resources**: Use tools to **track CPU, memory, disk, and network usage** across all containers on a host.
  - Tools like **Docker stats**, **Prometheus**, and **cAdvisor** can help you monitor real-time container resource consumption.
- **Optimize Resource Allocation**: 
  - Set **limits and reservations** for CPU and memory usage (`--memory`, `--cpu-shares`) to prevent containers from consuming too many resources.
  - Regularly monitor and adjust resource limits to ensure your containers are using resources efficiently without overwhelming the host.

---

### 3. **Inconsistent Container Frameworks**

**Issue:**
- **Inconsistent environments** (e.g., different operating systems, varied configurations, and resources) can make it difficult to manage performance across your containerized system. If some containers are running on different OSes or using varying infrastructure resources, monitoring and managing them becomes complex, leading to inconsistent performance results.

**Solution:**
- **Standardize Your Container Environments**:
  - Use **standardized Dockerfiles** and **base images** for consistency across environments.
  - Implement consistent tools across all containers, such as **centralized logging** and **monitoring** solutions (e.g., **ELK stack** or **Prometheus/Grafana**).
  - **Automation**: Use **orchestration tools** like **Kubernetes** to automate container deployment, scaling, and management to ensure consistency.

Standardizing environments allows for easier performance monitoring and debugging, and reduces the potential for misconfigurations affecting performance.

---

### 4. **Network Performance Issues**

**Issue:**
- **Network bottlenecks** often go unnoticed because developers tend to test containers in a local development environment where network traffic is minimal. However, in production, containers communicate across networks, and any inefficiencies can have a large impact on performance.

**Solution:**
- **Test in Production-Like Environments**:
  - Regularly perform **integration testing** in environments that mirror production. This ensures you know how your containers will behave when network traffic increases.
- **Network Management**:
  - Use **load balancing** to distribute network traffic evenly across containers.
  - Optimize **network protocols** for better communication efficiency.
  - Implement **network namespaces** and **overlay networks** (e.g., Docker's `bridge` and `overlay` network drivers) to isolate and optimize communication between containers.
  
Testing under production-like conditions and ensuring optimized networking configurations will help identify potential network-related performance issues before they become a problem.

---

### 5. **Legacy Software and APIs**

**Issue:**
- When containerizing **legacy software** or **APIs**, older services may not be optimized for distributed network environments. These legacy systems often rely on inefficient network protocols and local resources, which can cause bloated network traffic and overburden host resources.

**Solution:**
- **Containerize with Care**:
  - When moving legacy code to Docker, ensure the application is optimized for network-based communication.
  - **Refactor old APIs** to use modern, efficient protocols (e.g., HTTP/2, gRPC) instead of outdated ones.
  - Consider **rearchitecting** parts of legacy systems to better fit into a distributed, containerized environment (e.g., breaking monolithic applications into microservices).

Legacy software may need adjustments to run efficiently in a containerized setup, so it’s important to assess and optimize network-related components of older systems.

---

### 6. **Identifying Bottlenecks**

**Issue:**
- Performance bottlenecks can arise from many areas—CPU, memory, disk IO, network, or even within the container's internal application logic. Without identifying the exact source of the bottleneck, optimizations may be misdirected and ineffective.

**Solution:**
- **Use Monitoring and Profiling Tools**: Leverage **system monitoring** tools like `docker stats`, **Prometheus**, or **Datadog** to identify where the bottlenecks are occurring (CPU, memory, disk IO, etc.).
- **Log and Trace**: Set up logging and **tracing** (e.g., using **Jaeger** or **Zipkin**) to monitor the flow of requests through your system and identify where delays are happening.
- **Optimization**: Once you’ve pinpointed the bottleneck, apply targeted optimizations (e.g., adjusting resource limits, improving code efficiency, or scaling containers).

---

### 7. **Data-Driven Approach for Performance Optimization**

**Issue:**
- Many optimizations are attempted based on intuition or gut feeling, rather than data. This can lead to ineffective or even counterproductive changes.

**Solution:**
- **Measure Before and After**: Always collect **baseline metrics** before attempting any optimizations. After implementing changes, measure the results again to determine whether performance has truly improved.
- **Iterative Testing**: Apply a data-driven, **iterative approach** where you test, measure, optimize, and re-test, making adjustments based on actual data rather than assumptions.

This approach ensures that optimizations are based on solid evidence and results, improving performance without unnecessary guesswork.

---

### Summary

Here’s a recap of the solutions to address the common performance issues with Docker:

1. **Container Size**: Minimize container size by using minimal base images and cleaning up unnecessary files.
2. **Resource Usage**: Monitor and manage container resource usage (CPU, memory, IO) to prevent overload on the host.
3. **Inconsistent Frameworks**: Standardize environments and use consistent monitoring tools across containers.
4. **Network Issues**: Test containers in a production-like environment and optimize network performance.
5. **Legacy APIs**: Refactor legacy software and APIs to be more efficient in a distributed environment.
6. **Bottlenecks**: Use monitoring tools to identify bottlenecks, and then optimize based on data.
7. **Data-Driven Optimization**: Always measure performance before and after optimizations to validate changes.

By addressing these issues and following a data-driven approach to performance management, you'll be able to deploy more efficient and scalable Docker containers.

## 7
### Docker Metrics: Overview of `docker stats` and the Docker REST API

In this video, we explore two primary methods for monitoring Docker container performance: **`docker stats`** and the **Docker REST API**. Both provide valuable insights into the resources used by containers, but they serve different purposes and offer different levels of detail. Let’s dive into each of these tools and how you can use them to monitor and troubleshoot Docker container performance.

---

### 1. **Using `docker stats`**

**`docker stats`** is a built-in, command-line tool that provides real-time resource usage statistics for running Docker containers. It's a simple and effective way to monitor the health of your containers, especially when you're troubleshooting or need a quick snapshot of their resource consumption.

#### How to Use:
- You can invoke the tool by running the following command:
  ```
  docker stats
  ```
  This will display a constantly updating screen showing real-time statistics for each running container.

#### Key Metrics Provided:
- **CONTAINER**: The container ID or name.
- **CPU%**: The percentage of the host’s CPU that the container is using at the moment.
- **MEM%**: The percentage of the host’s total memory being consumed by the container.
- **MEM usage/limit**: The amount of memory the container is using versus its memory limit (if set).
- **NET I/O**: The amount of data received and transmitted over the network by the container.
- **BLOCK I/O**: The number of bytes read from and written to disk by the container.
- **PIDS**: The number of kernel process IDs (PIDs) the container is using.

**Example Output**:
```
CONTAINER ID   CPU %     MEM %     MEM USAGE / LIMIT   NET I/O     BLOCK I/O   PIDS
a1b2c3d4e5f6   12.34%    4.56%     500MB / 1GB         10MB / 2MB  200MB / 10MB  123
```

- **Real-Time Data**: The `docker stats` command continuously updates the statistics, providing a dynamic view of container resource usage, which is especially helpful for live monitoring.

---

### 2. **Using the Docker REST API for Metrics**

The **Docker REST API** allows you to programmatically access detailed container metrics in JSON format. Unlike `docker stats`, which provides only real-time data, the REST API allows you to stream data, enabling you to collect and store historical metrics for later analysis.

#### Accessing the Docker API:
By default, the Docker daemon listens for API requests on the Unix socket at `unix:///var/run/docker.sock`.

You can access container statistics through the API by sending an HTTP request like this:
```bash
curl -v --unix-socket /var/run/docker.sock http://localhost/containers/<container_id>/stats
```

This request will return detailed statistics in a streaming JSON format. The Docker REST API provides much more granular and in-depth data than `docker stats`.

#### Key Metrics in the JSON Response:

1. **CPU Stats**:
   - **total_usage**: The total CPU usage of the container.
   - **percpu_usage**: Array showing CPU usage for each individual CPU core.
   - **usage_in_kernelmode**: CPU usage by kernel components.
   - **usage_in_usermode**: CPU usage by user-level processes.
   - **system_cpu_usage**: The overall system CPU usage.
   - **online_cpus**: The number of CPUs available for the container.

   **Example (CPU stats) JSON**:
   ```json
   "cpu_stats": {
     "cpu_usage": {
       "total_usage": 198270823475,
       "percpu_usage": [4762809876, 3984202234798],
       "usage_in_kernelmode": 8080000000,
       "usage_in_usermode": 25520000000
     },
     "system_cpu_usage": 24583939802340000,
     "online_cpus": 3,
     "throttling_data": {
       "periods": 0,
       "throttled_periods": 0,
       "throttled_time": 0
     }
   }
   ```

2. **Memory Stats**:
   - **usage**: The current memory usage of the container.
   - **max_usage**: The highest memory usage recorded.
   - **cache**: The memory used by the container's cache.
   - **rss**: The resident set size, which refers to memory actively used by the container.
   - **swap**: The amount of swap space used by the container.

   **Example (Memory stats) JSON**:
   ```json
   "memory_stats": {
     "usage": 2346562365,
     "max_usage": 297430733,
     "cache": 4732987,
     "rss": 238974328,
     "swap": 0
   }
   ```

3. **Block I/O Stats**:
   - **io_service_bytes_recursive**: Total number of bytes read/written by the container's filesystem.
   
   **Example (Block I/O) JSON**:
   ```json
   "blkio_stats": {
     "io_service_bytes_recursive": [
       {"major": 6, "minor": 0, "op": "Read", "value": 19545354},
       {"major": 6, "minor": 0, "op": "Write", "value": 10203456}
     ]
   }
   ```

4. **Network Stats**:
   - **rx_bytes**: Bytes received by the container.
   - **tx_bytes**: Bytes transmitted by the container.
   - **rx_packets**: Packets received by the container.
   - **tx_packets**: Packets transmitted by the container.

   These stats can be useful for understanding the network bandwidth consumed by containers.

---

### Key Differences: `docker stats` vs Docker REST API

| Feature                     | `docker stats`                          | Docker REST API                                  |
|-----------------------------|-----------------------------------------|-------------------------------------------------|
| **Data Type**               | Real-time (live stats)                 | Streaming JSON data (can be stored for history) |
| **Metrics**                 | Basic (CPU, memory, network, I/O)      | Detailed (granular CPU, memory, block I/O, network, etc.) |
| **Usage**                   | Quick checks, troubleshooting          | Long-term monitoring, logging, advanced analysis |
| **Output Format**           | Tabular display (CLI)                  | JSON (programmatically accessible)               |
| **Historical Data**         | No history (real-time only)            | Can stream and store historical data            |

---

### Conclusion

- **`docker stats`** is a simple, easy-to-use tool that provides real-time container performance metrics, making it perfect for quick troubleshooting and live monitoring.
- **Docker REST API** offers a more granular, detailed set of stats, including CPU, memory, block I/O, and network metrics. It provides these stats in a JSON format, which is ideal for logging, long-term monitoring, or programmatically processing data.

For more in-depth, historical, or automated monitoring, the Docker REST API is the way to go. On the other hand, for day-to-day container monitoring and troubleshooting, `docker stats` is a quick and effective solution. Both tools are essential for Docker performance management, and using them together can help you better understand and optimize your containerized workloads.

## 8
This video covers various performance tools for Docker containers, each designed to improve different aspects of container management and deployment.

- **Gradle**: An open-source tool for automating the building and debugging of scripts, with support for multiple platforms and scripting languages.
- **Packer**: Automates the creation of machine images, including Docker images, and can run in parallel for better performance.
- **Chef**: Manages container infrastructure, configurations, and compliance, supporting continuous delivery and scaling automation.
- **Otter**: Provides a web dashboard for provisioning and managing servers with centralized management and monitoring.
- **Buddy**: A CI/CD tool that integrates natively with Docker, featuring an easy-to-use UI for managing workflows and logs.
- **BuildMaster**: A CI/CD tool focused on defining infrastructure and automating testing and release processes, with cloud-based storage for artifacts.
- **DigitalOcean**: Simplifies configuration optimization, with one-click Docker app deployment available in its marketplace.
- **Calico**: A security-focused platform that uses "micro firewalls" and network policies to enhance the security of Docker containers.
  
For orchestration, tools like **Kubernetes**, **Google Container Engine**, **Docker Swarm**, **Azure Container Service**, and **Amazon ECS** are available, each catering to different needs in scaling and managing containerized applications. **Clair** is also highlighted as an open-source tool for scanning containers for security vulnerabilities.

## 9
In this video, we explore why monitoring container systems is essential and review several tools that can help with this task. The key reason to monitor containerized environments is their inherent complexity. When you have hundreds or thousands of containers interacting in dynamic and sometimes unpredictable ways, it can be difficult to track performance without active monitoring. Containers are constantly being spun up, scaled, and destroyed, and the networks they rely on are subject to change. Without constant monitoring, issues can go unnoticed until they impact system performance, so it is important to ensure that containers and their networks remain healthy.

Here are some common monitoring tools and packages for Docker systems:

### 1. **Docker API**
   - **Purpose**: Provides HTTP-based access to Docker’s internal metrics and can be used by external tools to gather data on container performance.
   - **Use Case**: Ideal for integrating with other systems to collect Docker container metrics programmatically. It is secure and standardized, making it a powerful option for monitoring container health.

### 2. **ManageEngine Applications Manager**
   - **Purpose**: A comprehensive monitoring tool that supports Docker host monitoring and helps identify bottlenecks by monitoring both the containers and the services running within them.
   - **Key Features**: 
     - Rules-based alerting via email or SMS when performance deviates from the norm.
     - Useful for monitoring containerized applications in large environments.

### 3. **Librato**
   - **Purpose**: Provides monitoring for systems written in various programming languages, and can track custom metrics, such as RPC calls and request tracking.
   - **Key Features**:
     - Customizable dashboards to track performance.
     - Ideal for monitoring request flows and exposing potential bottlenecks within the system.

### 4. **cAdvisor**
   - **Purpose**: An open-source monitoring tool that runs as a container on the host and provides detailed stats about containers.
   - **Key Features**:
     - Exposes real-time network, CPU, memory, and disk usage stats.
     - Accessible via a web interface.
   - **Limitation**: Only monitors a single host.

### 5. **Scout**
   - **Purpose**: An enhanced version of cAdvisor that allows you to aggregate metrics from multiple hosts and containers.
   - **Key Features**:
     - Collects container-level performance metrics from multiple machines.
     - Ideal for monitoring complex container environments across several hosts.

### 6. **DataDog**
   - **Purpose**: A comprehensive cloud-based monitoring service that provides full-stack monitoring, including container and application-level metrics.
   - **Key Features**:
     - Customizable dashboards for visualizing application and infrastructure data.
     - Integrated alerting and annotation systems for real-time monitoring and issue communication.

### 7. **Dynatrace**
   - **Purpose**: A highly user-friendly out-of-the-box solution focused on log monitoring and performance tracking.
   - **Key Features**:
     - Automatically detects new containers as they are deployed.
     - Collects log data and integrates Docker-specific details like container names, IDs, and host information.
     - Lightweight storage footprint.

### 8. **Sysdig**
   - **Purpose**: A hosted monitoring solution that installs an agent at the OS level to collect container data.
   - **Key Features**:
     - Provides dashboards and alerting for container-level activity.
     - Useful for gaining insights at the container and system level.

### 9. **Sematext**
   - **Purpose**: A monitoring solution designed specifically for Docker environments that focuses on performance metrics and logs.
   - **Key Features**:
     - Automatic container discovery and integration with the application’s infrastructure.
     - High-performance metrics collection and log management, making it a solid choice for Docker-native environments.

### Conclusion
Monitoring your containerized environment is crucial to maintaining high performance and preventing issues that can affect your system’s health. The tools listed provide a range of features, from real-time stats collection to comprehensive logging and alerting capabilities, allowing you to identify performance bottlenecks, network issues, and container health in a dynamic and ever-changing infrastructure. By using the right monitoring tools, you can ensure your containers remain efficient and stable, even in large, complex environments.

## 10
In this video, we walk through the process of installing **ManageEngine Applications Manager** to monitor Docker containers. Here's a breakdown of the key steps covered in the demo:

### Step 1: Install Docker Desktop on Windows
1. **Download Docker Desktop** from the official Docker site (https://docs.docker.com/docker-for-windows/install/).
   - Click on "Docker Desktop for Windows" to download the installer.
2. **Run the installer** (which may take some time) to install Docker Desktop.
   - The installation will configure required components like **WSL 2** (Windows Subsystem for Linux 2) and create a Docker shortcut on the desktop.
   - Once the installation is complete, click "Close" to finish.

### Step 2: Install ManageEngine Applications Manager
1. **Download the free version** of **ManageEngine Applications Manager** from [ManageEngine's website](https://www.manageengine.com/products/applications_manager/applications-manager-comparison.html).
   - Click "Download Now" under the Free version to get started.
2. **Run the installer** for Applications Manager:
   - Accept the License Agreement.
   - Choose the **Free License** edition (which has some feature restrictions but is free to use).
   - Set the installation directory (default location is `C:\Program Files\ManageEngine\AppManager15`).
   - Configure the **web server port** (default is 9090).
   - **Skip the Registration for Technical Support** option.
   - Review and start the installation. After installation completes, you’ll see the option to launch **Applications Manager**.

### Step 3: Configure Database
1. For simplicity, choose **PostgreSQL** as the database option.
2. If you encounter a warning about antivirus software interfering with the database setup, just click **OK**.
3. Once the database setup is complete, click **Finish** to launch **Applications Manager**.

### Step 4: Access Applications Manager
- **Login** using the default credentials (`admin` / `admin`).
- After logging in, you're prompted to change your password, which you can do by entering the old password and setting a new one.
- Once logged in, you can close the setup screen.

### Step 5: Set Up Docker Monitoring in ManageEngine
1. In **Applications Manager**, click on the **New Monitor** button in the menu.
2. Select **Docker** from the list of monitor types.
3. Configure the following:
   - **Display Name**: Give your Docker monitor a name (e.g., `DemoDockerMonitor`).
   - **HostName**: Set to `localhost` (this is where Docker Desktop is running).
   - **Port**: Enter `2375` (default port for Docker's remote API).
4. In the **Credential Details** section:
   - Leave it blank since this is a localhost setup.
   - Ensure that **SSL** is not enabled (as it's not needed for this setup).
5. **Test the credentials** by clicking **Test Credential**. If successful, click **Add Monitor(s)**.

### Step 6: View Monitoring Data
1. Once the monitor is added, you’ll be taken to the **Monitor Details** page.
2. Key metrics include:
   - **Server Snapshot**: CPU, memory, and disk usage for Docker.
   - **Performance History**: Track the container’s performance over time (e.g., the last 6 hours).
   - **Overall Stats**: Includes the number of containers, images, running containers, and more.
   - **Container Details**: If you had any containers running, they would appear here, showing detailed stats for each one (e.g., resource usage per container).

### Conclusion
Using **ManageEngine Applications Manager**, you can easily monitor Docker containers. The process involves installing Docker Desktop, setting up ManageEngine, and configuring it to monitor Docker. Once set up, you can track key container metrics like CPU, memory, disk usage, and availability, helping ensure your Docker environment runs efficiently.

This setup is simple and fast, and the free version of ManageEngine allows monitoring of up to 5 containers, making it a great option for small-scale environments or for testing out container monitoring before scaling up to a larger deployment.

## 11
In this video, we go over the process of installing **Prometheus** and configuring it to monitor itself as an example, and then we discuss how Prometheus can be used to monitor Docker containers.

### Step 1: Download and Install Prometheus

1. **Download Prometheus** from the official website [Prometheus Downloads](https://prometheus.io/download).
   - For **Windows**, download the file labeled `prometheus-2.28.0.windows-amd64.zip`.
   - Extract the downloaded ZIP file to a folder of your choice.

2. **Open the Prometheus folder**: Inside the folder, you’ll find the `prometheus.yml` file. This is the main configuration file for Prometheus.

### Step 2: Configure Prometheus

1. **Edit the `prometheus.yml` file**:
   - Open `prometheus.yml` in a text editor.
   - Locate the `job_name` entry (line 23), which is set to `'prometheus'` by default. This configuration allows Prometheus to monitor its own metrics.
   - Under the `scrape_configs` section, you’ll see that `target` is set to `localhost:9090`. This is where Prometheus scrapes its own metrics. If you already have something running on port `9090`, you can change this port to something else (e.g., `9091`). Make sure to adjust the port in the configuration accordingly.

   Example configuration change:
   ```yaml
   scrape_configs:
     - job_name: 'prometheus'
       static_configs:
         - targets: ['localhost:9091']
   ```

### Step 3: Start Prometheus

1. **Run Prometheus**:
   - Open a **Command Prompt** in the folder where you extracted Prometheus.
   - Run the following command to start Prometheus with the modified configuration:
     ```bash
     prometheus.exe --config.file=prometheus.yml --web.listen-address=:9091
     ```
   - Prometheus will now start and listen on port `9091` (or whatever port you configured).

2. **Verify Prometheus is running**:
   - Once Prometheus has started, open a web browser and navigate to `localhost:9091` (or the port you configured).
   - You should see the **Prometheus web interface**, where you can start querying and visualizing metrics.

### Step 4: Access and View Metrics

1. **Access the `/metrics` endpoint**:
   - In your browser, go to `localhost:9091/metrics` (or whatever port you configured) to see the raw metric data that Prometheus is scraping from itself.
   - The data will be in **Prometheus format**, showing a list of metric names, labels, and values. For example:
     ```text
     go_gc_duration_seconds{quantile="0"} 0
     go_memstats_alloc_bytes_total 54881384
     ```

2. **Querying Metrics in Prometheus**:
   - Go back to the **Prometheus UI** and navigate to the **Graph** tab.
   - In the **Expression bar**, enter the metric name you want to query, such as `go_memstats_alloc_bytes_total`, and click **Execute**.
   - Prometheus will display the current value of that metric (e.g., memory allocated in bytes).
   - To see historical data, switch to the **Graph** view and click **Execute** again to refresh the graph, which will show the metric's trend over time.

   Example:
   - The current value of `go_memstats_alloc_bytes_total` might be `57521440`, and the graph will show how this metric has changed over time.

### Step 5: How Prometheus Monitors Docker Containers

Unlike **ManageEngine**, which integrates directly with Docker to pull metrics, **Prometheus** works by scraping metrics from an exposed HTTP endpoint (usually `/metrics`) provided by the monitored system. 

To collect metrics from Docker containers using Prometheus, your containers need to **expose a `/metrics` endpoint** that provides metrics in the **Prometheus format**.

### Conclusion

Prometheus is a flexible and powerful monitoring tool that relies on scraping metrics from endpoints that expose data in a specific format. While **Prometheus** doesn’t directly integrate with Docker like some other monitoring solutions, you can set up your Docker containers to expose metrics in the required format and configure Prometheus to scrape these endpoints.

To monitor Docker containers with Prometheus:
1. Make sure your containers expose metrics on an HTTP endpoint.
2. Update your `prometheus.yml` configuration to scrape these endpoints.

Prometheus is a great option for monitoring containerized applications, especially when you're dealing with complex setups where you need granular control over what metrics you collect and how you visualize them.

## 12
In this video, we walk through the process of creating and running a **MySQL instance inside a Docker container** and then using **ManageEngine** to monitor the container and optimize its performance. Let's break down the process:

### 1. **Creating and Running MySQL in Docker**

The first step involves setting up a **Docker container** for MySQL using a `docker-compose.yml` file. This file is used to define the configuration for your MySQL container.

#### **docker-compose.yml Breakdown**

- **Line 1: Version** – Specifies the Docker Compose file version (`'3.1'` in this case).
- **Line 2: Services** – Defines the list of services (containers) to be used in your project.
- **Line 4: mysql_db** – The name of the service (container) you're creating, here it's called `mysql_db`.
- **Line 5: image** – Specifies the Docker image to use for the container. In this case, it’s `mysql`, which pulls the official MySQL image from Docker Hub.
- **Line 6: restart** – Sets the container to always restart (`restart: always`) in case it stops unexpectedly.
- **Line 7: environment** – Defines environment variables for MySQL. In this case:
  - `MYSQL_ROOT_PASSWORD`: The root password for MySQL (`!qazXsw2#edc`).
  - `MYSQL_DATABASE`: The database that will be created on startup (`demodb`).
- **Line 10: ports** – Maps the host machine's port `3307` to the container's default MySQL port `3306`. This allows access to MySQL on the host via port `3307`.

#### Example of the `docker-compose.yml` file:
```yaml
version: '3.1'

services:
  mysql_db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: "!qazXsw2#edc"
      MYSQL_DATABASE: demodb
    ports:
      - "3307:3306"
```

#### **Running the Container**

After you’ve created your `docker-compose.yml`, you run the following command to start the container:
```bash
docker-compose up
```
This will download the MySQL image (if not already present), start the MySQL container, and configure it based on your `docker-compose.yml` settings.

#### **Checking the Running Containers**

After the container is up, you can verify it's running with the command:
```bash
docker ps
```
This shows all the running containers. The output will include details like the container ID, image (`mysql`), and the status of the container.

#### **Accessing MySQL Inside the Container**

To interact with the MySQL instance inside the container, you need to execute a command within the running container:
```bash
docker exec -it <container_id> bash
```
Once inside the container, you can access MySQL:
```bash
mysql -u root -p
```
After entering the password (`!qazXsw2#edc`), you can start interacting with MySQL, such as creating databases and tables.

#### **Creating a Database and Table**

For example:
```sql
USE demodb;
CREATE TABLE demo_table (demofield NVARCHAR(50));
INSERT INTO demo_table (demofield) VALUES ('Hello World');
SELECT * FROM demo_table;
```
This creates a table, inserts a record, and verifies the data.

### 2. **Monitoring with ManageEngine**

Now that your MySQL container is running, you can monitor its performance and optimize it using **ManageEngine**.

#### **Setting Up ManageEngine**

1. **Login to ManageEngine** – Open ManageEngine and log in as an admin.
2. **Navigate to Docker Monitoring**:
   - Go to the **Monitors** section.
   - Under **Virtualization**, click on **Docker** to view and manage Docker container monitoring.

#### **Adding the Docker Container to ManageEngine**

1. **Add Container** – You’ll see a list of all containers running on your machine. Select the `mysql_db` container.
2. **Add Containers** – After selecting your container, click **Add Containers** to monitor it. This will include it in the monitoring dashboard.

#### **Monitoring MySQL Container**

- **Overview Screen** – After adding the container, you’ll see details such as:
  - **Server Snapshot**: CPU, Memory, and Disk utilization.
  - **Docker Stats**: Details about the total number of containers, running containers, and crashed containers.
  - **Health Status**: A green circle for health indicates the container is running well.
  - **Resource Usage**: Monitor CPU and memory usage (e.g., `Memory Utilization(%) = 2.72`).

#### **Detailed Container Monitoring**

- **Container-specific Details** – Clicking on the container name (e.g., `it_adpcwddj_01_enus_12_assets_mysql_db_1`) takes you to detailed metrics about the container:
  - **Uptime**: Displays how long the container has been running.
  - **Memory and Configuration**: Monitors memory usage and other configuration settings.
  
You can now see the health and resource utilization of the MySQL container and identify any potential bottlenecks or optimization areas, such as high memory or CPU usage.

### Conclusion

In conclusion, setting up a **MySQL instance inside a Docker container** using **docker-compose** is simple, and managing it with **ManageEngine** allows you to monitor and optimize its performance effectively. With **ManageEngine**, you can track important metrics like memory usage, CPU utilization, and overall container health, helping you optimize your MySQL instance for better performance and reliability.

By monitoring your MySQL Docker container, you can proactively address performance bottlenecks, such as high CPU usage or memory issues, and take the necessary steps to ensure your application runs smoothly.

## 13
### Docker-Compose for WordPress with MySQL

This guide will walk you through setting up WordPress with MySQL as a backend database using Docker, and how to monitor the application with ManageEngine.

#### 1. **Setting Up the `docker-compose.yml` File**

This `docker-compose.yml` file defines the WordPress application and its MySQL backend. The file uses Docker Compose version 3.1.

```yaml
version: '3.1'

services:
  wordpress:
    image: wordpress
    restart: always
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: mysql_db:3306
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: "!qazXsw2#edc"
      WORDPRESS_DB_NAME: wordpress

  mysql_db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: "!qazXsw2#edc"
      MYSQL_DATABASE: wordpress
    ports:
      - "3307:3306"
```

#### 2. **Explanation of the Compose File**

- **WordPress Service:**
  - **image**: Pulls the WordPress image from Docker Hub.
  - **restart**: Ensures the WordPress container restarts automatically.
  - **ports**: Maps port 8080 on the host to port 80 on the container (default port for WordPress).
  - **environment**: Sets environment variables to connect WordPress to the MySQL database:
    - `WORDPRESS_DB_HOST`: Defines the database host (mysql_db:3306).
    - `WORDPRESS_DB_USER`: Sets the MySQL user (`root`).
    - `WORDPRESS_DB_PASSWORD`: Defines the root password.
    - `WORDPRESS_DB_NAME`: Specifies the database name (`wordpress`).

- **MySQL Service:**
  - **image**: Uses the MySQL image from Docker Hub.
  - **restart**: Ensures the MySQL container restarts automatically.
  - **environment**:
    - `MYSQL_ROOT_PASSWORD`: Sets the MySQL root password.
    - `MYSQL_DATABASE`: Creates a database named `wordpress`.
  - **ports**: Maps port 3307 on the host to port 3306 on the container (default port for MySQL). Using 3307 ensures compatibility with a MySQL instance on the host.

#### 3. **Running Docker Compose**

1. Navigate to the directory containing the `docker-compose.yml` file.
2. Run the following command to start the containers:
   ```bash
   docker-compose up
   ```
3. This will pull the WordPress and MySQL images, create the containers, and start the application.

#### 4. **Verifying the Containers**

Once the containers are running, you can verify them using:
```bash
docker ps
```
This will show both the WordPress and MySQL containers. Example output:

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
7b2282c049fb        wordpress           "/entrypoint.sh apach…"   20 minutes ago      Up 5 minutes        0.0.0.0:8080->80/tcp                it_adpcwddj_01_enus_13_assets_wordpress_1
e0be3d74f084        mysql               "docker-entrypoint.s…"    20 minutes ago      Up 5 minutes        0.0.0.0:3307->3306/tcp              mysql_db
```

You should now be able to access WordPress at [localhost:8080](http://localhost:8080).

#### 5. **Monitoring with ManageEngine**

1. **Access ManageEngine Applications Manager:**
   Open the "DemoDockerMonitor" dashboard.

2. **Adding Containers to Monitor:**
   - Scroll down to the "Docker Containers" table.
   - Click **"Add Containers"** on the right side.
   - Select the `wordpress` and `mysql_db` containers.
   - Click **"Add Containers"** to add them for monitoring.

3. **Monitor Application Performance:**
   - After adding, click **"Close"**.
   - Use the **Control** key to open the monitoring data for both containers in separate browser tabs.
   - Monitor metrics such as memory usage, container state, and availability.

#### 6. **Optimization and Monitoring**

With the containers added to ManageEngine, you can now monitor the performance of both WordPress and MySQL. Keep an eye on resource utilization, uptime, and health indicators to ensure optimal performance for your application.

---

This setup allows you to quickly deploy a WordPress site using Docker, backed by MySQL, and offers the ability to monitor and optimize the application with ManageEngine.