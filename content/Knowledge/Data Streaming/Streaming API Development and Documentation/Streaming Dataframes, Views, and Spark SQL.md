---
title: "Streaming Dataframes, Views, and Spark SQL"
date: 2001-01-01
tags: []
---

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

## Create a Spark Streaming Dataframe with a Kafka Source

Create a Spark Streaming Dataframe with a Kafka Source

Changing Data
Have you ever seen fireflies at night? Our world is full of data, which like fireflies is constantly changing and in motion.

Streaming DataFrame Capturing Data in Motion
Streaming DataFrame: Capturing Data in Motion

Streaming DataFrame: Capturing Data in Motion
Imagine each firefly is a different Data Stream
We want to be able to capture, compare, and gather their unique data, and see how they look when viewed together
DataFrames enable these unique comparisons to happen
They can make a short-term view of data in motion, that your application will use to create insights
What is a DataFrame?
DataFrame: A** **programming construct used to coordinate the processing of dynamic data.

DataFrames in Action
spark = SparkSession.builder.appName("balance-events").getOrCreate()

kafkaRawStreamingDF = spark \
   .readStream              \
   .format("kafka")         \
   .option("kafka.bootstrap.servers","localhost:9092") \
   .option("subscribe","balance-updates")              \
   .option("startingOffsets","earliest")              \    

kafkaStreamingDF = kafkaRawStreamingDF \
   .selectExpr("cast(key as string) key", "cast(value as string) value")

kafkaStreamingDF.writeStream \
   .outputMode("append") \
   .format("console") \
   .start() \
   .awaitTermination()
Explanation of DataFrames in Action
Here is a Spark Streaming Application using the DataFrame construct:

Our Source DataFrame in this example, kafkaRawStreamingDF, is created by reading from a readStream
The Sink DataFrame, kafkaStreamingDF, is used to write information to the console
Both DataFrames appear as coding variables, but they are powerful abstractions of moving DataSets
Source and Sink as discussed in the video above
Source and Sink

What is a Source?
Source: an external system that generates data.

What is a Sink?
Sink: an external system that consumes data.

Pop Quiz as discussed below
Pop Quiz

Pop Quiz
So which is a source and which is a sink? The key is the perspective. It is all determined based on the point of view. When drawing a map of the world, you orient the globe based on your current perspective. When viewed from different angles, the world can look very different. When diagramming a system, you must choose the perspective. Which system will be the source in this diagram? Which will be the sink?

In this picture, identify at least two sources
Identify at least one sink
Can you identify something in the picture that is both a source and a sink?
Answer Key as discussed below
Answer Key

Answer Key
The faucet represents both a data Source and a data Sink
Water flows to it from the Hot and Cold
Water flows from it to the washbasin
The washbasin represents a data Sink in this example
Water flows to it from the faucet
The Hot and Cold both represent data Sources here
They provide both hot and cold water to the faucet
Remember, the key is in the Perspective!

Spark Sources as discussed below
Spark Sources

Spark Sources
Spark Streams can read from various input sources
So far we have read from a static file using just Spark without streaming
Spark Streams have the ability to monitor folders, watching for files as they appear, and then read them in real-time
Perhaps the most flexible source to read from is Kafka, because of its ability to broker data
Another source that can be used primarily for testing is a Unix socket - we will not be going into this in the course, but it can be useful for learning
Constructing a Kafka Stream
Constructing a Kafka Stream

To construct a Kafka Stream:
You first provide a broker name
Then you choose a topic
Last you should indicate if you want the earliest or latest messages:
Earliest means you would like to read your messages starting with the oldest
Latest means you would like to read the most recent messages first (this option doesn't read the older messages, just those messages from the time the stream starts going forward
Kafka Stream in Action
kafkaRawStreamingDF = spark                          \    
.readStream                                          \
.format("kafka")                                     \
.option("kafka.bootstrap.servers", "localhost:9092") \
.option("subscribe", "balance-updates")              \
.option("startingOffsets","earliest")                \ 
Explanation of Kafka Stream in Action
Here is a Spark Streaming Application using a Kafka Stream as a Source

Our Source DataFrame in this example, called kafkaRawStreamingDF is created by reading from a readStream
We chain the option function to provide multiple connection parameters
The first parameter we pass is the kafka.bootstrap.servers parameter...this is our broker
The next parameter we pass is the subscribe parameter...this is the topic
The last parameter we send is the startingOffsets parameter...this tells Kafka we want messages starting at the earliest message received for the topic
Keep in mind that messages do expire eventually, so earliest is actually the earliest message Kafka still remembers.

What's a Broker?
Broker: in a Kafka configuration, the server to which requests from external systems can be addressed; also the central processing component of a Kafka cluster.

What's a Topic?
Topic: in a Kafka configuration, a communication channel; often representing similar or related data; sometimes called a mailbox.

What is an Offset?
Offset: in a Kafka configuration, a value that determines the mode of consumption of a topic; earliest starts at the oldest message; the latest starts at the newest message.

The Topic of the Conversation
Have you ever known someone who can intelligently discuss just about anything? It doesn't seem to matter what the conversation is about, they just happen to know something about it?

Kafka has a similar quality. It can provide data from dozens or hundreds of topics. Each topic's data can come from a different source.

Topic of the Conversation
Topic of the Conversation

Keys and Values
Every message you read from Kafka has 2 fields:

The Key column is like the primary key for a database table and is often a unique identifier
The Value column contains the bulk of the data being transmitted
By default, the Kafka key and value are in binary format
Keys and Values as discussed above
Keys and Values

Additional Resources
For more information on integrating Spark with Kafka, see the official Kafka Integration Guide(opens in a new tab).

## Walkthrough 2: Create a Spark Streaming Dataframe

Steps in the walkthrough video:

(0:02) ps -ef command to check if Spark processes are running
(0:26) import libraries and start a Spark session
(0:32) read streaming data and store it to a dataframe
(0:41) cast Kafka dataframe to a readable single column value
(0:52) output the dataframe to the console
Create a Spark Streaming Dataframe with a Kafka Source
From the console type: /home/workspace/startup/startup.sh to start Kafka, and the Trucking Simulation
Start the spark master and spark worker
From the terminal type: /home/workspace/spark/sbin/start-master.sh
View the log and copy down the Spark URI
From the terminal type: /home/workspace/spark/sbin/start-slave.sh [Spark URI]
Complete the kafkaconsole.py python script
Submit the application to the spark cluster:
From the terminal type: /home/workspace/spark/submit-kafka-console.sh
Watch the terminal for the values to scroll past (it may take up to 2 minutes)
Check the Solution File
To access the solution .py file, click on File (in the top menu of the workspace), click Open From Path and enter /kafkaconsole.solution.py.
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Optional Long Walkthrough with Troubleshooting

##  Spark Views

Create a Spark View

What is a Spark View?
Spark View: in a Spark application, a session-bound representation of data in a certain configuration (ex: a view of discounted inventory).

Create a View
Creating a view is like using a colored filter that changes certain things in a picture
Using spark you can create temporary views of data which emphasize or reveal certain attributes
For example, if you wanted to extract a year from a field that contains a month, day, and year, you could save that as a view
The purpose of temporary views is to save a certain configuration of a DataFrame for later reference within the same Spark application
The view won't be available to other Spark Applications
Create a View Example. Choosing the right fields is important.
Create a View Example

Create a View
In this example, we started with several fields available from our source
We have an urgent need for a combination of these fields
We then create a subset in a view for later querying
Creating a Spark View in Action
fuelLevelStreamingDF.createOrReplaceTempView("FuelLevel") 
Explanation of Spark View in Action
In this snippet, we are working with a DataFrame previously instantiated, called fuelLevelStreamingDF
Using the createOrReplaceTempView function call we create a Temporary View: "FuelLevel"
Notice the view has a name which is the way we will later query the view
Any filtering we want to be applied to the DataFrame can be done before this point
The DataFrame will be represented by the temporary view
Creating then Querying a Spark View in Action
fuelLevelStreamingDF.createOrReplaceTempView("FuelLevel")
fuelLevelSelectStarDF=spark.sql("select * from FuelLevel")
Explanation of Creating then Querying a Spark View
In this snippet, we are working with a DataFrame previously instantiated, called fuelLevelStreamingDF
Using the createOrReplaceTempView function call we create a Temporary View: "FuelLevel"
Notice the view name is the way we access and query the view
This is different from the way we act on DataFrames
We query the view using a select statement which includes the name of the view
The spark.sql call results in another DataFrame called fuelLevelSelectStarDF
This DataFrame holds the results of the query
Flexibility, Familiarity, SQL
Views give you a lot of flexibility in querying your streaming data
SQL syntax is familiar to many people
Spark has SQL functions for data manipulation
You can use the usual field aliasing
There are many other features of SQL included in the query syntax
Query a View then Sink to Kafka
fuelLevelKeyValueDF=spark.sql("select key, value from FuelLevel")

fuelLevelKeyValueDF                       \
.selectExpr("cast(key as string) as key", \
"cast(value as string) as value")         \   
.writeStream                              \    
.format("kafka")                          \    
.option("kafka.bootstrap.servers", "localhost:9092")\    
.option("topic", "fuel-changes")          \    
.option("checkpointLocation","/tmp/kafkacheckpoint")\ 
.start()                                  \    
.awaitTermination()
Explanation of Querying a View and Sinking to Kafka
After querying your view, you have something to offer to other systems
Let's learn how to share that data via a Kafka topic
First, select the fields using spark.sql
Next, use a select expression on the resulting DataFrame to cast the fields
Be sure to pass the Kafka bootstrap servers parameter
Last sink the DataFrame to your new Kafka topic, using the writeStream
Now any Kafka consumer can access your data by subscribing to the topic called fuel-changes
Key Points as discussed in the video
Key Points

## Walkthrough 3: Query a Spark View

Note, the instructor refers to this as a solution. However, it is a walkthrough.

Steps in the walkthrough video:

(0:06) import libraries and start a Spark session
(0:16) read streaming data and store it to a dataframe
(0:31) cast Kafka dataframe to a readable string
(0:44) create a temporary streaming view to enable query
(0:47) query data from the temporary streaming view into a new dataframe
(0:52) write the new dataframe into a Kafka topic
(1:33) ouput Kafka topic to the console
Create and Query a Temporary Spark View and Sink to Kafka
If you just started the workspace, from the console type: /home/workspace/startup/startup.sh to start Kafka, and the Trucking Simulation
If you just started the workspace, start the spark master and spark worker
From the terminal type: /home/workspace/spark/sbin/start-master.sh
View the log and copy down the Spark URI
From the terminal type: /home/workspace/spark/sbin/start-slave.sh [Spark URI]
Complete the gear-position.py python script
Submit the application to the spark cluster:
From the terminal type: /home/workspace/spark/submit-gear-position.sh
Use the kafka-console-consumer command to watch the data you are sinking: /data/kafka/bin/kafka-console-consumer --bootstrap-server localhost:port_number --topic topic_name --from-beginning
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Optional Long Walkthroughs with Troubleshooting

## Edge Cases

* **Command Used:**
  `ps -ef`

* **Purpose:**
  List all running processes on the server

* **What to Look For:**

  * Two separate lines containing the word `spark`
  * These lines indicate:

    * One process running the **Spark Master**
    * One process running a **Spark Worker**

* **Example Output (Spark Running):**

  ```
  /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -cp /data/spark/conf/:/data/spark/jars/* -Xmx1g org.apache.spark.deploy.master.Master
  /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -cp /data/spark/conf/:/data/spark/jars/* -Xmx1g org.apache.spark.deploy.worker.Worker
  ```

* **Conclusion:**

  * **Spark is running** if you see **two Java processes** involving `org.apache.spark.deploy.master.Master` and `org.apache.spark.deploy.worker.Worker`
  * **Only one correct response** expected in quiz scenario

## Lesson Review

Lesson Review

Lesson Learning Objectives
Lesson Learning Objectives

Lesson Learning Objectives
Upon completion of Lesson 1, you should be able to successfully carry out the following tasks:

Start a Spark Cluster and deploy a Spark application
Create a Spark Streaming DataFrame with a Kafka Source
Create a Spark View
Query a Spark View
Additional Resources
Spark Cluster-Mode Resources:
For more details about various Spark deployment configurations see the official Spark Cluster Mode Overview(opens in a new tab)

Kafka Integration Guide Resources
For more information on integrating Spark with Kafka, see the official Kafka Integration Guide(opens in a new tab)

Using Data Sets and DataFrames
For more information on using DataFrames see the official Spark Documentation Using Data Sets and DataFrames(opens in a new tab)

Course Overview as discussed in the video above
Course Overview

Where we are in the Course
Here's where we are in the course:

We just learned about Streaming DataFrames
Next, we're going to talk about Joins and JSON

## Glossary

Glossary
KeyTerm	Definition
Broker	In a Kafka configuration, the server to which requests from external systems can be addressed; also the central processing component of a Kafka cluster.
Cluster	An orientation of two or more servers in such a fashion that they can communicate directly with one another or with a cluster manager; often for the purpose of high availability or increased capacity.
Data Pipeline	A series of steps of processing that augment or refine a raw data source in preparation for consumption by another system.
DataFrame	A programming construct used to coordinate the processing of dynamic data.
Kafka	A durable message broker used to mediate the exchange of messages between multiple applications.
Kubernetes	An open-source technology used to coordinate and distribute computing.
Offset	In a Kafka configuration, a value that determines the mode of consumption of a topic; the earliest starts at the oldest message; the latest starts at the newest message.
Sink	An external system that consumes data.
Source	An external system that generates data.
Spark	An open-source framework for distributed computing across a cluster of servers; typically programming is required.
Spark View:	in a Spark application, a session-bound representation of data in a certain configuration
Topic	In a Kafka configuration, a channel of communication; often representing similar or related data; sometimes called a mailbox.
Zookeeper	An open-source technology that enables semi-autonomous healing of a server cluster.