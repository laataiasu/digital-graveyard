---
title: "Redis, Base64, and JSON"
date: 2026-05-19
tags: [note]
publish_external: true
---

# Redis, Base64, and JSON

## Lesson Overview

Introduction

## Why are Redis and Base64 Important?

What is Redis?
Redis: A database used primarily for caching; this means it is optimized for fast reads and writes.

Why is Redis Important?
Why is Redis Important?

Why is Redis important?
Used by a lot of companies
Great for rapid prototyping of new applications
It can take you well beyond a proof of concept, all the way to production without having to create or maintain schemas
Later you can create a structured schema, and migrate to a relational database
You can stick with Redis, and create a nightly extract for reports
Redis is super fast in terms of read/write execution and in the development process

Base64 is the encoding of the Internet
Example: https://ordersometakeout.com?coordinates=ODIuODYyOMKwIFMsIDEzNS4wMDAwwrAgRQ==

Translation: Deliver my takeout to these coordinates: 82.8628° S, 135.0000° E

Base64 is used to make the text more readable by servers
In this example, the URL has a long encoded string after coordinates=
Decoded the string is the latitude and longitude where the takeout is needed
What is Base64?
Base64: An encoding format used by computers to transmit and store information.

## How an Expert Thinks About Redis and Base64

How an Expert Thinks About Parsing Base64

Redis, Fast Reads and Writes
Redis has become so wildly popular in large part due to its performance
Redis can read and write very quickly
This makes it very useful
 How do I recognize Base64?
How do I recognize Base64?

How can I recognize when something is encoded in Base64 format?
Base64 encoding is always a string of letters that is meaningless at first glance:

If you see a string of letters that don't spell anything intelligible, you are probably looking at Base64
Another tell-tale indicator is if the string ends with an equals sign
Last, try to decode it using a free online decoder like base64decode.org

## Manually Save and Read with Redis and Kafka

All Kafka Data Originates Somewhere
Any data you read from a Kafka Source, originates somewhere else. Data can come from:

Databases
IoT devices
Log Files
Applications
Other sources
From the Source to the Sink
From the Source to the Sink

From the Source to the Sink
When reading information from a Kafka topic, the path it follows can look something like this:

The source system transmits some data to Kafka
Kafka transmits that same data to a topic without modification
The sink, or receiving system, decodes the information that was encoded by the source system
The Sink Transforms the Data
Encoded	Decoded
{"key":"dGVzdGtleQ=="}	{"key":"testkey"}
{"element":"dGVzdHZhbHVl"}	{"element":"testvalue"}
Often the final consumer is responsible to transform the original system's data.
In the above example:

The first message has a key and an encoded value
The decoded value is "testkey"
The second message has a key called "element", and an encoded value
The decoded value is "testvalue" Once the sink has decoded the data, it can be used for processing
Typical Core Application
Typical Core Application

Typical Core Application
A Core Application is a system that is used to run critical processes for a business.

Here is a sample diagram where the core application stores data in a database. When given this scenario, we need to decide whether:

We want to modify the Core Application to transmit messages
Or instead, use the database as the source of messages

Direct Source or Indirect Source
When faced with the decision in this example of whether to stream directly from the source as a new project or to stream from the current database, should consider these implications:

When streaming directly from the source, the quality is high
This is because it is directly written by the Core Application
The Time to Value can be slower
Time to Value is the time it takes for a customer to benefit from your service
The time to value can be slower due to coordination with the main development team who supports ongoing work on the core application
The team often has several high priority initiatives
Regression risk of modifying the core application is moderate due to the critical role it has in performing business functions
Choosing an indirect source can make Time to Value lower
Reducing development strain on the core team CLICK
Reducing risk to the main application
An indirect source may have lower quality data because it is not directly produced by the core system
Banking Application
Banking Application

Banking Application
In this lesson, we will be dealing with a sample banking application that currently uses Redis for storing customer information.

Using Redis Data Types
Using Redis Data Types

Using Redis Data Types
Redis data is stored in various data types:

A sorted set is a Redis collection that includes a value and a score.
A score is a secondary index. We use zadd to add records to a sorted set.
A Redis key/value pair is a simple key with one value.
We use the set command to set the value.
Banking Example:
Let's discuss a phone number that is shared by multiple systems

A Banking Application writes the data as the system of record
The Customer Service System uses the information to help employees interact with customers
The Auto Dialer uses the phone number to make automated phone calls
Redis Writing to a Topic with a Source Connector
Redis Writing to a Topic with a Source Connector

Redis Writing to a Topic
In some scenarios, it may be useful for one of the reading applications to be updated immediately when a phone number changes.
For example, an autodialer making phone calls may be in violation of the law if it repeatedly calls a phone number recently placed on a Do Not Call list.
In this case, the secondary system, the Auto-Dialer should receive updates by subscribing to a Kafka topic.
Kafka Connect
Redis Source Connector Properties:

name=redis-config
connector.class=org.apache.kafka.connect.redis.RedisSourceConnector
tasks.max=1
topic=redis-server
host=redis
port=6379
password=notreally
dbName=0
Kafka Source Connector
What if there is no Kafka topic currently transmitting the phone number? This is where we would leverage a Kafka Source Connector:

We will configure Kafka Connect to Redis using a Redis Specific Source Connector
The way we configure the Redis Source Connector is by updating the properties file.
The file includes several properties
The topic is the topic where the data from Redis will be made available- in this case, the configured topic is called "redis-server"
The host, port, password, and dbName are used to establish a connection with Redis
What is Kafka Connect?
Kafka Connect: part of the Confluent Kafka distribution; it is the component responsible for providing a path from an external system (a source) to a Kafka topic or from a Kafka topic to an external system (a sink).

What is a Source Connector?
Source Connector: A Source Connector provides a connection from an outside system (a source) to a Kafka topic.

What is a Sink Connector?
Sink Connector: A Sink Connector provides a connection from a Kafka topic to an outside system (a source).

How a Source Connector Works
How a Source Connector Works

Here's how a Source Connector Works
Kafka starts the connector
The connector begins reading from the source
New records appear in the configured topic
Wireframe

Redis QuickStart
For resources on how to get started using Redis on your own system, see the Redis QuickStart Guide(opens in a new tab)

How to Install the Kafka Redis Source Connector
For more information on using the Kafka Redis Source Connector used in the lesson, see the Forked Kafka Connect Redis Repository(opens in a new tab) I used to set up your workspace.

## Exercise 1: Manually Save and Read with Redis and Kafka

Exercise: Manually Save and Read with Redis and Kafka
Working with Redis, it is extremely important to know how to use the Redis Command Line Interface (redis-cli) command. This command allows you to directly interact with the Redis database, by creating, updating, or deleting data.

Now that we have connected Redis with Kafka using the Kafka Connect Redis Source, we should verify that it is working correctly.

Task List

Important Note About Redis CLI
There is a know issue with connecting the terminal to the Redis CLI. The terminal may not be able to connect, although the Redis CLI will run fine in the background. In such cases, you can run the complete command as shown in the code block below.

```
/data/redis/redis-stable/src/redis-cli -a notreally PING
## You will get PONG. 
## Check the default server IP and port. They seem to be fine.
/data/redis/redis-stable/src/redis-cli -h 127.0.0.1 -p 6379 -a notreally PING
## Run any sample redis commands
/data/redis/redis-stable/src/redis-cli -a notreally -r 5 INCR mycounter
## Run any sample redis commands
/data/redis/redis-stable/src/redis-cli -a notreally keys *
```
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Parse Base64 Encoded Information

Parse Base64 with Pyspark

Bsae64 Table
Base64 Table

What is Base64?
Base64 is a system of representing binary data (8-bit data), in text format.
Each binary sequence has a letter.
It can be used to represent any binary data, including text and photographs.
Above is a table that shows the key for each letter, and what it represents. The padding character is an equals sign.

HTML Using Base64
```html
<div>
<p>Smiley Face</p>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" alt="Smiley Face" />
</div>
```
Explanation of HTML Using Base64
Sometimes document formatted messages contain encoded information:

It can be convenient to embed small images as text directly in an HTML document
In this example, a smiley face is embedded in the HTML snippet
The base64 encoded data is truncated here for brevity
Base64 Decoded Image showing a smiley face.
Base64 Decoded Image

This is the Base64 decoded smiley face displayed in a browser
Base64 Smiley Face
Base64 Smiley Face

This is what the entire Base64 string looks like in the HTML source
Redis Kafka Source vs Decoded Message
Message Sample

{
"key":"cHVtcGtpblBpZUluZ3JlZGllbnRz",
"existType":"NONE",
"ch":false,
"incr":false,           
"zSetEntries":[{"element":"cHVtcGtpbg==","score":0.0}],
"zsetEntries":[{"element":"cHVtcGtpbg==","score":0.0}]
}
In our Business Application, the Redis Source Connector uses Base64 to send new records to Kafka. Here is a message sample. Can you decode the encoded information?

Decoding Base64
To decode the element from the JSON above. Try this: from a Linux or Unix bash prompt, type: echo "cHVtcGtpbg==" | base64 -d

Message Decoded

{   
  "key":"pumpkinPieIngredients",
  "existType":"NONE",  
  "ch":false,  
  "incr":false,
  "zSetEntries":[{"element":"pumpkin","score":0.0}],
  "zsetEntries":[{"element":"pumpkin","score":0.0}]
}
Here is the message decoded from Base64 to plain text. The decoded key is "pumpkinPieIngredients". The decoded element is "pumpkin".

How would I do that in Spark?
unbase64: unbase64(encodedStreamingDF.reservation).cast("string")

Using unbase64
In this example, the encodedStreamingDF DataFrame has a field called "reservation". We are decoding it and then casting it to a string. This statement must be used in a spark SQL or DataFrame select.

More on PySpark SQL Functions
To see the full list of possible SQL functions that come with PySpark, see the PySpark SQL Module(opens in a new tab)

Wikipedia on Base64
For more information about Base64, see the Wikipedia Base64 Article

## Exercise 2: Parse Base64 Encoded Information

Exercise: Parse Base64 with Pyspark
Now that we have validated the Kafka Connect Redis Source, we can start writing code to extract data from the redis-server topic. Redis transmits its data to Kafka in Base64 encoded format. We will need to use the unbase64 method to decode it in our Spark application.

Write a pyspark application
Read a stream from the redis-server kafka topic containing Base64 encoded data
Write the dataframe from kafka to the console with the key, value fields
Base64 decode the dataframe
Write the decoded stream to the console
Start spark master, and worker
Deploy and run the pyspark application

Task List

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Sink a Subset of JSON

Select Using Spark
There are two main functions used for selecting data in Spark Streaming: .select and spark.sql.

.select
truckReservationDF.select("reservationId", "truckNumber")
Here is an example of using the.select method to select the columns "reservationId" and "truckNumber". Notice the .selectfunction accepts from one to many column names separated by a comma.

spark.sql
spark.sql("select reservationId, truckNumber from TruckReservation")
This is the same select using spark.sql. Notice the spark.sql function accepts valid SQL statements.

Spark SQL Functions
Function	Purpose
to_json	Create JSON
from_json	Parse JSON
unbase64	Base64 Decode
base64	Base64 Encode
split	Separate a string of characters
Spark SQL Functions
Here are some useful Spark SQL Functions. These can be used within the spark.sql function or within the .select function:

to_json and from_json are for working with JSON
unbase64 and base64 are for working with Base64 encoded information.
split is for separating a string of characters
We have worked with to_json, from_json, unbase64 so far.

Using the Split Function - First Name
Sample Data

{
"customerName":"June Aristotle",
"email":"June.Aristotle@test.com",
"birthDay":"1948-01-01"
}
Example Code

split(customerStreamingDF.customerName," ")\
.getItem(0) \
.alias("firstName") \
Output

{
"firstName": "June"
}
Explanation of First Name
In this example we are parsing a DataFrame field "customerName" which contains both a first and the last name (ex: June Aristotle):

Using split we extract both first and last names.
We then call .getItem to get the 0th element.
We then call .alias to create a field called "firstName".
How would you approach this same data to get the customer's email provider?

Using the Split Function - Email Domain
Sample Data

{

"customerName":"June Aristotle",

"email":"June.Aristotle@test.com",

"birthDay":"1948-01-01"

}
Example Code

split(customerStreamingDF.email,"@") \

.getItem(1) \

.alias("emailDomain") \
Output

{

"emailDomain": "test.com"

}
Explanation of Email Domain
To get the email domain:

We call split passing the "customerStreamingDF.email" field, and then the @ symbol.
We then get the element from position 1, which will be the email domain.
So we call the .alias function to create an alias called "emailDomain".
Using to_json
You have a DataFrame called truckStatusDF that contains several fields including "statusTruckNumber". You want to prepare to sink the DataFrame by converting it to JSON. Kafka also expects a key for every message:

truckStatusDF \
.selectExpr(
"cast(statusTruckNumber as string) as key", 
"to_json(struct(*)) as value"
) 
Notice the following:

We first call .selectExpr
Within the select expression, we are creating two expressions
The key field
The value field
We use the to_json function
Sink it to Kafka
Now that we got the key and value fields in a DataFrame, you can sink to a Kafka topic:

truckStatusDF \
.selectExpr(
"cast(statusTruckNumber as string) as key",
"to_json(struct(*)) as value"
) \
.writeStream \
.format("kafka") \
.option("kafka.bootstrap.servers", "kafkabroker.besthost.net:9092")\
.option("topic", "truck-status")\
.option("checkpointLocation","/tmp/kafkacheckpoint")\
.start()\
.awaitTermination()
Notice the following:

After the select expression ends, we call .writeStream
The bootstrap server (the broker) is kafkabroker.besthost.net
The bootstrap port is 9092
The topic is truck-status
We specified a writable path on the Spark Worker server for the checkpointLocation
More on PySpark SQL Functions
To see the full list of possible SQL functions that come with PySpark, see the PySpark SQL Module

## Walkthrough 3: Sink a Subset of JSON Fields

Steps in the walkthrough video:

(0:02) ps -ef command to check if Spark and Kafka processes are running
(0:18) import required Spark SQL functions and types
(0:24) define Kafka message schema using StructType
(0:31) connect to Spark through SparkSession and read Kafka stream to a dataframe
(0:41) cast dataframe to JSON string
(0:49) create a temporary streaming view to enable query
(1:00) query data from the temporary streaming view into a new dataframe
(1:20) decode Base64 data from Redis
(1:38) store the decoded data into a new dataframe
(1:55) store the SQL query into a new dataframe
(2:04) write the new dataframe into a Kafka topic
(3:19) output from Kafka topic to the console
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Optional Long Walkthrough with Troubleshooting

Note: In the video above the instructor also added customerName to the output, but that is not required.

## Exercise 3: Sink a Subset of JSON

Sink a Subset of JSON
There are a few customer fields we are looking for from the redis-server server:

account number
location
birth year
We want to combine those fields into one JSON message and transmit them in a customer-attributes topic.

Task List

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Edge Cases

Edge Cases

What If I subscribe to the wrong Kafka topic?
What if you subscribe to the wrong Kafka topic in your Spark application and then correct it later? You may run into the error:

Current committed Offsets: {KafkaV2[Subscribe[topic-name]]: {'wrong-topic-name':{'0':0}}}

Some data may have been lost because they are not available in Kafka any more; 
either the data was aged out by Kafka or the topic may have been deleted
before all the data in the topic was processed. If you don't want your 
streaming query to fail on such cases, set the source option
"failOnDataLoss" to "false."
In this case, simply add the option failOnDataLoss to your .writeStream as below:

checkinStatusDF.selectExpr("cast(statusTruckNumber as string) as key", "to_json(struct(*)) as value") \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("topic", "checkin-status")\
    .option("checkpointLocation","/tmp/kafkacheckpoint")\
    .option("failOnDataLoss","false")\    
    .start()\
    .awaitTermination()

## Bringing it all Together Walkthrough

Please note that the video below is a longer version with troubleshooting.

Steps in the walkthrough video:

(0:04) overview of this final walkthrough
(0:25) ps -ef command to check if Spark and Kafka processes are running
(0:33) start Kafka server and worker
(1:30) create two Kafka schema for reservation and payment
(3:01) start a Spark session
(3:17) create a dataframe to read streaming data from Redis database
(3:42) cast dataframe from binary to string to make it readable
(4:05) extract Base64 data from JSON payload into a temporary view
(4:40) use Spark SQL to select keys from Redis events
(5:23) decode Base64 data and case as a string for both reservation and payment dataframes
(6:18) apply filter to select non null values on both dataframes
(9:45) perform outer joins on both dataframes into a new dataframe
(10:33) output the new database to the console
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Final Exercise 4

Decode and Join two Base64 Encoded JSON DataFrames
Now that you have learned how to use unbase64 to extract useful data, let's take things a step further. There is often a need to join data from separate data types. In this exercise we join data from the customer and the customerLocation message types.

Decode and Join two Base64 Encoded JSON DataFrames
Click the button to start Kafka: Start Kafka
Start the spark master and spark worker
From the terminal type: /home/workspace/spark/sbin/start-master.sh
View the log and copy down the Spark URI
From the terminal type: /home/workspace/spark/sbin/start-slave.sh [Spark URI]
Start the Banking Simulation: Start Banking Simulation
Complete the current-country.py python script
Submit the application to the spark cluster:
From the terminal type: /home/workspace/submit-current-country.sh
Watch the terminal for the values to scroll past (may take 2-3 minutes)

Task List

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Lesson and Course Recap

Lesson Review
Lesson Structure
Lesson Structure

Learning Objectives Review
After finishing this lesson you should be able to:

Manually Save and Read from Redis
Parse Base64 Encoded Information
Sink a Subset of JSON
Additional Resources
How to Install the Kafka Redis Source Connector
For more information on using the Kafka Redis Source Connector used in the lesson, see the Forked Kafka Connect Redis Repository(opens in a new tab) I used to set up your workspace.

Also, here is the Original Redis Source Connector Repository(opens in a new tab) we based it on.

More on PySpark SQL Functions
To see the full list of possible SQL functions that come with PySpark, see the PySpark SQL Module(opens in a new tab)

Wikipedia on Base64
For more information about Base64, see the Wikipedia Base64 Article(opens in a new tab)

More on PySpark SQL Functions
To see the full list of possible SQL functions that come with PySpark, see the PySpark SQL Module(opens in a new tab)

Course Review
Course Review

Where we are in the course
Let's look at the course overview. You just learned about Redis, Base64, and JSON.

Next you will get to work with a real-world challenge to evaluate human balance. You'll apply techniques from the course to a streaming analytics application. I hope you are ready to put your skills to the test.

## Glossary

Glossary
Term	Definition
Base64	Base64 is an encoding format used by computers to transmit and store information.
Kafka Connect	Kafka Connect is part of the Confluent Kafka distribution; it is the component responsible for providing a path from an external system (a source) to a Kafka topic or from a Kafka topic to an external system (a sink).
Redis	Redis is a database used primarily for caching; this means it is optimized for fast reads and writes.
Source Connector	A Source Connector provides a connection from an outside system (a source) to a Kafka topic.

