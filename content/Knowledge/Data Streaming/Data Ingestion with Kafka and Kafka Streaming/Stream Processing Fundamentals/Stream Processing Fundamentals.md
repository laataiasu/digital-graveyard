---
title: "Stream Processing Fundamentals"
date: 2001-01-01
tags: []
---

# Stream Processing Fundamentals

## Glossary of Terms for Lesson

Glossary of Key Terms You Will Learn in this Lesson
Join (Streams) - The process of combining one or more streams into an output stream, typically on some related key attribute.
Filtering (Streams) - The process of removing certain events in a data stream based on a condition
Aggregating (Streams) - The process of summing, reducing, or otherwise grouping data based on a key attribute
Remapping (Streams) - The process of modifying the input stream data structure into a different output structure. This may include the addition or removal of fields on a given event.
Windowing (Streams) - Defining a period of time from which data is analyzed. Once data falls outside of that period of time, it is no longer valid for streaming analysis.
Tumbling Window (Streams) - The tumbling window defines a block of time which rolls over once the duration has elapsed. A tumbling window of one hour, started now, would collect all data for the next 60 minutes. Then, at the 60 minute mark, it would reset all of the data in the topic, and begin collecting a fresh set of data for the next 60 minutes.
Hopping Window (Streams) - Hopping windows advance in defined increments of time. A hopping window consists of a window length, e.g. 30 minutes, and an increment time, e.g. 5 minutes. Every time the increment time expires, the window is advanced forward by the increment.
Sliding Window (Streams) - Sliding Windows work identically to Hopping Windows, except the increment period is much smaller -- typically measured in seconds. Sliding windows are constantly updated and always represent the most up-to-date state of a given stream aggregation.
Stream - Streams contain all events in a topic, immutable, and in order. As new events occur, they are simply appended to the end of the stream.
Table - Tables are the result of aggregation operations in stream processing applications. They are a roll-up, point-in-time view of data.
Stateful - Stateful operations must store the intermediate results of combining multiple events to represent the latest point-in-time value for a given key

## Stream Processing Basics

Stream Processing Fundamentals

Stream processing applications make use of streaming data stores like Apache Kafka to provide real-time analytics. Developing an understanding of common strategies, calculations, and learning how to handle data based on time will prepare you for building these applications and getting the most out of your data.

## Stream Processing Strategies

Stream Processing Strategies
This section introduces a number of core stream processing strategies, such as combining, filtering, aggregating, and reducing streams.

Stream processing applications, never stop running.

How do you JOIN a dataset that is evolving while you’re performing the calculation?
How do you FILTER a dataset that's changing as your code runs?
Kafka provides us no functionality to help us with these problems out of the box.

This is where stream processing frameworks come into play. In the following sections, we’ll see how we can accomplish this functionality on constantly evolving streams.

## Combining Streams

Combining or joining streams is the action of taking one or more streams and creating a single new output stream.

Joined streams always share some common attribute across the data in all of the streams. For example, we might use a user_id to merge user streams.

State must be kept as events flow through the join calculation, until all of the related data has arrived. Once this happens, the new event can be emitted, and the state can be flushed

If the related data never fully arrives, at some point the data in memory should be cleared
This process is typically accomplished through windowing, which is covered in a later section of this lesson.

The critical difference in combining streams scenarios relative to traditional batch processing approaches is that calculations run continually, and not on a specific scheduled basis.

Quiz Question
What are some of the reasons you might want to combine streams? (may be more than one answer)

## Filtering Streams

Filtering a stream is the process of removing unwanted or unneeded data from an input stream, and outputting the desired data into a new stream

Filtering may be a step in joining or combining two or more streams

Filtering is often desirable when data clients don’t need access to all data for throughput or security reasons

Applying filters earlier, rather than later, in the processing pipeline, can allow stream processing calculations to scale better and analyze less data.

A classic example of data filtering is refining a given dataset for a specific audience.

Many streaming data stores house what are referred to as “raw” streams – streams in which all data is present. For example, we might work at a marketing firm, and we want to perform some sentiment analysis on our client’s brands.

Given that we want to perform sentiment analysis, we might pipe in raw social data feeds. An example of this might be twitter. Even if we limit the data in the “raw” datafeed to tweets that mention our clients, this will still be quite a bit of data. So we might apply a filter that splits out the raw feed for each one of our clients into their own field. This is a simple example of filtering.

Filtering allows for taking a massive, difficult to understand dataset, and quickly refining it into smaller relevant chunks.

Quiz Question
What are some of the reasons you might want to filter streams? (may be more than one answer)

## Remapping Streams

Remapping Streams
Remapping streams is the process of transforming an input event and outputting it in a different form to a new stream
Remapping may be done in conjunction with other processing steps, such as filters or joins
Remapping is commonly used for data health, application compatibility, and security reasons
Example Scenario 1: Transforming one data serialization format to another. E.g., Avro -> JSON, or JSON-> Avro
Example Scenario 2: Removing sensitive or unnecessary fields from an input payload
Example Scenario 3: Transforming an input event into a format suitable for downstream use by moving data fields or renaming them
One of the most common use cases of data remapping is filtering out personally identifiable information, or PII, from input data streams.

Quiz Question
What are some of the reasons you might want to remap streams? (may be more than one answer)

## Aggregating Streams

An aggregation involves taking two or more distinct events and creating one or more new events based on a transformation function

Aggregate Functions: Max, Min, Sum, TopN, HIstograms, Sets, Lists, and more

Aggregates in streaming applications almost always involve a timeframe, unless the source topic is compacted

Aggregation functions provide some of the most exciting insights from our streaming data.

Let’s pretend we work at a software as a service company together. We’re trying to understand the kinds of problems that our customers have, as well as the types of problems that particular categories have so that we can better improve our product.
We might have a raw datastream of all pageviews for our support site, broken down by user.
If we simply counted this data by page, we could see, by timeframe, what our most visited support pages were.
Quiz Question
What are some of the reasons you might want to aggregate streams? (may be more than one answer)

## Handling Time

Understanding time and how it applies to our data is a critical part of building a successful stream processing application. In the following sections we will review the various types of time windowing.

In the previous sections, we learned about the types of processing we might perform on an input data stream in a stream processing application. We also vaguely touched on the notion of time periods, noting that in stream processing, we don't usually look at all of the data in a stream at once.

How we decide the timeframe containing the data that we do look at is a process known as windowing.

A window in a stream processing application is a period of time, with a start and an end, in which data is gathered for analysis, by key
Windows can also take place in the past - they don't always have to be relative to the current moment in time
Windows are the building blocks of the aggregation and join functions that allow us to create interesting stream processing applications

## Tumbling Window

Tumbling Window
Tumbling windows represent a fixed period of time that rolls over after that period of time has elapsed - ex: A 15 minute tumbling window started now would include all data from now until the 15th minute. On the 15th minute, the data is cleared and a new 15 minute window is started.
Tumbling windows do not overlap
Tumbling windows do not have gaps between windowed periods
Tumbling Window
A tumbling window is a fixed period of time that rolls over after the fixed window has ended

Quiz Question
Which of the following scenarios would require a tumbling window? (may be more than one answer)

## Hopping Window

Hopping windows have both a duration and an increment by which they are advanced

ex.- A window of 45 minutes with an increment of 5 minutes would advance every 5 minutes. The oldest 5 minutes of the previous window would be dropped, and the newest 5 minutes of data would be added.
Hopping windows can overlap with previous windows

Hopping windows can have gaps if the increment time is larger than the duration period

Hopping Window
Hopping windows have a fixed increment which advances the window

Quiz Question
Which of the following scenarios would require a hopping window? (may be more than one answer)

## Sliding Window

Similar to Hopping Window, except the increment is not directly configurable and updates in real-time

A sliding window of the last 12 hours always includes all of the last 12 hours of data. Data is expired as soon as it reaches the 12-hour threshold, and new data is added as soon as it is received.
Sliding Windows have no gaps between windows

Sliding Windows do overlap

Sliding Window
Sliding windows are hopping windows that increment in real-time

Quiz Question
Which of the following scenarios would require a sliding window? (may be more than one answer)

## Streams and Tables

In this section, you will learn to distinguish between streams and tables in stream processing frameworks. You will also learn when to apply each type of approach.

One of the most confusing terminology issues to stream processing newcomers is understanding the difference between a streaming processing “stream” and a stream processing “table.”

Table implies a state and aggregation of some kind
Stream is simply an immutable series of ordered events.

## Streams

Streams contain all events in a topic, immutable, and in order. As new events occur, they are simply appended to the end of the stream.

The output of many stream processing applications are themselves streams. Common examples of scenarios in which a stream processing application might emit another stream are:

filtering
remapping
Streams are used in many stream processing workflows, such as data enrichment.

Quiz Question
What is a stream? (may be more than one answer)

## Tables

Tables are the result of aggregation operations in stream processing applications. They are a roll-up, point-in-time view of data.

This point-in-time analysis represents the equivalent of a snapshot in time. Unlike streams, which are ordered, boundless, and immutable, tables are:

bounded
mutable
not necessarily ordered!
Tables are how we most often derive insights from the influx of data from our streams and topics. As new data arrives into our aggregate calculations, our stream processing applications update an aggregated view of that data in time.

Quiz Question
What is a Table?

## Streams vs Tables

Comparing Streams and Tables
Streams and tables are not opposing concepts. In practice, the differentiation of a stream from a table in a stream processing application serves as a description of the type of data that is produced. Applications that are performing aggregations across incoming data are creating tables. Applications that are transforming incoming data into an unending sequence of events are streams.

Further Optional Reading on Streams and Tables
Of Streams and Tables in Kafka and Stream Processing, Part 1(opens in a new tab)

Question 1 of 2
Which of the following scenarios would call for a stream? (may be more than one answer)

Question 2 of 2
Which of the following scenarios would call for a table? (may be more than one answer)

## Data Storage

Data Storage
Table operations are stateful, meaning we must store the intermediate results of combining multiple events to represent the latest point-in-time value for a given key. Therefore, table operations require some form of storage. Options range from using in-memory storage, to dedicated databases such as RocksDB. In this section, we’ll review the options that are available.

Whether you are using KSQL, Faust, Kafka Streams, or Flink, all of these stream processing frameworks use Kafka topics to store the internal state of the stream processing applications they are running.

Stream processing frameworks create topics on Kafka to track all of the changes occurring in a stream, so that state could be easily recreated if needed.

These stream processing frameworks use Kafka’s log compaction to ensure that these topics do not grow unbounded and it helps keep the size of these topics smaller as well, which can aid in startup time.

While storing data in Kafka is great for recovery, clients still need a datastore to utilize while running on the various nodes.

By default, most streaming frameworks will simply use an in-memory store to hold state.
While this is fast, and the usage of the compacted Kafka topics provides fault tolerance, there are better strategies to aid boot times on our nodes than to use in-memory storage.

RocksDB is a highly-optimized local state store that was built at Facebook for situations just like this.

RocksDB can run on all application nodes and store state for that particular stream processing application
This local state store can dramatically speed up recovery times, especially for high throughput streams
RocksDB is used for quick start times between reboots on the same node.
It's worth noting that RocksDB is used by all of the major stream processing frameworks as an option to store state. KSQL, Kafka Streams, Faust, and Flink all use RocksDB as an option.

Further Optional Reading - Data Storage
RocksDB(opens in a new tab)
Kafka Streams State(opens in a new tab)
Question 1 of 2
What is Kafka’s role as a data store? (may be more than one answer)

Question 2 of 2
What is RocksDB’s role as a data store? (may be more than one answer)

## Lesson Summary

In this lesson you learned:

Common strategies for stream processing applications, such as filtering, joins, and aggregates
Time windowing for stateful aggregations
What types of data storage options are typical of streaming applications
Glossary of Key Terms for this Lesson (same as glossary at beginning of lesson)
Join (Streams) - The process of combining one or more streams into an output stream, typically on some related key attribute.
Filtering (Streams) - The process of removing certain events in a data stream based on a condition
Aggregating (Streams) - The process of summing, reducing, or otherwise grouping data based on a key attribute
Remapping (Streams) - The process of modifying the input stream data structure into a different output structure. This may include the addition or removal of fields on a given event.
Windowing (Streams) - Defining a period of time from which data is analyzed. Once data falls outside of that period of time, it is no longer valid for streaming analysis.
Tumbling Window (Streams) - The tumbling window defines a block of time which rolls over once the duration has elapsed. A tumbling window of one hour, started now, would collect all data for the next 60 minutes. Then, at the 60 minute mark, it would reset all of the data in the topic, and begin collecting a fresh set of data for the next 60 minutes.
Hopping Window (Streams) - Hopping windows advance in defined increments of time. A hopping window consists of a window length, e.g. 30 minutes, and an increment time, e.g. 5 minutes. Every time the increment time expires, the window is advanced forward by the increment.
Sliding Window (Streams) - Sliding Windows work identically to Hopping Windows, except the increment period is much smaller -- typically measured in seconds. Sliding windows are constantly updated and always represent the most up-to-date state of a given stream aggregation.
Stream - Streams contain all events in a topic, immutable, and in order. As new events occur, they are simply appended to the end of the stream.
Table - Tables are the result of aggregation operations in stream processing applications. They are a roll-up, point-in-time view of data.
Stateful - Stateful operations must store the intermediate results of combining multiple events to represent the latest point-in-time value for a given key

