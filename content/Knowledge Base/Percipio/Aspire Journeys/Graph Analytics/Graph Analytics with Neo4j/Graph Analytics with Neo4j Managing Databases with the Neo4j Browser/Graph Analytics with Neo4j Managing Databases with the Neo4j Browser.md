---
date: 2001-01-01
---

# Graph Analytics with Neo4j Managing Databases with the Neo4j Browser

### Connecting to Neo4j Database

- **Connection Methods**: 
  - Neo4j Browser
  - Cypher Shell
  - Web browser (HTTP/HTTPS)

### Setting Up Neo4j Desktop

1. **Create a New Project**:
   - Name: **Exploring the Neo4j Browser**.

2. **Add Local DBMS**:
   - Name: **My Local DBMS**.
   - Set a memorable password.
   - Choose the latest version.
   - Click **Create** and then **Start** to activate it.

### Databases Overview

- **Databases Available**:
  - **system** (grayed out)
  - **neo4j** (default)
  
3. **Add a Third Database**:
   - Name: **loonydb**.

### Interacting with the Neo4j Database

- **Open Neo4j Browser**:
  - Accessible from the Neo4j Desktop or a regular web browser (navigate to `localhost:7474`).
  - Three options appear:
    - Getting started with Neo4j Browser
    - Try Neo4j with live data
    - Cypher basics

### Communication Protocols

- **Neo4j Browser vs. Regular Web Browser**:
  - Neo4j Browser uses **Bolt protocol** (faster).
  - Regular web browsers use **HTTP protocol**.

### Loading Data into Neo4j

- **Dataset**: Movie graph dataset (actors, directors, movies).
- **Load Data**:
  - Use command: `:play movie graph`.
  - Follow prompts to execute CREATE statements to add nodes and relationships.
  
### Database Management

- **Switching Databases**:
  - Use command: `:use <database_name>`.
  - Or use the database dropdown menu.

### Querying Data

- **Check for Data**:
  - Run query: `MATCH (nodes) RETURN nodes LIMIT 25`.
  - **For `loonydb`**: No data (empty).
  - **Switch back to neo4j**: Query returns movie and person nodes.

### Creating a New User

1. **User Management**:
   - Currently connected as **neo4j** (admin role).
   - Use command: `:server user list` to view existing users.

2. **Add New User**:
   - Command: `:server user add`.
   - Input:
     - Username: **loonycorn**.
     - Password: [choose a memorable password].
   - Assign Role: **reader** (limited permissions).

3. **User Roles**:
   - Roles include: PUBLIC, admin, architect, editor, publisher, reader.
   - Readers can access and read data but cannot modify it.

4. **Password Management**:
   - Option to require a password change on first login.

5. **Confirmation**:
   - Run `:server user list` to verify creation of **loonycorn** user.
   - Confirm that the user has **reader** and **PUBLIC** roles.
   - Password change required for the new user upon first login. 

### Additional Resources

- For detailed role permissions: [Neo4j Built-in Roles Documentation](https://neo4j.com/docs/operations-manual/current/authentication-authorization/built-in-roles/).

### User Permissions Testing

1. **Disconnecting from Admin User**:
   - Run command: `:server disconnect` as the **neo4j** admin user.

2. **Connecting as New User**:
   - Connect using username **loonycorn** and the assigned password.
   - Since a password change is enforced, enter a new password (e.g., **new_password**).

3. **Confirm Connection**:
   - Check the "Connected as" section to confirm the user is **loonycorn** with roles **reader** and **PUBLIC**.

### Testing Permissions

- **Create Query Attempt**:
  - Attempt to run: `CREATE (n:Company {name: "loonycorn"})`.
  - Result: ERROR indicating lack of permissions to create nodes.

- **Confirm Read Permissions**:
  - Run query: `MATCH (n:Person {name: "Keanu Reeves"}) RETURN n`.
  - Result: Successfully retrieves node with properties:
    - **Person, id: 1, born: 1964, name: Keanu Reeves**.

### User Administration as Admin

1. **Reconnect as Admin**:
   - Log back in with **neo4j** credentials.

2. **View User List**:
   - Check existing users and their statuses.

3. **Suspending a User**:
   - Select **loonycorn** and click **Suspend**.
   - Status changes to **Suspended**, preventing access.

4. **Removing a User**:
   - Choose to delete **loonycorn** from the user list.

### Database Management Commands

1. **List Databases**:
   - Run command: `:dbs` to view available databases (three listed).

2. **System Information**:
   - Execute command: `:sysinfo` to access system-related metrics.
   - Key metrics include:
     - **Store Size**: Disk space used by the database.
     - **Id Allocation**: 171 nodes, 253 relationships, 6 relationship types, 391 properties.
     - **Page Cache**: 18,000+ hits; Page Faults: 191; Hit Ratio: 100.00%; Usage Ratio: 0.29%.

3. **Transaction Metrics**:
   - Review transaction-related metrics: Last Transaction ID, Current Read/Write, Peak Transactions.

### Managing Queries

1. **View Active Queries**:
   - Run command: `:queries` to list currently executing queries.
   - Monitor long-running queries for resource consumption.

2. **Simulate Long-Running Query**:
   - Example: Create nodes using `FOREACH` to generate close to one billion nodes.

3. **Terminate a Query**:
   - Select the running query and execute the **Kill** operation to stop it.

### Favorites Menu

1. **Saving Favorite Queries**:
   - Add a new favorite query (e.g., name it **My Favorite Query**).
   - Update to ensure the name is reflected correctly.

2. **Complex Queries**:
   - Include more complex queries for easier access.

3. **Organizing Queries**:
   - Create a new folder (e.g., **My Favorite Queries Folder**) and drag **My Favorite Query** into it.
   - Run queries directly from this organized structure.

### Exploring Neo4j Browser Settings

#### User Interface Settings

1. **Theme Options**:
   - Navigate to **Settings** > **User Interface**.
   - Change the theme from **Auto** to **Normal**, **Outline**, or **Dark**.
   - The **Dark Theme** is the most noticeable change.

#### Text Formatting

2. **Code Font Ligatures**:
   - Enable/disable ligatures to see combined characters like "does not equal" (≠) and "approximately equal" (≈).
   - Disabling shows original characters (e.g., `!=` for does not equal).

#### Multi-Statement Queries

3. **Multi Statement Configuration**:
   - Enable multi-statement execution in the settings.
   - Attempt to execute multiple `CREATE` statements; an error occurs if this is disabled.
   - After enabling, re-execute and both nodes (e.g., "Millie Bobby Brown" and "Finn Wolfhard") are created successfully.

#### Initial Command & Connection Timeout

4. **Initial Command**:
   - Change the default initial command to `:play movie graph`.
   - Test by disconnecting with `:server disconnect` and reconnecting. The new command executes automatically.

5. **Connection Timeout**:
   - Set a custom connection timeout (e.g., **40000 ms**).

#### Result Frames Configuration

6. **Result Frame Settings**:
   - Configure maximum result frames and history (default is 30).
   - Adjust settings under **Graph Visualization**: 
     - **Initial Node Display** to 300, **Max Neighbours** to 100, **Max Rows** to 1000.

#### Running Queries

7. **Running MATCH Queries**:
   - Execute a query to retrieve nodes and relationships (e.g., 173 nodes, 508 relationships).
   - Adjust result frame settings to limit displayed results (e.g., set max result frames to 1 and history to 3).

8. **Viewing Results in Different Formats**:
   - **Graph View**: Visual representation of nodes and relationships.
   - **Table View**: Display results in tabular format, showing columns for node1, relation, and node2.
   - **Text View**: List properties of nodes and relationships without identifiers.
   - **Code View**: Shows the executed query and server details.

#### Node Connection Setting

9. **Connecting Result Nodes**:
   - Option to **Connect result nodes** after executing a query.
   - If checked, nodes will display their relationships; if unchecked, they will be displayed independently.
   - Useful for analyzing nodes alone or in context with their relationships.

### Exploring the Neo4j HTTP API

#### Introduction to HTTP API

In this segment, we shift focus from managing the Neo4j database using the Neo4j Desktop and Browser to utilizing the HTTP API, which is essential for developers. The HTTP API allows applications to communicate with Neo4j via HTTP requests, enabling various operations like creating nodes and executing queries.

#### Configuring the Settings

1. **Update Settings File**:
   - Add the line `dbms.rest.transaction.idle_timeout=3600` (for one hour) in the settings file to enable REST communication.
   - Restart the local DBMS to apply the settings.

#### Sending GET Requests

2. **Using GET Requests**:
   - Open Neo4j Browser and send a GET request to `http://localhost:7474`.
   - The response is a JSON object containing details about the DBMS, such as:
     - `"bolt_routing"`: `neo4j://localhost:7687`
     - `"neo4j_version"`: `4.3.6`
     - `"neo4j_edition"`: `enterprise`

#### Creating Nodes with POST Requests

3. **Creating a Node**:
   - To create a node, you need to initiate a transaction using a POST request.
   - The endpoint for starting a transaction is `http://localhost:7474/db/{databaseName}/tx`.

4. **Constructing the POST Request**:
   - Format the POST request with a JSON body that includes the `statements` array:
     ```json
     {
       "statements": [
         {
           "statement": "CREATE (n:Human {name: \"Jamie Hipster\", age: 55})"
         }
       ]
     }
     ```
   - Send this POST request to the transaction endpoint.

5. **Response Handling**:
   - The response includes a `results` property and a `commit` URL:
     - Example commit URL: `http://localhost:7474/db/neo4j/tx/1/commit`.
   - Transactions need to be committed within the set idle timeout.

#### Committing the Transaction

6. **Committing the Transaction**:
   - To commit, send a POST request to the commit URL.
   - Verify the response shows no errors, indicating success.

#### Extending Transaction Timeout

7. **Extending Timeout**:
   - If needed, extend the transaction timeout by sending a POST request to the transaction endpoint with an empty JSON object:
     ```json
     {
       "statements": []
     }
     ```
   - This can provide additional time before the transaction expires.

#### Verification of Node Creation

8. **Confirming Node Creation**:
   - Check the database information to confirm the new node exists under the "Human" label.
   - Click on the label to view the properties of the newly created node (e.g., name: "Jamie Hipster", age: 55).

### Conclusion

By utilizing the Neo4j HTTP API, developers can effectively create, read, update, and delete nodes and relationships programmatically. This knowledge equips you with the tools to interact with the Neo4j database directly from your applications, leveraging the capabilities of the RESTful architecture.