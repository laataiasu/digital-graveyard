# Streaming Dataframes, Views, and Spark SQL

## Importance of Spark

Why are Spark Sources and Dataframes Important?

What is Spark?
Spark: an open-source framework for distributed computing across a cluster of servers; typically, programming is required.

What is Kafka?
Kafka: a durable message broker used to mediate the exchange of messages between multiple applications.

The Case for Streaming
Data at rest is not the most relevant information
Act in response to conditions
Respond to events
Spark sources connect to the outside world
Kafka source can connect to virtually anything
What Does Spark Do?
Using information from a variety of sources, Spark allows you to create relationships with other data
Spark reads streams of information in near real-time
Spark can read from folders, sockets, or Kafka topics
What is a Cluster?
Cluster: an orientation of two or more servers in such a fashion that they can communicate directly with one another or with a cluster manager; often for the purpose of high availability or increased capacity.

Spark Kubernetes Cluster Mode
What is Kubernetes?
Kubernetes: an open-source technology used to coordinate and distribute computing.

What is Zookeeper?
Zookeeper: an open-source technology that enables semi-autonomous healing of a server cluster.

Spark Standalone Cluster Mode
Wireframe
Wireframing an application before building it out is important. We will start the wireframe here and continually add to it throughout the course as a best practice.

You can use draw.io(opens in a new tab) or any other similar tool to follow along and try it yourself.


Quiz Question
Match the correct node with the configuration.

### Spark Cluster and Application Deployment - Key Points

---

#### 🔧 Spark Component Inventory

* **Zookeeper**: Connects to Spark Master.
* **spark-submit**: Deploys Spark Applications.
* **Spark Master**: Connects to Spark Workers.
* **Spark Workers**:

  * Standalone: Connect to Spark Master via Spark URI.
  * Kubernetes: Orchestrated by Kubernetes.

---

#### 🚀 Spark Startup Sequence

1. Run `start-master.sh`
2. Check logs for Spark Master URI:

   ```bash
   tail -f /opt/spark-2.3.4-bin-hadoop2.7/logs/spark--org.apache.spark.deploy.master.Master-1-719f72471d5b.out
   ```
3. Run `start-slave.sh` with Spark Master URI:

   ```bash
   /data/spark/sbin/start-slave.sh spark://719f72471d5b:7077
   ```

---

#### 🌐 Language Support (Polyglot)

* **R**: DataFrames (Data Science)
* **Java / Scala**: Typed Datasets
* **Python**: DataFrames (Dynamic Typing, Data Science)

---

#### 🔁 Data Pipelines in Spark

* **Definition**: Series of processing steps to transform raw data for downstream systems.
* **Pipeline Structure**:

  * Start with data source
  * Apply transformation steps
  * Output as DataFrame to external sink
  * **Streaming**: Source is continuously polled

---

#### 🧪 Sample Spark Streaming App (Kafka Source)

```python
spark = SparkSession.builder.appName("balance-events").getOrCreate()

kafkaRawStreamingDF = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "balance-updates") \
    .option("startingOffsets", "earliest") \
    .load()

kafkaStreamingDF = kafkaRawStreamingDF.selectExpr(
    "cast(key as string) key", "cast(value as string) value")

kafkaStreamingDF.writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()
```

---

#### 🚢 From Start to Deployment

```bash
# Start Master
/home/workspace/spark/sbin/start-master.sh

# Start Worker
/home/workspace/spark/sbin/start-slave.sh spark://719f72471d5b:7077

# Submit Application
/home/workspace/spark/bin/spark-submit /home/workspace/hellospark.py

# Stop Master
/data/spark/sbin/stop-master.sh

# Stop Worker
/data/spark/sbin/stop-slave.sh
```

---

#### 📈 Streaming Results

* Spark runs in **micro-batches**
* Console sink:

  * Shows batches (e.g., Batch 0)
  * May take **up to 2 minutes** to appear
* Other sinks:

  * No console output

---

#### 📚 Additional Resources

* See [Spark Cluster Mode Overview](https://spark.apache.org/docs/latest/cluster-overview.html) for more deployment options.

### ✅ Walkthrough 1: Start a Spark Cluster - Key Steps

---

#### 🖥️ Video Walkthrough Timeline

* **(0:02)** Run `ps -ef` to check Spark processes
* **(0:23)** Start a Spark session
* **(0:28)** Read data from a log file
* **(0:34)** Use Spark chain commands: `filter`, `count`
* **(0:48)** Stop the Spark session

---

#### 🚀 Start Spark Cluster

```bash
# Navigate to Spark sbin directory
cd /home/workspace/spark/sbin

# Start Spark Master
./start-master.sh

# Check logs for Master URI
tail -f /home/workspace/spark/logs/spark--org.apache.spark.deploy.master.Master-1-5a00814ba363.out

# Look for URI like:
spark://5a00814ba363:7077

# Start Spark Worker
./start-slave.sh spark://5a00814ba363:7077
```

---

#### 🧪 Submit "Hello World" Spark App

```bash
# Ensure hellospark.py is saved
# Navigate to Spark bin
cd /home/workspace/spark/bin

# Submit app
./spark-submit /home/workspace/hellospark.py
```

---

#### 📁 Access Solution File

* Click **File > Open From Path**
* Enter path: `/hellospark.solution.py`
* Or use folder icon in upper-left to browse to the file

---

#### ⚠️ Workspace Notes

* Shuts down after **30 min of inactivity**
* Can take **up to 5 minutes** to start
* Use **Expand** button for full view
* Open video in separate window for parallel viewing

---

#### 🛠️ Optional

* Long walkthrough with **troubleshooting** also available


## 

