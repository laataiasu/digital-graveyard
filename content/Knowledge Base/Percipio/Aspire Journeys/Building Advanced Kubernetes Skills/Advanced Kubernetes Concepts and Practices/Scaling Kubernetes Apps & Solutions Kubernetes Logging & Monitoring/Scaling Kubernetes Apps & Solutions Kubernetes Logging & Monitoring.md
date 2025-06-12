# Scaling Kubernetes Apps & Solutions Kubernetes Logging & Monitoring

## What's Involved in Application Logging & Monitoring

### Types of Log Consumers

1. **Developers**:  
   - Developers use logs to understand application behavior, debug issues, and track variables.
   - Logs help trace code paths, identify where errors occur, and provide stack traces when exceptions happen.

2. **System Administrators**:  
   - Admins focus on application health and performance, rather than granular details like stack traces.
   - They use logs to diagnose and resolve issues, ensuring the application runs smoothly.

3. **Security Teams**:  
   - Security teams analyze logs to monitor for potential threats or breaches.
   - Logs help track who accessed the application and when, which can identify suspicious activities.

### Application Monitoring

1. **Alerts**:  
   - Monitoring systems track specific conditions (e.g., high memory usage) and send notifications to relevant parties when thresholds are exceeded.
  
2. **Dashboards**:  
   - Dashboards provide a centralized view of the system's health, helping users quickly identify any issues that need attention.

3. **Importance**:  
   - Monitoring helps maintain a good user experience by ensuring applications function properly.
   - It can also alert teams to issues and potential attacks, helping to mitigate risks and maintain performance.

### Logging vs. Monitoring

- **Logging**:  
   - Logs collect information about the application’s internal operations, both good and bad.
   - Logs are essential for understanding what happened at any point in time.

- **Monitoring**:  
   - Monitoring systems consume log data to assess the application's current state and health.
   - The goal of monitoring is to alert users when the application deviates from expected behavior.

### Challenges with Logging

1. **Multiple Log Files**:  
   - Logs are often stored in multiple files, which can be split by application component or by date.
   - This is common and helps with performance and file maintenance.

2. **Log Volume**:  
   - Some applications generate large log files, containing millions of rows, which can be hard to read.
   - Verbosity impacts readability and performance, so logs need to be structured effectively.

3. **Lack of Correlation**:  
   - Logs may not always clearly show how events across different components relate to each other.
   - This can be solved with correlation identifiers that tie log entries to specific actions across components.

### Best Practices for Logging

1. **Contextual Logs**:  
   - Logs should include sufficient detail about what happened, where it happened, and any relevant context.
   - This makes logs more actionable and helps resolve issues faster.

2. **Structured Logging**:  
   - Use structured formats (e.g., JSON) to allow easier parsing and querying.
   - Structured logs can be broken down into distinct fields, making them more useful for analysis.

3. **Centralized Logging**:  
   - Use logging tools or services (like Fluentd or Application Insights) to centralize and aggregate logs.
   - This makes it easier to search, analyze, and visualize logs from all parts of the application.

4. **Use of APIs and Plugins**:  
   - Standardize logging through APIs or plugins to ensure consistency across the application.
   - Centralized logging setup allows changes to logging behavior without modifying each application.

### Implementing Logging and Monitoring

1. **Collect Data**:  
   - Gather relevant log data from the application in real-time. This includes user activity, errors, and performance metrics.

2. **Aggregate Logs**:  
   - Store logs in a centralized location for easier access and analysis.
   - Tools like Application Insights (Azure) or EFK stack (Elasticsearch, Fluentd, Kibana) help aggregate and store logs.

3. **Viewing and Analysis**:  
   - Logs can be accessed through dashboards for visualization and monitoring.
   - Tools like Kibana (with Elasticsearch) or Application Insights provide powerful ways to view and analyze logs, as well as trigger notifications based on thresholds or anomalies.

## What's Involved in Cloud Monitoring

### Benefits of Cloud Monitoring

1. **Comprehensive Monitoring**:  
   - Cloud providers offer built-in tools to track and monitor various aspects of your application, from performance to resource utilization.  
   - These tools help you assess not only the application’s health but also the underlying infrastructure, including servers, virtual machines (VMs), databases, and networks.

2. **Infrastructure-Level Monitoring**:  
   - Cloud monitoring tools allow you to track infrastructure metrics like resource consumption, server response times, and network performance.
   - Monitoring the entire stack, from the application to the cloud infrastructure, helps ensure smooth operation and predict potential failures or attacks.

3. **Predictive Monitoring**:  
   - By analyzing performance data, you can identify anomalies or trends (like slower response times) that may indicate future issues, even before they become critical problems.
   - For instance, monitoring API response times can reveal performance issues even when no explicit errors are logged.

### Types of Cloud Monitoring

1. **Application Monitoring**:  
   - Track metrics like uptime, activity, and performance for web applications and APIs.  
   - For example, API monitoring can show request volumes, request types, response times, and request locations, providing detailed insights into how your system behaves.

2. **Database Monitoring**:  
   - Monitor database health, capacity, and throughput to ensure optimal performance.
   - This is particularly important for systems with heavy data demands, where performance bottlenecks can affect overall application speed.

3. **Infrastructure Monitoring**:  
   - Cloud providers also allow you to monitor network traffic, storage, and virtual machines (VMs), which are critical components of cloud-based systems.
   - Virtual machines (VMs) require close monitoring for health, uptime, memory usage, and performance, ensuring they run smoothly.

4. **Cloud Storage Monitoring**:  
   - If you're using cloud storage, the monitoring tools will track usage patterns and data transfer rates, similar to database monitoring, ensuring that storage capacity and performance are within acceptable limits.

### Key Advantages of Cloud Monitoring

1. **Troubleshooting**:  
   - Cloud monitoring helps you detect issues quickly, minimizing downtime and reducing the impact of failures.
  
2. **Scaling**:  
   - Monitoring enables you to detect when your system is under heavy load, allowing you to scale resources appropriately to meet demand.
  
3. **Accessibility**:  
   - Monitoring tools are cloud-based, meaning they are easily accessible from anywhere and on any device (desktop, tablet, or mobile), making it simple to track system health remotely.

4. **Cost Efficiency**:  
   - Cloud monitoring tools are generally cost-effective, often included in the cloud provider’s services. Building your own solution would typically be more expensive than using the tools already available from your cloud provider.

5. **Simplicity**:  
   - Many cloud providers offer integrated monitoring tools that require minimal setup, reducing the effort needed to implement monitoring across your cloud environment.

6. **Availability**:  
   - Cloud monitoring tools are highly available, ensuring that you can always access the data needed to diagnose issues, even when troubleshooting the cloud system itself.

### Monitoring in Hybrid and Private Clouds

1. **Hybrid Cloud Monitoring**:  
   - In a hybrid cloud environment, you need to monitor both private and public cloud resources. This may involve sending logs from private systems to public cloud monitoring tools.
  
2. **Private Cloud Monitoring**:  
   - For private cloud or on-premise data centers, cloud monitoring tools are less automated. You’ll need to implement custom solutions or third-party tools to capture and analyze logs, which can require more management effort.

### Best Practices for Cloud Monitoring

1. **Monitor Usage and Costs**:  
   - Always track system usage and associated costs. Cloud resources can quickly lead to unexpected expenses if not monitored effectively.
   - Example: A company spent $250,000 in three months because they didn’t monitor usage, leading to unnecessary resource allocation.

2. **Identify Key Metrics and Events**:  
   - Focus on metrics that matter most for your system. For example, API performance metrics (e.g., throughput, response times) are crucial for services handling high traffic, while database capacity is critical for data-heavy applications.

3. **Use a Single Platform for Monitoring**:  
   - If possible, centralize monitoring on a single platform. Having a unified view makes it easier to track and act on data from different parts of the system.

4. **Set up Alerts and Rules**:  
   - Create rules and thresholds based on collected data to trigger notifications when action is required. This proactive approach ensures that potential problems are addressed before they escalate.

5. **Partition Centralized Data**:  
   - While centralizing data is important for analysis, avoid dumping all data into a single location. Partitioning and separating data makes querying more efficient and easier to manage.

6. **Monitor User Experience (UX)**:  
   - Beyond system health, monitor UX-related metrics such as system speed, responsiveness, uptime, and availability. These factors directly impact user satisfaction.

7. **Establish and Test Standards**:  
   - Define what constitutes a “healthy” system for your application, and regularly test to ensure that your system is meeting these standards. This helps maintain a baseline for performance and reliability.

### Conclusion

Cloud monitoring offers powerful tools that help you maintain application health, optimize resources, troubleshoot issues, and plan for future scaling needs. By leveraging the built-in monitoring features of cloud providers, you can gain comprehensive insights into your infrastructure and applications, ensuring optimal performance and security while keeping costs manageable. Following best practices for cloud monitoring can help you achieve both efficiency and reliability in your cloud deployments.

## Google Kubernetes Engine (GKE) Logging & Monitoring

### Google Kubernetes Engine (GKE) Logging and Monitoring

**Google Kubernetes Engine (GKE)** is a managed Kubernetes service within Google Cloud that comes with built-in logging and monitoring capabilities. This makes it easier to manage and monitor Kubernetes clusters, ensuring that your application and infrastructure are running smoothly.

### Cloud Operations for GKE

The **Cloud Operations** tool (formerly Stackdriver) is specifically designed to monitor Kubernetes clusters running in Google Cloud. This integrated tool provides powerful features for logging, monitoring, and troubleshooting. It automatically integrates with GKE, providing a dashboard and detailed metrics for Kubernetes applications and infrastructure.

- **Cloud Monitoring**: Allows you to track key metrics like CPU, memory, and resource utilization. It enables monitoring at various levels:
  - **Cluster Level**: Metrics related to cluster-wide resource usage.
  - **Workload Level**: Insights into specific workloads and pods.
  - **Service Level**: Metrics and performance for services running within the cluster.
  - **Component Level**: View metrics for individual components like namespaces, nodes, and pods.

- **Cloud Logging**: Captures detailed logs for Kubernetes workloads and system components. You can log information from both your applications and the underlying Kubernetes infrastructure (such as nodes, containers, and system events).

### Key Features of Cloud Operations

1. **Automatic Integration**:  
   When you create a GKE cluster, Cloud Operations is enabled by default. This means logging and monitoring support is automatically available without additional setup. However, you can disable it if necessary, though it's generally not recommended.

2. **GKE Dashboard**:  
   The GKE-specific dashboard provides a user-friendly interface for managing logs and metrics:
   - **Filter Bar**: Quickly locate specific GKE resources, such as pods or services.
   - **Alerts Timeline**: Visualize alerts and incidents in a timeline format to understand when issues occurred.
   - **Dashboard Tables**: View metrics in a table format for quick, at-a-glance analysis.
   - **Logs Explorer**: View, query, and filter logs to analyze system behavior or investigate issues.

3. **Audit Logs**:  
   You can capture audit logs from your Kubernetes nodes. This is crucial for security and operational auditing, as it provides insights into:
   - **System Logs**: Warnings and errors from the underlying system (VMs or physical servers).
   - **Authentication Logs**: Failed login attempts, which are useful for detecting unauthorized access attempts.
   - **Audit Trails**: Information about actions taken on the system, such as the execution of services or binaries, helping security teams understand who did what and when.

4. **Prometheus Integration**:  
   Cloud Operations integrates with **Prometheus**, a widely-used monitoring tool for Kubernetes. Prometheus can collect detailed metrics in the **Prometheus exposition format**, which can be exported to Google Cloud Monitoring for further analysis. This allows you to track and analyze application and system-level metrics in a unified dashboard.

### GKE Monitoring Best Practices

- **Configure Log Collection**:  
   By default, GKE collects logs for deployed workloads, but you may need to configure **Cloud Operations** to capture additional system-level logs (e.g., node-level logs) to get a complete picture of your cluster’s health.

- **Review Kubernetes-Specific Metrics**:  
   Make sure you monitor the key metrics that affect Kubernetes clusters, such as pod health, node resource usage, and container status. Use Cloud Monitoring’s GKE dashboard to stay on top of these metrics.

- **Enable Prometheus for Advanced Monitoring**:  
   If you require more granular metrics or specialized application-level monitoring, enable **Prometheus**. It can provide detailed metrics for your workloads, which can then be integrated with Cloud Monitoring.

### Summary

GKE offers robust built-in logging and monitoring capabilities through **Cloud Operations**, allowing you to easily manage and troubleshoot Kubernetes clusters. With features like the GKE dashboard, logs explorer, and Prometheus integration, you can monitor application performance, track system health, and enhance security by capturing important audit logs. By leveraging these tools, you can ensure the smooth operation and security of your Kubernetes workloads in Google Cloud.

## Amazon EKS Logging & Monitoring

### Amazon Elastic Kubernetes Service (EKS) Logging and Monitoring

**Amazon Elastic Kubernetes Service (EKS)** is AWS’s managed Kubernetes offering, which simplifies deploying, managing, and scaling Kubernetes clusters. Like Google Kubernetes Engine (GKE), EKS comes with built-in tools for monitoring and logging, leveraging **AWS CloudWatch** and **AWS CloudTrail** for comprehensive observability.

### EKS Logging and Monitoring Overview

EKS includes automatic logging of control plane activities, which makes it easier to secure and operate Kubernetes clusters. The logs are streamed directly to **Amazon CloudWatch**, providing a centralized location for logging and monitoring. Additionally, EKS integrates with **AWS CloudTrail** for capturing API activity and tracking security-related events.

### Key Features of EKS Logging and Monitoring

#### 1. **Control Plane Logging**
   EKS collects logs from the control plane by default, and you can enable or disable different types of logs on a per-cluster basis. The logs that are collected include:

   - **Kubernetes API Logs**: These logs provide insights into the behavior of the Kubernetes API server, which is the heart of your cluster’s control plane.
   
   - **Audit Logs**: Capture both successful and failed login attempts across users, roles, and system components. This is vital for security and compliance.
   
   - **Authenticator Logs**: These logs are unique to EKS and contain information about Role-Based Access Control (RBAC) requests. They let you know whether a user, service, or system component is authorized to perform certain actions.

   - **Controller Manager Logs**: The controller manager manages the state of the cluster by running control loops that handle tasks like node health checks and scaling. These logs are useful for troubleshooting issues with the control loops.

   - **Scheduler Logs**: The scheduler is responsible for placing pods on nodes. These logs can help diagnose issues related to pod scheduling, such as if the system is struggling to find an appropriate node for a pod.

   EKS allows you to configure the collection of these logs using the **AWS Management Console**, **AWS CLI**, or **EKS API**. When control plane logging is enabled, all logs are streamed directly to CloudWatch for real-time monitoring.

#### 2. **Integration with AWS CloudTrail**
   **CloudTrail** records API calls made to AWS services, and it integrates seamlessly with EKS to capture every action performed on your Kubernetes clusters. This includes:

   - **User and Service Actions**: CloudTrail logs actions made by users, roles, and AWS services, making it possible to audit changes to the cluster’s state.
   
   - **API Call Events**: CloudTrail logs all API calls made to the EKS API, providing records of actions like creating, deleting, or updating clusters and resources.

   - **Identity and Access Management (IAM) Details**: CloudTrail logs include details about the identity of the request initiator. This includes IAM users, roles, and AWS services that made the request. Even if temporary credentials are used, you will still know who performed the action.

   - **Security and Compliance**: CloudTrail logs are useful for security teams because they include details about who requested what and when. For example, if a cluster creation fails, CloudTrail will log the failed action along with the IAM role or service that initiated the request.

   - **Continuous Delivery with CloudTrail**: You can set up continuous delivery of CloudTrail logs to an **S3 bucket** for long-term storage and analysis, making it easy to analyze event history and perform forensic investigations if needed.

#### 3. **Metrics and Monitoring**
   EKS also generates useful **control plane metrics** related to the performance and health of your Kubernetes clusters. These include:

   - **Node Metrics**: Information on the state and performance of the nodes within your EKS cluster.
   - **Pod Metrics**: Data on the resource usage of pods, including CPU and memory utilization.
   - **Cluster-Level Metrics**: Overall metrics for the cluster, such as node availability, pod deployment status, and resource usage.

   These metrics can be collected and monitored through **CloudWatch** and viewed in CloudWatch dashboards. Additionally, you can integrate **Prometheus** with EKS for more advanced monitoring and metric collection.

   - **Prometheus Integration**: Prometheus is a popular open-source monitoring tool for Kubernetes. When integrated with EKS, Prometheus can scrape exposed metrics from your Kubernetes endpoints. These metrics can then be visualized and queried using Prometheus’ UI or through **Kubernetes utilities** like `kubectl`. Prometheus supports advanced features like:
     - **Time-Series Data**: Prometheus stores metrics in a time-series format, allowing for trend analysis.
     - **Histograms and Aggregations**: Prometheus can collect and store metrics as histograms, aggregating data over time.
     - **Metrics Querying**: With Prometheus, you can query metrics and generate visualizations based on specific time ranges or conditions.

   - **CloudWatch Metrics**: In addition to Prometheus, CloudWatch also supports monitoring of EKS and Kubernetes workloads. CloudWatch can track basic metrics such as CPU and memory usage, and it integrates with CloudWatch dashboards for visualizing and analyzing these metrics in real time.

   You can view raw metrics using `kubectl` commands like `kubectl get --raw/metrics`, which exposes the collected metrics data.

### Best Practices for EKS Logging and Monitoring

1. **Enable Control Plane Logging**:  
   Ensure that you have enabled control plane logging for all relevant log types. These logs provide crucial insights into the behavior and security of your cluster.

2. **Integrate CloudTrail for Full Audit Capability**:  
   Enable CloudTrail to capture all API calls and actions performed on your EKS clusters. This helps with security monitoring and allows you to investigate incidents effectively.

3. **Use Prometheus for Advanced Metrics**:  
   For advanced monitoring, integrate Prometheus into your EKS environment. Prometheus can collect granular metrics and expose them in a time-series format for detailed analysis.

4. **Monitor Node and Pod Health**:  
   Use CloudWatch or Prometheus to monitor the health and resource utilization of your nodes and pods. Keeping track of key metrics like CPU, memory, and network usage helps identify bottlenecks or performance issues.

5. **Configure Alerts and Dashboards**:  
   Set up CloudWatch dashboards to visualize key metrics and create alarms to notify you of any performance or security issues. This proactive approach helps you maintain high availability and security.

### Summary

Amazon EKS provides robust logging and monitoring features through integration with **CloudWatch** and **CloudTrail**, which offer visibility into the Kubernetes control plane, API activity, and system performance. By enabling control plane logging and integrating Prometheus, you can effectively monitor and troubleshoot your EKS clusters. CloudTrail logs capture detailed audit information for security and compliance, while Prometheus provides deep insights into your application performance, ensuring your Kubernetes environment remains secure, performant, and well-maintained.

## Microsoft AKS Logging & Monitoring

### Azure Kubernetes Service (AKS) Logging and Monitoring

**Azure Kubernetes Service (AKS)** is Microsoft's managed Kubernetes offering, designed to simplify deploying, managing, and scaling Kubernetes clusters in the Azure cloud. Like other cloud providers, AKS comes with built-in monitoring and logging capabilities, but its default logging solution is relatively basic. To unlock deeper insights and more advanced monitoring, Azure offers several tools and integrations, including **Azure Monitor for Containers** and **Container Insights**. Additionally, Azure allows integration with **Prometheus** for more advanced metric collection and monitoring.

### Key Components of AKS Logging and Monitoring

#### 1. **Default Logging in AKS**
   - **Elastic Stack**: By default, AKS uses the **Elastic Stack** for logging, which is relatively simple but may not provide enough context for deep troubleshooting. Raw logs are collected and can be easily viewed, but for more detailed analysis, additional tools are needed.
   - **Log Aggregation**: The first step in AKS logging is to aggregate logs from the Kubernetes cluster and its workloads into a central location. This enables easier storage, querying, and integration with downstream services.

#### 2. **Azure Monitor for Containers**
   **Azure Monitor for Containers** is a built-in service that provides comprehensive monitoring for containerized workloads running on Kubernetes, including AKS. It helps you collect, analyze, and visualize logs and metrics from your AKS clusters. Here’s what it offers:

   - **Cross-Orchestrator Support**: Azure Monitor is versatile and can monitor not just Kubernetes (AKS), but also other container orchestrators like Docker Swarm, DC/OS, and Red Hat OpenShift. This unifies your monitoring experience across different environments.
   - **Log and Metric Collection**: Azure Monitor collects both **logs** and **metrics** from containers and clusters, allowing you to correlate logs with performance metrics for more effective troubleshooting.
   - **Platform Agnostic**: The service works across various operating systems, so whether you are running AKS on Linux or Windows nodes, or using other orchestrators, the logs and metrics will be presented in a familiar format.
   - **Centralized Dashboards**: Logs and metrics from your AKS clusters can be viewed and analyzed in centralized dashboards, giving you a bird’s-eye view of your entire environment.

#### 3. **Azure Container Insights**
   **Container Insights** is a feature within Azure Monitor specifically designed for monitoring the performance and health of containers and workloads in Kubernetes environments. It provides deep insights into your AKS workloads and helps you monitor the overall health of your cluster:

   - **Cluster Health and Performance**: Container Insights allows you to monitor both the **health** and **performance** of your Kubernetes clusters and workloads. It tracks key metrics like CPU and memory usage, disk and network I/O, and pod statuses.
   
   - **Workload Monitoring**: You can monitor specific **workloads** running in AKS. These workloads include containers, pods, and controllers (like Deployments or StatefulSets), allowing you to drill into the performance and resource utilization of individual workloads.
   
   - **Resource Utilization**: With Container Insights, you can track the **CPU** and **memory** utilization of individual containers, nodes, and pods. This helps identify resource bottlenecks and understand the consumption patterns of your workloads.
   
   - **Performance of Pods and Controllers**: Container Insights lets you see how your **containers** are performing within specific **pods** and **controllers**. You can easily identify performance issues and optimize resource allocation.
   
   - **Behavior Under Load**: Understanding how your AKS cluster behaves under different **load conditions** is crucial for capacity planning and scaling. Container Insights helps you analyze this behavior and figure out when and where to scale your resources.
   
   - **Alert Configuration**: You can set up **alerts** to proactively notify you when certain thresholds are breached, such as when resource usage exceeds a certain level or when pods are experiencing errors.
   
   - **Prometheus Integration**: Azure Container Insights offers integration with **Prometheus**, an open-source monitoring tool, allowing you to view and analyze **Prometheus metrics** collected from Kubernetes clusters. Prometheus can scrape metrics from endpoints within your AKS cluster, and you can integrate it with Azure Monitor for more advanced metric aggregation and analysis.

#### 4. **Prometheus Integration**
   **Prometheus** is a widely-used open-source monitoring and alerting toolkit, commonly used with Kubernetes environments. It integrates easily with AKS for advanced monitoring and metrics collection:

   - **Open-Source Flexibility**: Prometheus is part of the Cloud Native Computing Foundation (CNCF) and works seamlessly across all cloud environments, including Azure. It is highly configurable and allows you to collect any metric, aggregate data as you see fit, and expose it through a user-friendly interface.
   
   - **Metrics Collection and Querying**: Prometheus collects time-series data from **Kubernetes endpoints** and stores metrics such as CPU usage, memory consumption, request rates, and error rates. You can use Prometheus queries to extract valuable insights and visualize the data over time.
   
   - **Kubernetes Integration**: Prometheus natively integrates with Kubernetes, including AKS, and can automatically discover and scrape metrics from Kubernetes objects (e.g., nodes, pods, and containers). You can also use Kubernetes annotations to expose custom metrics.
   
   - **Azure Monitor and Prometheus**: Azure Monitor for Containers integrates with Prometheus metrics. If you prefer using Prometheus to collect detailed metrics but don’t want to manage your own Prometheus server, Azure Monitor can handle the **Prometheus server** and **metric store** for you, simplifying the setup and reducing the operational overhead.

#### 5. **Log Analytics and Querying**
   Azure Monitor provides **Log Analytics**, a tool that allows you to query, analyze, and visualize logs collected from your AKS clusters. You can use the **Kusto Query Language (KQL)** to run complex queries against your logs to derive meaningful insights. For example:

   - **Error Tracking**: Use queries to search for error logs, audit trails, and failures across your Kubernetes environment.
   - **Anomaly Detection**: Set up queries to detect unusual activity or abnormal resource usage patterns, which might indicate a problem or inefficiency in your AKS deployment.

### Best Practices for AKS Logging and Monitoring

1. **Enable Azure Monitor and Container Insights**:  
   By default, enable **Azure Monitor for Containers** and **Container Insights** for your AKS clusters to capture and analyze metrics and logs. These tools provide you with centralized visibility into your cluster’s health and performance.

2. **Integrate with Prometheus**:  
   If you need more advanced metrics collection and monitoring capabilities, integrate **Prometheus** with Azure Monitor for Containers. This gives you powerful metric aggregation and querying capabilities, and allows for deeper insights into your workloads.

3. **Configure Alerts**:  
   Set up **alerts** within **Container Insights** to be notified of any potential issues, such as high resource usage or pod failures. This proactive approach ensures you can address problems before they impact users.

4. **Log Aggregation and Analysis**:  
   Ensure that logs from all your Kubernetes resources, including workloads, control plane, and nodes, are properly aggregated and stored in a central location. Use **Log Analytics** to query and analyze these logs effectively.

5. **Monitor Resource Utilization**:  
   Track **CPU**, **memory**, and **network** resource utilization across your containers, nodes, and pods. Use this data to identify bottlenecks and optimize resource allocation for your AKS workloads.

6. **Monitor Cluster Behavior Under Load**:  
   Use **Container Insights** to understand how your cluster behaves under varying loads, and ensure that you can scale resources as needed to meet demand.

### Summary

**Azure Kubernetes Service (AKS)** provides robust logging and monitoring tools to ensure that your Kubernetes clusters and workloads are performing well. By leveraging **Azure Monitor for Containers** and **Container Insights**, you can collect detailed logs and metrics to track the health of your cluster and troubleshoot issues effectively. Additionally, **Prometheus** integration allows for advanced metric collection and monitoring. These tools give you everything you need to maintain visibility into your AKS clusters and ensure that your containerized workloads run smoothly.

## Kubernetes Logging & Monitoring

### Prometheus and Kubernetes Monitoring with Azure Container Insights

In this video, the focus is on **Prometheus** and its integration with **Azure Container Insights** for collecting metrics in Kubernetes environments. The video explains how to use Azure's monitoring tools to seamlessly collect Prometheus metrics without the need for managing a separate Prometheus server. Below are the key concepts and best practices mentioned in the video, along with insights into what should be monitored in a Kubernetes environment.

### Key Concepts from the Video:

#### **Prometheus Overview:**
Prometheus is a widely-used **open-source** monitoring tool designed for **metric collection** in containerized environments like Kubernetes. Normally, Prometheus requires setting up and managing your own server to scrape metrics, but with **Azure Container Insights**, this process becomes simplified. You only need to expose the **Prometheus metrics endpoint**, and Container Insights will handle the scraping and collection of metrics.

#### **Azure Container Insights and Prometheus Integration:**
- **No Server Needed**: The typical Prometheus setup requires you to manage a server and its storage backend. However, with **Azure Monitor and Container Insights**, the platform handles the Prometheus server for you.
- **Scraping Modes**:
  1. **Cluster-wide Scraping**: This collects metrics from the entire Kubernetes cluster, including core services like **kube-dns** and **kube-state-metrics**, and can also collect application-specific metrics exposed by pod annotations.
  2. **Node-wide Scraping**: This targets individual node metrics, enabling monitoring of the infrastructure hosting the Kubernetes clusters.

#### **When and Where to Use Prometheus in Kubernetes:**
Prometheus is particularly useful in environments like **Azure Kubernetes Service (AKS)**, **Azure Stack**, and **Azure Red Hat OpenShift** where scalability and real-time metric collection are essential.

---

### What Should Be Monitored in Kubernetes?

Monitoring in Kubernetes is crucial for ensuring the health and performance of your clusters and workloads. As Kubernetes is complex, monitoring should occur at **multiple layers** of the stack, covering infrastructure, services, and specific applications. Here are the key things to monitor in Kubernetes:

#### **1. Infrastructure Monitoring (Nodes, Pods, and Resources):**
- **Nodes**: Monitor the physical machines or virtual machines that provide resources (CPU, memory, disk) to your Kubernetes workloads. Resource consumption metrics like **CPU utilization**, **memory usage**, and **disk I/O** are essential.
- **Pods**: Pods are the smallest deployable units in Kubernetes and run your application containers. Monitoring **CPU** and **memory usage** at the pod level helps identify resource bottlenecks or potential performance issues. Additionally, monitoring the **pod lifecycle** and whether they’re running or failing is crucial.
- **Resource Usage**: Track how much **CPU**, **memory**, and **disk space** are being consumed by your pods and containers. For example, if a pod is consuming an excessive amount of CPU, it may indicate a problem that needs to be addressed.

#### **2. Kubernetes Services and Core Components:**
- **Kube-scheduler**: The **kube-scheduler** is responsible for placing pods onto the correct nodes. If it's not functioning properly, pods won’t get scheduled, leading to deployment failures. Monitoring the health of the scheduler is critical for ensuring that new pods are placed correctly within the cluster.
- **Etcd**: **etcd** is the key-value store for Kubernetes' cluster state. It’s a critical component that stores all configuration and state data for the cluster. If etcd is compromised or unavailable, the entire cluster's state is at risk, so its health needs to be carefully monitored.
- **Control Plane**: The **control plane** manages the Kubernetes cluster. Monitoring the control plane ensures that all components, like **kube-apiserver**, **kube-controller-manager**, and **kube-scheduler**, are operating properly. A failure in the control plane can disrupt the cluster’s ability to function.

#### **3. Application Monitoring (Workloads and Custom Services):**
- **Applications**: Kubernetes is often used to deploy microservices that are composed of multiple pods and services. Monitoring the health and performance of these applications—whether they’re running, their resource consumption, and response times—is critical for ensuring optimal performance.
- **Custom Kubernetes Services**: In addition to core Kubernetes services, many organizations deploy custom services in their clusters. These could include internal microservices, databases, and APIs. Monitoring these applications will help you identify when they’re failing or consuming excessive resources.

#### **4. Disk Usage and Storage Monitoring:**
Disk usage can often be an overlooked aspect of monitoring in Kubernetes. As workloads like **Elasticsearch** generate large volumes of logs or data, failing to monitor disk usage can lead to unexpected **disk overflow** or **storage issues**. It’s essential to track disk usage and storage capacity over time to prevent performance degradation or outages.

---

### The Importance of Monitoring in Kubernetes

Kubernetes is a highly dynamic platform, and with multiple components running across a distributed environment, monitoring is essential to ensure that everything is functioning correctly. With hundreds or even thousands of containers in play, monitoring every layer—**nodes**, **pods**, **services**, and **control plane**—becomes even more important.

#### **Why Monitoring Is Crucial:**
- **Scalability**: Kubernetes is designed to scale horizontally. Monitoring helps you track how well the system is scaling under load and identify potential performance bottlenecks.
- **Reliability**: With complex microservices architectures, you need to ensure that every service and container is running smoothly. Monitoring helps detect issues before they cause service disruptions.
- **Availability**: If a component fails (e.g., a pod crashes or a service becomes unresponsive), proactive monitoring can help detect and resolve issues quickly, ensuring higher availability.
- **Security**: Monitoring also plays a key role in identifying potential security issues, such as unauthorized access or abnormal activity in the system.

---

### Tools for Kubernetes Monitoring

The video mentions several popular tools for Kubernetes monitoring:

1. **Prometheus**: A robust solution for **metric-based monitoring** that is highly customizable and works well with Kubernetes environments. It is particularly good at collecting time-series data and can be integrated with various cloud platforms, including Azure.
2. **cAdvisor**: Built into the **kubelet**, cAdvisor is useful for monitoring container resource usage (CPU, memory, disk, and network).
3. **Sensu Go**: A versatile monitoring tool suitable for multi-cloud environments. It can integrate with Prometheus and provide insights into the health of containers, services, and infrastructure.
4. **Fluentd**: A log aggregation tool that collects logs from Kubernetes resources and sends them to a downstream service for processing. Useful for centralized log management.
5. **Elastic Stack**: A suite of tools (including **Logstash**, **Elasticsearch**, and **Kibana**) used for capturing, transforming, storing, and visualizing logs and metrics from Kubernetes clusters.
6. **NetApp Cloud Insights**: A monitoring tool designed to provide insights into infrastructure health, performance, and security. It can visualize Kubernetes topology and help optimize cost, detect ransomware, and monitor compliance.

---

### Conclusion

Effective monitoring is essential to ensure the health, performance, and reliability of Kubernetes clusters and workloads. Tools like **Prometheus** and **Azure Container Insights** allow you to collect metrics from every layer in Kubernetes, from infrastructure components like nodes and pods, to core Kubernetes services like kube-scheduler and etcd. With the right monitoring solution, you can identify issues early, take corrective actions, and keep your Kubernetes clusters running smoothly.

## Using Kubernetes System Components Logging

### Kubernetes Logging and Visualization with Azure

In this demo, the focus is on inspecting logs generated by Kubernetes using **klog** (Kubernetes' structured logging system), deploying an application via **Helm**, and visualizing logs using **Azure Monitor**. Here's a breakdown of the process and the key steps involved:

---

### 1. **Connecting to Azure Kubernetes Service (AKS)**

- **Step 1: Connect to AKS using Azure CLI:**
  The demo starts by connecting to an Azure Kubernetes Service (AKS) cluster. To do this, the Azure CLI command is used:

  ```bash
  az aks get-credentials --resource-group <resource-group-name> --name <aks-cluster-name>
  ```

  This command fetches the credentials for the AKS cluster and configures them on your local machine's Kubernetes configuration file. This allows you to interact with your AKS cluster using `kubectl`.

- **Step 2: Validate Cluster Connectivity:**
  After connecting, a simple `kubectl get nodes` command is used to verify that the connection is successful and the cluster is accessible.

  ```bash
  kubectl get nodes
  ```

---

### 2. **Deploying a Simple Application with Helm**

- **Step 1: Create an Application Using Helm:**
  **Helm** is a package manager for Kubernetes that simplifies application deployment. The demo creates a simple application using Helm:

  ```bash
  helm create sbdemo03
  ```

  This command creates a folder with Helm's template for a basic Kubernetes application. The folder contains essential files like `Chart.yaml`, `values.yaml`, and a `templates/` directory.

- **Step 2: Define a Pod for the Application:**
  A **Pod** definition is added to the Helm chart using a custom `pod-counter.yaml` file, which describes a simple pod running a **BusyBox** container. The container runs an infinite loop that echoes the current date and iteration number every second.

  **pod-counter.yaml** example:

  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: sbdemo03-counter
  spec:
    containers:
    - name: count
      image: busybox
      command:
        - /bin/sh
        - -c
        - "while true; do echo $(date) Iteration $(($i++)); sleep 1; done"
  ```

- **Step 3: Deploy the Application:**
  The application is deployed to the AKS cluster using Helm:

  ```bash
  helm install sbdemo03 ./sbdemo03
  ```

- **Step 4: Verify the Deployment:**
  After deploying the application, verify that the pod is running:

  ```bash
  kubectl get pods
  ```

  The output will show the running pod `sbdemo03-counter`.

---

### 3. **Inspecting Application Logs**

- **Step 1: View Application Logs:**
  The application logs (echo output) can be viewed by using the `kubectl logs` command:

  ```bash
  kubectl logs sbdemo03-counter
  ```

  This will display the logs generated by the **BusyBox** container, showing the date and iteration output from the echo command.

---

### 4. **Exploring Kubernetes Logs Using klog**

- **Kubernetes Logging Mechanism - klog:**
  Kubernetes uses **klog** (Kubernetes' structured logging system) for logging various activities within the cluster, such as pod lifecycle, scheduling, and resource usage. The logs generated by Kubernetes are structured to allow for better querying and analysis.

- **Step 1: View Logs in Azure Monitor:**
  In the Azure portal, you can visualize Kubernetes logs more easily. To do this:

  1. Navigate to the **Azure Kubernetes Service** in the portal.
  2. Under the **Monitoring** section, select **Logs**.
  3. The **Logs** page provides various pre-defined queries for things like **alerts**, **auditing**, **availability**, **performance**, etc.

- **Step 2: Run Performance Queries:**
  In the **Performance** category, you can run queries to check the performance of containers in your cluster. For instance, you can view **average CPU usage** for your cluster by selecting a pre-built query, like the one for **Average CPU usage per minute**:

  - **Query:**
    This query aggregates the CPU usage across the cluster over a specific period (e.g., the last hour).

  - **Result:**
    The query returns metrics such as **TimeGenerated**, **ClusterName**, **AggregatedValue**, and **CPU usage**. This data is visualized in a graph for easier analysis.

- **Step 3: Visualize Data:**
  After running the query, you can visualize the CPU usage in a **Chart** format. This chart shows the **minute-by-minute CPU utilization** over the past hour, helping you understand how the system is performing.

---

### 5. **Structured Logging Benefits**

- **Structured Logging via klog:**
  Kubernetes logs are structured using **klog**, which organizes log entries into predefined fields (e.g., time, resource name, status) to make them easier to query. Azure Monitor and other log management tools can then take advantage of this structured logging to efficiently search, analyze, and visualize the logs.

- **Querying Logs:**
  With **structured logs**, you can perform complex queries that aggregate data across different parts of the cluster, making it easier to identify performance bottlenecks, resource usage trends, and potential issues.

---

### Conclusion

By leveraging **Helm** to deploy a simple application to **Azure Kubernetes Service (AKS)** and using **klog** for structured logging, this demo demonstrated how to:

1. Deploy an application to a Kubernetes cluster.
2. Use `kubectl` to inspect application logs.
3. Visualize logs and metrics in **Azure Monitor** using structured queries, benefiting from Kubernetes' built-in **klog** logging.

The integration of structured logging in Kubernetes (via **klog**) and cloud tools like **Azure Monitor** allows for efficient log management, better observability, and proactive monitoring of your cluster's performance and health.

## Monitoring Using Kubernetes Audit Logs

### Debugging Issues in Kubernetes Using Audit Logs

In this demo, the focus is on **monitoring and exploring Kubernetes audit logs** to help debug issues in a Kubernetes cluster. The audit logs track actions performed by users, applications, and even the Kubernetes control plane, helping administrators answer questions like "who did what and when?"

Here's a breakdown of the steps involved and how audit logging and policy enforcement can be configured and explored within **Azure Kubernetes Service (AKS)**.

---

### 1. **What is Kubernetes Auditing?**

- **Audit Logs** in Kubernetes are crucial for tracking security-relevant events in the cluster. They document actions performed by users, applications, and Kubernetes components.
- These logs help answer questions like:
  - **Who performed an action?**
  - **What action was performed?**
  - **When did the action occur?**

Kubernetes provides mechanisms like **audit policies** and **YAML configurations** to capture these logs, and **Azure** simplifies accessing and querying them.

---

### 2. **Enabling Auditing in Azure Kubernetes Service (AKS)**

- **Step 1: Access the Azure Portal**:
  Start by navigating to the Azure portal and searching for your Kubernetes cluster (in this case, **sbdemo03**).

- **Step 2: Enable Audit Logging**:
  On the cluster settings page, scroll down to the **Policies** section. If audit logging is not enabled, you can enable it here. In the demo, it’s assumed that audit logging is already enabled for the cluster.

  - **Audit Logs**: These logs capture actions and events related to the cluster's security and resource management.
  - **Policies**: Policies help ensure that the cluster follows the correct configuration and security standards. You can view the current policies and enable new ones.

---

### 3. **Configuring Azure Policies for Kubernetes**

- **Step 1: View Existing Policies**:
  In the **Azure Policy** service, policies are listed, and compliance states for each policy are visible. You can view whether the cluster is compliant with the existing policies, and modify them as necessary.

- **Step 2: Assign New Policies**:
  You can assign new policies to your Kubernetes cluster using the **Assign policy** page in Azure. This allows you to control which resources (pods, deployments, etc.) are monitored and audited.

  - **Scope**: You can specify the scope of the policy (e.g., all resources in the cluster, or only certain pods).
  - **Policy Definitions**: Azure offers a range of built-in policies, but you can also create custom ones to meet your specific requirements.

---

### 4. **Accessing and Querying Kubernetes Audit Logs**

- **Step 1: Access Logs in Azure**:
  Navigate to the **Logs** section of your AKS cluster in the Azure portal to query the audit logs. 

  **Steps**:
  - Open the **Logs** option on the left menu.
  - Click on **New Query** to start writing your query for container logs.

- **Step 2: Write a Query to Filter Audit Logs**:
  To explore audit logs in Azure, you can write a Kusto query in the query editor.

  Example Query:
  ```kusto
  ContainerLog
  | where LogEntry contains "audit"
  | order by TimeGenerated desc
  ```

  This query:
  - Filters logs from the **ContainerLog** table.
  - Looks for entries containing the word **"audit"**.
  - Orders results by **TimeGenerated** in descending order.

- **Step 3: Review Results**:
  Once you run the query, you will see a list of logs related to auditing. For example, this could include logs for user actions, authentication attempts, or other significant events.

---

### 5. **Audit Logs Example: Authentication Scenario**

Imagine you’ve deployed a **web API** in your Kubernetes cluster, and you’ve configured authentication policies. If a user tries to access the API without proper authentication, the application might reject the request with a **401 Unauthorized** status code.

- When these events occur, they are captured by the **audit logging** mechanism. The logs generated would include the user who made the request, the time of the request, and whether the authentication was successful or failed.

- These logs are then available for inspection through **Azure's log management system**, allowing you to monitor security events and troubleshoot access-related issues.

---

### 6. **Exploring Additional Audit Capabilities in Azure**

In addition to Kubernetes-specific auditing, Azure also provides **Activity Logs** for general auditing of Azure resources.

- **Activity Logs** track **management actions** performed on the Kubernetes cluster itself (e.g., changes to the cluster’s configuration, scaling operations, etc.).
- These logs are useful for tracking what actions were performed against the cluster, by whom, and when.

  **Steps**:
  - Navigate to the **Activity log** section in Azure.
  - You can review all the management actions taken against the Kubernetes resource, including administrative operations like **updates**, **deletions**, or **role assignments**.

---

### 7. **Benefits of Kubernetes Audit Logging with Azure**

- **Security and Compliance**: Audit logs help ensure that your Kubernetes cluster adheres to security and compliance standards.
- **Visibility and Debugging**: Audit logs provide a clear trail of actions taken in the cluster, making it easier to troubleshoot and debug issues (e.g., unauthorized access attempts).
- **Azure Integration**: The centralized logging and querying tools in Azure, like **Azure Monitor**, provide a clean, user-friendly interface for querying and visualizing logs, which enhances operational efficiency.

---

### 8. **Conclusion**

By enabling audit logging in your AKS cluster and using the **Azure Portal** to explore these logs, you gain valuable insights into:

- **Who performed actions** on the cluster.
- **What actions** were taken, and **when** they occurred.
- **Security events** like unauthorized access attempts or configuration changes.
- **Compliance** with organizational policies and security standards.

This visibility is key for debugging, compliance, and securing your Kubernetes environment.

### Key Takeaways:
- **Audit logs** provide a historical record of actions performed on the cluster, which is critical for debugging and security.
- Azure makes it easy to query and visualize Kubernetes audit logs with powerful built-in tools like **Azure Monitor**.
- **Policies** help ensure your cluster is configured correctly and conforms to security requirements.

## Pulling Kubernetes Events Using kubectl

### Exploring Pod Events in Kubernetes with `kubectl`

In this demo, we’re going to explore how to troubleshoot Kubernetes pods by examining the events related to them. The events can give us valuable information about the state and lifecycle of our pods, and can help in identifying issues such as startup failures, image pull issues, or resource constraints.

We will be using the `kubectl` command line tool to view and filter the events of our pods. Let’s break this down step by step:

---

### **1. Setting Up the Application in Kubernetes**

- **Step 1: Navigate to the Project Directory**:
  In this demo, we assume you already have a simple application deployed in your Kubernetes cluster. The application, created earlier, prints the current date every second. Make sure you're in the `C:\demo` folder where your application files are located.

- **Step 2: Check Existing Pods**:
  To verify the current state of your pods, run:
  ```bash
  kubectl get pods
  ```
  If there are no pods running, the output will be empty, which is expected at the beginning.

- **Step 3: Deploy the Application**:
  To deploy the application, use the following `helm` command:
  ```bash
  helm install sbdemo03 ./sbdemo03
  ```
  This command installs the application defined in the `sbdemo03` directory to your Kubernetes cluster. Helm will handle the deployment and setup of the necessary resources for the application.

- **Step 4: Verify Pod Deployment**:
  Once the deployment is complete, you can verify the pods are running by executing:
  ```bash
  kubectl get pods
  ```
  You should see two pods listed under the `NAME` column, corresponding to your application.

---

### **2. Exploring Pod Events**

Once the application is deployed, let’s focus on retrieving the **events** associated with our pods. Events can help us understand if any issues occurred during pod creation, resource allocation, or startup.

- **Step 1: Describe Pod to View Events**:
  To get detailed information about a specific pod, including the events that have occurred, run:
  ```bash
  kubectl describe pod sbdemo03-counter
  ```
  This command provides detailed information about the pod, including:
  - **Pod status** (e.g., Running, Pending)
  - **Container information** (e.g., image, status)
  - **Node assignments**
  - **Events** (this is the section we're interested in)

  Scroll to the bottom of the output to see the **events** section. These events will be listed from the oldest to the most recent, providing insights into the pod's lifecycle. For example:
  - **Scheduled**: When the pod was assigned to a node.
  - **Pulling**: When the image was pulled.
  - **Started**: When the pod container was started.
  - If there were any issues (e.g., image pull failures, resource allocation problems), they would appear in this list as well.

---

### **3. Viewing Events for the Entire Cluster**

If you want to view events from the entire cluster rather than a specific pod, you can use the following command:
```bash
kubectl get events
```
This will show you all events that have occurred in the cluster, such as pod scheduling, image pulling, and pod startup. These events are useful when you want to monitor what is happening across the entire cluster.

---

### **4. Filtering Events for Specific Pods**

In a real-world scenario, you might have many pods running, and you might want to filter events for a particular pod. To filter events for a specific pod, use the `--field-selector` option in the `kubectl get events` command.

Example:
```bash
kubectl get events --field-selector involvedObject.name=sbdemo03-counter
```
This will return only the events associated with the pod named `sbdemo03-counter`. It can be very useful when trying to troubleshoot a specific pod in a large cluster.

---

### **5. Cleaning Up After the Demo**

After exploring the events, it’s important to clean up the resources you've created in your cluster. To delete the application and its associated resources, you can run:
```bash
helm delete sbdemo03
```
This removes the deployment, including the pods, services, and other resources that were created by Helm.

---

### **Summary of Key Commands**

1. **Check the status of pods**:
   ```bash
   kubectl get pods
   ```

2. **Deploy an application using Helm**:
   ```bash
   helm install sbdemo03 ./sbdemo03
   ```

3. **Describe a specific pod and view detailed events**:
   ```bash
   kubectl describe pod sbdemo03-counter
   ```

4. **View all events in the cluster**:
   ```bash
   kubectl get events
   ```

5. **Filter events for a specific pod**:
   ```bash
   kubectl get events --field-selector involvedObject.name=sbdemo03-counter
   ```

6. **Delete the application from the cluster**:
   ```bash
   helm delete sbdemo03
   ```

---

### **Conclusion**

In this demo, we explored how to retrieve and filter **pod events** in Kubernetes using `kubectl`. These events are crucial for troubleshooting issues in your pods, such as startup failures, image pulling problems, or resource constraints. By using simple commands like `kubectl describe` and `kubectl get events`, we can quickly diagnose issues and ensure our applications are running as expected.

## Collecting Application Log Info Using Fluentd

### Using Fluentd for Log Collection in Kubernetes

In this demo, we’re going to use **Fluentd** to collect log data from an application running on **Azure Kubernetes Service (AKS)**. Fluentd is part of the **EFK stack** (Elasticsearch, Fluentd, Kibana), which is a common logging solution used in Kubernetes environments. In this demo, we'll focus on Fluentd and how it collects logs from our Kubernetes application and sends them to Elasticsearch for storage and visualization.

---

### **1. Setting Up the Environment**

- **Step 1: Navigate to the Working Directory**  
   First, make sure you're in the `C:\demo` folder (or your project directory). This is where we've stored the demo files.
   ```powershell
   cd C:\demo
   ```

- **Step 2: Install the Application Using Helm**  
   We'll deploy an application to Kubernetes using **Helm**, a package manager for Kubernetes. The Helm chart we're using has components for the **EFK stack**. To install the Helm chart:
   ```powershell
   helm install sbdemo03efk ./sbdemo03efk
   ```
   This will deploy the EFK stack and the sample application into the Kubernetes cluster.

---

### **2. Exploring the Application and Fluentd Configuration**

The application we’ll be using is a simple app that prints the current date to `stdout` every second. Since logs are written to `stdout`, we can capture these logs using **Fluentd**.

- **Step 1: Explore the Application Code**  
   Open the application files in **Visual Studio Code** to review the configurations:
   ```powershell
   code sbdemo03efk
   ```

   - Open the **templates/sbdemo03efk-app.yaml** file:
     - **Namespace**: The application is deployed in the `sbdemo03efk` namespace.
     - **Pod Configuration**: The pod simply echoes the current date and an indexer every second to `stdout`, which means its logs are easily capturable.
   
   - Open the **sbdemo03efk-namespace.yaml** file:
     - This file defines the namespace `sbdemo03efk` in which the application and Fluentd will run.

   - Open the **sbdemo03efk-fluentd.yaml** file:
     - **Service Account**: Defines a `fluentd` service account.
     - **Cluster Role**: Fluentd is given `get`, `list`, and `watch` permissions for Kubernetes resources like `pods` and `namespaces`.
     - **DaemonSet**: This is where we define the **Fluentd DaemonSet**, which ensures that Fluentd is running on each node in the cluster.
     - **Fluentd Configuration**:
       - The logs will be pulled from the standard output (`stdout`) of the containers in the `sbdemo03efk` namespace.
       - Fluentd is configured to send these logs to **Elasticsearch** running within the same Kubernetes cluster.

     **Key Configuration Lines**:
     ```yaml
     FLUENT_ELASTICSEARCH_HOST: "elasticsearch.sbdemo03efk.svc.cluster.local"
     FLUENT_ELASTICSEARCH_PORT: "9200"
     FLUENT_CONTAINER_TAIL_PARSER_TYPE: "/^(?<time>.+) (?<stream>stdout|stderr) [^ ]* (?<log>.*)$/"
     ```
     - This configures Fluentd to send logs to the Elasticsearch instance at `elasticsearch.sbdemo03efk.svc.cluster.local:9200`.
     - The regular expression (`FLUENT_CONTAINER_TAIL_PARSER_TYPE`) is crucial because it tells Fluentd how to parse the logs from `stdout`.

---

### **3. Deploying and Validating the Application**

- **Step 1: Check Pods in the Namespace**  
   Once the Helm chart is deployed, verify that the pods are running in the `sbdemo03efk` namespace:
   ```bash
   kubectl get pods --namespace=sbdemo03efk
   ```

   You should see multiple pods:
   - **app**: The application pod that outputs logs.
   - **es-cluster-0**: The Elasticsearch pod.
   - **fluentd**: The Fluentd pod collecting logs.
   - **kibana**: The Kibana pod (for visualizing the logs, though we'll focus on Fluentd for now).

- **Step 2: Check the Application Logs**  
   Check the logs of the application to ensure it’s generating log data:
   ```bash
   kubectl logs app --namespace=sbdemo03efk
   ```
   You should see output similar to:
   ```
   2024-11-14 09:00:00 indexer-001
   2024-11-14 09:00:01 indexer-001
   2024-11-14 09:00:02 indexer-001
   ...
   ```

   This confirms that the application is generating logs and outputting them to `stdout`.

---

### **4. Fluentd in Action**

If Fluentd is correctly configured, it should now be collecting these logs and sending them to **Elasticsearch**. Here's how it works:

- **Log Collection**: Fluentd collects logs from the `stdout` of your pods in the `sbdemo03efk` namespace.
- **Log Shipping**: Fluentd ships these logs to Elasticsearch using the configuration we defined.
- **Log Storage**: The logs are stored in Elasticsearch, ready for indexing and searching.

---

### **5. Troubleshooting and Verification**

- **Step 1: Check Fluentd Logs**  
   If you want to ensure Fluentd is working as expected, you can check the logs of the Fluentd pod:
   ```bash
   kubectl logs fluentd-gmj9h --namespace=sbdemo03efk
   ```
   This should show you logs related to Fluentd’s activities, such as the logs it has processed.

- **Step 2: Verify Elasticsearch**  
   You can also check Elasticsearch to ensure logs are being indexed correctly. We’ll go over that in more detail in the next demo, but for now, you can use `kubectl` to check the Elasticsearch pod's logs:
   ```bash
   kubectl logs es-cluster-0 --namespace=sbdemo03efk
   ```

---

### **6. Cleaning Up**

After you’ve verified that everything is working, it’s important to clean up your resources:

- **Delete the Helm Release**:
   ```bash
   helm delete sbdemo03efk
   ```

This will remove the Helm release, along with all the associated Kubernetes resources like the pods, deployments, and services.

---

### **Summary of Key Commands**

1. **Install Helm Chart**:
   ```bash
   helm install sbdemo03efk ./sbdemo03efk
   ```

2. **Check Pods in Namespace**:
   ```bash
   kubectl get pods --namespace=sbdemo03efk
   ```

3. **Check Application Logs**:
   ```bash
   kubectl logs app --namespace=sbdemo03efk
   ```

4. **Check Fluentd Logs**:
   ```bash
   kubectl logs fluentd-gmj9h --namespace=sbdemo03efk
   ```

5. **Clean Up**:
   ```bash
   helm delete sbdemo03efk
   ```

---

### **Conclusion**

In this demo, we’ve set up Fluentd within a Kubernetes cluster to collect and ship logs from a sample application. We explored how Fluentd is configured to parse logs from `stdout` and send them to Elasticsearch, forming part of the EFK stack. We also verified the setup by checking the logs of the application and Fluentd pod. In the next demo, we'll focus on Elasticsearch for log storage and visualization.

## Monitoring Kubernetes Apps with Elasticsearch

### Monitoring a Kubernetes Application Using Elasticsearch

In this demo, we’ll build on our previous setup, where we used **Fluentd** to collect logs from a sample Kubernetes application. Now, we’re going to focus on **Elasticsearch** and configure it to store the logs coming in from **Fluentd**. Elasticsearch is a powerful search engine that stores and indexes logs, making them accessible for querying and analysis.

---

### **1. Setting Up Elasticsearch in Kubernetes**

We need to install and configure Elasticsearch in our Kubernetes cluster to store logs coming from **Fluentd**.

- **Step 1: Navigate to the Project Folder**  
   As in the previous demo, make sure you're in the `C:\demo` folder or your project directory:
   ```powershell
   cd C:\demo
   ```

- **Step 2: Open the Code Files**  
   Let's open the sample code we’ve been working with. In this demo, we’ll look at the `sbdemo03efk` folder, which includes the Kubernetes YAML files for setting up Elasticsearch.

   Open the folder in **VS Code**:
   ```powershell
   code sbdemo03efk
   ```

---

### **2. Configuring the Elasticsearch Service**

We’ll start by looking at the **Elasticsearch service** definition.

- **File: `sbdemo03efk-es-svc.yaml`**
   - **Namespace**: Just like before, Elasticsearch is deployed in the `sbdemo03efk` namespace.
   - **Service Type**: It’s defined as a **headless service** (by setting `clusterIP: None`). This is useful for stateful applications like Elasticsearch that need stable network identities across pods.
   - **Ports**: We expose two ports:
     - **9200**: The REST API for interacting with Elasticsearch.
     - **9300**: For internal node-to-node communication in a multi-node Elasticsearch cluster.

   Here's an example snippet of the service configuration:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: elasticsearch
     namespace: sbdemo03efk
   spec:
     ports:
       - port: 9200
         targetPort: 9200
       - port: 9300
         targetPort: 9300
     selector:
       app: elasticsearch
     clusterIP: None
   ```

---

### **3. Configuring the Elasticsearch StatefulSet**

The **StatefulSet** ensures that Elasticsearch pods get stable identities and persistent storage.

- **File: `sbdemo03efk-es-statefulset.yaml`**
   - **StatefulSet**: We use a StatefulSet because Elasticsearch needs persistent storage that survives pod restarts.
   - **Replicas**: For this demo, we're setting the replica count to **1**. For production, you'd want to have more replicas to distribute load and ensure high availability.
   - **Ports**: We expose ports 9200 (REST API) and 9300 (inter-node communication) as before.
   - **Image**: We're using Elasticsearch version **7.2.0** for this demo.

   Here's the StatefulSet configuration for Elasticsearch:
   ```yaml
   apiVersion: apps/v1
   kind: StatefulSet
   metadata:
     name: es-cluster
     namespace: sbdemo03efk
   spec:
     serviceName: "elasticsearch"
     replicas: 1
     selector:
       matchLabels:
         app: elasticsearch
     template:
       metadata:
         labels:
           app: elasticsearch
       spec:
         containers:
         - name: elasticsearch
           image: docker.elastic.co/elasticsearch/elasticsearch:7.2.0
           ports:
             - containerPort: 9200
             - containerPort: 9300
           env:
             - name: cluster.name
               value: "k8s-logs"
             - name: discovery.seed_hosts
               value: "es-cluster-0.elasticsearch"
             - name: cluster.initial_master_nodes
               value: "es-cluster-0"
             - name: ES_JAVA_OPTS
               value: "-Xms512m -Xmx512m"
   ```

---

### **4. Configuring Fluentd to Send Logs to Elasticsearch**

As we saw in the previous demo, Fluentd is configured to collect logs from the Kubernetes pods and send them to Elasticsearch.

- **File: `sbdemo03efk-fluentd.yaml`**
   - **Environment Variables for Fluentd**: Fluentd is configured with the following environment variables:
     - **`FLUENT_ELASTICSEARCH_HOST`**: This points Fluentd to the Elasticsearch service (`elasticsearch.sbdemo03efk.svc.cluster.local`).
     - **`FLUENT_ELASTICSEARCH_PORT`**: We use port `9200` (as defined earlier in the service configuration).
   
   Example configuration from the `sbdemo03efk-fluentd.yaml`:
   ```yaml
   - name: FLUENT_ELASTICSEARCH_HOST
     value: "elasticsearch.sbdemo03efk.svc.cluster.local"
   - name: FLUENT_ELASTICSEARCH_PORT
     value: "9200"
   ```

---

### **5. Verifying Elasticsearch Deployment**

Once you've applied the configurations and deployed Elasticsearch, let’s verify if everything is working as expected.

- **Step 1: Check the Rollout Status of the StatefulSet**
   First, let's check if the **StatefulSet** for Elasticsearch has rolled out correctly:
   ```bash
   kubectl rollout status sts/es-cluster --namespace=sbdemo03efk
   ```

   This command will show you if the pod was successfully deployed. If everything is working, you’ll see a message saying "deployment succeeded."

- **Step 2: Set Up Port Forwarding**
   We need to expose the Elasticsearch service to the outside world (i.e., your local machine) for testing. We can do this using **kubectl port-forward**:
   ```bash
   kubectl port-forward es-cluster-0 9200:9200 --namespace=sbdemo03efk
   ```

   This command will forward requests from your local machine's port 9200 to the Elasticsearch pod inside Kubernetes.

- **Step 3: Access Elasticsearch from the Browser**
   Now open your browser and go to [http://localhost:9200](http://localhost:9200). You should see a response like this, which confirms that Elasticsearch is up and running:
   ```json
   {
     "name": "es-cluster-0",
     "cluster_name": "k8s-logs",
     "cluster_uuid": "xyz123",
     "version": {
       "number": "7.2.0",
       "build_flavor": "default",
       "build_type": "docker",
       "build_hash": "abc123",
       "build_date": "2024-11-14T10:00:00.000Z",
       "lucene_version": "8.4.0",
       "minimum_wire_compatibility_version": "6.8.0",
       "minimum_index_compatibility_version": "6.0.0"
     },
     "tagline": "You Know, for Search"
   }
   ```

   This confirms that Elasticsearch is running and accessible.

- **Step 4: Check Elasticsearch Cluster State**
   To verify that Elasticsearch is actually storing logs, append `/ _cluster/state` to the URL:
   ```
   http://localhost:9200/_cluster/state
   ```

   You should see details about the state of the Elasticsearch cluster, including nodes and indexes. If you're using Fluentd correctly, you should also see indexes for **Logstash** (or any other index name that Fluentd has configured).

---

### **6. Conclusion**

In this demo, we’ve gone over how to configure **Elasticsearch** in a Kubernetes environment to store log data coming from **Fluentd**. Here's a quick summary of what we've covered:

1. **Configured Elasticsearch** in Kubernetes using a **StatefulSet** to ensure persistent storage.
2. **Verified Elasticsearch** deployment using port forwarding and the REST API.
3. **Checked Elasticsearch indexes** to ensure logs from Fluentd are being stored properly.

In the next step, you can explore using **Kibana** to visualize the logs stored in Elasticsearch, which we’ll cover in a future demo.

## Logging Time Series Analytics Using Kibana

### Monitoring Logs with Kibana in Kubernetes

In this demo, we'll explore how to use **Kibana** to visualize the log data that was collected by **Fluentd** and stored in **Elasticsearch**. This builds on our previous demos where we set up an application to generate logs, captured those logs with Fluentd, and stored them in Elasticsearch. Now, we’re going to use Kibana to view those logs in a user-friendly, visual interface.

---

### **1. Setting Up Kibana in Kubernetes**

To get started, we'll configure Kibana to connect to Elasticsearch and visualize the log data.

- **Step 1: Navigate to Your Project Directory**  
   As in the previous demos, make sure you're in your project directory (`C:\demo`) in PowerShell:
   ```powershell
   cd C:\demo
   ```

- **Step 2: Open the Code in VS Code**  
   Let's open the code for the demo, which is stored in the `sbdemo03efk` folder:
   ```powershell
   code sbdemo03efk
   ```

   In **VS Code**, open the `sbdemo03efk-kibana.yaml` file to examine the Kubernetes YAML configuration for Kibana.

---

### **2. Configuring the Kibana Service and Deployment**

In the `sbdemo03efk-kibana.yaml` file, we’re creating both a **Kubernetes Service** and a **Deployment** to expose and run Kibana.

- **Kibana Service**:
   - The **Service** is named `kibana`, and it’s placed in the same namespace (`sbdemo03efk`) as the other components.
   - The service is exposed on **port 5601**, which is the default port Kibana uses.

   Here’s the YAML for the Kibana service:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: kibana
     namespace: sbdemo03efk
   spec:
     ports:
       - port: 5601
         targetPort: 5601
     selector:
       app: kibana
   ```

- **Kibana Deployment**:
   - We’re creating a **Deployment** for Kibana with a single replica. For a production setup, you might consider multiple replicas for high availability, but for this demo, one replica will suffice.
   - We are using the **Kibana Docker image** (`docker.elastic.co/kibana/kibana:7.2.0`).
   - We specify environment variables to tell Kibana where Elasticsearch is located (it uses the service name `elasticsearch` and port `9200`).
   - Kibana will be accessible on **port 5601**.

   Here’s the YAML for the Kibana deployment:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: kibana
     namespace: sbdemo03efk
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: kibana
     template:
       metadata:
         labels:
           app: kibana
       spec:
         containers:
           - name: kibana
             image: docker.elastic.co/kibana/kibana:7.2.0
             ports:
               - containerPort: 5601
             env:
               - name: ELASTICSEARCH_HOSTS
                 value: "http://elasticsearch:9200"
   ```

---

### **3. Accessing Kibana via Port Forwarding**

Now that we’ve configured Kibana, let’s access it from our local machine to visualize the logs stored in Elasticsearch.

- **Step 1: List the Running Pods**  
   Use `kubectl get pods` to check the pods running in the `sbdemo03efk` namespace and find the pod name for Kibana:
   ```bash
   kubectl get pods --namespace=sbdemo03efk
   ```

   Example output:
   ```bash
   NAME                                   READY   STATUS    RESTARTS   AGE
   app-xxxxxxxxxx-yyyyy                    1/1     Running   0          5m
   es-cluster-0                            1/1     Running   0          5m
   fluentd-xxxxxxxxxx-zzzzz               1/1     Running   0          5m
   kibana-56fd46c9c-k7qww                  1/1     Running   0          5m
   ```

- **Step 2: Port Forward Kibana**  
   Find the name of the Kibana pod (in this case, `kibana-56fd46c9c-k7qww`) and use port forwarding to access Kibana on your local machine:
   ```bash
   kubectl port-forward kibana-56fd46c9c-k7qww 5601:5601 --namespace=sbdemo03efk
   ```

   This command will forward port 5601 from the Kibana pod to your local machine.

- **Step 3: Open Kibana in Your Browser**  
   Open your web browser and navigate to `http://localhost:5601`. You should see the Kibana dashboard.

---

### **4. Configuring Kibana to Read Elasticsearch Data**

Once Kibana is accessible, let’s configure it to read the logs stored in Elasticsearch.

- **Step 1: Set Up the Index Pattern**  
   - In the Kibana UI, click on the **Discover** tab (the compass icon).
   - Since Kibana doesn’t know about the log data yet, it will prompt you to create an **index pattern** to match the data from Elasticsearch.
   - In the **Index pattern** field, type `logstash-*` to match the indices where Fluentd has stored the logs (Logstash is the default name for the index created by Fluentd).
   - Click **Next step**.

- **Step 2: Select the Timestamp Field**  
   - Kibana will ask you to choose a **timestamp field** to use for filtering and visualizing logs. Select `@timestamp` as the field for the time filter.
   - Click **Create index pattern** to finish the configuration.

---

### **5. Exploring and Filtering Logs in Kibana**

With Kibana now configured, let’s explore the logs that Fluentd has captured and stored in Elasticsearch.

- **Step 1: View Logs in the Discover Tab**  
   - Go back to the **Discover** tab in Kibana, and you should now see logs displayed in a **histogram** along with log details below.
   - You can see log data like the **timestamp**, **index**, and the actual log message generated by your application.

- **Step 2: Filter Logs for a Specific Pod**  
   - If you want to view logs for a specific pod, you can apply a filter. For example, to see logs from the `app` pod, type `kubernetes.pod_name:app` in the filter bar at the top.
   - This will narrow down the logs to just the ones coming from the `app` pod.

---

### **6. Conclusion**

In this demo, we configured **Kibana** to visualize logs stored in **Elasticsearch**, which were generated by our **application** and captured by **Fluentd**. Here’s a quick recap of what we did:

1. **Set up Kibana** in Kubernetes with a Service and Deployment.
2. **Accessed Kibana** using port forwarding to view the logs.
3. **Created an index pattern** in Kibana to connect it to Elasticsearch and visualize logs.
4. **Filtered logs** for a specific Kubernetes pod using Kibana's UI.

With Kibana set up, you can now easily monitor and analyze your application logs in real-time. This is a powerful setup for any Kubernetes-based application, especially when combined with **Fluentd** for log collection and **Elasticsearch** for log storage.

## Monitoring Kubernetes Logs Using the EFK Stack

### **Monitoring Kubernetes Logs with the EFK Stack (Elasticsearch, Fluentd, Kibana)**

In this demo, we’re going to show how to monitor and visualize **Kubernetes logs** using the **EFK stack**: **Elasticsearch**, **Fluentd**, and **Kibana**. This builds on our previous setup, where we configured the EFK stack to capture and visualize logs generated by an application running inside a Kubernetes cluster. In this demo, we’ll take it a step further and explore logs from Kubernetes itself, not just our app.

---

### **1. Accessing Kibana on Kubernetes**

To start, we need to access **Kibana**, which is running inside our Kubernetes cluster, to visualize the logs.

#### **Step 1: Check Running Pods**

Run the following command to list the running pods in your `sbdemo03efk` namespace (this is the namespace where we’ve deployed the EFK stack):

```powershell
kubectl get pods --namespace=sbdemo03efk
```

Example output:
```bash
NAME                                   READY   STATUS    RESTARTS   AGE
app-xxxxxxxxxx-yyyyy                    1/1     Running   0          5m
es-cluster-0                            1/1     Running   0          5m
fluentd-xxxxxxxxxx-zzzzz               1/1     Running   0          5m
kibana-56fd46c9c-k7qww                  1/1     Running   0          5m
```

Here, we can see the **Kibana pod** is running. Let’s use port forwarding to access it locally.

#### **Step 2: Port Forward to Kibana**

To forward Kibana’s port (5601) to your local machine, use the following command, replacing `kibana-56fd46c9c-k7qww` with the actual Kibana pod name:

```powershell
kubectl port-forward kibana-56fd46c9c-k7qww 5601:5601 --namespace=sbdemo03efk
```

Once this is done, you can access Kibana in your browser at `http://localhost:5601`.

---

### **2. Exploring Kubernetes Logs in Kibana**

Now that we have Kibana running locally, we’ll explore the **Kubernetes logs** stored in **Elasticsearch**.

#### **Step 1: Access the Discover Tab**

- In Kibana, click on the **Discover** icon in the left-hand menu (the compass icon).
- This takes you to the **Discover** page, where you can see logs from Elasticsearch.

#### **Step 2: Filter Logs by Application**

Earlier, we were viewing logs for our application. To do that, we applied a filter for our specific pod name. Let’s quickly revisit that:

- In the **Filter** field, type:
  ```text
  kubernetes.pod_name:app
  ```
  This will filter the logs to show only those generated by your application pod.

#### **Step 3: Viewing Logs Excluding the Application Pod**

What if we want to view logs that **don’t** relate to our application pod? Here’s how to do it:

- Modify the filter to:
  ```text
  not kubernetes.pod_name:app
  ```
  This will now show logs for all pods except for the `app` pod.

---

### **3. Filtering and Viewing Kubernetes System Logs**

The goal is to view logs generated by Kubernetes itself, not just our application. Here's how you can do that:

#### **Step 1: Filter Logs for the Kubernetes System**

To view logs generated by the Kubernetes system (e.g., from system components like the kubelet or controller manager), we can filter by the `kube-system` namespace:

- In the **Filter** field, type:
  ```text
  kubernetes.namespace_name:"kube-system"
  ```
  This will filter logs to show those related to the Kubernetes system, such as logs from the kubelet, scheduler, or other system services.

#### **Step 2: Viewing the Log Details**

- Scroll through the logs. You’ll see information about various Kubernetes components, such as the pod name, container name, container image, and many other metadata fields like `docker.container_id`, `kubernetes.host`, and `kubernetes.labels`.
- These logs can help you monitor the health and performance of your Kubernetes cluster.

#### **Step 3: Querying for Errors**

You can refine your search to find specific logs that might indicate issues. For example, to search for logs related to **errors**, we can filter by the `stderr` stream:

- In the **Filter** field, type:
  ```text
  stream:stderr
  ```
  This will show logs that were written to the standard error stream, which is often where error messages are logged.

#### **Step 4: Expanding Log Entries**

- Once you find an interesting log message, click on it to expand it.
- You’ll be able to see detailed information, such as:
  - **Timestamp**
  - **Log Level** (e.g., error, info)
  - **Container Info** (e.g., container image, container ID)
  - **Kubernetes Metadata** (e.g., pod name, namespace)

This detailed information is a result of **structured logging**, which makes it easier to analyze and troubleshoot Kubernetes issues.

---

### **4. Cleanup the EFK Deployment**

Once you’re done monitoring and troubleshooting, it’s important to clean up your deployment. Since we used **Helm** to deploy the application, we can also use Helm to clean up the resources.

#### **Step 1: Cleanup with Helm**

To remove the **EFK stack** and all the associated resources, run the following command in PowerShell:

```powershell
helm delete sbdemo03efk
```

This will delete all resources created by the Helm chart, including Elasticsearch, Fluentd, and Kibana.

---

### **5. Conclusion**

In this demo, we successfully:

1. Accessed **Kibana** running on a Kubernetes cluster using **port forwarding**.
2. Explored **Kubernetes logs** in Kibana, filtering logs by specific criteria such as pod name and namespace.
3. Used Kibana’s powerful filtering and querying capabilities to analyze logs from both our application and the **Kubernetes system**.
4. Performed cleanup of our **EFK stack** deployment using **Helm**.

This approach, using the **EFK stack**, makes it easy to monitor and troubleshoot **Kubernetes clusters** in real-time by centralizing log data in **Elasticsearch** and visualizing it in **Kibana**.

