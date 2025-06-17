---
date: 1970-01-01T00:00:00Z
---

# Data Schemas and Apache Avro

## Lesson Glossary of Key Terms

Glossary of Key Terms You Will Learn in this Lesson
Data Schema - Define the shape of a particular kind of data. Specifically, data schemas define the expected fields, their names, and value types for those fields. Data schemas may also indicate whether fields are required or optional.
Apache Avro - A data serialization framework which includes facilities for defining and communicating data schemas. Avro is widely used in the Kafka ecosystem and data engineering generally.
Record (Avro) - A single encoded record in the defined Avro format
Primitive Type (Avro) - In Avro, a primitive type is a type which requires no additional specification - null, boolean, int, long, float, double, bytes, string.
Complex Type (Avro) - In Avro, a complex type models data structures which may involve nesting or other advanced functionality: records, enums, maps, arrays, unions, fixed.
Schema Evolution - The process of modifying an existing schema with new, deleted, or modified fields.
Schema Compatibility - Determines whether or not two given versions of a schema are usable by a given client
Backward Compatibility - means that consumer code developed against the most recent version of an Avro Schema can use data using the prior version of a schema without modification.
Forward Compatibility - means that consumer code developed against the previous version of an Avro Schema can consume data using the newest version of a schema without modification.
Full Compatibility - means that consumers developed against the latest schema can consume data using the previous schema, and that consumers developed against the previous schema can consume data from the latest schema as well. In other words, full compatibility means that a schema change is both forward and backward compatible.
None Compatibility - disables compatibility checking by Schema Registry.

## Understanding Data Schemas

What are Data Schemas?
Data schemas help us define:
The shape of the data
The names of fields
The expected types of values
Whether certain data fields are optional or required.
Data schemas provide expectations for applications so that they can properly ingest or produce data that match that specification
Data schemas are used for communication between software
Data schemas can help us create more efficient representations with compression
Data schemas help systems develop independently of each other
Data schemas are critical in data systems and applications today
gRPC in Kubernetes
Apache Avro in the Hadoop Ecosystem

## Real-world Usage

Real-world use cases of data schemas
First, think about defining a SQL Table in your favorite database, like MySQL or Postgres. When you declare your table, you always tell the database what columns it should have, and what the data types are for those columns.

When defining a database table in this manner, you’re telling the database what data to expect, what shape it will take, and what the possible types of accepted values are for each column. This is a very common type of schema.
Outside of SQL databases, if you’ve ever worked with tools such as Hadoop, Hive, or Presto, you’ve likely seen Apache Avro used to describe data.

Schemas and Containers
Schemas are also used in traditional backend development.

The container orchestration platform Kubernetes relies heavily on a tool called gRPC to facilitate communication between components. gRPC is a communication protocol built on Google’s Protocol Buffers schema definition language.

Using schemas has allowed Kubernetes to provide a fast and scalable platform that can easily integrate new functionality from third parties. Any third-party application can communicate with Kubernetes using these pre-defined schemas and expect the system to work properly.

Schemas play an important part in today’s software ecosystem.

They can increase speed and clarity of expected data
They help reduce mistakes and errors.

## Data Streaming with Schemas

Streaming applications are highly dependent on data schemas

Schemas are widely used in data streaming applications to codify the data being produced and received

Schemas allow for data producers to evolve largely independently of their data consumers -- namely, streaming applications

Schemas provide the tool that stream processing applications need to evolve independently of their upstream producers

Schemas can help shield data consumers from unexpected changes in the system

Some schema systems even provide detailed information about data compatibility to help applications understand what they can or cannot do with a given piece of data, as it arrives

## Apache Avro

Intro to Apache Avro
Apache Avro is a widely used data schema system in the data engineering space, and especially in the Apache Kafka ecosystem. In this section, we’ll review key concepts as they relate to Avro and Stream Processing.

## What is Apache Avro?

Apache Avro is a data serialization system that uses a binary data format.

when data in an application is shared in the Avro format, it is compressed into a binary format over the network
this binary format improves speed over the network and can help reduce storage overhead
this binary formatted data includes the application data in the Avro schema format and the schema definition.
When clients receive data from an application in Avro format, not only do they receive the data, but they also receive the Avro instructions, or schema, for how to deserialize the data from binary into their own application data model representation.

## How Avro Schemas are Defined

Avro Schema - Key Points
Apache Avro records are defined in JSON.
Avro records include a required name, such as "user"
Avro records must include a type defined as record
Avro records may optionally include a namespace, such as "com.udacity"
Avro records are required to include an array of fields that define the names of the expected fields and their associated type. Such as "fields": [{"name": "age", "type": "int"}]
Avro can support optional fields by specifying the field type as either null or some other type. Such as "fields": [{"name": "age", "type": [“null”, "int"]}]
Avro records are made up of complex and primitive types
Complex types are other records, arrays, maps, and others
Please reference the Avro documentation for full documentation(opens in a new tab) and additional examples
Here is what a stock ticker price change schema might look like:
{
    “type”: “record”,
    “name”: “stock.price_change”,
    “namespace”: “com.udacity”,
    “fields”: [
        {“name”: “ticker”, “type”: “string”},
        {“name”: “prev_price”, “type”: “int”},
        {“name”: “price”, “type”: “int”},
        {“name”: “cause”, “type”: [“null”, “string”]}
    ]
}
Question 1 of 2
Which of the following are required fields for Avro records? (may be more than one answer)

Question 2 of 2
Avro schemas are defined as JSON

## Apache Avro Data Types

Avro Types
Full documentation is available on the Avro website(opens in a new tab)
Primitive Types(opens in a new tab) should be familiar, as they closely mirror the built-in types for many programming languages.
null
boolean
int
long
float
double
bytes
string
Complex Types(opens in a new tab) allow nesting and advanced functionality.
records
enums
maps
arrays
unions
fixed
Question 1 of 3
Which of the following are supported primitive types in Avro? (more than one answer)

Question 2 of 3
Which of the following are supported complex types in Avro? (more than one answer)

Question 3 of 3
Which of the following is a properly defined Avro record?

## Apache Avro and Kafka

The Apache Kafka development community decided early on to incorporate support for Avro into Kafka(opens in a new tab) and Kafka ecosystem tools. In this section, you will learn how to use Avro with Kafka.

Although Avro is not required to use Kafka, and you can in fact use any other schema format you like, Avro is used extensively in the Kafka ecosystem, and using it will improve your experience.

When using Avro with Apache Kafka, the producer must define an Avro Schema for messages they would like to produce to Kafka

Many client libraries have built-in support for Avro

When using the confluent_kafka_python library’s special Avro consumer, it will automatically unpack the Avro data it receives from Kafka using the Avro schema that was packaged alongside it

While it does take a little more effort to define your schema in Avro, versus JSON or plain text, you will be grateful to have spent that effort when your application tolerates downstream data changes more gracefully!

Apache Avro and Kafka - Helpful Documentation
confluent_kafka_python Avro Producer(opens in a new tab)
confluent_kafka_python Avro Consumer

## Schema Registry

Confluent Schema Registry(opens in a new tab) is an open-source tool that provides centralized Avro Schema storage. In this section, you’ll learn how Schema Registry can improve your Kafka Stream Processing applications.

## Kafka - Schema Registry Integration

Sending an Avro schema definition alongside every message:

introduces some additional network and storage overhead in our producer and consumer applications
introduces additional work on the consumer and producer to correctly serialize and deserialize from Avro
Schema Registry is a tool built by Confluent and deployed alongside Apache Kafka that can help reduce some of the overhead involved with using Avro.

if Schema Registry is in use in a cluster, there is no need to send schemas alongside payloads to Kafka
the Kafka client can be configured to send the schema to the schema registry over HTTP instead
Schema Registry:

assigns the named schema a version number

stores the version number in a private topic and the producer never needs to send the schema to either the Schema Registry or the Kafka broker, until the schema definition is updated again

can pull historical schemas as well, so all data stored in the Kafka topic can be deserialized by clients.

does not support deletes by default

can be used by any application that wants to efficiently store and retrieve schema data across multiple versions

is typically used by Kafka clients, but it has also been utilized by applications that are not interacting with Kafka

When using schema registry, Consumers and producers only fetch a schema when they don’t have it in memory. Once they’ve fetched a schema version, it is never fetched again. This can dramatically decrease networking overhead for high-throughput topics.

Schema Registry Architecture

At its core, Schema Registry is simply a web server built on the JVM using Java and Scala.

it is highly portable
it will run on just about any operating system
it utilizes Kafka itself to store data in a schemas topic
it uses compaction to ensure that no data loss occurs
You can run more than one schema registry node at a time, to form a schema registry cluster. However, only one schema registry node at a time acts as the leader for the cluster. The leader, as with Kafka, is chosen by using Zookeeper to perform elections.

Schema Registry
Schema Registry runs as an HTTP service and interacts with producer and consumer clients

## Schema Evolution & Compatibility

Schema Evolution and Compatibility
Schemas change over time with new requirements. This process of schema change is known as Schema Evolution.

In this section, you will see how Avro and Schema Registry can aid in the process of Schema Evolution.

We’ll also discuss in this series of concepts how evolving schemas can be forward or backward compatible with previous versions.

## Understanding Schema Evolution

Schema evolution – the process of changing the data schema for a given dataset.

In other words, it means that a Kafka producer has modified the shape of the data, as well as the data schema, that it intends to send.

In practice, evolving a schema simply means updating the Avro definition and resubmitting the schema to schema registry with some compatibility information.

Quiz Question
What is schema evolution?

## Schema Compatibility

Schema Compatibility

Schema Compatibility
The process of schema change is known as Schema Evolution
Schema Evolution is caused by a modification to an existing data schema
Adding or removing a field
Making a field optional
Changing a field type
Schema Registry can track schema compatibility between schemas
Compatibility is used to determine whether or not a particular schema version is usable by a data consumer
Consumers may opt to use this compatibility information to preemptively refuse to process data that is incompatible with its current configuration
Schema Registry supports four categories of compatibility(opens in a new tab)
Backward / Backward Transitive
Forward / Forward Transitive
Full / Full Transitive
None
Managing compatibility requires both producer and consumer code to determine the compatibility of schema changes and send those updates to Schema Registry

## Backward Compatibility

Backward Compatibility - Key Points
Backward compatibility(opens in a new tab) means that consumer code developed against the most recent version of an Avro Schema can use data using the prior version of a schema without modification.
The deletion of a field or the addition of a new optional field is backward compatible changes.
Update consumers before updating producers to ensure that consumers can handle the new data type
The BACKWARD compatibility type indicates compatibility with the current version (N) and the immediately prior version (N-1)
Unless you specify otherwise, Schema Registry always assumes that changes are BACKWARD compatible
The BACKWARD_TRANSITIVE compatibility type indicates compatibility with all prior versions (1 → N)
Quiz Question
Which of the following changes to a new schema would be backward compatible? (may be more than one answer)

## Forward Compatibility

Forward Compatibility
Forward compatibility(opens in a new tab) means that consumer code developed against the previous version of an Avro Schema can consume data using the newest version of a schema without modification
The deletion of an optional field or the addition of a new field is forward compatible changes
Producers need to be updated before consumers
The FORWARD compatibility type indicates that data produced with the latest schema (N) is usable by consumers using the previous schema version (N-1)
The FORWARD_TRANSITIVE compatibility type indicates that data produced with the latest schema (N) is usable by all consumers using any previous schema version (1 → N-1)
Quiz Question
Which of the following changes would be forward compatible?

## Full Compatibility

Full Compatibility
Full compatibility(opens in a new tab) means that consumers developed against the latest schema can consume data using the previous schema, and that consumers developed against the previous schema can consume data from the latest schema as well. In other words, full compatibility means that a schema change is both forward and backward compatible.
Changing the default value for a field is an example of a full compatible change.
The order in which producers or consumers are updated does not matter.
The FULL compatibility type indicates that data produced is both forward and backward compatible with the current (N) and previous (N-1) schema.
The FULL_TRANSITIVE compatibility type indicates that data produced is both forward and backward compatible with the current (N) and all previous (1 → N-1) schemas.
Quiz Question
Which of the following changes would have full compatibility? (may be more than one answer)

## No Compatibility

No Compatibility (NONE Compatibility)
No compatibility(opens in a new tab) disables compatibility checking by Schema Registry.
In this mode, Schema Registry simply becomes a schema repository.
Use of NONE compatibility is not recommended.
Schemas will sometimes need to undergo a change that is neither forward nor backward compatible.
Best practice is to create a new topic with the new schema and update consumers to use that new topic.
Managing multiple incompatible schemas within the same topic leads to runtime errors and code that is difficult to maintain.
Quiz Question
Which of the following changes would have None compatibility? (may be more than one answer)

