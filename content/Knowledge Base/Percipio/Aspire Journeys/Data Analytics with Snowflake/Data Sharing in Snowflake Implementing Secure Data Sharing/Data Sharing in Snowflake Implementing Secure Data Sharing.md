# Data Sharing in Snowflake Implementing Secure Data Sharing

Which is a valid query to set up a replica of a database in a target Snowflake account?

B.ALTER DATABASE PROVIDERDB 
  ENABLE REPLICATION TO ACCOUNTS AWS_US_EAST_2.GT57526;

---

From these Snowflake objects, three can be part of a share. Pick the odd one out. (Hint: It is session-scoped)

Temporary table

---

Which operations is a consumer of data allowed to make on a database created from a secure share?

Select

---

Given that consumers of shares have read-only permissions in Snowflake, which needs to be granted on shared tables and views?

SELECT

---

What can you do in the Snowflake marketplace?

You can buy or sell datasets

---

What do reader accounts allow providers to do in Snowflake?

They allow them to manage Snowflake accounts which consumers will use to access shared data
Selected
Good job, you selected this correct option.

They allow them to share data with read-only permissions with consumers
Selected
Good job, you selected this correct option.

---

Which properties must match in provider and consumer accounts for secure data sharing to work between them?

The Snowflake Region (cloud + region) of the accounts

---

Which role in Snowflake has the requisite permissions to create a new Snowflake account?

ORGADMIN

---

You have replicated a database across two Snowflake accounts. Which query can you run so that the replica is in sync with the original?

ALTER DATABASE REPLICA_DATABASE REFRESH;

---

Which TWO objects in Snowflake can you include in a secure share?

Result: Correct. Great job! 

Secure views
Selected
Good job, you selected this correct option.

Transient tables
Selected
Good job, you selected this correct option.

---

Which statements about secure data sharing are true?

The providers pay storage fees for the shared data

Both the provider and consumer must use a Snowflake account

---

Which queries can be used to take away permissions on a table securely shared with another account?

A.REVOKE SELECT ON TABLE 
   PROVIDER.PUBLIC.EMPLOYEES
  FROM SHARE EMPLOYEE_DETAILS;