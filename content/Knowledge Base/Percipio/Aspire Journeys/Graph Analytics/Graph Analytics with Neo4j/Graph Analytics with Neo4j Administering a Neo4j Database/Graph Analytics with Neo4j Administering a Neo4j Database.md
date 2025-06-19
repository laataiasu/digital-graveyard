---
date: 2001-01-01
---

# Graph Analytics with Neo4j Administering a Neo4j Database

### Creating Projects in Neo4j Desktop

1. **Neo4j Desktop Overview**:
   - Interact with databases using Neo4j Desktop and Neo4j Browser.
   - Initially, a default database is loaded upon startup.

2. **Creating a New Project**:
   - Navigate to the **Projects** menu.
   - Click on **New Project**.
   - An empty project is created, initially named "Project". 
   - Rename the project using the **Edit** button. Example: "Project using Local DBMS".

3. **Adding a Database Management System (DBMS)**:
   - Within the project, you can create one or more DBMS instances.
   - Click on the **Add** button to add a new DBMS.
   - Choose between:
     - **Local DBMS**
     - **Remote Connection**
     - **File**
   - Select **Local DBMS**.
   - Assign a name (e.g., "My Local DBMS") and set a password.

4. **Setting DBMS Version**:
   - By default, version 4.2.1 is selected, but you can choose a newer version if available.
   - Newer versions may require downloads, so be prepared for a wait.

5. **Starting the DBMS**:
   - After setup, click **Create** to initialize the DBMS.
   - The system displays the new DBMS with its version.
   - Start the DBMS to activate it.

6. **Creating Databases within the DBMS**:
   - The default system database is automatically created.
   - To add a new database, click **Create Database** and enter a name (e.g., "dbUsingUI").

7. **Adding a Remote DBMS**:
   - Open a web browser to access hosted Neo4j databases.
   - Example URL: [Neo4j Developer Hosted Databases](https://neo4j.com/developer/example-data/#_hosted_databases).
   - Select a database (e.g., "fincen") to connect to.
   - Note the connection URL, username, and password for later use.

8. **Connecting to the Remote DBMS**:
   - Back in Neo4j Desktop, add a **Remote Connection** within the project.
   - Enter the connection details:
     - Name: "My Remote DBMS"
     - Connection URL: `demo.neo4jlabs.com` (use secure protocol `neo4j+s`).
     - Username and password corresponding to the database name (e.g., "fincen").

9. **Switching Between DBMS Instances**:
   - Only one DBMS can be active at a time. Starting the remote DBMS will stop the local one.
   - Open the Neo4j Browser to explore the active remote DBMS.

10. **Viewing Database Contents**:
    - Use commands like `MATCH (nodes) RETURN nodes LIMIT 25` to view data in the active database.
    - Use `CLEAR` to remove command history from the Neo4j Browser.

11. **Creating Projects from Directories**:
    - Navigate to **New** > **Create Project from Directory** to utilize existing project files.
    - Select an empty folder or one with project files to create a new project.

12. **Importing Sample Projects**:
    - Use **Import Sample Project** to load example projects provided by Neo4j.
    - Choose a sample (e.g., "twitter-v2"), specify the Neo4j version, and set a password.
    - Install and start the sample DBMS.

In the previous video, we explored various ways to create projects in Neo4j Desktop and now we’ll shift our focus to some key settings related to these projects.

First, let’s select the project we created from scratch, named **Project using Local DBMS**. After selecting it, we can see the details of the database management systems (DBMS) associated with it.

### Exploring DBMS Settings

1. **DBMS Details**: Clicking on **My Local DBMS 4.3.6** brings up a pane that shows information about this DBMS. Here, we can add a description, view the version, edition, and status, as well as reset the DBMS password.

2. **Plugins**: Next, let’s look at the **Plugins** tab. Currently, there are several plugins available:
   - **APOC**: A library of over 450 procedures for Cypher queries, offering many useful operations.
   - **Graph Data Science Library**: Simplifies data science tasks on a graph database.
   - **Neo4j Streams**: Connects Neo4j to streaming services like Kafka.
   - **Neosemantics**: Allows communication with RDF data formats.

   We can install the APOC library and the Graph Data Science Library, but for now, we won’t be using them.

3. **Upgrade Options**: In the **Upgrade** tab, we can see the option to upgrade the DBMS version. Since we're already on the latest version, there are no upgrade prompts available.

### Deleting Projects and DBMS

Now, let’s discuss how to delete projects and DBMS. First, we’ll delete the **twitter-v2** project, which is currently active. We need to stop it first, then confirm its deletion.

Next, we can delete the **Project from Directory** since it has been offline. Finally, for **Project using Local DBMS**, we will remove **My Remote DBMS** while keeping the local DBMS intact.

### Starting the Local DBMS

With only the local DBMS remaining, let’s start it up and focus on changing its password. Before we do this, we’ll disconnect from the DBMS in the Neo4j Browser to demonstrate the impact of the password change.

### Changing the Password

After disconnecting, we’ll re-enter the DBMS using the old password to verify that it no longer works. Next, we’ll go back to Neo4j Desktop, enter a new password for the local DBMS, and apply the changes.

Once the password is reset, we’ll reconnect to the DBMS using the new password. This should allow us to access it successfully.

### Viewing Logs

Next, let’s examine the logs of our local DBMS. We can access several log files, including:
- **neo4j.log**: Records the starting and stopping of the DBMS.
- **debug.log**: Offers detailed logging information for debugging.
- **query.log**: Logs each query executed, either by users or the system.
- **security.log**: Tracks login attempts, primarily by the default user.

These logs can also be accessed through a file explorer for a more detailed view.

### Exploring DBMS Folders

Finally, we’ll look at the **Open folder** menu options, which includes:
- **Import**: Where you can drop files like CSVs to load into the DBMS.
- **Plugins**: Shows installed plugins.
- **Logs**: Contains log files.
- **DBMS Directory**: Contains various folders, including binaries and configuration files.

With this overview, we’ve covered the essential settings and configurations in Neo4j Desktop, including how to manage projects, DBMS, and their associated files and logs. In the next video, we’ll delve deeper into using Neo4j with actual data and queries.

In this section, we’ll delve into how to interact with databases in Neo4j using the Cypher Shell. We’ll build on the foundational knowledge we've established and demonstrate practical database administration tasks through command-line operations.

### Accessing the Cypher Shell

First, let’s access the Terminal in Neo4j Desktop:

1. **Open Terminal**: From the DBMS menu, select **Terminal** to launch a shell interface.
2. **Check Directory**: Use the command `pwd` to confirm you’re in the top-level DBMS folder, and `ls` to list the contents. This should include directories like **bin**, **certificates**, and **logs**.

### Launching Cypher Shell

To start using Cypher, navigate to the **bin** directory and execute the Cypher Shell:

```bash
./bin/cypher-shell
```

You'll be prompted for your credentials. Enter the username (`neo4j`) and the password you set earlier. Upon successful entry, you’ll be connected to the Neo4j database via the Cypher Shell.

### Viewing Databases

Now that we’re connected, let’s view the databases available in the DBMS:

```cypher
SHOW DATABASES;
```

This command displays all databases, indicating their current status. You should see the default databases: **system**, **neo4j**, and any others you created, like **dbusingui**.

### Creating a New Database

To create a new database, we can use the following command:

```cypher
CREATE DATABASE newDB;
```

After executing this command, confirm the creation by running `SHOW DATABASES;` again. The new database should appear as online.

### Syncing with Neo4j Desktop

Next, let’s check if the new database shows up in the Neo4j Desktop:

1. Navigate back to Neo4j Desktop and hit the **Refresh** button.
2. You should see **newDB** listed among the databases, confirming the update.

### Stopping and Starting Databases

To manage databases effectively, you might need to stop and start them:

- **Stop a Database**:

```cypher
STOP DATABASE newDB;
```

Check the status with `SHOW DATABASES;` to ensure it shows as offline. 

- **Start a Database**:

```cypher
START DATABASE newDB;
```

Run `SHOW DATABASES;` again to verify that it’s back online.

### Deleting a Database

When a database is no longer needed, you can delete it using:

```cypher
DROP DATABASE newDB;
```

Confirm the deletion with `SHOW DATABASES;`, which should now list only the remaining databases. 

Now that we’re familiar with the Cypher Shell for basic database administration, let's explore how to execute Cypher queries within it. This will enhance our ability to manage and manipulate data in Neo4j effectively.

### Creating a New Database

First, we need to create a database where we can run our Cypher queries. We'll create a new database called **newDatabase**:

```cypher
CREATE DATABASE newDatabase;
```

After confirming its creation with:

```cypher
SHOW DATABASES;
```

we should see **newDatabase** listed as online. This database is empty, so we'll proceed to create some nodes.

### Switching Databases

To interact with our newly created database, we need to switch to it using the following command:

```cypher
:use newDatabase;
```

The prompt will now indicate that we're connected to **newDatabase** as the `neo4j` user.

### Creating Nodes

Next, we’ll create our first node. For instance, let’s create a node representing a person named Ben:

```cypher
CREATE (ben:Human {name: "Ben", age: 46}) RETURN ben;
```

Here’s what’s happening:
- **CREATE** specifies we want to create a new node.
- We define the node with a variable `ben`, label it as `Human`, and set its properties (name and age).
- Finally, **RETURN ben** allows us to view the created node’s details.

When executed, the output will provide a text representation of the node.

### Using Parameters

Next, let’s create another node using parameters, which are handy for reusability:

1. Define a parameter for the name:

```cypher
:param name => "jasmine";
```

Parameters allow us to set values once and reference them multiple times. Next, we’ll create a second node:

```cypher
CREATE (jasmine:Human {name: $name, age: 45}) RETURN jasmine;
```

In this query:
- We reference the parameter `$name`, which will be replaced by "jasmine".
- This query creates another node with the name Jasmine.

### Viewing Created Nodes

To see all nodes in our database, we can run:

```cypher
MATCH (nodes) RETURN nodes;
```

This will return the two nodes we’ve date: Ben and Jasmine.

### Checking in Neo4j Browser

To compare, let’s switch to the Neo4j Browser:

1. Run the command:

```cypher
:dbs
```

This will list available databases. We’ll switch to **newDatabase** using:

```cypher
:use newDatabase;
```

Now, execute:

```cypher
MATCH (nodes) RETURN nodes;
```

In the graph view, we should see both nodes displayed as isolated entities, confirming their successful creation.

Let's continue our exploration of database administration tasks in Neo4j, focusing on making detailed configuration changes through the settings file.

### Setting Up a New Project

We'll start by creating a new project in Neo4j Desktop. For clarity, I’ve cleared all previous projects, but you can keep yours if you prefer. 

1. Open the Projects pane and create a new project, which defaults to **Project**.
2. Rename this project to **Project Demo Settings** for clarity.

### Creating a Local DBMS

Next, we’ll set up a Local DBMS:

1. Click on **Add** and select **Local DBMS**.
2. Assign a name and a memorable password, then choose the latest version of Neo4j.

Once created, start the DBMS. By default, it includes two databases: **system** and **neo4j**.

### Adjusting Database Limits

To manage the number of databases, we’ll change the maximum allowed:

1. Access the **Settings** through the DBMS menu.
2. In the settings file, locate the `dbms.max_databases` property, which defaults to 100 (commented out).
3. Uncomment this line and change its value to **3** to simplify testing.

Now, apply the changes. This will prompt you to restart the DBMS. Choose to restart now.

### Creating Databases

After the restart:

1. Verify that the DBMS is active and note the new limit of 3 databases.
2. Create a third database, naming it **database3**. This should succeed since we’re within the limit.

If you attempt to create a fourth database, you’ll receive an error message indicating that the limit has been reached.

### Changing the Default Database

Now, let’s change the default database from **neo4j** to **database3**:

1. Open the **Settings** again and locate `dbms.default_database`.
2. Uncomment this line and set its value to **database3**.
3. Apply the changes and restart the DBMS.

After restarting, the default database will now be **database3**. 

Let’s dive deeper into the DBMS settings file to explore how to change HTTP connection settings for the Neo4j database management system.

### Accessing the Default HTTP Port

Before making any changes, we want to check if we can access the default HTTP port. Open your web browser and navigate to:

```
http://localhost:7474/
```

This should bring up the Neo4j connection page, allowing you to connect to the database.

### Disabling HTTP Connections

Next, we’ll disable HTTP connections to see what happens:

1. Go back to **Neo4j Desktop** and select **My Local DBMS**.
2. Click on **Settings**.

Scroll down to the connector settings. You’ll see entries for HTTP, Bolt, and HTTPS:

- `dbms.connector.bolt.enabled=true`
- `dbms.connector.http.enabled=true`
- `dbms.connector.https.enabled=false`

Change the `dbms.connector.http.enabled` property to `false`:

```
dbms.connector.http.enabled=false
```

Now, apply the changes and restart the DBMS. After the restart, try to access the database again via the web browser at port 7474. You should see that the connection fails, confirming that HTTP is disabled.

### Modifying the HTTP Port

Next, let’s change the port for HTTP connections:

1. Return to the **Settings** menu in Neo4j Desktop.
2. Set `dbms.connector.http.enabled` back to `true`.
3. Uncomment the following lines to specify the HTTP port:

```
dbms.connector.http.listen_address=:7474
dbms.connector.http.advertised_address=:7474
```

Change these to a new port, say 7477:

```
dbms.connector.http.listen_address=:7477
dbms.connector.http.advertised_address=:7477
```

Apply the changes and restart the DBMS. After the restart, confirm that port 7474 is still inaccessible. Now, navigate to:

```
http://localhost:7477/
```

You should successfully connect to the database on the new port.

### Resetting to Default Settings

If at any point you feel overwhelmed by the changes, you can easily revert to the original settings:

1. Go back to the **Settings** menu for your DBMS.
2. Click **Reset to defaults**. 

After confirming, you’ll see that all settings return to their defaults, including the default database being set back to **neo4j** and the HTTP port reverting to **7474**.

### Summary

In this exploration, we successfully:
- Accessed the default HTTP port.
- Disabled HTTP connections.
- Changed the HTTP connection port.
- Reset settings to their defaults.

These tasks illustrate how flexible and customizable Neo4j is, allowing you to tailor configurations to your needs. In future sessions, we can explore other aspects of DBMS configuration and management.