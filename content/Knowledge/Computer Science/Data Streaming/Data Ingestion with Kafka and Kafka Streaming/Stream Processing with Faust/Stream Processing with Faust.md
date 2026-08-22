---
title: "Stream Processing with Faust"
date: 2001-01-01
tags: [note]
publish_external: true
---

# Stream Processing with Faust

## Glossary of Terms in Lesson

Glossary of Key Terms You Will Learn in this Lesson
DSL - Domain Specific Language. A metaprogramming language for specific tasks, such as building database queries or stream processing applications.
Dataclass (Python) - A special type of Class in which instances are meant to represent data, but not contain mutating functions
Changelog - An append-only log of changes made to a particular component. In the case of Faust and other stream processors, this tracks all changes to a given processor.
Processor (Faust) - Functions that take a value and return a value. Can be added in a pre-defined list of callbacks to stream declarations.
Operations (Faust) - Actions that can be applied to an incoming stream to create an intermediate stream containing some modification, such as a group-by or filter

## Stream Processing with Faust

In this lesson, you will learn how to construct stream processing applications using the Faust framework. Faust was developed at the financial services company, Robinhood, as a Python-native alternative to many of the JVM-only stream processing frameworks like Kafka Streams and Flink. By the end of this lesson, you will know how to create powerful stream processing applications quickly, and with minimal code!

## Introduction to Faust

Faust is built using modern Python features such as asyncio(opens in a new tab). Faust is embeddable as a library in existing applications. It can also be configured to be deployed as a stand-alone application in your infrastructure. Faust implements storage, time windowing, streams, tables, and many of the aggregate functions discussed in Lesson 5. It is important to note that Faust requires Python 3.6+ and does not support Avro or Schema Registry natively at this time.

Robinhood Faust - Key Points
Built at Robinhood to tackle stream processing problems natively in Python(opens in a new tab)
Faust takes its design inspiration from Kafka Streams, a JVM-only framework(opens in a new tab)
Faust is built using modern Python features like asyncio, and requires Python 3.6 or higher(opens in a new tab)
Faust’s API implements the storage, windowing, aggregation, and other concepts discussed in Lesson 5
Faust is a native Python API, not a Domain Specific Language (DSL) for metaprogramming
Requires no external dependency other than Kafka. Does not require a resource manager like Yarn or Mesos.
Faust does not natively support Avro or Schema Registry
Question 1 of 3
Faust is compatible with Python 2.7+ and Python 3.5+

Question 2 of 3
Faust is a Domain Specific Language (DSL)

Question 3 of 3
Faust does not require a resource manager like Yarn or Mesos

## Serialization and Deserialization in Faust

Serialization and Deserialization
Deserializing and serializing data into native Python objects can make working with streaming data simpler and easier to test. In the following section you will see how to map your internal Python data structures to incoming and outgoing data with Faust.

Python Dataclasses
A dataclass is a special type of Class in which instances are meant to represent data, but not contain mutating functions.
Python dataclass objects can be marked as frozen(opens in a new tab), which makes them immutable - Nothing in Python is truly immutable, but this attribute gets you about as close as you can get
dataclass objects require type annotations on fields and will enforce those constraints on creation. This helps ensure you’re always working with data in the expected format, reducing and preventing errors.
Can be paired with the asdict function(opens in a new tab) to quickly transform dataclasses into dictionaries
New in Python 3.7(opens in a new tab)
Default to using dataclass to work with data coming into and out of your Faust applications unless you have a good reason not to
Quiz Question
Which of the following are benefits of dataclasses? (may be more than one answer)

## Storage in Faust

In this section you will learn about the storage options available for Faust applications, including in-memory and RocksDB-based storage.

Kafka State

Faust keeps track of all state changes in stream processing applications in a topic dedicated to each stream.
Doing so allows Faust to scale up from one node to thousands of processing nodes without skipping a beat.
How does this work?

Similar to Kafka producer works, as events happen in a stateful table, an event is emitted for that specific event.

Storing State In Memory

When a Faust application starts and reads state from the changelog topic, or as it processes data during execution, it needs to store the current state of the application somewhere.

The first, and default, option, is to simply store the state in memory – this means that an up-to-date copy of the state of a table is kept in application memory on every node.

While this is fast and simple to reason about, it has significant disadvantages:

Every time the application restarts it has to completely rebuild state from the Kafka changelog topic.

It might take our application minutes or even hours to recover and begin processing again.

What happens if the state of the table is too large to fit in memory?

Because of these significant disadvantages, it is not recommended to use in-memory storage for anything but testing and local development where data sets are limited, and recovery times aren't critical.

Storing State in RocksDB

The second option for storing application state locally is to use RocksDB.

RocksDB is a highly performant datastore that runs side-by-side with a stream processing application.
As changes are made in your streaming table, the state is stored in RocksDB in addition to being sent to Kafka.
It is always recommended to use RocksDB in production.
Question 1 of 3
Why is in-memory storage inappropriate for Production? (may be more than one answer)

Question 2 of 3
How is Kafka used by Faust?

Question 3 of 3
Why is RocksDB useful? (may be more than one answer)

## Streams Basics in Faust

Creating Streams with Faust
In this section, you will learn how to create streams with Faust.

Creating streams with Faust is as simple as:

defining a Faust topic
defining an app agent decorated processing function
In the above example, we:

first create a subscription to a topic
define an async function called process, which is decorated with an app agent subscribed to the source topic
have an infinite async iterable which receives data from the stream as it is produced, from within the function
the stream is the argument provided to our agent processing function
Once we have the message, we can transform it, print it, and do any type of processing we’re interested in.

Message Life Cycle and Acknowledgment

How does Faust manage that state?
Faust does all of this for you automatically using aiokafka.

Faust creates a Kafka consumer within the context of the underlying library which is responsible for subscribing and consuming events from any requested topics.

The aiokafka consumer is responsible for managing the offsets, and will periodically commit its offsets back to Kafka.

The consumer can then forward the message onto the subscribed agent for the topic, where it is processed.

When the processing of an event completes the message is automatically acknowledged.

Faust Streams - Key Points
Faust streams are simply infinite asynchronous iterables which perform some processing on incoming messages(opens in a new tab)
Faust handles consumption, consumer groups, and offsets for you, in addition to managing message acknowledgements(opens in a new tab)
Faust applications may choose to forward processed messages on to another stream by using the topic.send(<data>) function at the end of the processing loop.

## Stream Processors & Operations

Faust Stream Processors and Operations
Faust provides the ability to provide pre-defined processor callbacks for data streams. Processors can add missing fields, change the meaning of fields, and perform any kind of desired processing.

Faust Processors - Key Points
Processors are functions that take a value and return a value and can be added in a pre-defined list of callbacks to your stream declarations(opens in a new tab)
Processors promote reusability and clarity in your code
Processors may execute synchronously or asynchronously within the context of your code
All defined processors will run, in the order they were defined, before the final value is generated.

Faust Operations - Key Points
Faust Operations are actions that can be applied to an incoming stream to create an intermediate stream containing some modification, such as a group by or filter(opens in a new tab)
The group_by(opens in a new tab) operation ingests every incoming event from a source topic, and emits it to an intermediate topic with the newly specified key
The filter(opens in a new tab) operation uses a boolean function to determine whether or not a particular record should be kept or discarded. Any records that are kept are written to a new intermediate stream.
The take(opens in a new tab) operation bundles groups of events before invoking another iteration of the stream. Be careful to specify the within datetime.timedelta argument to this function, otherwise your program may hang.
Faust provides a number of other operations that you may use when working with your streams. Have a look at the documentation for further information(opens in a new tab).

## Windowing in Faust

Faust provides two windowing methods: hopping and tumbling. In this section, you will learn how to use these windowing approaches.

Faust Windowing - Key Points
Faust supports Hopping(opens in a new tab) and Tumbling(opens in a new tab) windows
Windowing applies only to Tables
Faust provides semantics for classifying specifically which pool of data is desired from a window(opens in a new tab), such as current(), now(), relative_to_now(), etc.

## Lesson Summary

In this lesson, you learned how to use Faust as a Python-based alternative to build Stream Processing applications. You learned:

How to construct a Faust application
How to serialize and deserialize data with Python models and dataclasses
How Faust stores state with Kafka, In-Memory and RocksDB stores
How to create stream applications with operations and processes
How to build table applications with windows and co-partitioned streaming data
Glossary of Key Terms in this Lesson (same as glossary at beginning of lesson)
DSL - Domain Specific Language. A metaprogramming language for specific tasks, such as building database queries or stream processing applications.
Dataclass (Python) - A special type of Class in which instances are meant to represent data, but not contain mutating functions
Changelog - An append-only log of changes made to a particular component. In the case of Faust and other stream processors, this tracks all changes to a given processor.
Processor (Faust) - Functions that take a value and return a value. Can be added in a pre-defined list of callbacks to stream declarations.
Operations (Faust) - Actions that can be applied to an incoming stream to create an intermediate stream containing some modification, such as a group-by or filter
