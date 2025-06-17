---
date: 1970-01-01
---

# Graph Analytics with Neo4j An Introduction to Graph Databases & Neo4j

### Understanding Graph Databases

#### What is a Graph?
A graph is a data structure made up of nodes and edges:
- **Nodes**: Also known as vertices or points, nodes represent entities such as individuals, companies, or locations.
- **Edges**: These are connections between nodes, representing relationships. Edges can be directed (one-way) or undirected (two-way).

#### Nodes
- Each node represents an entity.
- Nodes can have properties stored as key-value pairs.
  - **Example**:
    - **Node: Adele**
      - Name: Adele
      - Date of Birth: 23/10/1989
      - City: Leeds
    - **Node: Karim**
      - Name: Karim
      - Date of Birth: 14/04/1997
      - City: Cairo

#### Edges
- Edges represent relationships between nodes.
- Relationships can have properties.
  - **Example**: 
    - Relationship: "Adele is Karim's manager"
    - Edge Property: Since (indicating when the relationship started)

#### Relationship Types
- Relationships can be directed or undirected:
  - **Directed**: One node influences another (e.g., manager to employee).
  - **Undirected**: Mutual relationship (e.g., friends).

#### Complex Graph Structures
- A graph can represent multiple nodes and relationships:
  - **Example**: 
    - Nodes: Adele, Karim, Emma, Leo (all employees)
    - Relationships: Adele manages Karim, Emma, and Leo; Karim manages Irma and Andy.
  
#### Different Entity Types
- Graphs can include various entity types:
  - **Example**: 
    - Nodes for individuals (Adele, Karim, Emma, Leo) and clients (e.g., Diallonic).
    - Two types of relationships: "Manages" between individuals, "Works with" between individuals and clients.

#### Neo4j Representation
- Different entity types can be represented by labels associated with each node.
- Relationship types help model different relationships between entities.

This structure allows for representing complex interconnections in a clear and organized manner, optimized for exploring relationships.

### Features of Graphs

#### Types of Graphs

1. **Connected Graph**
   - Every pair of nodes has a connection, either direct or indirect.
   - **Example**: In a graph with nodes A through F, you can travel from any node to any other node via existing paths.

2. **Disconnected Graph**
   - At least one pair of nodes lacks a direct or indirect connection.
   - **Example**: If the connection between nodes E and D is broken, nodes F and E become inaccessible from the other nodes.

3. **Strongly Connected Graph**
   - Every pair of nodes has a direct connection.
   - All nodes are interconnected without needing to traverse through others.

#### Cyclic vs. Acyclic Graphs

- **Cyclic Graph**
  - Contains at least one cycle or loop.
  - **Example**: If there’s a direct connection between nodes B and E, traversing from B can lead back to B, forming a cycle.

- **Acyclic Graph**
  - Contains no loops or cycles.
  - **Example**: A graph with six nodes and five edges without any connections that lead back to the same node.

#### Special Graph Structures

- **Tree**
  - A connected, acyclic graph.
  - Commonly used in various applications.

- **Directed Acyclic Graph (DAG)**
  - Edges have a direction, and no cycles exist.
  - Frequently used in fields like machine learning.

#### Importance of Graph Properties
Understanding these graph properties is essential for analyzing relationships in data structures effectively. In practical applications, such as transportation networks, recognizing connected vs. disconnected graphs can reveal accessibility issues. 

### Comparing Relational Databases and Graph Databases

#### Similarities
- Both relational and graph databases store data about entities (e.g., people, organizations, vehicles).
- Each can model relationships between entities, accommodating one-to-one, one-to-many, and many-to-many relationships.

#### Relational Database Example
Consider a restaurant chain with:
- **Restaurant Table**: 
  - Columns: Name, City, Address, Category Code, ID
- **Sales Table**: 
  - Columns: Restaurant ID, Customer ID, Sale Date, Sale Amount
- **Customer Table**: 
  - Columns: Name, DOB, ID

In this setup:
- **Relationships**: 
  - Many-to-one from Sales to Restaurant (via Restaurant ID).
  - One-to-many from Customers to Sales (via Customer ID).

**Advantages**:
- Ideal for highly structured data.
- Supports join operations for combining data from multiple tables.

**Typical Queries**:
- Retrieve specific customer details.
- Find top-performing students or aggregate sales for products.

#### Graph Database Example
Using a news website:
- **Nodes**: Represent users (e.g., Karim) and articles (e.g., Sports, Politics).
- **Relationships**: 
  - Read articles (one-way).
  - Like articles (one-way).
  - Follow other users (bidirectional).

**Advantages**:
- Well-suited for many-to-many relationships.
- Easier to analyze patterns and connections between nodes.
- Relationships are first-class citizens, allowing for more complex queries about engagement.

#### Key Differences
- **Data Structure**:
  - **Relational DBs**: Data is organized in tables (rows and columns).
  - **Graph DBs**: Data is stored in nodes and relationships, with properties defining their attributes.

- **Focus**:
  - **Relational DBs**: Emphasis on entities and their attributes.
  - **Graph DBs**: Emphasis on the relationships and how entities connect.

- **Querying**:
  - **Relational DBs**: Efficient for retrieving specific entity data.
  - **Graph DBs**: Efficient for exploring relationships and detecting patterns (e.g., fraud detection, social network analysis).

#### Conclusion
Choosing between a relational or graph database depends on the nature of your data and the types of queries you need to perform. Relational databases excel with structured data and straightforward queries, while graph databases shine in scenarios where relationships and connections are paramount.

### Exploring Graph Databases: Use Cases and Neo4j

#### Recap of Graph Database Features
- Graph databases excel at representing connections between entities, prioritizing relationships over individual entity data.
- They facilitate various graph-based operations, such as finding the shortest path between nodes and calculating metrics like centrality and PageRank.

#### When to Use a Graph Database
1. **Is Your Data Graph-Structured?**
   - If you need to model complex relationships (e.g., social networks), a graph database is ideal.
   
2. **Are Relationships Critical to Your Queries?**
   - If your queries focus on relationships (e.g., identifying articles read but not liked), a graph database is the way to go.

If you answered "no" to both questions, consider a relational or document database instead.

#### Key Use Cases for Graph Databases
- **Product Recommendations**: Analyze connections among users and their purchases to suggest new products.
- **Social Networks**: Model interactions among users, friends, and shared content.
- **Supply Chain Management**: Represent and analyze relationships between suppliers, distributors, and consumers.
- **Neural Networks & AI**: Leverage graph structures for data representation and algorithms.

### Introduction to Neo4j
- **Overview**: Neo4j is a leading graph database management system developed by Neo4j Inc., launched in 2010. It's built in Java and supports various programming languages.
- **Access**: Interact with Neo4j via a REST API or the more efficient Bolt protocol.

#### Working with Neo4j
- **Neo4j Desktop**: A client application for setting up and managing your Neo4j database.
- **Neo4j Browser**: A tool included with Neo4j Desktop for running Cypher queries and performing administrative tasks.
- **Cypher Query Language**: Inspired by SQL, it’s designed for querying graph data in Neo4j.

#### Communication Protocols
- **Bolt Protocol**: Offers efficient communication between applications and the database, preferred for performance.
- **HTTP API**: Supports standard RESTful operations (GET, POST, PUT, DELETE) for database interaction.

#### Additional Tools and Libraries
- **APOC Library**: Provides utility functions to enhance Cypher queries, streamlining complex operations.
- **GraphQL Plugin**: Enables GraphQL queries to be translated into Cypher for Neo4j.
- **Graph Data Science Library**: Allows in-memory graph creation for advanced operations like shortest path analysis and machine learning pipelines.

### Getting Familiar with Neo4j Desktop

Now that you’ve installed Neo4j Desktop, let's dive into its interface and features, which are designed for developers to experiment with graph databases before moving to production.

#### Overview of Neo4j Desktop
- **Example Project**: When you open Neo4j Desktop, you’ll see an Example Project featuring the **Movie DBMS**, which contains two databases:
  - **System Database**: Contains system-related data (not for user interactions).
  - **Neo4j Database**: This is where you’ll create and manipulate nodes and relationships, starting with a movie dataset.

#### Managing DBMS
- **Active DBMS**: The Movie DBMS is marked as **ACTIVE**. You can only have one active DBMS at a time in a single Neo4j Desktop instance.
- **Stopping the DBMS**: To create another DBMS, you need to stop the active one. You can do this by:
  1. Minimizing the project pane.
  2. Hovering over the Movie DBMS line to reveal the **Stop** button.
  3. Clicking the **Stop** button until it shows **No active DBMS**.

#### Features of a Stopped DBMS
Once the DBMS is stopped, you can:
- Access **Settings** and **Logs**.
- Use a **Terminal** for command-line interactions.
- Perform operations such as:
  - **Clone**: Create a copy of the DBMS.
  - **Dump**: Export the database contents to a file.
  - **Remove**: Delete the DBMS entirely.

#### Creating a Dump
- **Dump Feature**: This allows you to capture the state of the database. Click on **Dump** and a file (e.g., `movie-dbms-neo4j-2021-10-19T094707.dump`) will be generated.
- **Finding the Dump File**: Use the **Reveal files in Finder** option to locate the dump file, which will be stored in your Neo4j Desktop directory.

#### Restoring from a Dump
To create a new DBMS from the dump:
1. Navigate back to Neo4j Desktop.
2. Click on the dump file to expand the menu.
3. Select **Create a new DBMS from this dump**.
4. Provide a name and password, choose the version, and click **Create**.

Once created, you can start the new DBMS. This DBMS will contain the same structure and data as the original Movie DBMS, including:
- **Nodes and Relationships**: In the example, there are 169 nodes and 250 relationships, indicating many-to-many relationships typical in graph databases.
- **Labels and Relationships**: In the Movie DBMS, you’ll see labels representing entity types (like people and movies) and relationship types (acting, directing, etc.).

#### Managing DBMS and Files
- **Stopping and Deleting**: After exploring, you can stop the new DBMS and remove it along with its dump file.
- **Exploring Details**: Clicking on the Movie DBMS will show details such as version, edition (e.g., enterprise), and status (e.g., stopped). You can also manage plugins and upgrade the DBMS.

### Exploring Neo4j Desktop Features

Before we start using Neo4j Desktop, it's helpful to understand the various options available. This will shed light on the features of graph databases in general, and Neo4j specifically.

#### Databases Menu
- **Navigating DBMS**: Click on the **Databases** menu (database icon) to see the different DBMS instances on your system. For instance, you might see a single instance of Neo4j version 4.2.1 under the Example Project, specifically in the Movie DBMS.
- **Multiple DBMS**: Neo4j Desktop allows you to have multiple DBMS instances, each potentially running different versions of Neo4j. This flexibility is useful for testing new features and deciding on upgrades.

#### Graph Apps Menu
In the **Graph Apps** section, you’ll find default applications that enhance your experience with Neo4j:
1. **Neo4j Browser**: This app lets you interact with databases, run queries, and explore data.
   - Version: 4.3.5
2. **Neo4j Bloom**: A visualization tool that allows you to see your data from different business perspectives.
   - Version: 1.9.0
3. **Neo4j ETL Tool**: Simplifies the process of loading data from relational databases into Neo4j.
   - Version: 1.5.1

You can also **Install additional apps** to extend the functionality of Neo4j Desktop.

#### Help & Learn
- In the **Help & Learn** section, you can access various resources, including the **Neo4j Desktop Manual** and **User Interface Guide**, along with other documentation like:
  - Operations Manual
  - Knowledge Base
  - Neo4j Browser Developer Pages

#### Notification Center
- The **Notification Center** displays updates related to Neo4j Desktop. You can check for updates, and in this case, you might find a new version available. It's important to note that the Neo4j Desktop version is different from the versions of the DBMSs you are using.

#### Settings
- The **Settings** menu allows you to configure Neo4j Desktop. Here, you can manage options like:
  - **Product Analytics**: Options to send crash reports and usage statistics.
  - **Proxy Configuration**: If needed, you can set up a proxy (HTTP, Local PAC file, Remote PAC file).

#### Software Keys and About
- **Software Keys**: This section confirms that you have entered your keys correctly during installation.
- **About Section**: Here, you can check the current version of Neo4j Desktop.

### Exploring Nodes and Relationships in Neo4j

Now that we've installed Neo4j Desktop and familiarized ourselves with its features, it's time to dive deeper into what a Neo4j database contains—specifically, the nodes and relationships that make up the data.

#### Starting the Movie DBMS

We will use the **Movie DBMS** that was automatically loaded. First, ensure that you **start** it so that it becomes the **ACTIVE DBMS**. To interact with the database, we’ll open the **Neo4j Browser**. You can do this by expanding the **Open** menu and selecting **Neo4j Browser**.

#### Neo4j Browser Overview

The Neo4j Browser is where you can execute queries and visualize the database. When you connect, you’ll see a message confirming your connection as the user **neo4j** on **localhost**, using the **Bolt protocol** on port **7687**.

#### Running Commands

At the top of the Neo4j Browser, there’s a prompt where you can type commands. You can run **Cypher queries** here, or use commands by preceding them with a colon (`:`). Some available commands include:
- `:play` (to access guides)
- `:param` (to define parameters for queries)
- `:clear` (to clear the output)

#### Using the :play Command

To get started, run the command:
```
:play movie graph
```
This will pull up a guide specifically designed for the movie graph dataset, which can help you understand how to interact with Neo4j.

#### Running a Cypher Query

Next, let’s execute a Cypher query to retrieve all nodes and relationships in the database. This is analogous to a SQL `SELECT *` query but for a graph database. The query structure is as follows:
```cypher
MATCH (nodes)
RETURN nodes
```
Here, `MATCH` identifies the pattern (in this case, all nodes), and `RETURN` specifies what to retrieve.

After running the query, you’ll see the nodes represented as circles, with relationships shown as lines connecting them.

#### Analyzing the Graph

- **Node Labels**: In the results, nodes will have labels, such as **Movies** (orange) and **Persons** (blue). 
- For example, the movie **Cloud Atlas** (orange node) has relationships with various persons, like actors or directors. 
- The relationship **ACTED_IN** connects actors to movies, while **DIRECTED** connects directors.

#### Exploring Relationships

Using the right-hand menu, you can see the different types of relationships, including:
- **ACTED_IN**: Connects actors to movies.
- **WROTE**: Links writers to movies.
- **DIRECTED**: Shows directors of movies.
- **PRODUCED**: Indicates producers associated with films.

#### Navigating the Graph

You can zoom in and out to explore different areas of the graph. For example, examining the movie **Snow Falling on Cedars** will show both its actors and director, along with their connections to the film. You might find that **Danny DeVito** has multiple relationships with different movies, showcasing the many-to-many nature of relationships in a graph database.

### Exploring the Movie Graph Schema in Neo4j

In our previous exploration, we observed how movies and persons are interconnected through various many-to-many relationships. Now, we’ll take a closer look at the schema of our Movie Graph database and delve into executing additional queries.

#### Visualizing the Database Schema

To start, we can visualize the current schema by running the following command in the Neo4j Browser:
```cypher
CALL db.schema.visualization
```
This command will provide a summary of the database schema. When you execute it, you’ll see two node types—**Movies** (in orange) and **Persons** (in blue)—and six types of relationships:

- **ACTED_IN**
- **REVIEWED**
- **PRODUCED**
- **WROTE**
- **DIRECTED**
- **FOLLOWS** (connecting Persons to other Persons)

#### Exploring Node Properties

Clicking on the **Person** node will reveal its properties, such as:
- **ID**: A unique identifier (e.g., -2).
- **Name**: The label "Person."
- **Constraints** and **Indexes**: Currently none are defined.

Next, clicking on the **Movie** node displays similar properties:
- **ID**: (e.g., -1).
- **Name**: The label "Movie."

#### Understanding Relationship Types

The relationships between persons and movies include:
- **DIRECTED** (ID: -2)
- **WROTE** (ID: -4)
- **PRODUCED** (ID: -3)
- **REVIEWED** (ID: -6)
- **ACTED_IN** (ID: -1)

The **FOLLOWS** relationship (ID: -5) connects persons to each other. Notably, all relationships in Neo4j are directed by default, but you can query them without regard to direction in your Cypher queries.

#### Executing Find Operations

Now, let’s navigate to the **find operations** section of the guide. We’ll run a query to retrieve the node corresponding to the actor **Tom Hanks**.

The query structure will look like this:
```cypher
MATCH (tom:Person {name: "Tom Hanks"})
RETURN tom
```
In this query:
- `MATCH` finds the node with the label `Person` where the `name` property is "Tom Hanks."
- `RETURN` projects the matching nodes.

When you run this query, you’ll see a single node representing Tom Hanks. From the right panel, you can see his properties, including his **ID** and **birth year**.

#### Analyzing Tom Hanks's Relationships

By clicking on the Tom Hanks node, you can visualize his relationships with various movies. You’ll notice that he primarily has **ACTED_IN** relationships, along with a directorial role in **That Thing You Do**.

To expand your view, you can select a movie, like **The Green Mile**, to see its connections with other nodes. For example, you might see:
- **Frank Darabont** as the director.
- Other actors involved, such as **Patricia Clarkson** and **Sam Rockwell**.

#### Visual Interaction

Neo4j’s interface allows you to drag nodes for better visibility. If a view becomes cluttered, you can hide specific nodes, simplifying your focus. For example, hiding the node for **Bonnie Hunt** can help declutter the graph.

#### Modifying Variable Names in Queries

You can also modify the variable name in your MATCH query. For instance, changing `tom` to `tomhanks` in the following query:
```cypher
MATCH (tomhanks:Person {name: "Tom Hanks"})
RETURN tomhanks
```
Running this will yield the same result, demonstrating that variable names can be customized as long as they match in both the MATCH and RETURN clauses.

#### Exporting Query Results

If you want to save your results, you can use the **Exports** menu to export your data in various formats like CSV, JSON, PNG, or SVG.

### Exploring Relationships in the Movie Graph with Neo4j

In our previous video, we examined how to query nodes based on exact property matches, specifically focusing on the actor **Tom Hanks**. We also learned that variable names in Cypher can be anything, as long as they are consistent throughout the query.

#### Searching for Tom Hanks and His Movies

Now, let’s build on that by querying to find all the movies Tom Hanks has acted in. The query looks like this:

```cypher
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies)
RETURN tom, tomHanksMovies
```

In this query:
- We use `MATCH` to find a `Person` node labeled **Tom Hanks**.
- The `ACTED_IN` relationship links this node to any movie node, represented by the variable `tomHanksMovies`.

When we run this, we see both the Tom Hanks node and the associated movies he has acted in. This highlights how relationships enrich the data we retrieve.

#### Modifying the Relationship Type

Now, if we want to see only the movies that Tom Hanks has directed, we can adjust our query:

```cypher
MATCH (tom:Person {name: "Tom Hanks"})-[:DIRECTED]->(tomHanksMovies)
RETURN tom, tomHanksMovies
```

When executed, this returns just the Tom Hanks node and the movie **That Thing You Do**, confirming that he directed this film.

#### Default Relationships Display

It's worth noting that Neo4j automatically displays the relationships between matched nodes in the results, which reinforces the importance of connections in graph databases.

#### Utilizing the shortestPath Function

Next, we’ll explore a more complex query using the `shortestPath` function, which helps find connections between two nodes. Specifically, we’ll look for the shortest path between actors **Kevin Bacon** and **Meg Ryan**.

The query structure will look like this:

```cypher
MATCH p = shortestPath((bacon:Person {name: "Kevin Bacon"})-[*]-(meg:Person {name: "Meg Ryan"}))
RETURN p
```

In this query:
- We define the pattern for **Kevin Bacon** and **Meg Ryan**, using the `Person` label.
- The `[*]` denotes any kind of relationship between these two nodes, allowing for indirect connections.

When executed, this query reveals the shortest path in terms of movies and actors connecting Kevin Bacon and Meg Ryan. 

For example, you might find that:
- Kevin Bacon acted in **Apollo 13**, which also starred **Tom Hanks**.
- Tom Hanks and Meg Ryan featured together in **Sleepless in Seattle**.

#### Confirming Connections

If we try a direct query between Kevin Bacon and Tom Hanks, we can verify that they acted together in the same movie, resulting in a simpler graph output.

### Connecting to a Remote Database with Neo4j Desktop

In our journey through Cypher queries, we will now explore how to connect to a remote Neo4j database using Neo4j Desktop. Before we proceed, let’s clean up our current database.

#### Cleaning Up the Local Database

To clear out all nodes and relationships in our local database, we can run the following command:

```cypher
MATCH (n) DETACH DELETE n
```

Executing this will notify us of the number of nodes and relationships cleared. To confirm that our database is empty, we can run:

```cypher
MATCH (n) RETURN n
```

This should return no results, indicating that we have successfully reset the database.

#### Connecting to a Remote Database

Next, we’ll connect to a remote database hosted by Neo4j. We'll navigate to a specific URL where several example databases are set up for us to explore. You can find this at [neo4j.com/developer/example-data](https://neo4j.com/developer/example-data/#_hosted_databases). 

From the available databases, we’ll choose the **Recommendations** database, which contains information about movies and their genres.

#### Connection Details

On the Recommendations database page, we’ll find the following connection details:
- **Connection URL:** `neo4j+s://demo.neo4jlabs.com`
- **Username:** `recommendations`
- **Password:** `recommendations`

#### Using Neo4j Browser

1. **Disconnect from the Local Database:** In the Neo4j Browser, we first disconnect from the local database using the command:
   ```plaintext
   :server disconnect
   ```

2. **Connecting to the Remote Database:**
   - Set the protocol to `neo4j+s`.
   - Enter the connection URL: `demo.neo4jlabs.com`.
   - For authentication, input the username and password as `recommendations`.
   - Click on **Connect**.

Once connected, you should see a confirmation message indicating that you are now connected to the remote database.

#### Exploring the Remote Database

To view the available databases, we can run:

```cypher
:dbs
```

This will show the **Recommendations** database and the system database. To switch to the Recommendations database, simply run:

```cypher
:use recommendations
```

#### Querying the Database

To explore the contents of the Recommendations database, we can run:

```cypher
MATCH (n) RETURN n LIMIT 30
```

This command will return 30 nodes from the database. The results will include various nodes, with orange nodes representing Movies and red nodes representing Genres. 

#### Visualizing the Schema

Next, we can visualize the schema of the database by running:

```cypher
CALL db.schema.visualization
```

This will display the different node types (e.g., Movie, User, Actor, Director, Genre, Person) and the relationships between them (e.g., ACTED_IN, RATED, IN_GENRE, DIRECTED).

#### Configuring Node and Relationship Appearance

In the Neo4j Browser, you can customize how nodes and relationships appear:
- Change the color of relationships (e.g., red for ACTED_IN, green for RATED).
- Adjust the size and color of nodes.

These customizations help in visualizing data in a more meaningful way.

#### Summary

Now you know how to connect to a remote Neo4j database using Neo4j Desktop, explore its contents, and visualize its schema. In the next video, we’ll look at the help command to assist us in running queries and navigating features in Neo4j Desktop and Browser.

### Using the Help Features in Neo4j Browser

Now that we’ve covered how to use the Neo4j Browser for querying both local and remote databases, let’s take a moment to explore the help features available. This can be useful for finding assistance on various topics related to Neo4j.

#### Accessing the Help Menu

To view the help menu, simply run the command:

```plaintext
:help
```

This will display the entire help menu, which includes different topics you can explore. Here are some useful commands:

- **Cypher Help:** To get assistance with Cypher queries, run:
  ```plaintext
  :help cypher
  ```
- **Commands Help:** For additional details on available commands, use:
  ```plaintext
  :help commands
  ```
- **Keys Help:** To see keyboard shortcuts, run:
  ```plaintext
  :help keys
  ```

#### Exploring Guides and Examples

The help menu also includes various guides and examples:

- **Guides:** You can access conceptual guides using commands like:
  - `:play concepts`
  - `:play cypher`
  - `:play iconography`
- **Graph Examples:** Explore specific example databases, such as:
  - `:play movie graph`
  - `:play northwind graph`

These commands help you understand Neo4j better and get hands-on experience with specific datasets.

#### Running Help Commands

To run any of these commands, you can click on them directly from the help menu. For instance, clicking on `:help keys` will display the keyboard shortcuts for both Windows and Mac users.

#### Learning About Specific Cypher Commands

If you want detailed information about specific Cypher commands, you can run:

```plaintext
:help CREATE
```

This command will provide you with a description of the `CREATE` clause, including usage examples. You can do the same for other commands like `MATCH`:

```plaintext
:help MATCH
```

#### Cleaning Up the Neo4j Database

Now, as we prepare for our next demo, let’s clean up the contents of the Neo4j Database by deleting our project.

1. **Navigate to Neo4j Desktop:** Switch from the Neo4j Browser to the Neo4j Desktop application.
2. **Access Projects:** Click on the **Projects** menu item to view your existing projects.
3. **Delete the Example Project:** Find the Example Project entry and click on the delete (bin) icon next to it. 
4. **Confirm Deletion:** A prompt will appear asking you to confirm the deletion. Once you confirm, the project will be removed.

After deletion, if you have no other projects, you will see an option to create a new project.