## Glossary

Stream - An unbounded sequence of ordered, immutable data
Stream Processing - Continual calculations performed on one or more Streams
Immutable Data - Data that cannot be changed once it has been created
Event - An immutable fact regarding something that has occurred in our system.
Batch Processing - Scheduled, periodic analysis of one or more groups of related data.
Data Store - A generic place that holds data of some kind, like a message queue or data store
Stream Processing Application - An application which is downstream of one or more data streams and performs some kind of calculation on incoming data, typically producing one or more output data streams
Stream Processing Framework - A set of tools, typically bundled as a library, used to construct a Stream Processing Application
Real-time - In relation to processing, this implies that a piece of data, or an event, is processed almost as soon as it is produced. Strict time-based definitions of real-time are controversial in the industry and vary widely between applications. For example, a Computer Vision application may consider real-time to be 1 millisecond or less, whereas a data engineering team may consider it to be 30 seconds or less. In this class when the term "real-time" is used, the time-frame we have in mind is seconds.
Append-only Log - files in which incoming events are written to the end of the file as they are received
Change Data Capture (CDC) - The process of capturing change events, typically in SQL database systems, in order to accurately communicate and synchronize changes from primary to replica nodes in a clustered system.
Log-Structured Storage - Systems built on Append-Only Logs, in which system data is stored in log format.
Merge (Log Files) - When two or more log files are joined together into a single output log file
Compact (Log Files) - When data from one or more files is deleted, typically based on the age of data
Source (Kafka) - A term sometimes used to refer to Kafka clients which are producing data into Kafka, typically in reference to another data store
Sink (Kafka) - A term sometimes used to refer to Kafka clients which are extracting data from Kafka, typically in reference to another data store
Topic (Kafka) - A logical construct used to organize and segment datasets within Kafka, similar to how SQL databases use tables
Producer (Kafka) - An application which is sending data to one or more Kafka Topics.
Consumer (Kafka) - An application which is receiving data from one or more Kafka Topics.

## Intro to Stream Processing

### 🔹 **Stream Basics**

* **Stream**: A potentially unbounded (endless) sequence of data.
* **Data Streams**: Contain immutable data that is continuously generated.
* **Immutable Data**: Once added to a stream, it cannot be changed; only new data can supersede it.
* **Data Size**: Typically small, <1MB per record.
* **Data Throughput**: Can range from a few records/hour to thousands/second.

---

### 🔹 **Stream Processing**

* Performs continual computations on streaming data.
* Works on **immutable, evolving data** in **real-time**.
* Requires processing engines that can handle:

  * High variability in data input rate.
  * Time-sensitive calculations.

---

### 🔹 **Events**

* **Event**: An immutable fact that represents something that has happened.

  * Once created, cannot be modified.
  * Equivalent to a data record in data streaming.
* **Events vs Commands**:

  * **Message Queues**: Often deliver **commands** to perform specific actions.
  * **Evented Systems**: React to **events/facts**, such as user interactions (e.g., clicks).
* Traditional SQL systems often do **not** store historical state changes.

## Stream Processing Example

Stream Processing Examples
Log Analysis
One of the first places many companies use stream processing is in log analysis. Companies often run microservices that constantly produce logs that are full of information that can be mined for:

User behavior patterns
Failure prediction
Debugging
These logs generate a tremendous amount of data on an ongoing basis, which can be difficult to then analyze. To solve this issue, each log produced by a microservice becomes an event in a data stream.

Companies then build programs that can analyze and join on the events in these data streams to find insights into the data.

Log Analysis condenses logs from many servers into a single ordered stream
Log Analysis condenses logs from many servers into a single ordered stream

Web Analytics
Modern web applications measure almost every action a user takes on their site, for example:

button clicks
Page load times
Session duration
The volume of these actions can quickly overwhelm a traditional data store (any place you keep data). Ingesting and analyzing this data can be difficult and companies use stream processing to analyze the data as it is generated.

The benefits of this process are:

it lessens the long-term processing burden for companies because of the smaller dataset
provides real-time analysis instead of long-running bath analyses that may only be updated periodically
Streaming user events into a stream processing application
Analyzing streaming user events for web analytics

Real-Time Pricing
Ride-sharing applications are a great example of data streaming for real-time analysis. They use real-time pricing that adjusts with environmental factors and instantaneous demand.

Determining ride-share pricing on streaming real-time event data
Determining ride-share pricing on streaming real-time event data

Stream Processing Examples Recap
Stream Processing is a critical component in a number of familiar technology applications:

Finding patterns and meaningful data in disparate log messages in a microservices architecture
Tracking user engagement in real-time with streaming website analytics
Real-time pricing in ride-sharing applications based on demand and environmental conditions
Stock buying/selling based on price, news, and social media sentiment

## Stream vs. Batch Processing

Batch Processing
Runs on a scheduled basis
May run for a longer period of time and write results to a SQL-like store
May analyze all historical data at once
Typically works with mutable data and data stores
Stream Processing
Runs at whatever frequency events are generated
Typically runs quickly, updating in-memory aggregates
Stream Processing applications may simply emit events themselves, rather than write to an event store
Typically analyzes trends over a limited period of time due to data volume
Typically analyzes immutable data and data stores
Batch and Stream processing are not mutually exclusive. Batch systems can create events to feed into stream processing applications, and similarly, stream processing applications can be part of batch processing analyses.

Components of a Stream Processing Solution

Streaming Data Store
May look like a message queue, as is the case with Apache Kafka
May look like a SQL store, as is the case with Apache Cassandra
Responsible for holding all of the immutable event data in the system
Provides guarantee that data is stored ordered according to the time it was produced
Provides guarantee that data is produced to consumers in the order it was received
Provides guarantee that the events it stores are immutable and unchangeable
Stream Processing Application and Framework
Stream Processing applications sit downstream of the data store
Stream Processing applications ingest real-time event data from one or more data streams
Stream Processing applications aggregate, join, and find differences in data from these streams
Common Stream Processing Application Frameworks in use today include:
Confluent KSQL
Kafka Streams
Apache Flink
Apache Samza
Apache Spark Structure Streaming
Faust Python Library
Further Optional Reading on Message Queues
RabbitMQ(opens in a new tab)
ActiveMQ(opens in a new tab)
Benefits of Stream Processing

Benefits of Stream Processing
Faster for scenarios where a limited set of recent data is needed
More scalable due to distributed nature of storage
Provides a useful abstraction that decouples applications from each other
Allows one set of data to satisfy many use-cases which may not have been predictable when the dataset was originally created
Built-in ability to replay events and observe exactly what occurred, and in what order, provides more opportunities to recover from error states or dig into how a particular result was arrived at

## Append-Only Logs

Data streams are Append-Only Logs

Append-only logs
Append-only logs are text files in which incoming events are written to the end of the log as they are received.
This simple concept -- of only ever appending, or adding, data to the end of a log file -- is what allows stream processing applications to ensure that events are ordered correctly even at high throughput and scale.
We can take this idea a step farther, and say that in fact, streams are append-only logs.
Append-Only Logs in SQL Databases
Append-only logs were not originally created for stream processing. Years ago SQL database developers needed a way to track changes and then synch those changes between primary and secondary nodes.

Change Data Capture (CDC) – the process of how SQL databases use append-only logs to track, communicate and synchronize changes in the primary database to replica/secondary nodes.

Change Data Capture (CDC)
Change Data Capture (CDC) process in a database system using append-only logs

## Log-structured storage

Log-Structured Storage
One of the key innovations over the past decade in computing has been the emergence of log-structured storage as a primary means of storing data.

Log-structured streaming
Log-structured streams build upon the concept of append-only logs. One of the hallmarks of log-structured storage systems is that at their core they utilize append-only logs.
Common characteristics of all log-structured storage systems are that they simply append data to log files on disk.
These log files may store data indefinitely, for a specific time period, or until a specific size is reached.
There are typically many log files on disk, and these log files are merged and compacted occasionally.
When a log file is merged it means that two or more log files are joined together into one log file.
When a log file is compacted it means that data from one or more files is deleted. Deletion is typically determined by the age of a record. The oldest records are removed, while the newest stay.
Examples of real world log-structured data stores: Apache HBase, Apache Cassandra, Apache Kafka

While Apache Cassandra and HBase are not the focus of this course, both:

are data stores that surface SQ-like interfaces
are appropriate for working with massive datasets
use append-only logs to store and coordinate data across nodes
tend to be used in batch processing systems
On the other hand, Apache Kafka is a message queue system based on the concept of log-structured, append-only storage. It may appear similar to the others but is based on a different storage and scaling mechanism.

## Kafka: A Stream Processing Tool

Apache Kafka as a Stream Processing Tool
Kafka is one of the most popular streaming data platforms in the industry today.
Provides an easy-to-use message queue interface on top of its append-only log-structured storage medium
Kafka is a log of events
In Kafka, an event describes something that has occurred, as opposed to a request for an action to be performed
Kafka is distributed by default
Fault tolerant by design, meaning it is hard to lose data if a node is suddenly lost
Kafka scales from 1 to thousands of nodes
Kafka provides ordering guarantees for data stored within it, meaning that the order in which data is received is the order in which data will be produced to consumers
Commonly used data store for popular streaming tools like Apache Spark, Flink, and Samza
Kafka History
Created at Linkedin to service internal stream processing needs
Kafka is one of the Apache Foundation’s most popular projects
Used widely in production. Some famous users include Uber, Apple, and Airbnb
Creators of Kafka left LinkedIn to found Confluent, which now acts as the owner and leader of the Kafka project
Jay Kreps, one of the core authors of Apache Kafka, named the system after Czech author Franz Kafka. Kreps, who enjoys Kafka’s work, thought the name was a good fit because Kafka was built to be a “system optimized for writing.”

## Kafka in Industry

Kafka in Use in Industry
The term source is sometimes used to refer to Kafka clients which are producing data into Kafka, typically in reference to another data store
The term sink is sometimes used to refer to Kafka clients which are extracting data from Kafka, typically in reference to another data store
Further Optional Reading
How Uber uses Kafka:

The Uber Engineering Tech Stack Part 1(opens in a new tab)
The Uber Engineering Tech Stack Part 2