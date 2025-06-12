# Managing Snowflake Administering a Snowflake Account

Which query can you use to restore a modified parameter to its original value?

A.	ALTER ACCOUNT UNSET DATE_OUTPUT_FORMAT;

---

Which statements about Snowflake’s security configurations are true?

Snowflake allows you to configure access to rows in tables

Snowflakes allows you to set up multi-factor authentication

---

SELECT * 
FROM SNOWFLAKE.ORGANIZATION_USAGE.STORAGE_DAILY_HISTORY
ORDER BY USAGE_DATE DESC;

Which Snowflake role can you use to execute the above query?

USERADMIN

---

What does Okta allow you to do?

It allows you to sign into multiple services with a single, Okta-provided identity
Selected

---

What does key pair authentication allow you to do?

It allows you to regulate Snowflake access via a combination of a private key and a public key

---

Which are warehouse-level parameters in Snowflake?

STATEMENT_QUEUED_TIMEOUT_IN_SECOND

MAX_CONCURRENCY

---

If you would like to integrate Snowflake with Okta for SSO, which account-level parameter must you configure?

SAML_IDENTITY_PROVIDER

---

Which query can you use to configure an account-level parameter?

D.	ALTER ACCOUNT SET DATE_OUTPUT_FORMAT = 'DD/MM/YYYY';

---

Which Snowflake role can you use to view all the accounts in an organization?

ORGADMIN

---

At which levels can session parameters be set in Snowflake?

User level

Session level

Account level

---

What do resource monitors allow you to do?

They allow you to specify a credit spending limit, which, if breached, leads to an action being performed

---

CREATE OR REPLACE MASKING POLICY SALESMASK 
	AS (VAL NUMBER) RETURNS NUMBER ->
		CASE
		  WHEN CURRENT_ROLE() IN ('BOB_ROLE') THEN VAL
		  ELSE 0
		END;

Which statements about this masking policy are true?

This policy not allow a user using ALICE_ROLE to view the data

This policy applies to numerical data