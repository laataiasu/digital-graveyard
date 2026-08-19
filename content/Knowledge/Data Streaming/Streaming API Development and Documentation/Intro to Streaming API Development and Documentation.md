---
title: "Intro to Streaming API Development and Documentation"
date: 2001-01-01
tags: [note]
publish_external: false
---

# Intro to Streaming API Development and Documentation

## Introduction to Apache Spark and Spark Streaming

Consciousness is a Data Stream
What is a "stream of consciousness"? It refers to the organic flow of thoughts and ideas in the brain.

Thoughts:

Are always moving when you are awake
Are constantly changing and evolving
Start with one subject and move to another topic quickly
Multiple sources of data are aggregated to form ideas and conclusions
Consciousness - a Data Stream
Streaming Application, a series of events from a real event to an insight gained
The World Around Us Generates Loads of Information
Just as in our consciousness, the world around us generates loads of information

A real-world event is often responsible for producing the stream of information ingested by a Streaming Application:

An application event is created in response to a real-world event
A listener responsible for responding to this event ingests it
As a result, a new insight is produced
What is Data Streaming?
Data Streaming: Data Streaming is the process of transmitting and/or receiving data envelopes or messages over a potentially undefined space of time, while applying computational algorithms to those data envelopes or messages.

Course Prerequisites

Prerequisites
Intermediate SQL
Python
Some experience with ETL (Extracts - Transforms - Loads) in data processing may be helpful

## Why Data Streaming Is Important

Apache Spark and Spark Streaming Is Important

Why is Data Streaming Important?
Video Streaming Application
The world around us has become filled with opportunities to gain valuable streams of data. Let's take a video streaming platform for example. In the simple process of watching a video, the average viewer generates and consumes various types of data:

The actual video feed is itself a data stream, sending thousands of frames per minute in small network packets
Like the network packets, most streams are composed of small application messages
A user logging in to view their favorite TV series will present their online profile as they log in to the website
Then several events take place that make their video available for viewing in the browser
Hopping on their cell phone to take the rest of the video on the road, the mobile app will send device messages to catch up to the previously played frame
Messages both created and consumed in this process of viewing videos can be aggregated and used to recommend future video selections to the user.

Streaming Map Application
Streaming Map Application
Another example of streaming is a map application. With a map application, data is constantly exchanged between the application and the data processing engine:

The phone application transmits a continual stream of GPS Coordinates
As the GPS Coordinates are delivered, the server analyzes the best route to the destination
The current best route is delivered to the app
This process is repeated until the destination is reached

## Business Stakeholders

Note: the order of two items was switched in the video above.

Teams You Work With
The Application Development Team produces Data Streams that you will consume
They also consume Data Streams you will produce
Data Engineering teams may maintain the infrastructure you use to run Streaming Applications
Often Data Science is the area responsible for creating and maintaining Streaming Applications
C-Level executives come to rely on rapidly available recommendations produced by streaming analytics. Running a company can be very challenging unless the right information is available

## When To Use Data Streaming

When To Use Apache Spark and Spark Streaming
Qualifications for a Data Streaming Project
Data Streaming should not be considered a universal solution to all Data requirements. Certain elements qualify a project as ideal for a Data Streaming project:

There must be a way of producing the information that is needed (example: I want to know how many times a user clicks on my website per hour in real-time)
The data should be actionable in a real-time manner (example: I want to pop a chatbot to users who click more than 100 times per hour on my website)
The proposed solution must provide business value
Value is defined as something that is worth more than the resources expended
Stakeholders should agree the proposed project has merit
Just because something is interesting doesn't mean it provides value to your business

## History of Data Streaming

History of Apache Spark and Spark Streaming

Messaging Systems Timeline
1964 - IBM System/360 (Mainframe)- including BTAM and QTAM (Basic and Queued Telecommunications Access Methods)

1971 - IBM offered TCAM- Telecommunications Access Method - more advanced message routing

1992 - IBM announced MQSeries- available off the mainframe

1998 - Sun Microsystems published The Java Message Service (JMS)

1999 - IBM Andy Stanford-Clark and Arlen Nipper authored MQTT

Messaging Systems Timeline
Evolution of Streaming
2003 - Apache Nutch created by Doug Cutting and Mike Cafarella

2006 - Apache Nutch moved to Apache Hadoop project

2007 - Rabbit Technologies Ltd. developed RabbitMQ

2009 - Spark started by Matei Zaharia at UC Berkeley

2011 - Kafka developed by LinkedIn

2013 - Spark donated to Apache

2017 - Spark 2.2 Released with Kafka Streaming Support

## Tools & Environment

Tools Used in this Course
Some of the tools you will use in the course include:

bash
Python
Kafka
Spark
Redis
Docker (optional if you choose to do the exercises using your computer, instead of the provided classroom workspace)
The workspace environment has Kafka, Spark, Python, and Bash installed for you. The Docker images provided for the course also have all of these things included. A simulated Business Application is provided as part of the workspace and as part of the Docker image.

Tools Used in this Course
Tools Used Elsewhere for Streaming
Some examples of tools that are used elsewhere in streaming include:

JMS
RabbitMQ
Hadoop
SQS
Firebase

## Workspace Setup Outside of Classroom

This Entire Page is Optional
You can complete all of the exercises and the project for this course successfully using the provided workspaces here in the Udacity classroom. You do not need to install anything on your computer. So the directions on this page are optional, and you can skip to the next page if you'd like.

But if you would like to work on the exercises and project on your local computer rather than in the provided workspaces in the classroom, please follow the directions on this page.

Clone the Github Repository
The first step to setting up your local workspace is to clone the GitHub Repository:

git clone https://github.com/udacity/cd0036-Data-Streaming-API-Development-and-Documentation
Windows Users
It is HIGHLY recommended to install the latest stable Windows update(opens in a new tab).

You will then want to install the latest version of Docker on Windows: (opens in a new tab)https://docs.docker.com/docker-for-windows/install/(opens in a new tab)

Using Docker for your Exercises
You will need to use Docker to run the exercises on your own computer. You can find Docker for your operating system here: (opens in a new tab)https://docs.docker.com/get-docker/(opens in a new tab)

It is recommended that you configure Docker to allow it to use up to 2 cores and 6 GB of your host memory for use by the course workspace. If you are running other processes using Docker simultaneously with the workspace, you should take that into account also.

The docker-compose file at the root of the repository creates 9 separate containers:

Redis
Zookeeper (for Kafka)
Kafka
Banking Simulation
Trucking Simulation
STEDI (Application used in Final Project)
Kafka Connect with Redis Source Connector
Spark Master
Spark Worker
It also mounts your repository folder to the Spark Master and Spark Worker containers as a volume /home/workspace, making your code changes instantly available within the containers running Spark.

Let's get these containers started!

cd [repositoryfolder]
docker-compose up
You should see 9 containers when you run this command:

docker ps

## Apache Spark and Spark Streaming Glossary

#### Lesson 1

* **Broker**
  In a Kafka configuration, the server to which requests from external systems can be addressed; also the central processing component of a Kafka cluster.

* **Cluster**
  An orientation of two or more servers in such a fashion that they can communicate directly with one another or with a cluster manager; often for the purpose of high availability or increased capacity.

* **Data Pipeline**
  A series of steps of processing that augment or refine a raw data source in preparation for consumption by another system.

* **DataFrame**
  A programming construct used to coordinate processing of dynamic data.

* **Kafka**
  A durable message broker used to mediate the exchange of messages between multiple applications.

* **Kubernetes**
  An open source technology used to coordinate and distribute computing.

* **Offset**
  In a Kafka configuration, a value which determines the mode of consumption of a topic; earliest starts at the oldest message; latest starts at the newest message.

* **Sink**
  An external system which consumes data.

* **Source**
  An external system which generates data.

* **Spark**
  An open source framework for distributing computing across a cluster of servers; typically programming is required.

* **Topic**
  In a Kafka configuration, a channel of communication; often representing similar or related data; sometimes called a mailbox.

* **Zookeeper**
  An open source technology that enables semi-autonomous healing of a server cluster.

#### Lesson 2

* **Join**
  To connect two data collections by referencing a field they share in common; or the state which connects two data collections by referencing a common field.

* **JSON (JavaScript Object Notation)**
  Originally created to serialize objects in JavaScript, a data serialization standard consisting of keys and values.

* **Spark View**
  In a Spark application, a session-bound representation of data in a certain configuration.

* **StructField**
  A Python class used to create a typed field in a StructType.

* **StructType**
  A Spark class that defines the schema for a DataFrame.

#### Lesson 3

* **Base64**
  An encoding format used by computers to transmit and store information.

* **Kafka Connect**
  Part of the Confluent Kafka distribution; it is the component responsible for providing a path from an external system (a source) to a Kafka topic or from a Kafka topic to an external system (a sink).

* **Redis**
  A database used primarily for caching; this means it is optimized for fast reads and writes.

* **Source Connector**
  A Source Connector provides a connection from an outside system (a source) to a Kafka topic.

## Project Overview: Evaluate Human Balance with Spark Streaming

Project Overview: Evaluate Human Balance with Spark Streaming

Project Overview
You will work on this project at the end of this course after you've mastered the learning objectives. On this page, we just provide an early overview of the project for you.

STEDI is a small startup focused on assessing balance for seniors
STEDI has an application that collects data from seniors during a small exercise
The user starts a timer and clicks a button with each step the senior takes
When the senior has reached 30 steps their test is finished
The data transmitted enables the application to monitor seniors' balance risk
Project Overview: Evaluate Human Balance with Spark Streaming
The Problem
Your product manager has requested a graph that shows fall risk
The development team has built the graph
Their graph is ready to receive data
The Problem to solve. 
The Problem

## Lesson Recap

Lesson Recap

Lesson Recap
So we've introduced you to Apache Spark and data streaming. We've talked about:

Why data streaming is important
Business stakeholders you would work with
Data streaming
History of data streaming
Your tools and environment
Final project
