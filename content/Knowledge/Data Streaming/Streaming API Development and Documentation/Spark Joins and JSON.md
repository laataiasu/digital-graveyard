---
title: "Spark Joins and JSON"
date: 2026-05-19
tags: []
---

# Spark Joins and JSON

## Why JSON is important

Why are JSON and Joins Important in Spark?
Could you write streaming spark applications without using JSON?
Do you need to use Joins?
In this lesson, we will discuss the details of when and why we would use both

Putting it All Together
In the previous lesson, you learned how to write a basic streaming application
In this lesson, you will learn how to read streaming JSON messages
Streaming messages usually are JSON formatted
Parsing JSON in Spark
If you are using a version before Spark 3.0.0, JSON field inference is not available
In this lesson, you will learn how to create a JSON schema based on an expected format
You will learn how to explicitly parse JSON into independent fields in a temporary view
Joins allow you to merge data from separate DataFrames into a single DataFrame just like you would in a SQL Join

Explore Streaming Data
JSON has become the de facto standard for data exchange
You will work extensively with JSON throughout the rest of the course
We will explore multiple JSON payloads streaming from Kafka
Providing streaming data to others is best done through JSON format
What is JSON?
JSON: JavaScript Object Notation; originally created to serialize objects in JavaScript, a data serialization standard consisting of keys and values (ex: { "firstName":"Sally", "lastName":"Smith"}).

## Why JSON and joins are important

Why JSON is important? Why are joins important?

JSON is Universally Used to Transmit Data
It is simple to read and write
Almost any system will accept it
The JSON format can be used to describe most record types
Joining Streaming Data is Typically Difficult
Joining Streams Typically Difficult

Joining Streaming Data is Typically Difficult
Usually joining streams of data is not straightforward
Without built-in streaming join functionality, you will have to write code to cache or query extra data
This can be very IO intensive because the data is often stored in very large tables, and may be difficult to index
The time to retrieve the secondary data is often prohibitive

## Parse a JSON Payload

Parse a JSON Payload
Wireframe

Puzzle Pieces are your JSON Fields
Puzzle Pieces JSON Fields

Creating a sink can be compared with assembling a puzzle
The JSON fields are the pieces to the puzzle
Just as the picture of the finished puzzle will help you decide where pieces belong, seeing the end goal for your sink format guides your programming

Searching for Pieces of the Puzzle
It is important to know what the data looks like in the sources you will be joining so you know which fields will come from which streams
Try to get samples payloads of each source as early as possible so you can create a picture of the complete sink and where all the pieces might come from
It is ok if the payload format is not 100% finalized at first
However, if fields change in the sources that are used in your join, the format of the final output will be affected
Examine Some Sample Data
{"truckNumber":"5169", "destination":"Florida","milesFromShop":505,"odomoterReading":50513}

Formatted JSON
{
  "truckNumber":"5169", (Type: String)
  "destination":"Florida", (Type: String)
  "milesFromShop":505, (Type: Integer)
  "odomoterReading":50513 (Type: Integer)
}
Pop Quiz: How would this JSON data look when properly formatted?
{"answerId":98333113,"questionId":13253463,"isSolution":true,"quizId":438934543,
"body":"50 States"}
Pop Quiz Answer
{
"answerId":98333113,
"questionId":13253463,
"isSolution":true,
"quizId":438934543,
"body":"50 States"
}
What is StructType?
StructType: a Spark class that defines the schema for a DataFrame

StructType Code
JSON Sample: {"firstName":"Muhamed","lastName":"Adel"}
personSchema = StructType (
  [
    StructField("firstName",StringType()),
    StructField("age",IntegerType())
  ]
)
StructType Important Points
Using an array of StructFields, you create your StructType
Each StructField correlates with a JSON field
What is a StructField?

StructField: a Python class used to create a typed field in a StructType.

Example: StructField("truckNumber", StringType())

StructField Code
JSON Sample: {"firstName":"Aarthi","lastName":"Singh"}

StructField("firstName", StringType())
StructField("age", IntegerType())
StructField Important Points
The field name needs to match your JSON field
Make sure to define the data type
Creating a StructType Schema in Action

```
# Sample JSON: 
# {
#    "truckNumber":"2352523",
#    "destination":"Accra",
#    "milesFromShop":100,
#    "odometerReading": 99789
# }
```

truckStatusSchema = StructType (   
        [
          StructField("truckNumber", StringType()),        
          StructField("destination", StringType()), 
          StructField("milesFromShop", IntegerType()),  
          StructField("odometerReading", IntegerType())
        ]
)   
Explanation of Creating a StructType Schema in Action
You define a StructType by instantiating it in code
List the array of fields by name and type
Notice the field names in this example correspond with the JSON fields earlier
Parsing JSON in Action

```
# Sample JSON: 
# {
#    "truckNumber":"2352523",
#    "destination":"Accra",
#    "milesFromShop":100,
#    "odometerReading": 99789
# }
```

truckStatusSchema = StructType (   
        [
          StructField("truckNumber", StringType()),        
          StructField("destination", StringType()), 
          StructField("milesFromShop", IntegerType()),  
          StructField("odometerReading", IntegerType())
        ]
) 

vehicleStatusStreamingDF \
  .withColumn("value",from_json("value",truckStatusSchema))      
Explanation of Parsing JSON in Action
Once you have defined the schema, you are ready to use it to parse a field containing JSON:

withColumn

In this example, the DataFrame is called vehicleStatusStreamingDF
We parse the JSON field called value, using the .withColumnmethod
.withColumn** **creates or overwrites an existing column
from_json

Because the value column already exists, we are overwriting it
The new value is assigned using the from_json function
The from_json function uses the column name containing the JSON, value, and the truckStatusSchema
How to call .withColumn
vehicleStatusStreamingDF \
  .withColumn("newFieldName", "data Value")
Passing Parameters using .withColumn
The new or existing column name we are assigning data to
The data we want to assign
How to call from_json
from_json("columnName", structSchemaVariable)

Passing Parameters using from_json
The column name we want to extract JSON out of
The variable which holds the StructType defining our schema

## Walkthrough 1: Parse a JSON Payload

The workspaces in this lesson progressively build on the results of the previous walkthrough or exercise. To assist students, all workspaces in this lesson contain the preceding workspace's solution set(s) that are needed to successfully execute the next step. To avoid errors, we highly encourage students to use the file names provided in the workspace guide.

Steps in the walkthrough video:

(0:07) ps -ef command to check if Spark processes are running
(0:22) import required Spark SQL functions and types
(0:35) define Kafka message schema using StructType
(0:40) connect to Spark through SparkSession and read Kafka stream to a dataframe
(1:13) extract the JSON into a temporary view and use the schema to serialize JSON
(1:50) store the SQL query into a new dataframe
(2:03) output the new dataframe on the console
Important: Whenever a video references starting Kafka, please follow the instructions below.
Parse a JSON Payload Into Separate Fields for Analysis
If you just started the workspace, from the console type: /home/workspace/startup/startup.sh to start Kafka and the Trucking Simulation
If you just started the workspace, start the spark master and spark worker
From the terminal type: /home/workspace/spark/sbin/start-master.sh
View the log and copy down the Spark URI
From the terminal type: /home/workspace/spark/sbin/start-slave.sh [Spark URI]
Complete the vehicle-status.py python script
Submit the application to the Spark cluster:
From the terminal type: /home/workspace/spark/submit-vehicle-status.sh
Watch the terminal for the values to scroll past (can take up to 2 minutes)
Check the Solution File
To access the solution .py file, click on File (in the top menu of the workspace), click Open From Path and enter /vehicle-status.solution.py
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Optional Long Walkthrough with Troubleshooting

## Exercise 1: Parse a JSON Payload

Exercise: Parse a JSON payload into separate fields for analysis
In this exercise, we will be working with a Kafka topic created to broadcast deposits in a bank. Each message contains the following data:

account number
amount
date and time
You will create a view with this data so you can query it using spark.sql.

Task List

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Solution 1: Parse a JSON Payload

Solution: Parse a JSON Payload for Analysis

Task List

Optional Long Solution with Troubleshooting

## Join Streaming Dataframes from Different Datasources

Join Streaming Dataframes from Different Datasources

Joining Data Delivers Value
Joining Data Delivers Value

Joining Data Delivers Value
One of the main purposes of writing a streaming application is to accept data from multiple sources
Joining on streaming data can be very powerful because typically the data is changing very rapidly
Creating a combined view of the data as it changes together adds tremendous value
Plan Your Sink
Plan Your Sink

Plan Your Sink
Now that you have looked at your source data, it's time to start planning the sink:

What is the final goal?
What is the format of the data you plan to send to the other system?
Often the person who knows the answer is someone on another team who needs the data you provide
Other times, there is no definitive answer, so you create your own format
Data Mocking
Data Mocking

Data Mocking
As you interview system owners from other teams it will be important to discuss the fields they need
Once you have discussed the data that is needed you can create a mock data sample
Ask for feedback on the mock data sample before writing the spark application
This will give you the chance to refine the data model
What is Data Mocking?
Data Mocking: to create a representative sample of an undefined source of data (ex: we mocked the data so they could see it).

Create the Destination Format
{
    "customerId": 213923498,
    "originatingAirport": "LAX",
    "destinationAirport": "PDX"
}
Remember
Sometimes only a few critical fields are what is needed:

In this example, there are three fields: "customerId", "originatingAirport", and "destinationAirport"
It is a common practice to include all available fields, but this can be risky
The downstream consumers may rely on fields that are subject to change
The fewer fields you transmit, the less likely it is that something will change
Identify Redundant Data Fields
Identify Redundant Data Fields

Identify Redundant Fields
Now that you have designed the format for your sink, you should decide where the data will come from:

Certain fields will be present in multiple sources
Some data sources are less authoritative than others
Try to identify which sources are more authoritative for certain types of data
In the above diagram, Customer ID is present in all three sources. This could be helpful for joining customer data as it is generated with departure data.

The flight number is present in both the Flight Data and Departure Data sources. This could be helpful for joining Flight Data and Departure Data as it is generated. The Customer Email field is probably more authoritative in the Customer source than the Flight source.

Find Data Source Fields
Find Data Source Fields

Find Data Source Fields
Once you have identified redundant fields, you should be sure you have all your bases covered:

Make sure every field you need in your destination data sink has been identified
In the above diagram, the first payload has the "customerId"
The second payload contains the "originatingAirport" and "destinationAirport" fields
We will need both payloads to create the final sink which includes the "customerId", "originatingAirport"*, and "destinationAirport" fields
Identify Join Fields
Identify Join Fields

Identify Join Fields
Before we write our join, we need to ensure we have a common field to join on:

I may see all the fields I need in various sources
But unless there is a common field, the join won't work
In this example, there are four Data Fields: Reservation, VehicleStatus, Checkin, and Payment
They each have unique data
There are some common fields that connect these together. What are they?

Join Fields Identified
Join Fields Identified

Join Fields Identified
Reservation, VehicleStatus, and Checkin all have a field called "truckNumber".

Reservation, Checkin, and Payment all contain a field called "reservationId".

In theory, this example would make joining possible between any two data types with the same field.

New DataFrame with joined fields
New DataFrame with joined fields

New DataFrame with joined fields
Joining the Reservation and the VehicleStatus DataFrames we now have the ReservationWithStatus DataFrame with all the data from both DataFrames.

What is a Join?
Join: to connect two data collections by referencing a field they share in common; or the state which connects two data collections by referencing a common field.

Verifying Data Standards
It is a very good idea to look at samples of each DataSource to see if fields are standardized. Unfortunately, it is common to use the same field name to mean different things, especially in different systems.

Look at the four Data Types below. Do you see anything different about them?

Reservation
{
  "reservationId":"1603561552180",
  "customerName":"Chuck Jones",
  "truckNumber":"2416",
  "reservationDate":"2020-10-24T17:45:52.180Z"
}
VehicleStatus
{
  "truckNumber":"5169",
  "destination":"Florida",
  "milesFromShop":505,
  "odometerReading":50513
}
CheckIn
{
   "reservationId":"00001601485848310",
   "locationName":"New Mexico",
   "truckNumber":"3944",
   "status":"In"
}
Payment
{
  "reservationId":"9856743232-L",
  "customerName":"Frank Aristotle",
  "date":"Sep 29, 2020, 10:06:23 AM",
  "amount":"946.88"
}
Data Differences Identified
Reservation, Checkin, and Payment all format the "reservationId" differently
After examining Reservation and Checkin it appears the main difference is the leading zeros
Until further data samples are obtained for Payment, it is hard to say if the "reservationId" is the same field, due to the significant difference in format
Reservation
"reservationId":"1603561552180"

CheckIn
"reservationId":"00001601485848310"

Payment
"reservationId":"9856743232-L"

Identify the Common Field
In this example, we want to join the two payloads shown
What is the common field we can join on?
Ticketing
{
   "customerId" : 213923498,
   "ticketId" : 0922345566,
   "flightNumber": 573819429
}
Flight Info
 {
  "flightNumber": 573819429,
  "originatingAirport": "LAX",
  "destinationAirport": "PDX"
}
Common Field Identified
The common field in both Ticketing and Flight Info is "flightNumber":

Ticketing
"flightNumber": 573819429

Flight Info
"flightNumber": 573819429

Using a Column Alias in Spark SQL
Using "select columnName as columnNameAlias" can be useful when joining two DataFrames. Usually they will both share at least one column. If you don't use aliases, you may run into errors when trying to join them together.

Example:

flightInfoDF=spark.sql("select flightNumber as flightInfoFlightNumber from FlightInfoView")
What does calling .join do?
join: A function called on a DataFrame that accepts the right hand of the join (another Dataframe), and the join expression (includes the fields to join on). This is the Spark function that implements the concept of joining two different groups of data.

Example:

checkinStatusDF = vehicleStatusSelectStarDF \
.join(vehicleCheckinSelectStarDF, expr("""
    statusTruckNumber = checkinTruckNumber
"""                                                                                 
))
Calling .join Key Points
You will need two DataFrames defined already
You will want to avoid using the same column names in each DataFrame to avoid collisions
Using field aliases in each DataFrame where needed (ex: "truckNumber as statusTruckNumber")
The default join type is a left outer join
Additional Resources
For more reading on joining Spark Streams, check out the Join Section in the Official Spark Streaming Guide

## Walkthrough 2: Join Streaming Dataframes

The workspaces in this lesson progressively build on the results of the previous walkthrough or exercise. To assist students, all workspaces in this lesson contain the preceding workspace's solution set(s) that are needed to successfully execute the next step. To avoid errors, we highly encourage students to use the file names provided in the workspace guide.

Steps in the walkthrough video:

(0:13) import required Spark SQL functions and types
(0:24) define Kafka first schema for vehicle status
(0:30) define Kafka second schema for "vehicle-checkin"
(0:42) create the first dataframe to read vehicle status stream
(1:43) create the second dataframe to read vehicle checkin stream
(2:08) join both dataframes into a new dataframe
(2:29) output the new dataframe on the console
Join Streaming Dataframes from Different Sources
If you just started the workspace, from the console type: /home/workspace/startup/startup.sh to start Kafka, and the Trucking Simulation
If you just started the workspace, start the spark master and spark worker
From the terminal type: /home/workspace/spark/sbin/start-master.sh
View the log and copy down the Spark URI
From the terminal type: /home/workspace/spark/sbin/start-slave.sh [Spark URI]
Complete the vehicle-checkin.py python script
Submit the application to the spark cluster:
From the terminal type: /home/workspace/spark/submit-vehicle-checkin.sh
Watch the terminal for the values to scroll past (can take up to 2 minutes)
Check the Solution File
To access the solution .py file, click on File (in the top menu of the workspace), click Open From Path and enter /vehicle-checkin.solution.py
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Optional Long Walkthrough with Troubleshooting

## Exercise 2: Join Streaming Dataframes

Exercise: Join Streaming DataFrames from Different Datasources
In this exercise you will be working with the deposit topic and a topic that contains customer information. Each customer message contains the following information:

customer name
email
phone
birth day
account number
customer location
You will join the information from the bank deposit topic and the customer topic to create a view that contains the customer and the deposit.

Task List
Write a pyspark application

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Solution: Join Streaming Dataframes

Solution: Join Streaming Dataframes from Different Datasources

Optional Long Solution with Troubleshooting

Task List

## Sink to Kafka

Write a Streaming Dataframe to Kafka with Aggregated Data

Sinking Data to Kafka
Sinking Data to Kafka

Sinking Data to Kafka
In order to sink to Kafka, you need to have something to sink
That will be a Streaming DataFrame you create
When we sink to Kafka we need to identify the topic we will be sending data to
Then it is just a matter of writing a few lines to sink your DataFrame
They will look similar to what you have done to sink to the console
Sink to Kafka in Practice
 vehicleStatusDF\
 .selectExpr("cast(statusTruckNumber as string) as key", "to_json(struct(*)) as value") \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("topic", "vehicle-status-changes")\
    .option("checkpointLocation","/tmp/kafkacheckpoint")\
    .start()\
    .awaitTermination()
Explanation of Sink to Kafka
After creating a view, you have something unique to offer to other systems. Let's learn how to share that data via a Kafka topic:

Use a select expression on the DataFrame to cast the key, and structure your fields as JSON
Be sure to pass the Kafka bootstrap servers parameter
Last sink the DataFrame to your new Kafka topic, using the writeStream
Now any Kafka consumer can access your data by subscribing to the topic called vehicle-status-changes.

What does calling .selectExpr do?
selectExpr: A function called on a DataFrame to pass a select expression.

Example:.selectExpr("cast(statusTruckNumber as string) as key", "to_json(struct(*)) as value")

Select Expression Key Points
We are creating a DataFrame with two fields
Each parameter defines a field
When streaming to Kafka, the fields should be called "key" and "value"
The key is a unique identifier
The value contains the JSON
What does calling to_json do?
to_json: A Spark SQL function that accepts multiple columns containing JSON and creates a single column containing the JSON formatted data.

Example: to_json(struct(*)) as value)

Using to_json Key Points :
We use to_json in a select expression on a DataFrame
First, pass the fields you want to be serialized
Then alias them as a field
When passing the JSON to Kafka we want the field name to be "value"
What is the checkpointLocation?
checkpointLocation: an option passed when connecting to Kafka to send data to a topic; must be a writeable filesystem path for the Spark Worker.

Example: .option("checkpointLocation","/tmp/kafkacheckpoint")

Passing checkpointLocation Key Points:
When streaming to Kafka, you must define the same options when reading from Kafka
You also need an additional option: checkpointLocation
This needs to be a writeable path
It is used by Spark to offload some data to disk for recovery
Kafka Integration Resources
For more information on integrating Spark with Kafka, see the official Kafka Integration Guide

## Walkthrough 3: Sink to Kafka

The workspaces in this lesson progressively build on the results of the previous walkthrough or exercise. To assist students, all workspaces in this lesson contain the preceding workspace's solution set(s) that are needed to successfully execute the next step. To avoid errors, we highly encourage students to use the file names provided in the workspace guide.

Using the Kafka Console Consumer Command
So far we have mainly used the console as our sink. That is perfect for beginning a new data pipeline, as it helps us see the data produced. However, ultimately you will want to send the data to another system. Often, that will be done using a kafka sink.

There is a very useful tool installed with Confluent Kafka called the kafka-console-consumer command. To use this tool, you just type the path to the tool. So for example in our workspace the command looks like this:

/data/kafka/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic gear-position-updates

Steps in the walkthrough video:

(0:03) ps -ef command to check if Spark processes are running
(0:22) continue the exercise from walkthrough 2 solution and replace output to console to Kafka sink
(0:46) cast dataframe to JSON string
(1:14) configure Kafka writeStream and its options
(1:36) start the operations to sink to Kafka
(2:46) output from Kafka sink to the console
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Optional Long Walkthrough with Troubleshooting

## Exercise 3: Sink to Kafka

Exercise: Write a Streaming Dataframe to Kafka with Aggregated Data
In this exercise you will be working with a bank withdrawals topic and an Automated Teller Machine (ATM) visit topic. The goal will be to join both those data streams in a way that allows you to identify withdrawals connected with an ATM visit.

Task List

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Edge Cases

Edge Cases

Quiz Question
If you had a Spark application that wasn't outputting any data, with the last few lines below, what small code change could you make?

customerSelectStarDF=spark.sql("select * from BankCustomers")
customerWithDepositDF = bankDepositsSelectStarDF \
.join(customerSelectStarDF, expr("""   accountNumber = customerNumber"""    ))
customerWithDepositDF \
.writeStream \
.outputMode("append") \
.format("console") \
.start() \
.awaitTermination()

## Lesson Review

Lesson Review

Lesson Learning Objectives
Lesson Learning Objectives

Lesson Learning Objectives
Now that you have completed Lesson 2, you should be able to successfully complete the following:

Parse a JSON payload into separate fields for analysis
Join two streaming DataFrames from different data sources
Write a streaming DataFrame to Kafka with aggregated data
Additional Resources
Joining Spark Streams Resources
For more reading on joining Spark Streams, check out the Join Section in the Official Spark Streaming Guide(opens in a new tab)

Kafka Integration Resources
For more information on integrating Spark with Kafka, see the official Kafka Integration Guide(opens in a new tab)

Course Overview
Course Overview

Where we are in the Course
Here's where we are in the course:

We just learned about Joins and JSON
Next we will work with Redis, Base64, and JSON

## Glossary

Glossary
Term	Definition
Join	To connect two data collections by referencing a field they share in common, or the state which connects two data collections by referencing a common field.
JSON	JavaScript Object Notation; originally created to serialize objects in JavaScript, a data serialization standard consisting of keys and values.
Spark View	In a Spark application, a session-bound representation of data in a certain configuration.
StructField	A Python class used to create a typed field in a StructType.
StructType	A Spark class that defines the schema for a DataFrame.