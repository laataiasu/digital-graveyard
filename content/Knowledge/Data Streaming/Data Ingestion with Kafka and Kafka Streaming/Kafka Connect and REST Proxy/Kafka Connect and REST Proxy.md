---
title: "Kafka Connect and REST Proxy"
date: 2001-01-01
tags: []
---

# Kafka Connect and REST Proxy

## Lesson Glossary of Key Terms

Glossary of Key Terms You Will Learn in this Lesson
Kafka Connect - A web server and framework for integrating Kafka with external data sources such as SQL databases, log files, and HTTP endpoints.
JAR - Java ARchive. Used to distribute Java code reusably in a library format under a single file.
Connector - A JAR built on the Kafka Connect framework which integrates to an external system to either source or sink data from Kafka
Source - A Kafka client putting data into Kafka from an external location, such as a data store
Sink - A Kafka client removing data from Kafka into an external location, such as a data store
JDBC - Java Database Connectivity. A Java programming abstraction over SQL database interactions.
Task - Responsible for actually interacting with and moving data within a Kafka connector. One or more tasks make up a connector.
Kafka REST Proxy - A web server providing APIs for producing and consuming from Kafka, as well as fetching cluster metadata.

## Kafka Connect

Kafka Connect is a web server and framework for integrating Kafka with external data sources such as SQL databases, log files, and HTTP endpoints.

That team at Confluent recognized that there are many common and repeated scenarios that developers encounter to get data into and out of Kafka. So the team set to work to build a pluggable framework for building reusable Kafka producers and consumers.

The result of their effort was Kafka Connect.

Kafka Connect is a framework, written in Java, which:

allows developers to build an integration once
then use it repeatedly with just a bit of configuration
makes it possible to avoid integrating Kafka client code into your applications entirely

## Kafka Connect Architecture

Kafka Connect is an extension of the Kafka project and is built in Scala and Java. Because it is built on the JVM, Kafka Connect can run on most types of hardware and operating systems.

On its own, Kafka Connect is a web server. For Kafka Connect to be able to interact with the outside world, it needs plugins to tell it how to do so.

Kafka Connect plugins:

implement the actual functionality
must be implemented against the connect framework API
are written in a JVM language, like Java
Kafka Connect uses Kafka to store its configuration and track its internal state and it can be run as a single node, or as a cluster.

Kafka Connect
Kafka Connect uses Kafka as its configuration store and uses Framework JARs to provide functionality

The Connect Framework
Kafka Connect plugins are similar to the Kafka consumers and producers you’ve already built!

At a high level, every Kafka Connect plugin defines a few things.

Connectors: which are a high-level abstraction responsible for managing tasks
Tasks: contain the code that specifically manages how data should be produced into or consumed out of Kafka
Converters: which are responsible for defining the mapping between the source or destination system and Kafka Connect and can be used to turn data into Avro or JSON
Question 1 of 3
Which of the following best describes the Kafka Connect architecture?

Question 2 of 3
Which of the following actions does Kafka Connect support? (may be more than one answer)

Question 3 of 3
Why are Connectors not built into the web server directly?

## Kafka Connect Connectors

In this section we will review the catalogue of open-source Kafka Connectors and highlight some of the most commonly used connectors.

There are many types of Kafka Connect plugins available today. Most existing connector plugins are focused on databases and data sources.

Most common connector categories:

Local file source and sink – for moving logs into and out of Kafka
Cloud Key Value Store
Traditional SQL databases such as MySQL or postgres are also common and useful plugins.
HDFS data sources
REST APIs
Kafka Connect Connector Plugins
Here are some popular Kafka Connect plugins:

Confluent Kafka Connect Plugin Search(opens in a new tab)
Amazon S3 Connector(opens in a new tab)
SQL JDBC Connector(opens in a new tab)
HDFS Connector(opens in a new tab)
HTTP Connector

## The Kafka Connect API

Kafka Connect REST API
Your Connector configuration can be Created, Updated, Deleted and Read (CRUD) via a REST API
You can check the status of a specific Connectors task(s) via the API
You can start, stop, and restart Connectors via the API
The choice of a REST API provides a wide-array of integration and management opportunities
Official REST API Documentation(opens in a new tab)
Quiz Question
Which of the following are accessible via the Kafka Connect API? (may be more than one answer)

## Key Connectors

Key Kafka Connectors
In this section, you will learn how to use some of the most common Kafka Connectors, such as the JDBC sink and source connector and the FileStream Source connector.

One of the most common uses of Kafka in many organizations is the routing of log data from many disparate microservices.

While some logging tools do support integrations with Kafka, one of the easiest and most ubiquitous ways to pipe log data into Kafka is to use Kafka Connect.

Kafka Connect can be configured to use a FileStream Source Connector to monitor changes in a file on disk. As data in that file changes, Kafka captures those changes and emits each new line as an event to a Kafka topic.

## JDBC Sinks and Sources

JDBC Sinks and Sources
JDBC = Java DataBase Connector. The JDBC API is used to abstract the interface to SQL Databases for Java applications. In the case of Kafka Connect, JDBC is used to act as a generic interface to common databases such as MySQL, Postgres, etc.
JDBC Sinks are a common way to move data into Kafka from existing databases. Once the data is available in Kafka, it can be used in stream processing operations to enrich data or provide insights that may otherwise be missing
JDBC Sources are a common way to move data out of Kafka to traditional SQL datastores. This is a common way of making stream processing insights available for more ad-hoc or batch querying.

## Kafka REST Proxy

Some applications, for legacy reasons or otherwise, will not be able to integrate a Kafka client directly. Kafka REST Proxy can be used to send and receive data to Kafka topics in these scenarios using only HTTP.

## REST Proxy Architecture

Like the rest of the Kafka Ecosystem tools, REST Proxy is written in Scala and Java and runs on the JVM. Because of this choice, REST Proxy can run just about anywhere.

REST Proxy is a simple HTTP web server and can be deployed to just one instance, or a cluster of many instances

REST proxy transforms structured JSON data from an application Kafka’s binary format and it can translate data from Kafka into a JSON payload for an application

REST proxy can optionally be made aware of Schema Registry so that it can help you manage your Avro schemas.

REST proxy is most useful when you really can’t use a Kafka client directly. If using a Kafka client is possible, it is strongly preferable to take that route.

Kafka clients not only help abstract some of the interaction with Kafka in a more efficient way than REST proxy, but they also have substantial speed and payload size benefits as well.

## Using REST Proxy

In this section, you will see first-hand how to produce and consume data with the Kafka REST Proxy. Though REST Proxy is conceptually similar to traditional Kafka clients, we will highlight some of the important differences and considerations.

REST Proxy Producer
POST data to /topics/<topic_name> to produce data(opens in a new tab)
The Kafka data may be POSTed in Binary, JSON, or Avro
When sending Avro data you must always include the schema data as a string
Always check your Content-Type header to ensure that it is correctly configured(opens in a new tab)
Content-Type is in the format application/vnd.kafka[.embedded_format].[api_version]+[serialization_format]
embedded_format is how the data destined for Kafka is formatted. Must be one of binary, json, or avro
api_version is the API version for REST Proxy -- this should always be v2 as of this writing
serialization_format has nothing to do with your Kafka data, this is how the actual data being sent to REST proxy is serialized. Only json is supported for now -- so always set this to json!
When using REST Proxy, always start by ensuring that the Content-Type is correctly set before running your code. A misconfigured Content-Type can lead to confusing and hard-to-debug errors.

## Consuming Data with REST Proxy

REST Proxy Consumer
POST to /consumers/<group_name> to create a consumer group(opens in a new tab)
POST to /consumers/<group_name>/instances/<instance_id>/subscriptions to create a subscription(opens in a new tab)
GET from /consumers/<group_name>/instances/<instance_id>/records to retrieve records(opens in a new tab)
Always check your Accept header to ensure that it is correctly configured(opens in a new tab)
Content-Type is in the format application/vnd.kafka[.embedded_format].[api_version]+[serialization_format]
embedded_format is how the data requested from Kafka is formatted. Must be one of binary, json, or avro
api_version is the API version for REST Proxy -- this should always be v2 as of writing
serialization_format has nothing to do with your Kafka data, this is how the actual data being received from REST proxy is serialized. Only json is supported for now -- so always set this to json!
DELETE to /consumers/<group_name>/instances/<instance_id>/subscriptions to unsubscribe a coinsumer(opens in a new tab)
Question 1 of 3
How can REST Proxy clients specify how much data to fetch?

Question 2 of 3
REST Proxy clients cannot choose offsets.

Question 3 of 3
REST Proxy clients do not need to unsubscribe from topics.

## Lesson Summary

Lesson Recap
In this lesson you learned how to use Kafka Connect to quickly integrate Kafka into a number of your existing data stores and workflows. We went hands-on with the JDBC and FileStream connectors and saw how to configure and deploy them. Next, we saw how REST Proxy can be used to bring Kafka to applications that can’t integrate native clients, but do have REST capabilities.

Glossary of Key Terms in this Lesson: (same as provided in beginning of lesson)
Kafka Connect - A web server and framework for integrating Kafka with external data sources such as SQL databases, log files, and HTTP endpoints.
JAR - Java ARchive. Used to distribute Java code reusably in a library format under a single file.
Connector - A JAR built on the Kafka Connect framework which integrates to an external system to either source or sink data from Kafka
Source - A Kafka client putting data into Kafka from an external location, such as a data store
Sink - A Kafka client remove data from Kafka into an external location, such as a data store
JDBC - Java Database Connectivity. A Java programming abstraction over SQL database interactions.
Task - Responsible for actually interacting with and moving data within a Kafka connector. One or more tasks make up a connector.
Kafka REST Proxy - A web server providing APIs for producing and consuming from Kafka, as well as fetching cluster metadata.