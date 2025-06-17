---
date: 1970-01-01
---

# Graph Analytics Lab

Graph Analytics
3 Hr 24 Min Remaining
Exercise 1 - Network Analysis with networkx
Introduction
Welcome to the Network Analysis with networkx exercise.

Tasks
You can use Pycharm or Anaconda for this exercise. The data file is loaded in the Lab01 folder in Pycharm and can be accessed through the Lab Data folder on the desktop for Anaconda

Load the data.
The output format is a graph.

Create a new graph that users the word itself to create the node and lists the index number as the node attribute.

Identify the word or words that have the most listed synonyms and antonyms. [[2 words: indication and information]]

Identify the word or words that have the highest eigenvector centrality [[deception]]

Find all shortest paths from the word “laughing-stock” to the word “evil doer”.

Explain why there is no shortest path from the word “satan” to the word “hope”. This task has no output, but will be referenced later in the final question.

Instructions
Task 1 - Load the data
Execute the given code in python
import networkx 
import gzip 
import re 
import sys 



import matplotlib.pyplot as plt 
import networkx as nx 





def roget_graph(): 
    """Return the thesaurus graph from the roget.dat example in 
    the Stanford Graph Base. 
    """ 

    # open file roget_dat.txt.gz 
    fh = gzip.open("c:/users/aaron/desktop/roget_dat.txt.gz", "r") 
    G = nx.DiGraph() 


    for line in fh.readlines(): 
        line = line.decode() 
        if line.startswith("*"):  # skip comments 
            continue 
        if line.startswith(" "):  # this is a continuation line, append 
            line = oldline + line 
        if line.endswith("\\\n"):  # continuation line, buffer, goto next 
            oldline = line.strip("\\\n") 
            continue 

        (headname, tails) = line.split(":") 


        # head 
        numfind = re.compile(r"^\d+")  # re to find the number of this word 
        head = numfind.findall(headname)[0]  # get the number 
        word = headname.replace(head,"") # get the word 
        G.add_node(head, word = word) 


        for tail in tails.split(): 
            if head == tail: 
                print("skipping self loop", head, tail, file=sys.stderr) 
            else: 
                G.add_edge(head, tail) 
    return G 


G = roget_graph() 
print("Loaded roget_dat.txt containing 1022 categories.") 
print(G) 
UG = G.to_undirected() 
print(nx.number_connected_components(UG), "connected components") 



options = { 
    "node_color": "black", 
    "node_size": 1, 
    "edge_color": "gray", 
    "linewidths": 0, 
    "width": 0.1, 
} 

nx.draw_circular(UG, **options) 
plt.show() 
Task 2 - Create a new graph that users the word itself to create the node and lists the index number as the node attribute
The graph G uses an index number to create the nodes, and stores the actual word as a node attribute. This is less than ideal for most uses.

Create a new graph
G_words = nx.DiGraph()

Copy the nodes to the new graph in the appropriate format
for n in G: 
    word = nx.get_node_attributes(G,"word")[n] 
    G_words.add_node(word,index=n) 
Copy the nodes to the new graph in the appropriate format
for n in G: 
    for edge in G[n]: 
        node_word = nx.get_node_attributes(G,"word")[n] 
        edge_word = nx.get_node_attributes(G,"word")[edge] 
        G_words.add_edge(node_word,edge_word) 
Task 3 - Identify the word or words that have the most listed synonyms and antonyms
Create a dictionary of the degree of each node
degree = {} 
for n in G_words: 
    degree[n] = G_words.degree[n] 
Observe the top 10 highest degree nodes
top10 = sorted(degree, key=degree.get, reverse=True)[:10] 
for word in top10: 
    print(word,G_words.degree[word]) 
Indication and Information both have 39, which is the highest.
Task 4 - Identify the word or words that have the highest eigenvector centrality [[deception]]
Create a dictionary of the degree of each node
centrality = nx.eigenvector_centrality(G_words)

Observe the top 10 highest centrality nodes
top10 = sorted(centrality, key=centrality.get, reverse=True)[:10] 
for word in top10: 
    print(word,centrality[word]) 
Deception has the highest centrality at ~0.18
Task 5 - ind all shortest paths from the word “laughing-stock” to the word “evil doer”
Apply the shortest paths algorithms to the two nodes.
for p in nx.all_shortest_paths(G_words,'laughing-stock','evil doer'): 
    print(" --> ".join(p)) 
The output should be as follows:
laughing-stock --> dupe --> credulity --> incredulity --> bad man --> evil doer
laughing-stock --> wit --> amusement --> pleasurableness --> painfulness --> evil doer
laughing-stock --> wit --> dulness --> dejection --> painfulness --> evil doer
laughing-stock --> wit --> ridiculousness --> ugliness --> painfulness --> evil doer
Task 6 - Explain why there is no shortest path from the word “satan” to the word “hope”
The word “satan” is in a graph component with only the other words ‘angel’, ‘demon’, and ‘jupiter’. No other words will have a shortest path to ‘satan’.
Check your work
Check each box to confirm completion of the task.

Use the code snippet to load the data.
Create a new graph that users the word itself to create the node and lists the index number as the node attribute.
Identify the word or words that have the most listed synonyms and antonyms.
Identify the word or words that have the highest eigenvector centrality.
Find all shortest paths from the word “laughing-stock” to the word “evil doer”.
Explain why there is no shortest path from the word “satan” to the word “hope”.
Question
Why was there no shortest path, using synonyms and antonyms, from the word ‘satan’ to the word ‘hope’?

They were on different connected components.
The word ‘satan’ had no synonyms or antonyms listed in the data.
The index for ‘hope’ was an integer instead of a string.
The word ‘satan’ needed to be capitalized to ‘Satan’.
Correct!

Select Next below to move to the next exercise.

---

Graph Analytics
3 Hr 24 Min Remaining
Exercise 2 - Cypher MATCH
Introduction
Welcome to the Cypher MATCH exercise.

Tasks
Start Movies DMBS
Load Movies data into database
Use the Cypher command “MATCH (n) RETURN n” to view all nodes
Try several of the features of the Neo4j Browser
Explore movie producers
Explore movies with multiple producers
Fill in the blanks of the incomplete Cypher query to visualize the graph
Craft a Cypher query to return the “name” attribute of all People who both ACTED_IN at least one Movie and DIRECTED at least one Movie
Instructions
Task 1 - Start Movies DMBS
Launch the Neo4j Desktop application.

Navigate to the Projects tab (the top tab on the left). Click “Example Project.”

First, check if the Movies DMBS has launched automatically:

If it has launched automatically, the words “Active DMBS” will appear above “Movies DMBS.”

If it has not launched automatically, the “Start” button will appear to the right.

Click the “Start” button if the Movies DMBS has not automatically launched.
Task 2 - Load Movies data into database
In the Projects tab, hover over the file “load-movies.cypher” and click “Open.” A new window will launch.

In the new window, the top of the contents of the “load-movies.cypher” file will display. To the right will be a blue arrow. Click the blue arrow to execute the file.

Be sure to click Run only once.

Task 3 - Use the Cypher command “MATCH (n) RETURN n” to view all nodes
At the Neo4j command prompt, type “MATCH (n) RETURN n”

Click the blue arrow to execute the command.

Task 4 - Try several of the features of the Neo4j Browser
Zoom In and Zoom Out on the graph using the magnifying glass icons or using the scroll wheel.

Left click and drag in the graph window to move the graph.

Observe the number of nodes of type Movie and Person in the Overview window. The overview window is at the right hand side of the screen, and may be collapsed. If it is collapsed, click the left arrow at the top right of the Graph tab to expand it. There are 139 Person nodes and 40 Movie nodes.

Observe the number of edges of type PRODUCED in the Overview window. There are 14 PRODUCED edges.

Find and click the “Text” tab on the left side of the screen under the Neo4j prompt.

Find and click the “Graph” tab on the left side of the screen under the Neo4j prompt.

Task 5 - Explore movie producers
Enter “MATCH (p)-[:PRODUCED]->(m) RETURN p” at the Neo4j prompt and click the blue arrow to execute.

Find and click the “Text” tab on the left side of the screen under the Neo4j prompt. Notice that there are duplicates of many nodes.

At a new Neo4j prompt, enter “MATCH (p)-[:PRODUCED]->(m) RETURN DISTINCT p” and click the blue arrow to execute.

Find and click the “Text” tab on the left side of the screen under the Neo4j prompt. There will not be any duplicates.

Task 6 - Explore movies with multiple producers
Enter “MATCH (p1)-[:PRODUCED]->(m)<-[:PRODUCED]-(p2) RETURN p1, p2, m” at the Neo4j prompt and click the blue arrow to execute.

At a new Neo4j prompt, enter “MATCH (p1)-[:PRODUCED]->(m)<-[:PRODUCED]-(p2) RETURN DISTINCT p1.name” and click the blue arrow to execute.

At a new Neo4j prompt, enter “MATCH (p1)-[:PRODUCED]->(m)<-[:PRODUCED]-(p2) RETURN DISTINCT m.title” and click the blue arrow to execute.

Task 7 - Fill in the blanks of the incomplete Cypher query to visualize the graph
Determine the appropriate pattern for the Cypher query based on the incomplete command “MATCH ()-[:PRODUCED]->(:Movie)<-[:WROTE]-() RETURN , _”. The key here is that the 1st and 3rd nodes must have the same label. Any Neo4j-acceptable valuables a and b fitting the pattern “MATCH (a)-[:PRODUCED]->(b:Movie)<-[:WROTE]-(a) RETURN a, b” would work. (Since a and b are acceptable variables, this Cypher command will work.)

At a new Neo4j prompt, enter the chosen command, for example: “MATCH (a)-[:PRODUCED]->(b:Movie)<-[:WROTE]-(a) RETURN a, b”. It will return the following graph: graph.PNG

Task 8 - Craft a Cypher query to return the “name” attribute of all People who both ACTED_IN at least one Movie and DIRECTED at least one Movie
Determine the appropriate pattern for the Cypher query. There are several possibilities, but a query similar to the solution of the previous task would be:
“MATCH ()<-[:ACTED_IN]-(p)-[:DIRECTED]->() RETURN DISTINCT p.name”

In this instance, it is not necessary to name the Movie nodes, since they will not be returned. A query with more error checking might be: “MATCH (:Movie)<-[:ACTED_IN]-(p:Person)-[:DIRECTED]->(:Movie) RETURN DISTINCT p.name”

At a new Neo4j prompt, enter the chosen command. It will return a table with the following 5 people: "Tom Hanks", "Werner Herzog", "Clint Eastwood", "James Marshall", "Danny DeVito"
Check your work
Check each box to confirm completion of the task.

Start Movies DMBS
Load Movies data into database
Use the Cypher command “MATCH (n) RETURN n” to view all nodes
Try several of the features of the Neo4j Browser
Explore movie producers
Explore movies with multiple producers
Fill in the blanks of the incomplete Cypher query to visualize the graph
Craft a Cypher query to return the “name” attribute of all People who both ACTED_IN at least one Movie and DIRECTED at least one Movie
Question
The Cypher query “MATCH (person:Person)<-[:PRODUCED]-(movie) RETURN DISTINCT person.name” would not identify all producers of movies.


What is wrong with it?

The type of relationship, “PRODUCED”, is specified, but not assigned a name.
The node “movie” is named, but does not filter to only nodes of type “Movie.”
The direction of the relationship is backwards.
The variables “person” and “movie” are too long. Variables can only be 1 or 2 letters.
Select Next below to move to the next exercise.

---

Graph Analytics
3 Hr 23 Min Remaining
Exercise 3 - Conceptualizing Graph Data
Introduction
Welcome to the Conceptualizing Graph Data exercise.

This exercise will consider two graph models:

Nodes of type OriginAirport and DestinationAirport connected by directed ROUTE relationships.
Nodes of type Airport connect by ROUTE relationships. While the former is close to how the data is modelled in the original csv file, the latter will prove to be more versatile
Tasks
Open Neo4j Browser and create a new project, including starting the DMBS
Load the data into Neo4j
Explore the strengths and limitations of this first graph model
Delete the previous data and replace it with the second graph model
Explore the strengths and limitations of this second graph model
Instructions
Task 1 - Open Neo4j Browser and create a new project, including starting the DMBS
Launch the Neo4j Desktop application.

Navigate to the Projects tab (the top tab on the left). Click “+ New” followed by “Create Project”.

Check if there is a running DMBS, and click “Stop” at the top if there is. Add a DMBS to the new project by clicking “+ Add” followed by “Local DMBS”.

Navigate to the Projects tab (the top tab on the left). Click “+ New” followed by “Create Project”. Set a password and click Create.

Hover over the new DMBS and click “Start” to launch the new DMBS.

Click “-> Open” to launch the Neo4j Browser.

Task 2 - Load the data into Neo4j
Use the following code snippet to load data into Neo4j. Enter the following code in the Neo4j console and click the blue arrow.

LOAD CSV FROM 'file:///data.csv' AS row 
WITH row[0] AS Origin_airport, row[2] AS Origin_city, row[1] AS Destination_airport, row[3] AS Destination_city, toInteger(row[6]) as Flight_count 
MERGE (o:OriginAirport {Airport: Origin_airport}) 
  SET  o.CityName = Origin_city 
MERGE (d:DestinationAirport {Airport: Destination_airport}) 
  SET d.CityName = Destination_city 
MERGE (o)-[r:ROUTE]->(d) 
  SET r.Flights = Flight_count 
RETURN count(o); 
Task 3 - Explore the strengths and limitations of this first graph model
Use “MATCH (a {Airport:"SEA"}) RETURN a” to see the number of Seattle nodes.

Enter the following at the console: “MATCH (a {Airport:"SEA"}) RETURN a”

Craft a Cypher query to find the number of routes that originated in Seattle in January 2000.

There is an acceptable query: “MATCH (a {Airport:"SEA"})-[:ROUTE]->() RETURN count(a)”. The result is 67.

Use “MATCH (a {Airport:"SEA"})-[r]->(d) WHERE r.Flights > 100 return count(r)” to find all the routes with over 100 flights in January 2000.

Enter the following at the console: “MATCH (a {Airport:"SEA"})-[r]->(d) WHERE r.Flights > 100 return count(r)”. The result is 12.

The Seattle airport wants to run a customer satisfaction survey for their most important routes (with over 100 monthly flights). To find a comparison group, they would like to find the airports that also have important routes (with over 100 monthly flights) leading to the same destination cities. Find the names of the cities with airports that ran 100+ flights in January 2000 to the result of the previous query by modifying this Cypher query: MATCH (seattle {Airport:"SEA"})-[]->()<-[]-(:OriginAirport) WHERE .Flights > 100 and .Flights > 100 RETURN DISTINCT _

Here is an acceptable query: “MATCH (seattle {Airport:"SEA"})-[r1]->(d)<-[r2]-(other:OriginAirport) WHERE r1.Flights > 100 and r2.Flights > 100 RETURN DISTINCT other.CityName”. The correct result is a list of 31 city names.

Consider why this graph model makes it challenging to identify the airports that had flights that arrived from JFK and departed to LAX. The final question will be related to this question.

This task has no output. The problem highlighted is that the middle airport is considered a destination in the first part, but an origin in the second part. Solving problems like this would be easier if origin and destination nodes were combined.

Modify this Cypher query to identify the top 5 destination airports that received the most combined flights from JFK and LAX. MATCH (_ {Airport:"JFK"})-[]->()<-[]-( {Airport:"LAX"}) RETURN .Airport, .Flights + _.Flights AS total ORDER BY total DESC

Here is an acceptable query: “MATCH (jfk {Airport:"JFK"})-[r1]->(middle)<-[r2]-( lax {Airport:"LAX"}) RETURN middle.Airport, r1.Flights + r2.Flights AS total ORDER BY total DESC”

Task 4 - delete the previous data and replace it with the second graph model
Enter the following code in the Neo4j console and click the blue arrow.

MATCH (n) DETACH DELETE n; 
LOAD CSV FROM 'file:///data.csv' AS row 
WITH row[0] AS Origin_airport, row[2] AS Origin_city, row[1] AS Destination_airport, row[3] AS Destination_city, toInteger(row[6]) as Flight_count 
MERGE (o:Airport {Symbol: Origin_airport}) 
  SET  o.CityName = Origin_city 
MERGE (d:Airport {Symbol: Destination_airport}) 
  SET d.CityName = Destination_city 
MERGE (o)-[r:ROUTE]->(d) 
  SET r.Flights = Flight_count 
RETURN count(o); 
Task 5 - Explore the strengths and limitations of this second graph model
Use “MATCH (a {Symbol:"SEA"}) RETURN a” to see the number of Seattle nodes.

Enter the following at the console: “MATCH (a {Symbol:"SEA"}) RETURN a”

Craft a Cypher query to find the number of routes that originated in Seattle in January 2000.

Here is an acceptable query: “MATCH (a {Symbol:"SEA"})-[:ROUTE]->() RETURN count(a)”. The result is 67.

Craft a Cypher query to find the number of airports that had both 100+ flights to Seattle and 100+ flights from Seattle

Here is an acceptable query: “MATCH (b)-[r1:ROUTE]->(a {Symbol:"SEA"})-[r2:ROUTE]->(b) WHERE r1.Flights>100 and r2.Flights>100 RETURN count(DISTINCT b)”. The result is 8.

Use “Match (a {Symbol:"SEA"})-[r]->(d) where r.Flights > 100 return count(r)” to find all the routes with over 100 flights in January 2000. [[12]]

Enter the following at the console: “MATCH (a {Symbol:"SEA"})-[r]->(d) WHERE r.Flights > 100 RETURN count(r)”. The result is 12.

Craft a Cypher query to find airports that have 100+ flights that arrived in Seattle and 100+ flights that departed from Seattle.

Here is an acceptable query: “MATCH (b)-[r1]->(a:Airport {Symbol:"SEA"})-[r2]->(b) WHERE r1.Flights>100 AND r2.Flights>100 RETURN DISTINCT b.Symbol”. The results is 8.

Craft a Cypher query to identify the airports that had the largest sum of flights that arrived from JFK and departed to LAX. (This is the question that would have been very hard with the first graph model.)

Here is an acceptable query: “MATCH (jfk {Symbol:"JFK"})-[r1]->(middle)-[r2]->( lax {Symbol:"LAX"}) RETURN middle.Symbol, r1.Flights + r2.Flights AS total ORDER BY total DESC”. The result is 37 airports.

Check your work
Check each box to confirm completion of the task.

Open Neo4j Browser and create a new project, including starting the DMBS
Load the data into Neo4j
Explore the strengths and limitations of this first graph model
Delete the previous data and replace it with the second graph model
Explore the strengths and limitations of this second graph model
Question
The first graph model had nodes for Destination airports and Origin airports connected by ROUTE relationships. This model made it a challenge to find airports that received flights from JFK and sent flights to LAX.


Why was it so hard to answer this question with the first graph model?

This question considers a single airport as both a Destination and an Origin. This was not possible with the model because those were two different nodes.
This question asks about flights arriving at a specific airport. This was not possible with the model because it only models flights leaving an airport.
This question required filtering data by relationship attributes. This was not possible with this model because it only contains ROUTE relationships.
This question required there to be flights going to LAX. This was not possible with the model because there were none.
Select Next below to move to the next exercise.

---

Graph Analytics
3 Hr 23 Min Remaining
Exercise 4 - Reimagining Relational Databases in Neo4j
Introduction
Welcome to the Reimagining Relational Databases in Neo4j exercise.

Tasks
Explore the structure of the data
Identify how many SQL JOINS are required
Develop a Cypher query
Instructions
Task 1 - Explore the structure of the data
In this task, you will explore the structure of the data with prescribed queries.

Use the command “MATCH (s:Supplier)-->(p:Product)-->(c:Category) RETURN s, p, c” to observe the relationships between Suppliers, Products and Categories. Select a distinct color for each type of node in the UI.

Execute the query “MATCH (s:Supplier)-->(p:Product)-->(c:Category) RETURN s, p, c”

In the overview tab at right, click the node labels and select a unique color for each.

Use the command “MATCH (cust:Customer {customerID:"ALFKI"})-->(o:Order)-->(p:Product) RETURN cust, o, p” to observe the relationships between Customers, Orders and Products for one customer. Select a distinct color for each type of node in the UI.

Execute the query “MATCH (cust:Customer {customerID:"ALFKI"})-->(o:Order)-->(p:Product) RETURN cust, o, p”

In the overview tab at right, click the node labels and select a unique color for each.

Task 2 - Identify how many SQL JOINS are required
Each type of node was originally modelled as a table in a relational database. How many SQL JOINs would have been required for each of the above query? This question has no output, but will be referred to in the final question.
Task 3 - Develop a Cypher query
In this task, you will develop a Cypher query to respond to each of the following problems posed by this scenario: Canadian shipping has been suffering from a shortage of truckers.

Based on their order history, how many customers might be impacted due to a reliance on Canadian suppliers?

Here is an acceptable query: “MATCH (s:Supplier {country:"Canada"})-->(:Product)<-[*]-(cust:Customer) RETURN distinct cust“ . The result is 60

How many customer orders had two or more Canadian products from the same supplier?

Here is an acceptable query: “MATCH (o:Order)-->(p1:Product)<--(s1:Supplier {country:"Canada"})-->(p2:Product)<--(o:Order) RETURN distinct o, p1, p2” . The result is 1

How many customer orders had two or more Canadian products?

Here is an acceptable query: “MATCH (o:Order)-->(p1:Product)<--(s1:Supplier {country:"Canada"}),(s2:Supplier {country:"Canada"})-->(p2:Product)<--(o:Order) RETURN distinct o, p1, p2” . The result is 8

Which product category has the largest number of impacted products?

Here is an acceptable query: “MATCH (s:Supplier {country:"Canada"})-->(p:Product)-->(cat:Category) RETURN count(distinct p), cat.categoryName” . The result is “Meat/Poultry

Check your work
Check each box to confirm completion of the task.

Explore the structure of the data
Identify how many SQL JOINS are required
Develop a Cypher query
Question
How many SQL JOINs would it take to replicate the Cypher query “match (s:Supplier)-->(p:Product)-->(c:Category) return s, p, c” in a relational database?

2
4
1
3
Select Next below to move to the next exercise.

---

Graph Analytics
3 Hr 23 Min Remaining
Exercise 5 - Complex Searches in a Neo4j Database
Introduction
Welcome to the Complex Searches in a Neo4j Database exercise.

Tasks
Explore the graph model
Develop Cypher queries to address specific challenges
Instructions
Task 1 - Explore the graph model
Use “MATCH (n) RETURN n” to view all nodes.

Execute the query “MATCH (n) RETURN n”.

Assign the different node types to different colors.

In the overview tab at right, click the node labels and select a unique color for each.

Use “MATCH (n) WHERE (n:Recipe OR n:Instruction) RETURN n” to get a better overview of the data.

Execute the query “MATCH (n) WHERE (n:Recipe OR n:Instruction) RETURN n”.

Use “MATCH (n:Recipe {name:"Philly Cheesesteak"})-[*]->(b) RETURN b” to view the entire Philly Cheesestake recipe as a graph.

Execute the query “MATCH (n:Recipe {name:"Philly Cheesesteak"})-[*]->(b) RETURN b”.

Write a Cypher query to list the name of each ingredient required for the Philly Cheesestake recipe.

Here is an acceptable query “MATCH (n:Recipe {name:"Philly Cheesesteak"})-[*]->(b:Ingredient) RETURN b.name”.

Modify the following Cypher query to list the name of each technique required to create the Philly Cheesesteak recipe: MATCH (n:Recipe {name:"Philly Cheesestake"})-___________ RETURN DISTINCT type(_) [[[MATCH (n:Recipe {name:"Philly Cheesestake"})-[*]->(ins:Instruction)-[r]->(b:Ingredient) RETURN distinct type(r)]]]

Here is an acceptable query: “MATCH (n:Recipe {name:"Philly Cheesestake"})-[*]->(ins:Instruction)-[r]->(b:Ingredient) RETURN distinct type(r)”

How many recipes have Sea salt in them?

Here is an acceptable query: ”MATCH (n:Recipe)-[*]->(:Ingredient {name:”Sea Salt”}) RETURN DISTINCT n.name”

Task 2 - Develop Cypher queries to address specific challenges
Generate a table of all recipes and instructions requiring knifework. “MATCH (recipe:Recipe)-[*]->(instruction:Instruction)-[:KNIFEWORK]->(ingredient:Ingredient) RETURN DISTINCT recipe.name,ingredient.name,instruction.action”

Here is an acceptable query “MATCH (recipe:Recipe)-[*]->(instruction:Instruction)-[:KNIFEWORK]->(ingredient:Ingredient) RETURN DISTINCT recipe.name, ingredient.name, instruction.action”

You have leftovers of your “The Best Beef and Broccoli Sauce.” List all ingredients you still need for your “Beef and Broccoli” recipe. [[MATCH (recipe {name:"Beef and Broccoli"})-[:STARTS_WITH|PROCEEDS_TO*]->(instruction:Instruction)-->(c:Ingredient) RETURN distinct c.name]]

Here is an acceptable query: “MATCH (recipe {name:"Beef and Broccoli"})-[:STARTS_WITH|PROCEEDS_TO*]->(instruction:Instruction)-->(c:Ingredient) RETURN distinct c.name”

For each recipe, list the name of each ingredient that has both knifework and heat applied to it at some point. [[MATCH (r:Recipe)-[*]->(:Instruction)-->(ing:Ingredient) WHERE EXISTS {(:Instruction)-[:KNIFEWORK]->(ing:Ingredient)} AND EXISTS {(:Instruction)-[:HEAT]->(ing:Ingredient)} return distinct r.name, ing.name]]

Here is an acceptable query: “MATCH (r:Recipe)-[*]->(:Instruction)-->(ing:Ingredient) WHERE EXISTS {(:Instruction)-[:KNIFEWORK]->(ing:Ingredient)} AND EXISTS {(:Instruction)-[:HEAT]->(ing:Ingredient)} return distinct r.name, ing.name”

For each recipe in the dataset, list the name of the recipe and the instructions that call for “Sweet onions”. If a recipe does not use “Sweet onions”, return the name of the recipe and “null” as the action. [[MATCH (n:Recipe) OPTIONAL MATCH (n)-[*]->(b:Instruction)-->(:Ingredient {name:"Sweet onion"}) RETURN DISTINCT n.name,b.action]]

Here is an acceptable query: “MATCH (n:Recipe) OPTIONAL MATCH (n)-[*]->(b:Instruction)-->(:Ingredient {name:"Sweet onion"}) RETURN DISTINCT n.name, b.action”

Check your work
Check each box to confirm completion of the task.

Explore the graph model
Develop Cypher queries to address specific challenges
Question
The current recipe data does not include any information about the amount of an ingredient. Which of the following options would be the best alternative for adding the ingredient amount?

A new node could be created for each amount, and new edges could connect the recipe, the ingredient, and the amount.
It could be added as an edge attribute the first time an ingredient is used.
It could be added as a node attribute for the ingredient.
A new edge type could be created for each amount, and new edges could be created to connect the recipe to each ingredient.
Select Next below to move to the next exercise.

---

Graph Analytics
3 Hr 23 Min Remaining
Exercise 6 - Problem Solving Within a Neo4j Database
Introduction
Welcome to the Problem solving within a Neo4j Database exercise (data.csv).

Tasks
Load the data into Neo4j
Write a Cypher query to address questions
Instructions
Task 1 - Load data into Neo4j
Enter the following code in the Neo4j console and click the blue arrow.
LOAD CSV FROM 'file:///data.csv' AS row 
WITH row[0] AS Origin_airport, row[2] AS Origin_city, row[1] AS Destination_airport, row[3] AS Destination_city, toInteger(row[4]) as Passengers_count, toInteger(row[5]) as Seats_count, toInteger(row[6]) as Flight_count, toInteger(row[7]) as Distance  
MERGE (o:Airport {Symbol: Origin_airport}) 
  SET  o.CityName = Origin_city 
MERGE (d:Airport {Symbol: Destination_airport}) 
  SET  d.CityName = Destination_city 
MERGE (o)-[r:ROUTE]->(d) 
  SET r.Passengers = Passengers_count 
  SET r.Seats = Seats_count 
  SET r.Flights = Flight_count 
  SET r.Distance = Distance 
RETURN count(o); 
Task 2 - Write a Cypher query to address questions
In this task you will write a Cypher query to address several challenges:

A passenger surplus (or deficit) is defined as the difference between passengers arriving and departing from an airport during a month. When more passengers arrive than depart, that is considered a passenger surplus. Which airport has the largest passenger surplus and which airport has the largest deficit?

An acceptable query is:

“OPTIONAL MATCH (other:Airport)-[arriving]->(center:Airport)-[departing]->(other:Airport) RETURN center.Symbol, sum(arriving.Passengers) - sum(departing.Passengers) as surplus ORDER BY surplus DESC” (And replace DESC with ASC for deficit)

You’d like to choose a layover stop between PDX and MIA, but don’t want to get stuck if there’s poor weather. Which intermediate airport, on average, runs the emptiest flights to MIA?

An acceptable query is:

“MATCH (n {Symbol:"PDX"})-->(n2)-[r]->(n3 {Symbol:"MIA"}) WHERE r.Seats > 0 RETURN DISTINCT n2.Symbol, sum(r.Passengers) , sum(r.Seats), 100 * sum(r.Passengers) / sum(r.Seats)” .

The answer is SCJ.

* You’re responsible for holding a training for front desk staff on how to work in small airports. You will have one attendee from ATL, ORD, DFW, LAX, PHX and LAS. Which airports that serve fewer than 3000 departing flights can be reached directly from all 6 airports?

An acceptable query is:

“MATCH (n)-[x]->() with n, sum(x.Flights) as total_outgoing WHERE total_outgoing <3000 and EXISTS { ({Symbol:"ATL"} )-->(n)} and EXISTS { ({Symbol:"ORD"} )-->(n)} and EXISTS { ({Symbol:"DFW"} )-->(n)} and EXISTS { ({Symbol:"LAX"} )-->(n)} and EXISTS { ({Symbol:"PHX"} )-->(n)} and EXISTS { ({Symbol:"LAS"} )-->(n)} RETURN n.Symbol, total_outgoing.

The result is TUL, OMA, SMF, ABQ, ELP.

Check your work
Next below to move to the next exercise.

Load data into Neo4j
Write a Cypher query to address questions
Question
When sorting and aggregating, which of the following is true?

Only the count() aggregate function can be used with ORDER BY.
To use an ORDER BY on an aggregate in a query, the query must also include a GROUP BY.
Sorting cannot be done with aggregates in a single query. It requires two queries.
An aggregate must be included in the RETURN to be used in an ORDER BY.
Select Next below to move to the next exercise.

---

Graph Analytics
3 Hr 22 Min Remaining
Exercise 7 - Advanced Graph Analytics with Neo4j
Introduction
Welcome to the Advanced Graph Analytics with Neo4j exercise.

Open Neo4j Browser and create a new project, including starting the DMBS. Launch the Graph Data Science Playground, and Start it for the active project. Use the following code snippet to load data into Neo4j.

LOAD CSV FROM 'file:///data.csv' AS row 
WITH row[0] AS Origin_airport, row[2] AS Origin_city, row[1] AS Destination_airport, row[3] AS Destination_city, toInteger(row[4]) as Passengers_count, toInteger(row[5]) as Seats_count, toInteger(row[6]) as Flight_count, toInteger(row[7]) as Distance  
MERGE (o:Airport {Symbol: Origin_airport}) 
  SET  o.CityName = Origin_city 
MERGE (d:Airport {Symbol: Destination_airport}) 
  SET  d.CityName = Destination_city 
MERGE (o)-[r:ROUTE]->(d) 
  SET r.Passengers = Passengers_count 
  SET r.Seats = Seats_count 
  SET r.Flights = Flight_count 
  SET r.Distance = Distance 
RETURN count(o); 
Tasks
Find the ‘influencer’ airports by running the PageRank algorithm.
Apply the Louvain algorithm
Identify the shortest path between these two airports
Instructions
Task 1 - Find the ‘influencer’ airports by running the PageRank algorithm
The marketing team can only afford to pay for advertising space at 5 airports with < 1,000,000 arriving monthly visitors. Find the most influential 5 airports in their price range.

Select single algorithm and open the algorithm tab.

Select PageRank, and edit the configurations to store result as a node attribute.

Write a query to filter airports by monthly arriving visitors and to sort descending by the PageRank node attribute. Here is an acceptable query:

MATCH ()-[r]->(m) with DISTINCT m, sum(r.Passengers) as cost WHERE cost <1000000 RETURN DISTINCT m.Symbol, cost, m.pagerank ORDER BY m.pagerank DESC>

Task 2 - Apply the Louvain algorithm
The sales department needs to split the airports into regions so they can assign sales representatives. Instead of the typical split based on geography, they would like to use community detection to find relevant clusters of airports. Apply the Louvain algorithm to split the airports into groups of 60 or fewer airports. Identify the cluster with the highest average arriving passengers to give to your best sales rep.

Select single algorithm and open the algorithm tab.

Select Louvain clustering algorithm, and edit the configurations to store result as a node attribute and to accept a maximum of 60 nodes in each cluster.

Write a query that groups by cluster and reports the arriving passengers / total number of airports in the cluster. An acceptable query is:

MATCH ()-[r]->(m) return m.louvain, sum(r.Passengers), count(distinct m),sum(r.Passengers) / count(distinct m)

Note: Since randomization is used in the clustering, the results may be different at each run.

Task 3 - Identify the shortest path between these two airports
A sales rep got stuck at Fresno Yosemite International Airport (code FAT), and needs to get to Brownsville South Padre Island International Airport (code BRO). What is the shortest path between these two airports?

Run the PageRank algorithm.

Select single algorithm.

Select shortest path, and edit the configurations to enter FAT and BRO as the starting and ending airports respectively.

A result is FAT to SEA to IAH to BRO.

Check your work
Check each box to confirm completion of the task.

Question
The graph we analyzed had only one type of node and one type of edge. If there were more than one and we wanted to filter to a specific type of node or edge, which section of the configuration would be used?

Algorithm
Results
Projected Graph
Algorithm Parameters
Select Next below to move to the next exercise.

---

Graph Analytics
3 Hr 22 Min Remaining
Exercise 8 - Load Graph Data into Apache Spark
Introduction
Welcome to the Load graph data into Apache Spark exercise (Airports2.csv).

Tasks
Load the data into a Spark DataFrame
Create a new DataFrame with unique Airports
Create a new DataFrame with multiple criteria
Define a GraphFrame from the two DataFrames above.
Run the PageRank algorithm on the graph to find the most central Airports.
Instructions
Task 1 - Load the data into a Spark DataFrame
Use the following code snippet to load the data into a Spark DataFrame.
import pyspark 
import graphframes 
from pyspark.sql import SparkSession 
spark = SparkSession.builder.getOrCreate() 

df = spark.read.options(header='True',inferSchema='True',delimiter=',').csv("./Airports2.csv")
df.printSchema() 
df.head(5)
Task 2 - Create a new DataFrame
Create a new DataFrame with all unique Airports.

Transform df into a new DataFrame that contains all Origin Airports. This can be done with the code snippet:
df_origin = df.select('Origin_airport').distinct()

Transform df into a new DataFrame that contains all Destination Airports. This can be done with the code snippet:
df_destination = df.select('Destination_airport').distinct()

Combine these two DataFrames to get all unique Airports and rename column to ‘id’. This can be done with the code snippet:
df_airports = df_origin.union(df_destination).distinct().withColumnRenamed("Origin_airport", "id")

Task 3 - Create a new DataFrame with multiple criteria
Create a new DataFrame with Origin Airports, Destination Airports, Fly Date and the sum Flights for that combination of Origin Airports, Destination Airports, Fly Date. (There are potentially multiple rows of data for each combination of Origin Airport, Destination Airport and Fly Date).

This can be accomplished with the following code snippet:
df_edges = df.groupBy("Origin_airport","Destination_airport","Fly_date").sum("Flights").withColumnRenamed("Sum(Flights)", "Flights")

Task 4 - Define a GraphFrame from the two DataFrames above
Create a new DataFrame with edges connecting Origin Airports and Destination Airports, aggregated by Fly Date

This can be accomplished with the following code snippet:
g = GraphFrame(df_airports, df_edges)

Task 5 - Run the PageRank algorithm on the graph to find the most central Airports
Run the PageRank algorithm on the graph to find the most central Airports.

This can be accomplished with the following code snippet from the GraphFrames documentation:
results = g.pageRank(resetProbability=0.01, maxIter=20) 
results.vertices.select("id", "pagerank").show() 
Check your work
Check each box to confirm completion of the task.

Load the data into a Spark DataFrame
Create a new DataFrame with unique Airports
Create a new DataFrame with multiple criteria
Define a GraphFrame from the two DataFrames above.
Run the PageRank algorithm on the graph to find the most central Airports.
Question
If we wanted to calculate the number of airports with direct flights to LAX in January 2000, which Graph methods would be used?

“edges.filter” and “inDegree"
“groupBy” and “degree”
“select” and “calcDegree”
“edge.slicer” and “getDegree”
Congratulations! You have completed the lab.

---

