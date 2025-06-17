# KSQL

## Glossary of Terms for Lesson

Glossary of Key Terms You Will Learn in this Lesson
Kafka Streams - A Java library for constructing stream processing applications. KSQL translates SQL statements to Kafka Streams applications.
User Defined Function (UDF) - An extension to the SQL capabilities of KSQL written by the user. For KSQL, these are written in Java.
Key (KSQL) - Data that uniquely identifies the value contained in this data message relative to other pieces of data in the stream. For example, a user_id may uniquely identify a user object.
Session Windowing (KSQL) - A system that keeps track of when the last time a particular key was seen. When a new record with the same key arrives, the difference between the timestamps is calculated. If the difference is larger than a defined session window, then a new window is started for that session. If the difference is less than the defined session window, the new record is added to the existing window.

## Introduction to KSQL

Intro to KSQL
KSQL provides a SQL-like interface to transform Kafka Topics into streams and tables.

Joins, aggregates, filtering, and other forms of data manipulation can then be expressed over these streams and tables.

## KSQL Architecture

KSQL Architecture
KSQL is a Java application built on top of the Kafka Streams Java stream processing library. KSQL is a web-server with a REST API that accepts incoming or preconfigured requests containing SQL-like commands. These commands are translated by the KSQL server into the equivalent Kafka Streams application and then executed.

Users can interact with KSQL via a REST API, its dedicated CLI, or predefined SQL files.

KSQL was built by Confluent and released in 2018, in an attempt to bring stream processing to more users.

KSQL is built and open-sourced by Confluent, the major contributors and maintainers to the Apache Kafka open source project.

KSQL itself is a web server that accepts incoming HTTP REST calls to configure underlying Kafka Streams components to execute the stream processes described in our SQL queries.

KSQL uses a Kafka topic as a changelog, and RocksDB to store local state on every node where KSQL is deployed.

Question 1 of 2
KSQL is built on which stream processing framework?

Question 2 of 2
How can you interact with KSQL? (may be more than one answer)

## KSQL vs Traditional Frameworks

KSQL vs. Traditional Frameworks
Pros
It is often simpler to use KSQL and SQL than to build and deploy an entire application
KSQL is typically a better fit for rapid experimentation and exploration than a full stream processing application
KSQL doesn’t require a particular programming language, like Python for Faust, or Java for Kafka Streams
KSQL already comes bundled with standard logs, metrics, and tooling for you to use, so you don’t have to build it yourself
Cons
SQL does not always best capture certain types of data manipulation or remapping scenarios
Can’t just use whatever other libraries you want like you can with Faust
However, KSQL does allow User Defined Functions (UDFs), written in Java
Question 1 of 2
Which of the following are reasons you might choose to use KSQL over a traditional streaming framework? (may be more than one answer)

Question 2 of 2
Which of the following are reasons you might choose to use a streaming framework like Faust over KSQL? (may be more than one answer)

## Topics --> Tables & Streams

Before using tables or streams in KSQL, one or more of our existing input Kafka topics need to transform into a KSQL table or stream.

Ask KSQL to show the topics that it is aware of by using the SHOW TOPICS command
Show topics displays all of the available topics on the broker
A Kafka topic always underlies the stream or tables that are created

## Creating a Stream

Stream Creation
There are two options for creating streams in KSQL:

Define the stream attributes and types with a create statement
Create a stream with a select that excludes or modifies data from another stream
Creating Streams from an underlying topic requires you to specify column names and their types

You must also specify the serialization format as one of JSON, AVRO, or DELIMITED (csv)
You must also specify the underlying topic name
You may create a stream from another existing stream with CREATE STREAM <stream_name> AS SELECT …
For Additional resources regarding KSQL stream creation, check out the following links:

KSQL Create Stream Documentation(opens in a new tab)
KSQL Create Stream from SELECT documentation

## Creating a Table

Table Creation
Creating Tables from an underlying topic requires you to specify column names and their types
You must also specify the serialization format as one of JSON, AVRO, or DELIMITED (csv)
You must also specify the underlying topic name
You may create a table from another existing table with CREATE TABLE <table_name> AS SELECT …

## Hopping and Tumbling Windowing

Hopping and Tumbling Windowing
KSQL supports Tumbling windows with the WINDOW TUMBLING (SIZE <duration>) syntax(opens in a new tab)
KSQL supports Hopping windows with the WINDOW HOPPING (SIZE <duration>, ADVANCE BY <interval>) syntax(opens in a new tab)
Question 1 of 2
Which parameters are required to specify a Hopping Window in KSQL? (more than one answer)

Question 2 of 2
How might you approximate a Sliding Window in KSQL?

## Session Windowing

Session Windowing - Key Points
Keeps track of differences between the time a key was last seen and the current key arrival time.
If the difference between the time a key was last seen and the current key arrival time, for two records with the same key, is larger than the session window length defined, a new window is started.
If the difference between the time a key was last seen and the current key arrival time, for two records with the same key, is less than the session window length, the record is added to the current window, and the session expiration time is started anew.
Session expiration denotes that the full session period begins again
KSQL Session window documentation(opens in a new tab)
How many events in a Session Window?
If we used a session window of 15 minutes and the following actions occurred, how many events would have occurred in the most recent window?

HH:MM:SS	Action
01:10:10	Click
00:59:09	Click
00:37:47	Click
00:23:37	Click
00:17:09	Click
00:13:17	Click
00:10:48	Click
00:09:40	Click
00:04:38	Click
00:01:03	Click
00:00:00	Click
Tip: The above timestamps count down in time. A timestamp of 00:00:00 just occured, and a timestamp of 10:30:30 occurred 10 hours, 30 minutes, and 30 seconds ago.

Enter your response here
Quiz Question
Which of the following best describes a Session Window?

## Aggregating Data

Group bys are another very useful form of aggregation. The output of a group by in KSQL is always a table.

Key Takeaways
Use GROUP BY to create aggregations in KSQL(opens in a new tab)
GROUP BY always creates a KSQL Table
KSQL supports aggregations like COUNT, MAX, MIN, SUM, TOPK, HISTOGRAM and more(opens in a new tab)
Question 1 of 2
What types of aggregations are available in KSQL? (Checkmark all responses that apply)

Question 2 of 2
The result of a group-by is always a table.

## Lesson Summary

In this lesson you learned:

How KSQL is an excellent tool for rapid iteration and deployment of Stream Processing applications
That KSQL can GROUP BY aggregate data
That KSQL supports HOPPING, TUMBLING, and SESSION windows
That KSQL supports JOIN operations to merge two or more streams
Glossary of Key Terms for this Lesson (same as glossary at beginning of lesson):
Kafka Streams - A Java library for constructing stream processing applications. KSQL translates SQL statements to Kafka Streams applications.
User Defined Function (UDF) - An extension to the SQL capabilities of KSQL written by the user. For KSQL, these are written in Java.
Key (KSQL) - Data which uniquely identifies the value contained in this data message relative to other pieces of data in the stream. For example, a user_id may uniquely identify a user object.
Session Windowing (KSQL) - A system that keeps track of when the last time a particular key was seen. When a new record with the same key arrives, the difference between the timestamps is calculated. If the difference is larger than a defined session window, then a new window is started for that session. If the difference is less than the defined session window, the new record is added to the existing window.