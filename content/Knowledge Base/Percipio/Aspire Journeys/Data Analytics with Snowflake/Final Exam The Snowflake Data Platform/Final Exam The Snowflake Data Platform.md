# Final Exam The Snowflake Data Platform

You want to unload data from Snowflake to Google Cloud Storage. Which task must you perform on the storage integration object?

Delegate authentication responsibility to Snowflake identity

---

All rows from the same month in a table are grouped together. Which of the following is this an example of?

Window

---

What is the reason for executing this command?

alter session set use_cached_result = false;

To disable the results cache

---

You want to create a materialized view. Which three limitations should you be aware of?

It can query a single table

It cannot include the ORDER BY clause

It cannot include Windows functions

---

Which type of table is considered to be clustered?

One with a clustering key

---

You want to load JSON data Into a relational table. Which three pre-requisites should you meet?

A JSON file
Selected
Good job, you selected this correct option.

A running virtual warehouse
Selected
Good job, you selected this correct option.

Copy the JSON file into a temp directory

---

You want to load JSON data into an internal Snowflake stage. You have logged on to your account and selected the database. What is the next step that you need to perform?

Create file format for JSON

---

You have collected data into an XML file. You want to load the data into the Snowflake table. Which task should you perform first?

Create a table that has an XML column with a VARIANT data type

---

You have used the COPY INTO <location> command to copy the data from a table in the Snowflake database table to a Snowflake stage. You want to download files to the local filesystem. Which command should you use?

GET

---

Which tasks can be performed using the Snowsight user interface (UI)?

Creating and running queries

Monitoring query performance

Creating virtual warehouse

Loading data in tables

---

You want to suspend automatic clustering for a table. Which clause should you use with the alter table command?

SUSPEND RECLUSTER

---

You need to configure an Integration for Google Cloud Storage. What is the first step that you must perform?

Create the cloud storage integration in Snowflake

---

Which statements are true for the Snowflake Data Platform?

It is built on the Hadoop platform

It is built on an existing database technology using its analytics engine

---

You want to configure multi-factor authentication with Snowflake using the Duo app. Which port should be opened in the firewall for the app to work properly?

443

---

You want to create a Snowflake storage integration to set up a Simple Storage Service (S3) bucket as an external stage. Which is the first step that you need to perform?

Configure the S3 bucket with the required permissions

---

You need to set up Okta for SSO for Snowflake. You have created your organization's account in Okta. What is the next step that you need to perform?

Create the Snowflake application in Okta

---

You want to perform a bulk upload from a local filesystem using the internal stage. Which command should you use?

COPY

---

In which layer of the Snowflake Data Platform can you configure the security services?

Cloud Services

---

From which Azure storage account type does Azure not support data loading?

Data Lake Storage Gen1

---

You must set up a secure share of Snowflake objects between two accounts. Which of the following step must be performed first?

Use the GRANT command to provide access

---

You want to install Snowflake on a macOS using the installer. You want to change the location of the configuration file. Which environment variable should you set?

WORKSPACE

---

You want to use the CREATE SCHEMA command to create a pipe. Which two privileges do you require on the Schema object?

USAGE 

CREATE PIPE

---

Which of the following tasks can you perform in the Snowflake Marketplace?

Merge datasets with your datasets

Get datasets from third-party into your accounts

---

Which statements are true for Snowflake warehouses?

Warehouses are needed for queries

Warehouses cannot be resized

---

You have executed several SQL queries. You want to view the cache to list the executed queries. Which command should you execute?

cache - a

---

Which of the following receives the data from the pipeline used by Snowpipe?

Micro-batches

---

You need to create a resource monitor. Which role must be assigned to you?

ACCOUNTADMIN

---

You want to perform query the data files in an internal stage. Which two actions are meant to be performed with the queries?

Loading data
Transforming data

---

You created a bucket in Google Cloud Storage. After creating the bucket, which metadata is non-editable and cannot be changed later?

Geographic location

Bucket name

---

You want to configure Azure and Snowflake resources with a Snowpipe for continuous data ingestion. In which of the following command should you contain the COPY INTO <table> statement?

CREATE PIPE

---

You need to define variables before connecting to Snowflake. Which is the correct method you should use?

Add variables in the config file

---

Your organization wants to use the Snowflake Data Platform but has a strict mandate to meet the HIPAA and HITRUST CSF requirements. Which edition should they opt for?

Business Critical

---

You want to perform bulk uploading from Google Cloud Storage. What is the first step that you need to perform?

Ensure that the files have been uploaded to the Google Cloud Storage

---

You want to enable a search optimization service for performance optimization. On which two entities can you enable the search optimization to gain performance?

Views

Joins

---

Which type of subquery is given in the following statements?


Select fname, lname
  from users where fname = (select max(x) from employees);

Uncorrelated

---

You need to create a table that can store non-permanent and transitory data. Which type of table should you create?

Temp

---

A user with the ACCOUNTADMIN system role can enable or disable multi-factor authentication

Multi-factor authentication can be disabled for a certain number of minutes

---

You need to create an Identity and Access Management (IAM) account to grant privileges on the S3 bucket that Snowflake Storage Integration will use as external storage. Which type of account should you create?

Another AWS Account

---

You want to create a stage pointing to a set of private data files. Which method should you use?

Use the CREATE STORAGE INTEGRATION command

---

You want to query files on a table. Which privilege should you have on the table?

OWNERSHIP

---

As a consumer, you want to list the available shares. Which of the following command can you use?

SHOW SHARES

---

You have created a non-materialized view. However, you want to update the view. Which of the following method should you use?