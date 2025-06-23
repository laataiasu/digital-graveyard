---
date: 2001-01-01
---

# Introducing Apache Spark

## Apache Spark

### Big Data Characteristics

Big data refers to datasets with complex characteristics that challenge traditional data processing techniques. These characteristics can be summarized by the **Seven Vs**:
- **Volume**: The sheer amount of data (terabytes, petabytes).
- **Velocity**: The speed at which data is generated.
- **Variety**: The different types and sources of data.
- **Variability**: The inconsistency or fluctuating nature of data.
- **Veracity**: The uncertainty or trustworthiness of data.
- **Visualization**: The ability to understand and interpret large datasets.
- **Value**: The potential insights that can be extracted from data.

Given these complexities, processing big data typically requires more than a single machine. A **cluster of machines** is often needed to handle the data efficiently.

---

### Challenges of Processing Big Data

1. **Volume**: A large dataset (e.g., terabytes or petabytes) needs to be split into manageable chunks and stored across different machines in a cluster.
   
2. **Storage**: A **distributed storage system** tracks where each chunk of data is stored across nodes. This ensures that the data is accessible and can be efficiently processed.

3. **Parallel Processing**: To process the data quickly, it needs to be broken down into smaller tasks that can be run **in parallel** across different machines in the cluster.

4. **Cluster Management**: A **cluster manager** allocates resources across the cluster, ensuring tasks are distributed evenly. This helps in balancing workloads and optimizing resource usage.

---

### Key Components of Big Data Processing

- **Distributed Storage**: A system like the **Hadoop Distributed File System (HDFS)** stores and manages data across multiple nodes in a cluster. HDFS tracks where data chunks are located, both for input and intermediate results.

- **Parallel Processing**: The **MapReduce** programming model processes data in parallel across a cluster.
  - **Map phase**: The input data is processed in parallel, generating key-value pairs.
  - **Reduce phase**: The key-value pairs are aggregated to generate a final result.
  
Example: For word count, a large text document is split into chunks and distributed across the cluster. Each chunk is processed by a map task to count occurrences of words. Then, the results are shuffled and reduced to compute the final word count.

- **Cluster Manager**: **YARN (Yet Another Resource Negotiator)** monitors and manages cluster resources. It allocates CPU and memory to MapReduce tasks and ensures that both processing and storage tasks are balanced across the cluster.

---

### Apache Hadoop: The Core Framework

1. **HDFS**: Stores data across the cluster in chunks, facilitating distributed storage.
   
2. **MapReduce**: Processes data in parallel. 
   - The **Map phase** processes input data and generates key-value pairs.
   - The **Reduce phase** aggregates results from the Map phase.

3. **YARN**: Manages cluster resources, scheduling tasks based on available resources and monitoring the cluster’s health.

While powerful, Hadoop has limitations:
- Writing MapReduce code can be complex and unintuitive.
- Frequent reading/writing to disk (e.g., intermediate results stored in HDFS) can lead to performance bottlenecks due to slow I/O operations.
- Integrating Hadoop with newer use cases, such as machine learning, can be challenging.

---

### Apache Spark: An Alternative to Hadoop

Apache Spark builds on top of Hadoop, offering several key improvements:
- **In-Memory Processing**: Spark performs much of its data processing in memory, reducing the need for slow disk I/O operations.
- **Ease of Use**: Spark abstracts away the complexities of writing MapReduce code. Users can define tasks using higher-level APIs in languages like Python, Java, Scala, SQL, and R.
- **Speed**: Because of in-memory processing and optimization techniques, Spark offers **better performance** compared to traditional Hadoop MapReduce, particularly for iterative algorithms and machine learning workflows.
- **Integration with Other Technologies**: Spark integrates easily with tools like **MLlib** (machine learning) and **GraphX** (graph processing), making it a versatile option for a wide range of big data tasks.

---

### Apache Spark for Streaming Data

Spark provides an extension called **Spark Streaming**, which is particularly well-suited for processing **real-time data** (live streams or unstructured data). Spark's support for both **batch** and **stream processing** makes it a powerful tool for a wide range of big data applications.

---

### Key Benefits of Using Apache Spark

1. **Improved Performance**: Spark processes data in memory, which significantly reduces latency and increases throughput compared to Hadoop.
   
2. **Ease of Use**: With high-level APIs and language support (Python, Scala, Java, SQL, R), Spark simplifies the development of big data applications compared to the low-level MapReduce paradigm.

3. **Unified Platform**: Spark supports both **batch** and **streaming** data processing, making it versatile for a range of use cases, from batch analytics to real-time data processing.

4. **Integration with Machine Learning**: Spark's **MLlib** library and ability to process data in memory make it a strong platform for machine learning pipelines.

## Apache Spark Architecture

Apache Spark is an open-source, unified analytics engine designed for large-scale data processing. It is built on top of Apache Hadoop and supports both batch and streaming data on a single platform.

#### Clusters and Horizontal Scaling
- **Cluster**: Spark runs on a cluster of machines, enabling parallel data processing. A cluster is necessary to handle large-scale data and distribute tasks across multiple machines.
- **Horizontal Scaling**: Spark scales horizontally by adding more nodes to the cluster, rather than increasing the resources (CPU, memory) of individual nodes. This approach is cost-effective and easier to manage.
- **Hardware Requirements**: Spark does not require high-end hardware; it runs well on common machines. Thus, clusters can scale by adding more inexpensive nodes as needed.
- **Storage**: Spark is not limited to Hadoop's HDFS for storage. It can integrate with various storage systems like Apache Cassandra, Amazon S3, and local file systems, making it more flexible than Hadoop.
- **Development**: During development, Spark can use local file systems, which simplifies the process before scaling up to distributed systems.

#### Cluster Managers
Spark can link with various cluster managers to manage resources and execute tasks:
1. **Spark Standalone**: Built-in manager ideal for development and testing. It includes a web UI for monitoring but is not recommended for production.
2. **Hadoop YARN**: A resource manager that provides scalability and reliability for production environments.
3. **Apache Mesos**: A cluster manager for resource scheduling and allocation.
4. **Kubernetes**: Orchestrates Spark applications, providing another option for managing Spark clusters.

#### Spark Core and RDDs
- **Spark Core**: The foundational library of Spark, which includes interfaces for task dispatching, I/O operations, and data structures for managing distributed data.
- **RDD (Resilient Distributed Dataset)**: The primary data structure in Spark, RDDs represent distributed collections of objects that can be processed in parallel. RDDs enable fault tolerance and parallel computation across a cluster.

#### Spark's Data Abstractions: DataFrames
- **DataFrames**: An abstraction over RDDs, DataFrames allow structured data to be represented in rows and columns. They simplify working with both structured and semi-structured data and support SQL-like transformations.
- **Languages**: DataFrames can be used in multiple programming languages, including Java, Scala, Python, and R.
- **Data Sources**: Spark DataFrames integrate with various data sources like JSON, Parquet, Avro, and Hive. They can also connect to databases using JDBC or ODBC, facilitating integration with platforms like Tableau.
- **Optimizations**: DataFrames benefit from optimizations such as Catalyst and Tungsten, which improve query planning and execution efficiency.

#### Running a Spark Application
1. **Driver Program**: When a Spark application is launched, a driver program is created. The driver runs on the master node and manages the execution of tasks.
2. **SparkSession**: The entry point for Spark applications, encapsulating the various contexts (SparkContext, HiveContext, SQLContext). The session coordinates Spark's functionality, such as resource allocation and task execution.
3. **DAGScheduler**: Responsible for organizing the sequence of transformations (a Directed Acyclic Graph or DAG) that need to be applied to the data.
4. **Task Scheduler**: Manages individual tasks within a transformation and schedules them for execution.

#### Task Execution and Workers
- **Task Execution Flow**:
  - **DAG**: The transformations defined in the application are translated into a DAG, which is then split into execution stages.
  - **Stages**: Each stage represents a unit of work, which is further divided into tasks.
  - **Worker Nodes**: Tasks are executed on worker nodes in the cluster. Each worker runs one or more executors that process tasks in parallel.
- **Executors**: Executors are processes that run on worker nodes, responsible for executing the tasks assigned to them. Executors also handle data storage and caching.
- **Communication**: Worker nodes maintain communication with the master node, the cluster manager, and the SparkSession to receive tasks and report progress.

#### Key Points:
- Spark operates on clusters for parallel data processing and scalability.
- It uses **horizontal scaling** by adding nodes to the cluster rather than increasing the capabilities of individual nodes.
- Spark integrates with various storage systems, making it more flexible than Hadoop.
- **RDDs** and **DataFrames** are the primary abstractions for working with data, with DataFrames offering SQL-like capabilities.
- Spark applications are managed by a driver program, which schedules tasks and coordinates their execution across worker nodes.

## Structured Streaming in Apache Spark

#### Spark Streaming vs Structured Streaming
- **Spark Streaming**: Built on top of Spark RDDs and the DStream API, Spark Streaming processes live data as micro-batches. Each DStream represents a batch of data, and tasks are processed in discrete intervals, making it less suitable for low-latency requirements.
  
- **Structured Streaming**: A newer stream processing engine based on **Spark SQL** that provides higher-level abstractions, such as DataFrames, to process streaming data. Unlike Spark Streaming's micro-batching, Structured Streaming processes data continuously, offering better performance and lower latency.

#### Key Features of Structured Streaming
1. **DataFrames for Streaming**: 
   - Structured Streaming treats data as an **unbounded DataFrame** (an infinite table). This simplifies the stream processing workflow as DataFrames provide a higher-level API compared to RDDs.
   - You can perform **SQL-like operations** on streaming data using the DataFrame API, such as filtering, selecting, and aggregating, much like you would with static data.

2. **Exactly-Once Semantics**: 
   - Structured Streaming guarantees that data will only be processed once, even in the face of failures, which is crucial for ensuring data consistency.

3. **Low Latency**: 
   - By using continuous processing rather than micro-batches, Structured Streaming achieves **low-latency processing** with latencies as low as **one millisecond**.

4. **Time-based Operations**: 
   - You can perform operations based on **event time** (timestamps in the data), such as windowed aggregations or joins. This allows you to process time-sensitive data more effectively.

5. **Late Data Handling**: 
   - Spark allows you to handle **late data**—data that arrives after the expected processing window has passed—by configuring watermarking and windowing strategies.

#### Output Modes in Structured Streaming
Structured Streaming processes data in **micro-batches**, and the output is generated periodically based on a trigger (e.g., every minute). There are three main output modes to handle results:

1. **Append Mode**:
   - Only the **newly arrived data** (since the last trigger) is processed and written to the output. It is suitable for most stream processing scenarios where the output does not need to include historical data.
   - Example: Writing streaming data to a console or database.

2. **Complete Mode**:
   - All the data in the DataFrame is processed, including the **new data and the entire history**. This mode is typically used for aggregations where the output size is limited.
   - Example: Running aggregations like sum or count on streaming data and outputting the complete result.

3. **Update Mode**:
   - Updates both **newly arrived rows** and any **existing rows that have been updated** since the last trigger. This mode is suitable for situations where the data might change over time and needs to be reprocessed.
   - Example: Updating a rolling count of events.

#### Transformations in Structured Streaming
Structured Streaming supports a variety of **transformations** on streaming data:

1. **Selection and Projection**:
   - Filter or select specific columns or rows from the incoming stream. These are equivalent to **SQL SELECT** and **WHERE** operations.
   
2. **Aggregation**:
   - Perform **grouping** and **aggregation** on streaming data, such as counting or summing values over time windows.
   - Example: Aggregating user activity over a 5-minute window.

3. **Windowing**:
   - Apply time-based **window operations** to process data based on time intervals. You can define **event time windows** (based on timestamps) or **processing time windows** (based on when the data is processed).
   - Example: Aggregating events within a 10-minute time window.

4. **Joins**:
   - You can join multiple streaming DataFrames or join streaming data with static data. However, join operations on unbounded data can be challenging due to state management requirements.
   - Example: Joining two data streams based on a common key, such as customer IDs.

#### Limitations of Structured Streaming
While Structured Streaming simplifies many stream processing tasks, there are some operations that are not supported or are limited:

1. **Aggregations on Multiple Streams**: 
   - Structured Streaming does not support aggregating data across multiple streams.
   
2. **Limitations on `LIMIT` and `TOP N`**:
   - Operations like `LIMIT` and `TOP N` are not supported in Structured Streaming.

3. **Distinct Operations**:
   - The `DISTINCT` operation is not supported due to the challenges of maintaining unique values over an unbounded stream.

4. **Sorting**:
   - Sorting is supported only in **complete mode**, and only after performing an aggregation. Sorting without aggregation is not supported for streaming data.

5. **Outer Joins**:
   - Certain types of **outer joins** (e.g., left and right outer joins) are not supported due to the complexity of handling unbounded data.

#### Use Cases for Structured Streaming
Structured Streaming is highly suitable for **ETL pipelines**, where you can:
- **Extract** data from various sources (e.g., Kafka, files, databases).
- **Transform** the data using the DataFrame API.
- **Load** the transformed data into a destination like a database or data warehouse.

Structured Streaming's ability to integrate seamlessly with platforms such as **Kafka**, **NoSQL databases** (e.g., Cassandra), and **cloud storage** (e.g., Amazon S3) makes it a powerful tool for real-time data processing.

#### Example Use Case: Kafka Consumer
One common use case for Structured Streaming is reading data from a **Kafka topic**, performing transformations, and writing the results to a permanent storage system (e.g., **Apache Cassandra** or **Amazon S3**). 

1. **Input**: Read data from a Kafka stream.
2. **Transformation**: Apply various transformations using the DataFrame API, such as filtering, aggregation, or joining.
3. **Output**: Write the transformed data to a persistent storage system.

In this learning path, we will implement this Kafka-to-Cassandra pipeline using Structured Streaming.

#### Conclusion
Structured Streaming provides a modern, powerful approach to stream processing in Spark, offering:
- Low-latency, continuous processing.
- Easy-to-use DataFrame API.
- Fault tolerance and exactly-once processing semantics.
- Integration with streaming data sources like Kafka.

By leveraging Structured Streaming, Spark users can build efficient and scalable real-time applications with minimal effort.

## Downloading and Installing Spark

In this video, we walk through the process of installing **Apache Spark** and setting up a **PySpark** environment on your machine. Here’s a summary of the steps and key points mentioned:

### 1. **Check Python Version**
First, ensure that you have a version of Python installed on your system. The version recommended for this setup is **Python 3.x** (preferably **3.9.7**). You can check your Python version by running:
```bash
python --version
```

### 2. **Check Java Version**
Since **Apache Spark** runs on the **JVM (Java Virtual Machine)**, you'll need to have a compatible version of **Java** installed. As of this recording, **Spark** is compatible with **Java 1.8 through Java 11**, and you can check your Java version by running:
```bash
java -version
```

Make sure your **JAVA_HOME** environment variable points to the correct Java installation directory.

### 3. **Download Apache Spark**
To get Apache Spark:
- Navigate to the official [Apache Spark Downloads page](https://spark.apache.org/downloads.html).
- Choose the latest Spark version (e.g., **3.2.1** at the time of the recording).
- Select a **pre-built version for Hadoop 3.x** (which is common for modern setups).
- Download the `.tgz` file for the selected version.

### 4. **Unpack the Spark Distribution**
Once the download completes:
1. Copy the `.tgz` file to a directory on your machine (e.g., **~/Downloads**).
2. Extract the contents of the `.tgz` file:
   ```bash
   tar -xvzf spark-3.2.1-bin-hadoop3.2.tgz
   ```

### 5. **Set Up Environment Variables**
To make Spark easily accessible, you need to set the **SPARK_HOME** environment variable and update your **PATH**. Edit your **.bash_profile** (or **.bashrc** or **.profile** if you use a different shell):
```bash
nano ~/.bash_profile
```

Add the following lines:
```bash
export SPARK_HOME=~/spark-3.2.1-bin-hadoop3.2
export PATH=$SPARK_HOME/bin:$PATH
```

This will ensure that the **Spark binaries** (like `spark-submit`, `pyspark`, etc.) are available in your terminal.

### 6. **Apply the Changes**
After editing the **.bash_profile** file, apply the changes by running:
```bash
source ~/.bash_profile
```

### 7. **Launch PySpark Shell**
To confirm that Spark is installed and running properly, start the **PySpark shell** by running:
```bash
pyspark
```

This should initialize a **SparkSession** and display some startup messages, including the Spark context (`sc`) and web UI URL (`localhost:4040`), which you can access through your browser to monitor your Spark jobs.

### 8. **Verify Spark Context**
Once the PySpark shell is ready, verify that the **SparkContext** is accessible by simply typing:
```bash
sc
```

If everything is set up correctly, you'll see output similar to:
```bash
<SparkContext master=local[*] appName=PySparkShell>
```

### 9. **Exit the PySpark Shell**
When you're finished, you can exit the PySpark shell by typing:
```bash
exit()
```

### Summary:
- You’ve installed **Apache Spark** and set it up to use with **PySpark**.
- Your Spark environment is configured, and you’ve tested it by running the PySpark shell and accessing the Spark context.
- The next step is to set up a **Spark cluster**, which will be covered in the next video.

With this setup, you're now ready to build and execute **Spark applications** using Python.

## Deploying a Spark Cluster

In this video, we learn how to set up a **Spark cluster** in **standalone mode**. Here’s a breakdown of the steps demonstrated:

### 1. **Navigate to Spark Home Directory**
We start by navigating to the **Spark Home** directory, where the **bin** and **sbin** directories are located. The **bin** directory contains executable utilities like `pyspark`, `spark-submit`, etc., and the **sbin** directory contains the scripts for managing Spark clusters.

```bash
cd $SPARK_HOME
ls -l
```

### 2. **Start the Spark Master**
The first step in setting up a Spark cluster is to launch the **Spark master**. The master is responsible for managing and coordinating the cluster. In the **sbin** directory, we find the script `start-master.sh` that launches the master node.

```bash
cd sbin
./start-master.sh
```

After running this command, Spark will start the master instance, and you’ll see some logs showing the master’s status. 

### 3. **Access Spark Web UI**
Once the Spark master is running, you can monitor the cluster via the **Spark Web UI**. By default, the Spark Web UI is accessible at **http://localhost:8080**. 

On the Web UI:
- You'll find details about the master node, including its URL (`spark://<hostname>:7077`).
- **Alive Workers** will initially show as 0, as no workers are running yet.
- Information about the available memory and cores for the cluster will be displayed.

### 4. **Start a Spark Worker**
Next, we need to start a **Spark worker** to do the actual computations. This worker node connects to the master node and performs tasks distributed by the master.

To start a worker, run the `start-worker.sh` script and point it to the master’s URL (the address shown in the Spark Web UI):
```bash
$SPARK_HOME/sbin/start-worker.sh spark://<master-node-url>:7077
```

Once the worker is started, the Web UI will update to show the worker as **Alive** under the **Workers** tab. You can also see how many **cores** and **memory** the worker has available.

### 5. **Monitor the Worker and Executors**
By clicking on the worker’s ID in the **Web UI**, you can access detailed information about the worker’s **executors** (tasks being run by the worker), including:
- Executor ID
- Cores and memory allocated
- Job details and logs

The Web UI for the worker is typically accessible at **http://<worker-ip>:8081**.

### 6. **Check Running JVM Processes with `jps`**
To confirm the Spark processes running on your machine, you can use the `jps` command. This command lists active Java processes, including the **Master** and **Worker** processes for Spark. Example output:
```bash
$ jps
Master
Worker
```

### 7. **Running Multiple Workers**
You can add more workers to the cluster by running the `start-worker.sh` script again, but you must ensure the workers are on different machines or nodes. Running multiple workers on the same machine can lead to resource conflicts.

To stop a worker, you can use the `stop-worker.sh` script:
```bash
$SPARK_HOME/sbin/stop-worker.sh spark://<master-node-url>:7077
```

Once a worker is stopped, the **Web UI** will show the worker as **Dead**.

### 8. **Stop the Spark Master**
To terminate the entire cluster, you can stop the master node with the `stop-master.sh` script:
```bash
$SPARK_HOME/sbin/stop-master.sh
```

Once the master is stopped, the **Web UI** will no longer be accessible, and running the `jps` command will show that neither the master nor the worker processes are active.

### 9. **Summary**
- We launched a **Spark master** and connected a **worker** to it in **standalone mode**.
- We monitored the cluster's performance and resources through the **Web UI** and **jps**.
- We also learned how to add, monitor, and stop **worker nodes** in the cluster.

### Next Steps:
In the next video, we will explore running jobs on a Spark cluster and how to monitor the execution of those jobs using the Web UI.

---

By setting up the **master** and **worker** nodes in Spark, you now have a basic Spark cluster running on your local machine (or across multiple machines). This cluster is ready for running distributed Spark applications.

## Launching a Spark Job

### Setting Up Spark and Kafka Integration

1. **Directory Structure**  
   In this learning path, we are integrating Apache Kafka with Apache Spark. The working directory is called `ApacheKafka`, which contains a subfolder `code`. Inside `code`, there is a `datasets` directory with a file called `insurance.csv`. This file contains data that can be loaded into a Spark DataFrame for processing.

2. **Accessing the Dataset**  
   You can access the `insurance.csv` file either from the course materials or by downloading it from Kaggle. This dataset will be used for Spark application processing.

3. **Loading the CSV into a Spark DataFrame**  
   We will load this CSV file into a Spark DataFrame. The `SparkSession` object, accessible via the `spark` variable, is used as the entry point for this task.

4. **Setting Up Spark Cluster**  
   Before running Spark applications, we need to start a Spark cluster:
   - Start the Spark master node:  
     ```bash
     $SPARK_HOME/sbin/start-master.sh
     ```
   - Start the worker node:  
     ```bash
     $SPARK_HOME/sbin/start-worker.sh spark://<master-url>:7077
     ```

5. **Verifying the Cluster**  
   After starting the master and worker nodes, you can verify that they are running by checking the Spark Web UI at:
   - **Master UI**: `http://localhost:8080`
   - **Worker UI**: `http://localhost:8081`

   The Master UI shows the status of workers, running applications, and memory usage. The Worker UI shows detailed information about the worker node's resources and active executors.

6. **Launching PySpark**  
   Once the cluster is running, you can launch a PySpark session to interact with Spark. In the shell, execute the following command to start PySpark:
   ```bash
   $SPARK_HOME/bin/pyspark --master spark://<master-url>:7077
   ```

   This command starts PySpark, pointing it to the master node of the cluster. You can also configure the number of executors and memory allocation:
   - Set the number of executors:  
     ```bash
     --num-executors 5
     ```
   - Set the driver memory:  
     ```bash
     --driver-memory 2g
     ```

7. **Spark Web UI During Execution**  
   Once PySpark is running, the Spark Web UI will be updated with information about the application, including:
   - **Jobs tab**: Shows the status of jobs.
   - **Stages tab**: Displays stages of jobs in the application.
   - **Executors tab**: Displays detailed information about the executors.

   The **Executors tab** shows the status of executors and tasks, including active, failed, and completed tasks. You can also check the **Environment tab** for configuration details.

8. **Creating a DataFrame from CSV**  
   To load data from `insurance.csv` into a DataFrame, use the `SparkSession.read` method. Set the `header` option to `true` to indicate that the file contains a header row:
   ```python
   insurance_df = spark.read.option("header", "true").csv("path/to/insurance.csv")
   ```

   This command reads the CSV file and returns a DataFrame, which is a distributed collection of data organized in rows and columns.

9. **Monitoring Job Execution**  
   Once the DataFrame is created, you can track the job execution in the Spark Web UI. The job will be listed under the **Jobs** tab, showing the duration, number of tasks, and job status. The **Event Timeline** gives you a detailed view of the execution timeline, including when executors were added and when the CSV processing job was executed.

10. **Job and Task Details**  
   After the DataFrame is loaded, the **Spark Jobs** page will show a job with the status of "Succeeded" and the duration (e.g., 3 seconds). The **Executors** tab shows how long each executor spent processing the data, including task details like "Active", "Failed", and "Completed" tasks.

---

By following these steps, you can set up a Spark cluster, load data into a DataFrame, and monitor the execution of Spark jobs and tasks through the Spark Web UI. Next, we will explore Spark transformations and how they translate into Spark jobs.

## Monitoring Spark Apps with the Web UI

### Executing and Monitoring Spark Jobs

1. **Displaying DataFrame Contents**  
   In the previous session, we loaded a CSV file into a Spark DataFrame. Now, we will spawn more jobs to explore the DataFrame further and monitor them using the Spark UI.

   - To check the contents of the `insurance_df` DataFrame and confirm that it was populated correctly, use the following command:
     ```python
     insurance_df.show(5)
     ```
     This command will display the first 5 rows of the DataFrame.

     The output will show columns like `age`, `sex`, `bmi`, `children`, `smoker`, `region`, and `charges`, confirming that the data is loaded correctly.

2. **Running a Select and Filter Operation**  
   Next, let's create another job by selecting specific columns and filtering the data. We want to display the columns `age`, `bmi`, and `charges` for rows where the `charges` column is greater than 20,000:
   ```python
   insurance_df.select('age', 'bmi', 'charges') \
       .where(insurance_df.charges > 20000) \
       .show()
   ```
   This query selects the `age`, `bmi`, and `charges` columns and filters the rows where the `charges` are greater than 20,000. The results will show a subset of the data.

   In the output, PySpark will display the first 20 rows by default, but you can adjust this by passing a specific number to `.show()`.

3. **Grouping and Aggregating Data**  
   Now, let's perform a group-by operation on the data to compute the average charges per gender. The operation involves:
   - Selecting the columns `sex`, `age`, and `charges`.
   - Grouping by the `sex` column.
   - Aggregating the `charges` column by calculating the average:
     ```python
     insurance_df.select('sex', 'age', 'charges') \
         .groupBy('sex') \
         .agg({'charges': 'avg'}) \
         .show(5)
     ```
   This will output the average charges for each gender in the DataFrame, with the `avg(charges)` displayed alongside the `sex`.

4. **Monitoring Jobs in Spark Web UI**  
   After running these transformations, multiple jobs will be created. To monitor their execution:
   - Go to the **Application UI** in the Spark Web UI. Initially, there was one job running, but after performing the operations, you will see multiple jobs created—one for each transformation (`show`, `select`, `where`, etc.).
   - Refresh the page to view the updated list of jobs. You will see a total of **five jobs**, with descriptions like `showString` for each of the transformations.

   The **Event Timeline** in the UI will show when these jobs started and finished. Some jobs may run sequentially, while others may be split into multiple stages, depending on the complexity of the operation.

5. **Spark Master and Worker UI**  
   - In the **Spark Master UI** (`http://localhost:8080`), you will notice that the application is still in the **RUNNING** state. The **Running Applications** table shows the status of each job, including memory and CPU usage.
   - After executing all the jobs, the PySparkShell application will move to the **Completed Applications** section in the Master UI.

   In the **Worker UI** (`http://localhost:8081`), the running executor will be listed under the **Running Executors** section while the application is active. Once the application finishes, the executor will be moved to the **Finished Executors** section.

6. **Terminating the Spark Application**  
   To stop the running PySparkShell application, exit the PySpark shell by typing:
   ```python
   exit()
   ```
   This will terminate the application and return you to the shell prompt.

   - After exiting, refresh the **Application UI** and **Master UI**. The application should no longer be listed under running applications, and it will appear in the **Completed Applications** section with its final state as **FINISHED**.

7. **Stopping Spark Cluster**  
   To perform cleanup and stop all running Spark components (workers and master nodes), execute the following command:
   ```bash
   $SPARK_HOME/sbin/stop-all.sh
   ```
   The message confirming that the master is being stopped will appear in the terminal, indicating that all Spark processes have been terminated.

---

### Summary of Operations
- **Job Creation**: Each Spark operation (e.g., `.show()`, `.select()`, `.groupBy()`) creates a new job.
- **UI Monitoring**: The Spark Web UI allows you to track job progress, memory usage, executor status, and job completion.
- **Job Complexity**: Some operations, like `groupBy` and `agg`, may require multiple stages, resulting in multiple jobs being created.
- **Application Termination**: Once all tasks are complete, you can terminate the application and stop the Spark cluster.

By understanding how Spark jobs are spawned and how to monitor them in the Web UI, you can better manage the execution of Spark applications.

## Configuring a Spark Cluster

### Exploring Spark Configurations and Running Spark in Standalone Mode

In this demo, we will walk through configuring Spark settings and running Spark in both **Standalone mode** and **Local mode**. We'll also explore how to monitor the effects of these configurations through the Spark UI.

---

### Step 1: Exploring Spark Configuration Files

1. **Navigate to the Configuration Directory**  
   To start configuring Spark, we need to go to the `conf` directory inside the Spark installation. From the terminal:
   ```bash
   cd $SPARK_HOME/conf
   ```
   
2. **Listing Configuration Files**  
   Once in the `conf` directory, you will likely see several template files, which are just examples and need to be renamed and modified to become active configuration files:
   ```bash
   ls -l
   ```
   
   Look for the template files, like `spark-env.sh.template`.

3. **Copying Template to Active Configuration**  
   To enable the `spark-env.sh` configuration file, copy it to `spark-env.sh`:
   ```bash
   cp spark-env.sh.template spark-env.sh
   ```
   This will create an actual configuration file that Spark will use.

4. **Editing the Configuration File**  
   Open the new `spark-env.sh` file in a text editor (e.g., `nano`):
   ```bash
   nano spark-env.sh
   ```

---

### Step 2: Modifying Configuration Settings

In the `spark-env.sh` file, there are a variety of configurations that you can modify to customize Spark's behavior.

1. **SPARK_MASTER_HOST**  
   This setting binds the Spark Master to a specific IP address or hostname, which is useful when there is a public IP available or when working in a distributed setting.
   ```bash
   SPARK_MASTER_HOST=localhost
   ```

2. **SPARK_WORKER_CORES**  
   This sets the number of CPU cores available for Spark workers. In the example, we allocate 2 cores:
   ```bash
   SPARK_WORKER_CORES=2
   ```

3. **SPARK_WORKER_MEMORY**  
   This configures the amount of memory available for Spark workers. Here, we assign 2 GB of memory:
   ```bash
   SPARK_WORKER_MEMORY=2g
   ```

4. **SPARK_WORKER_PORT**  
   You can also specify the port on which the Spark worker will listen. For this example, we set it to port 10001:
   ```bash
   SPARK_WORKER_PORT=10001
   ```

   Once you've made these changes, save and close the file.

---

### Step 3: Starting Spark in Standalone Mode

Now that we've configured Spark, we can start the Spark cluster in **Standalone mode**.

1. **Starting the Spark Master**  
   To start the Spark Master, run the following command:
   ```bash
   $SPARK_HOME/sbin/start-master.sh
   ```

   This will start the master node of the Spark cluster, and it will be available at `spark://localhost:7077`.

2. **Starting the Spark Worker**  
   Next, we start the worker node, which will connect to the Spark Master. Be sure to specify the correct master URL:
   ```bash
   $SPARK_HOME/sbin/start-worker.sh spark://localhost:7077
   ```

   This will launch a worker that will communicate with the master node on the specified port (7077 in this case).

---

### Step 4: Verifying Configurations via Spark UI

Once both the master and worker nodes are running, you can verify that the configurations have taken effect through the **Spark Web UI**.

1. **Accessing the Spark Master UI**  
   Open a browser and go to the Spark Master UI at:
   ```
   http://localhost:8080
   ```
   Here, you should see the status of the master node, including details about the **number of alive workers**, **cores in use**, **memory in use**, and more.

   Under the **Workers** section, you will see details about the connected worker, including:
   - **Worker ID**
   - **Address** (which should show `10001` as the port, reflecting the change made in `spark-env.sh`)
   - **Cores** and **Memory** allocated to the worker, based on the configurations set earlier (2 cores, 2 GB memory).

   Example:
   ```
   Worker Id: worker-1
   Address: 192.168.0.104:10001
   Cores: 2
   Memory: 2g
   ```

2. **Accessing the Spark Worker UI**  
   Click on the worker link to view more details about the worker node. You'll be taken to the **Spark Worker UI**, where you can monitor active executors, resource allocation, and other metrics:
   ```
   http://192.168.0.104:10001
   ```

   If there are no executors running, you can go back to the **Spark Master UI** and see if any jobs have started.

---

### Step 5: Understanding Standalone Mode vs. Cluster Mode

In **Standalone mode**, Spark uses its built-in cluster manager, which works well for development and testing environments. However, in production environments, you might want to use a more scalable cluster manager like **YARN**, **Mesos**, or **Kubernetes**, especially when you're dealing with larger clusters and more complex workloads.

---

### Step 6: Next Steps

In the next demo, we will focus on running a **Spark streaming application**. This will give us the opportunity to monitor the flow of data in real-time and how Spark processes streaming data. For now, we've established how to configure Spark in standalone mode and have confirmed the changes through the Spark Web UI.

--- 

### Summary of Key Concepts

1. **Spark Configuration**:
   - Modify `spark-env.sh` to set key configurations like master host, worker cores, and memory.
   - Start Spark Master and Worker in standalone mode using `start-master.sh` and `start-worker.sh`.
   
2. **Standalone Mode**:
   - Standalone mode uses Spark's built-in cluster manager, suitable for small-scale clusters and development environments.
   - In production, consider using a cluster manager like YARN, Mesos, or Kubernetes.

3. **Spark UI**:
   - Use the Spark Master UI and Worker UI to monitor resources, workers, and active jobs.

These steps provide a foundation for configuring and running Spark in standalone mode and monitoring the results via the Spark Web UI.

## Building a Spark Streaming App

### Setting Up the Environment for Spark Streaming

1. **Spark Cluster in Standalone Mode**  
   - The Spark Master URL (`spark://localhost:7077`) provides details like:  
     - Alive workers, cores in use, memory in use, resources, applications, and status.

2. **Navigating the Workspace Folder**  
   - Use the shell to navigate to your workspace directory:  
     ```bash
     cd Projects/Skillsoft/ApacheKafka/code
     ```

3. **Setting Up Datasets**  
   - Two explorer windows: `datasets` and `code`.
   - The `datasets` folder will store CSV files.  
     - Example files: `insurance_1.csv`, `insurance_2.csv`, `insurance_3.csv` (chunks of the original `insurance.csv`).

4. **Starting the PySpark Application**  
   - Use `spark-submit` to launch Spark applications.
   - Verify options with `spark-submit --help` to explore various configuration options.

---

### Streaming Application Code

**File**: `streaming_pyspark.py`

#### 1. **Importing Required Libraries**  
   - Import `SparkSession` from `pyspark.sql`:
     ```python
     from pyspark.sql import SparkSession
     ```

#### 2. **Schema Definition**  
   - Define a schema using `StructType` and `StructField` for the CSV columns:
     ```python
     from pyspark.sql.types import *

     schema = StructType([
         StructField("age", IntegerType(), False),
         StructField("sex", StringType(), False),
         StructField("bmi", DoubleType(), False),
         StructField("children", IntegerType(), False),
         StructField("smoker", StringType(), False),
         StructField("region", StringType(), False),
         StructField("charges", DoubleType(), False)
     ])
     ```

#### 3. **Setting Up SparkSession**  
   - Check if the script is being run directly (`if __name__ == "__main__"`).
   - Initialize `SparkSession`:
     ```python
     sparkSession = SparkSession.builder.appName("Spark Streaming").getOrCreate()
     sparkSession.sparkContext.setLogLevel("ERROR")
     ```

#### 4. **Reading Streaming Data**  
   - Use `sparkSession.readStream` to read CSV files from the `datasets` directory:
     ```python
     fileStreamDf = sparkSession.readStream \
         .option("header", "true") \
         .schema(schema) \
         .csv("datasets/")
     ```

#### 5. **Checking the Stream**  
   - Verify that the stream is set up correctly:
     ```python
     print("Is the stream ready?", fileStreamDf.isStreaming)
     print("Stream schema", fileStreamDf.printSchema())
     ```

#### 6. **Data Transformation**  
   - Perform transformations on the incoming data:
     - Group by `sex` and `smoker`, aggregate the average `charges`.
     - Rename the aggregated column:
       ```python
       selectedDf = fileStreamDf.groupBy("sex", "smoker") \
           .agg({"charges": "avg"}) \
           .withColumnRenamed("avg(charges)", "Average Charges")
       ```

#### 7. **Writing to Console**  
   - Write the transformed data to the console:
     ```python
     query = selectedDf.writeStream \
         .outputMode("complete") \
         .format("console") \
         .option("numRows", 30) \
         .start()
     ```

#### 8. **Running the Streaming Application**  
   - Ensure the stream continues running until explicitly terminated:
     ```python
     query.awaitTermination()
     ```

---

### Key Concepts & Functions

1. **SparkSession**:  
   - The entry point for interacting with Spark, allowing us to read and process data.

2. **Streaming DataFrame**:  
   - A DataFrame that continuously receives new data, like streaming CSV files.

3. **`readStream` vs `read`**:  
   - `readStream` is used to read continuously streaming data, while `read` is for batch processing.

4. **Output Modes**:
   - `complete`: Outputs the complete result for each batch.

5. **Transformations**:
   - Grouping and aggregation can be performed on streaming data just like batch data.

6. **Termination**:  
   - Use `awaitTermination` to keep the streaming job running until manually stopped.

---

### References

- **PySpark Documentation**:  
  [Spark Python API](https://spark.apache.org/docs/latest/api/python/reference/api/)

## Running Apps on a Standalone Cluster

### Streaming PySpark Application Setup

#### File Structure
- **Directories**:
  - **ApacheKafka** → **code** → **streaming_pyspark.py**
  - **datasets** → Contains CSV files: `insurance_1.csv`, `insurance_2.csv`, `insurance_3.csv`.

#### Input Files
- Drag and drop the `insurance.csv` files into the **datasets** directory.

#### Listening for New Data
- The streaming application is continuously monitoring the **datasets** directory for new files. 
- When a new file is added, the application processes it by loading the data into a DataFrame and applying transformations.

#### Starting the Application with `spark-submit`
- Use `spark-submit` to launch the application:
  ```bash
  spark-submit --master spark://localhost:7077 streaming_pyspark.py
  ```
  - **Arguments**:
    - `--master spark://localhost:7077`: Specifies the master node of the Spark cluster.
    - `streaming_pyspark.py`: The Spark application script.

#### Monitoring the Application
1. **Spark UI**: Access the Spark UI via `localhost:4040` to monitor the application's progress.
   - The app will show up under **Running Applications** in the Spark UI.
   
2. **Job Progress**: Jobs and stages can be tracked through the Spark Jobs tab in the UI.

#### Initial Console Output
- The schema of the streaming DataFrame is displayed in the console when the application starts, indicating that it is actively listening for new data.

#### Data Processing
1. **Adding Data**: Drag and drop `insurance_1.csv` into the **datasets** directory.
   - The application will process the file and generate output showing aggregated data based on the `gender` and `smoker` columns.

2. **Aggregation Results**: The output shows average charges by gender and smoker status:
   - Smokers have higher average charges than non-smokers, regardless of gender.

#### Spark UI Updates
- After adding `insurance_1.csv`, a job with **Job ID 0** will appear in the Spark Jobs page. The job duration is shown along with its status.
- Each job typically consists of multiple stages, visible in the **Stages** tab.

#### Adding More Data
1. **Second File**: Drag and drop `insurance_2.csv` into the **datasets** directory.
   - The application processes the new file and produces aggregated results again.
   
2. **Aggregation on Multiple Files**: The aggregation will include data from both `insurance_1.csv` and `insurance_2.csv`, because the application is set to process the entire dataset in the DataFrame. 
   - This behavior is influenced by the **output mode**. The `complete` output mode causes the entire dataset to be reprocessed.

#### Output Modes in Structured Streaming
- **Complete Mode**: Recomputes the aggregation over the entire dataset whenever new data is added.
- **Append Mode**: Only processes the new data added after the last trigger.
- **Update Mode**: Updates the results for only the rows that have changed.

#### Checking the Job in Spark UI
- After adding the second file, **Job ID 1** will show up. The Spark Jobs page will detail the stages and tasks related to this job.
- **DAG Visualization**: Visualizes the execution plan for the job, showing stages like `Scan csv`, `WholeStageCodegen`, and `Exchange`.

#### Spark API for Monitoring Applications
- Access the list of running Spark applications via the API endpoint:
  ```text
  http://localhost:4040/api/v1/applications
  ```
  - This returns a list of JSON objects, each representing a Spark application.
  
- For job-specific details, use the endpoint:
  ```text
  http://localhost:4040/api/v1/applications/{app_id}/jobs
  ```
  - Retrieve job details such as status, stages, and task counts.

#### Executor Monitoring
- **Executors Tab**: Displays detailed information on the executors handling tasks, including task status, memory usage, and active tasks.

#### Spark Environment Information
- **Environment Tab**: Provides information about the Spark cluster and properties:
  - **spark.master**: Confirms connection to a standalone Spark cluster.
  - **spark.app.id**: Identifies the application running within the cluster.

#### Next Steps
- The application is currently running in **standalone mode**. Future videos will explore running the same application in **local mode** and highlight the differences between the two modes.

## Running Apps on Spark Local

### Running PySpark in Local Mode vs Standalone Mode

In the previous video, we ran a streaming PySpark application on a standalone cluster. The `spark.master` property in the **Environment** tab of the Spark UI showed the connection to the Spark master node. For production environments, it's recommended to use a cluster manager like Mesos or YARN instead of standalone mode.

#### Spark Web UI
- **Environment Tab**: Displays runtime information, Spark properties, Hadoop properties, system properties, and classpath entries.
- **Jobs Page**: Shows details of the application's execution, such as job ID, description, duration, and task completion status.

#### Switching to Local Mode
For small-scale testing during development, running Spark in **local mode** can be more efficient than using a full cluster. To run the application in local mode:

1. Terminate the current app.
2. Use `spark-submit` without specifying the `--master` option. This defaults to local mode.

Example:
```bash
spark-submit streaming_pyspark.py
```

In **local mode**, the application does not connect to a master node, and the Spark UI will be accessible at **port 4040**. However, there won’t be any connection to a Spark Master.

#### Local Mode vs Standalone Mode
- **Local Mode**: Spark runs on a single machine. Ideal for small-scale testing and development. No cluster manager is used for resource allocation.
- **Standalone Mode**: Runs Spark on a cluster of machines. Suitable for more extensive testing or when the application requires a cluster's resources.

While both modes produce the same output for small applications, the main difference lies in resource allocation:
- In **local mode**, no cluster manager is involved.
- In **standalone mode**, Spark utilizes the cluster’s resources, and Spark’s Web UI reflects its connection to the master node.

#### Spark Web UI in Local Mode
Even in local mode, the Spark UI is available at **port 4040**, but it does not show the master node in the UI. In **Standalone mode**, the master node can be viewed under the "Completed Applications" section in the **Spark Master UI**.

- **Standalone Mode**: The Spark job appears under "Running Applications."
- **Local Mode**: The job is not listed under "Running Applications" because it is not running on a cluster.

The **spark.master** property in the **Environment** tab of the Spark Web UI will show `local`, indicating that the job is running locally.

#### Choosing Between Local and Standalone Mode
- **Local Mode**: Best for small-scale testing during development when a cluster isn't necessary.
- **Standalone Mode**: More efficient for larger-scale testing and applications that require more resources than a single machine.

Once testing is complete, Spark can continue to listen for new input files, even in local mode. For example, you can drag and drop `insurance_3.csv` into the dataset directory, and Spark will process the new file in real-time.

#### Conclusion
For most of the remaining demos in this learning path, we’ll use **local mode**, as the datasets and applications are small-scale. Running a full cluster would add unnecessary overhead and potentially slow down the application.

Next, we’ll focus on other Spark features, including its integration with **Kafka**.