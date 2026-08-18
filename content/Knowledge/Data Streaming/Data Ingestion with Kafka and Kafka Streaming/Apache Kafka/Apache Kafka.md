---
title: "Apache Kafka"
date: 2001-01-01
tags: []
publish_external: false
---

# Apache Kafka

## Lesson Glossary of Key Terms

Glossary of Key Terms you Will Learn in this Lesson:
Broker (Kafka) - A single member server of the Kafka cluster
Cluster (Kafka) - A group of one or more Kafka Brokers working together to satisfy Kafka production and consumption
Node - A single computing instance. May be physical, as in a server in a datacenter, or virtual, as an instance might be in AWS, GCP, or Azure.
Zookeeper - Used by Kafka Brokers to determine which broker is the leader of a given partition and topic, as well as track cluster membership and configuration for Kafka
Access Control List (ACL) - Permissions associated with an object. In Kafka, this typically refers to a user’s permissions with respect to production and consumption, and/or the topics themselves.
JVM - The Java Virtual Machine - Responsible for allowing host computers to execute the byte-code compiled against the JVM.
Data Partition (Kafka) - Kafka topics consist of one or more partitions. A partition is a log which provides ordering guarantees for all of the data contained within it. Partitions are chosen by hashing key values.
Data Replication (Kafka) - A mechanism by which data is written to more than one broker to ensure that if a single broker is lost, a replicated copy of the data is available.
In-Sync Replica (ISR) - A broker which is up to date with the leader for a particular broker for all of the messages in the current topic. This number may be less than the replication factor for a topic.
Rebalance - A process in which the current set of consumers changes (addition or removal of consumer). When this occurs, assignment of partitions to the various consumers in a consumer group must be changed.
Data Expiration - A process in which data is removed from a Topic log, determined by data retention policies.
Data Retention - Policies that determine how long data should be kept. Configured by time or size.
Batch Size - The number of messages that are sent or received from Kafka
acks - The number of broker acknowledgements that must be received from Kafka before a producer continues processing
Synchronous Production - Producers which send a message and wait for a response before performing additional processing
Asynchronous Production - Producers which send a message and do not wait for a response before performing additional processing
Avro - A binary message serialization format
Message Serialization - The process of transforming an applications internal data representation to a format suitable for interprocess communication over a protocol like TCP or HTTP.
Message Deserialization - The process of transforming an incoming set of data from a form suitable for interprocess communication, into a data representation more suitable for the application receiving the data.
Retries (Kafka Producer) - The number of times the underlying library will attempt to deliver data before moving on
Consumer Offset - A value indicating the last seen and processed message of a given consumer, by ID.
Consumer Group - A collection of one or more consumers, identified by group.id which collaborate to consume data from Kafka and share a consumer offset.
Consumer Group Coordinator - The broker in charge of working with the Consumer Group Leader to initiate a rebalance
Consumer Group Leader - The consumer in charge of working with the Group Coordinator to manage the consumer group
Topic Subscription - Kafka consumers indicate to the Kafka Cluster that they would like to consume from one or more topics by specifying one or more topics that they wish to subscribe to.
Consumer Lag - The difference between the offset of a consumer group and the latest message offset in Kafka itself
CCPA - California Consumer Privacy Act
GDPR - General Data Protection Regulation

## Kafka Runs Anywhere

Kafka Runs Anywhere

Kafka Architecture
Kafka servers are referred to as brokers
All of the brokers that work together are referred to as a cluster
Clusters may consist of just one broker, or thousands of brokers
Apache Zookeeper(opens in a new tab) is used by Kafka brokers to determine which broker is the leader of a given partition and topic
Zookeeper keeps track of which brokers are part of the Kafka cluster
Zookeeper stores configuration for topics and permissions (Access Control Lists - ACLs)
ACLs are Permissions associated with an object. In Kafka, this typically refers to a user’s permissions with respect to production and consumption, and/or the topics themselves.
Kafka nodes may gracefully join and leave the cluster
Kafka runs on the Java Virtual Machine (JVM)
Kafka Clustering - Key Points
Kafka servers are referred to as brokers and organized into clusters.
Kafka uses Apache Zookeeper to keep track of topic and ACL configuration, as well as determine leadership and cluster management.
Usage of ZooKeeper means that Kafka brokers can typically seamlessly join and leave clusters, allowing Kafka to grow easily as its usage increases or decreases.
Kafka Cluster
A Kafka cluster consists of one or more brokers using ZooKeeper to determine leadership and track configuration

## How Kafka Stores Data

The way that Kafka stores data is pretty simple. It has a data directory on a disk where it stores logs of data and text files. /var/lib/kafka/data is a directory where Kafta sorts data in your workspace and in many Kafka productions systems.

Each topic receives its own sub-directory with the associated name of the topic.
Kafka may store more than one log file for a given topic
Kafka Log Storage
Kafka stores data on disk in folders for each of its topics

## Kafka Data Partitioning

Message Ordering
Message ordering is only guaranteed within a partition in Kafka. If your topic has more than one partition, Kafka provides no guarantees that the messages will be consumed in the order they were produced. For many applications, this is an acceptable tradeoff for increasing the parallelism and speed of consumption. Your producer applications may still add metadata to the event header or message body itself to indicate ordering. However, this logic would belong to your application, and not Kafka itself. For example, you may place an increasing ID sequence in every message (eg 1, 2, 3, and so on) or a granular timestamp to indicate the order of a message.

Kafka Partitions
A single topic may have more than one partition. Each partition, such as “a” and “b” above, may live on different brokers, or on all of the brokers.

## Kafka Data Replication

Preventing Data Loss

Based on an understanding that machines can fail, one of the core features of Kafka is the concept of replication.

Replication – when the data is written to many brokers
Leader Broker – the broker responsible for sending and receiving data to clients for a given topic partition
Replicas – any brokers that are storing replicated data
If the leader broker were to fail, one of the replicas would be elected the new topic partition leader by a zookeeper election.

The exact number of replicas used can be configured globally as a Kafta server configuration item or set individually on every topic you create. But keep a few things in mind:

You can not have more replicas than brokers
Data replication has overhead
Always enable replication in a production cluster to prevent data loss
**Data Replication helps prevent data loss by writing the same data to more than one broker**
Data Replication helps prevent data loss by writing the same data to more than one broker

## Kafka Topics in Depth

Kafka Topics are rich in configuration options. To get the most out of Kafka you will need to develop a strong understanding of how these options impact performance. This will include understanding how to replicate topics in Kafka.

Configuring Kafka Topics
To recap a few key points:

Kafka uses data replication to duplicate data across multiple machines to prevent data loss in case a broker fails
Commonlym the desired replication factor is set at the topic level and the value should always be specificed when creating a topic
If a leader broker fails or is removed from a cluster, a replica broker will be become the new leader
To become a new leader, the broker must be an In-Sync Replica (ISR)
Configuration in Kafka includes configured the desired number of ISRs
If the number of ISRs is too large this can slow down processing

## Partitioning Topics

* **Choosing Number of Partitions**

  * There is no fixed "right" number; depends on scenario and throughput needs.
  * Key factor: **Desired throughput (MB/s)**.

* **Modifying Partitions**

  * Partitions can be added later by modifying a topic.

* **Performance Impacts**

  * More partitions → increased networking latency and potential rebalances → possible unavailability.

* **Partition Calculation Formula**

  ```
  Partitions = Max(Overall Throughput / Producer Throughput,
                   Overall Throughput / Consumer Throughput)
  ```

* **Example Calculation**

  * Goal: 100 MB/s throughput
  * 3 Producers @ 10 MB/s each → 3 × 10 = 30 MB/s
  * 5 Consumers @ 10 MB/s each → 5 × 10 = 50 MB/s
  * Calculation:

    ```
    Max(100 / 30, 100 / 50) = Max(3.34, 2) ≈ 4 partitions needed
    ```

* **Ordering Consideration**

  * **Ordering is only guaranteed within individual partitions** of a topic.

## Naming Kafka Topics

Naming Conventions
The only enforced rules for topic names are that they must be less than 256 characters, consist only of alphanumeric characters (a-z, A-Z, 0-9), “.”, “_”, or “-”.
There is no idiomatic or universally correct naming convention.
Naming conventions can help reduce confusion, save time, and even increase reusability.
Example of a naming convention:
Consider starting with a namespace, like com.udacity
Consider segmenting on schema or model type, like com.udacity.lesson, where lesson is the model
Consider segmenting on event type, like com.udacity.lesson.quiz_complete, where quiz_complete is the event

## Topic Data Management

**Topic: Data Management in Kafka**

---

### 🔹 **Key Points**

* **Data Retention Policies:**

  * Kafka stores data in a topic for a configurable duration or size.
  * Controlled via:

    * `retention.ms` → time-based retention
    * `retention.bytes` → size-based retention
  * When limits are reached:

    * If `cleanup.policy = delete`: expired/old data is deleted.
    * If `cleanup.policy = compact`: data is retained indefinitely but duplicates are compacted.

* **Time-Based Retention:**

  * Data is deleted after a specified time (`retention.ms`).

* **Size-Based Retention:**

  * When topic size exceeds `retention.bytes`, oldest data is deleted.

* **Combined Retention:**

  * If both time and size thresholds are set, whichever limit is hit first triggers data deletion.

* **Log Compaction:**

  * No expiry by time or size.
  * Controlled by `cleanup.policy = compact`.
  * Uses message key to identify unique messages.
  * Keeps the latest value for each key; older duplicates are deleted.

* **Compression:**

  * Reduces storage and network usage.
  * Supported algorithms: `lz4`, `zstd`, `snappy`, `gzip`.
  * Controlled by `compression.type`.

* **Best Practice:**

  * Each Kafka topic should store only **one type of event**.
  * Mixing multiple event types in a topic makes it harder for consumers to process data.

---

### 🔸 **Assessment Questions**

1. **Which of the following are ways that Kafka manages data?**

   * Time-based expiration (`retention.ms`)
   * Size-based expiration (`retention.bytes`)
   * Log compaction (`cleanup.policy = compact`)
   * Compression (`compression.type`)

2. **Which scenario would be appropriate for time-based expiration?**

   * Use case: Events only need to be available for a certain duration (e.g., 7 days of logs).

3. **Which scenario would be appropriate for size-based expiration?**

   * Use case: Topic must not exceed a specific disk size due to storage limits.

4. **Which scenario would be appropriate for log compaction?**

   * Use case: Keeping only the latest value for each key (e.g., user profiles or account balances).

5. **Which scenario would be appropriate for both time and size expiration?**

   * Use case: System needs to manage both storage duration and capacity simultaneously.

## Kafka Producers

Kafka Producers
In this section you will learn the specifics of how Kafka Producers are created and managed. Specifically, you will see how to:

Synchronously and asynchronously send data to Kafka
Use key configuration options, such as batch size, client identifiers, compression, and acknowledgements
Specify data serializers

## Synchronous Production


The synchronous producer is the simplest type of Kafka producer, it:

sends data to Kafka
blocks program execution until the message receipt has been confirmed by the broker
is useful when you want to ensure data is sent before moving an application forward
should be used for specific use cases and not as a default producer type

## Asynchronous Production


Asynchronous production of Kafka is the most common method of producing data to topics. A few key points to remember about asynchronous producers:

they send the data and immediately continue
they are useful when maximizing throughput to Kafka with the least overhead and impact on the integrated application
they should be the default choice unless the specific use case requires synchronicity
Kafka clients offer callbacks for when messages are delivered or an error occurs so that applications can take rectifying action. Conversely, producers can decide to fire and forget and never check for delivery confirmation or error messages.

## Message Serialization


This process of transforming an application’s internal representation of a data model to a data model suitable for data stores or other applications is called serialization.

Kafka itself does not handle the serialization process. Instead, the Kafka client library helps facilitate the process.

Finally, never change the type of serialization in use without recreating the topic. This is a guaranteed way to cause a production outage, as consumers will have no idea what data to expect!

Quiz Question
Which of the following are common types of message serialization? (may be more than one answer)

## Producer Configuration

#### 🔧 **General Configuration**

* **Library**: `confluent_kafka_python` uses `librdkafka` under the hood.
* **Configuration Reference**: Use [librdkafka configuration options](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md).
* **client.id**:

  * Always set for better logging, debugging, and resource tracking.

#### 🔁 **Retries and Ordering**

* **retries**:

  * Number of resend attempts before marking a message as failed.
* **enable.idempotence**:

  * Set to `true` to preserve **ordering** when **retries** are enabled.

#### 📦 **Compression Settings**

* **compression.type options**:

  * `none`, `gzip`, `lz4`, `snappy`, `zstd`
* **Compression**:

  * Handled by the **producer** if enabled.
  * If the **topic** has a compression setting, it must match the producer’s or the broker will **decompress and recompress**.
  * **Consumer sees** the **topic-level** compression format.

#### ✅ **Acknowledgment (acks)**

* **acks setting values**:

  * `-1` or `all`: Wait for **all In-Sync Replicas (ISR)** to acknowledge.
  * `0`: Fire-and-forget mode (best performance, no durability guarantee).
* **Minimum ISR**:

  * With `min.insync.replicas = 3` and `replication.factor = 7`, **3 brokers** need to acknowledge the message.

---

### **Message Compression Algorithms – Pros & Cons**

| Algorithm  | Pros                           | Cons                          |
| ---------- | ------------------------------ | ----------------------------- |
| **lz4**    | Fast compression/decompression | Low compression ratio         |
| **snappy** | Fast compression/decompression | Low compression ratio         |
| **zstd**   | High compression ratio         | Slower than lz4/snappy        |
| **gzip**   | Ubiquitous, widely supported   | CPU-intensive, slowest option |

## Batching Configuration


When Kafka client libraries send data to Kafka, they do not send every message individually. Instead, the client libraries collect groups of messages together and then send them to the Kafka broker.

Batches – the collection of groups of messages that are sent to a Kafka broker, used to improve application performance
The count, frequency, and quantity of data sent in these batches are customizable.

## Kafka Consumers

In this section, you will learn the specifics of how Kafka Consumers are created and managed. Specifically, you will see how to:

Pull data from one or more Kafka topics into your application
Use key configuration options, such as consumers and consumers groups, offsets, and offset commits
Understand and handle topic rebalances
Specify data deserializers

Kafka Consumers - Key Points
client.id is an optional setting which is useful in debugging and resource limiting
Poll for data to read data from Kafka
poll(opens in a new tab)
consume

## Consumer Offsets


Consumer Offsets - Key Points
Kafka keeps track of what data a consumer has seen with offsets
Kafka stores offsets in a private internal topic
Most client libraries automatically send offsets to Kafka for you on a periodic basis
You may opt to commit offsets yourself(opens in a new tab), but it is not recommended unless there is a specific use-case.
Offsets may be sent synchronously or asynchronously
Committed offsets determine where the consumer will start up
If you want the consumer to start from the first known message, [set auto.offset.reset to earliest]
This will only work the first time you start your consumer. On subsequent restarts it will pick up wherever it left off
If you always want your consumer to start from the earliest known message, you must manually assign your consumer to the start of the topic on boot(opens in a new tab)

Question 1 of 2
Which of the following best describes what a Consumer Offset is?

Question 2 of 2
How does Kafka keep track of Consumer Offsets?

## Consumer Groups


Consumer Groups - Key Points
All Kafka Consumers belong to a Consumer group
The group.id parameter(opens in a new tab) is required and identifies the globally unique consumer group
Consumer groups consist of one or more consumers
Consumer groups increase throughput and processing speed by allowing many consumers of topic data. However, only one consumer in the consumer group receives any given message.
If your application needs to inspect every message in a topic, create a consumer group with a single member
Adding or removing consumers causes Kafka to rebalance
During a rebalance, a broker group coordinator identifies a consumer group leader
The consumer group leader reassigns partitions to the current consumer group members
During a rebalance, messages may not be processed or consumed

## Consumer Subscriptions


Topic Subscriptions - Key Points
You subscribe to a topic by specifying its name
If you wanted to subscribe to com.udacity.lesson.views, you would simply specify the full name as ”com.udacity.lesson.views”
Make sure to set allow.auto.create.topics to false so that the topic isn’t created by the consumer if it does not yet exist
One consumer can subscribe to multiple topics by using a regular expression
The format for the regular expression is slightly different. If you wanted to subscribe to com.udacity.lesson.views.lesson1 and com.udacity.lesson.views.lesson2 you would specify the topic name as ”^com.udacity.lesson.views.*”
The topic name must be prefixed with ”^” for the client to recognize that it is a regular expression, and not a specific topic name
Use regexp(opens in a new tab) to specify your regular expressions.
See the confluent_kafka_python subscribe()(opens in a new tab) documentation for more information

Question 1 of 5
What is a topic rebalance?

Question 2 of 5
Which of the following are reasons why consumer groups are important? (may be more than one answer)

Question 3 of 5
When would you use a single consumer?

Question 4 of 5
Client ID is mandatory for consumers

Question 5 of 5
Group ID is mandatory for consumers

## Consumer Deserializers


Deserializers - Key Points
Remember to deserialize the data you are receiving from Kafka in an appropriate format
If the producer used JSON, you will need to deserialize the data using a JSON library
If the producer used bytes or string data, you may not have to do anything
Consumer groups increase fault tolerance and resiliency by automatically redistributing partition assignments if one or more members of the consumer group fail.

## Retrieving Data from Kafka


Retrieving Data from Kafka - Key Points
Most Kafka Consumers will have a “poll” loop which loops infinitely and ingests data from Kafka
Here is a sample poll loop:
It is possible to use either poll(opens in a new tab) or consume(opens in a new tab), but poll is slightly more feature rich
Make sure to call close()(opens in a new tab) on your consumer before exiting and to consume any remaining messages
Failure to call close means the Kafka Broker has to recognize that the consumer has left the consumer group, which takes time and failed messages. Try to avoid this if you can.

## Metrics for Consumer Performance
In this section, you’ll learn how to measure the performance of the Kafka Consumer code you have built.

The most important metric to understand for your Kafka Consumer is consumer lag.

Consumer lag is measured by taking the difference between the current consumer offset, and the offset of the newest message for that topic partition.
There will almost always be some consumer lag
Kafka CLI tools to measure consumer lag.
If you notice that the consumer lag number continues to grow over time, though, that is an indicator that your consumer cannot keep up. In that case, you typically will need additional consumer processes in order to keep up.

Another important metric to measure is the number of messages per second passing through your Kafka topic.

This number indicates the throughput of your topic
It can be useful in understanding if you’re meeting performance goals
It is typically calculated in conjunction with consumer lag
Kafka emits metrics for throughput via the Java Metrics Exporter, or JMX, so that you can hook this metric directly into your monitoring dashboards and alerting systems.

What is the consumer lag of the following producer and consumer?
If I have a consumer offset of 15600 and the latest offset in my Kafka topic is 17000, what is my Consumer Lag?

Enter your response here
Quiz Question
Which of the following might help improve consumer lag? (may be more than one answer)

The question asks "Which of the following might help improve consumer lag?"

It's true that adding compression would reduce network overhead, but we're talking about overall consumer lag, which may not actually be related to network overhead at all. Thus, adding compression may actually slow the consumer down. Likewise, if the messages are compressed and we remove compression, that may also slow down the consumer. The best solution here is to increase the number of consumers, which in turn increases parallelism with respect to the number of messages that may be consumed at once.

Hide Quiz Explanation

## Producer Performance


When a producer sends messages to Kafka, there is always some inherent latency in that process. Ideally, that latency number is small and consistent.

High latency can indicate that your acks setting is too high and that too many ISRs nodes must confirm the message before returning.
It may also indicate that too many partitions or replicas have been assigned to this topic.
Another metric to keep your eyes on is the producer response rate. This metric is an indicator of how many messages are being delivered over time.

All of these metrics may be created by using producer delivery callbacks in the client library.
Note - The ack setting defines the number of acknowledgements required by Kafka brokers before a produced event can be considered to have been successfully published. In libraries such as librdkafka we can fine-tune this parameter, defining a specific number of brokers that must acknowledge our message. If a Kafka cluster consists of many nodes, that means that every message we produce must be acknowledged by every one of those brokers. In the simple examples, we've gone through so far this is no problem. But in a typical Kafka production environment, the Kafka Server will be handling thousands or even millions of messages per second. Even on a powerful server with significant networking capability, the time spent acknowledging messages quickly becomes a bottleneck because of the CPU cycles and network overhead required to engage with every produced message on every broker.

Question 1 of 2
If a Kafka producer was experiencing high latency, what might you investigate? (may be more than one answer)

Question 2 of 2
What is producer response rate?

## Broker Performance


The Kafka broker is the conduit through which data in a system flows.

First, disk usage should be monitored as Kafka retains data, sometimes indefinitely.

Network usage is a critical metric to measure.

Election frequency is another important metric

Question 1 of 3
Which of the following are consequences of a saturated network on a broker?
(Checkmark all correct responses)

Question 2 of 3
What might be an indicator of an unstable cluster?

Question 3 of 3
What could occur if your broker’s disk filled up? (may be more than one answer)

## Removing Records and Data Privacy
Removing data from Kafka requires special planning and consideration since it utilizes an append-only log. In this section, you will learn about strategies and privacy regulations related to removing Kafka records.


This is a serious issue in a world where privacy regulations are increasingly giving consumers the right to be forgotten. Regulations like the EU’s GDPR and the California Consumer Privacy Act, or CCPA, grant citizens of these regions the right to request that their data be removed from storage.


In this section, we’ll review a strategy popularized by Kafka User Daniel Lebrero to allow for deletion of records in existing Kafka topics.


Message Compaction
Kafka supports message expiration:

Kafka can expire messages based on time, topic size, or both
However, some use cases disallow the use of message expiration to manage user data. When this occurs, use log compaction instead of log expiration to manage a user’s personal data.

With a compacted topic, you can continue to publish updates to a particular message as long as the keys match.
A message with a matching key and a null value tells the Kafka broker that it should delete the key on the next compaction, effectively deleting the message.
There are log compaction timing settings on the topic.

One of the major problems with this approach, however, is that user data may be spread through many topics, and not always keyed on the user ID. So, unfortunately, this strategy is typically not enough.

## Per-User Key Encryption


Encrypted User Keys – create a topic that maps a user id to an encryption key

Used to encrypt any data related to a user before putting it into any other Kafka topic
Vastly reduces the management overhead of deleting user data
To delete the user, simply compact and delete their encryption key from the encrypted user key topic. Once the key is gone, it is effectively impossible for any application in the system to decrypt the user’s data ever again.

