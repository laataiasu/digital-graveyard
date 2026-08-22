---
title: "Prompt LLM to Summarize and Return Summary Message"
date: 2026-05-19
tags: [note]
publish_external: true
---

## Introduction to Agents with LangGraph
Lesson
Cloud Resources

Introduction to Agents with LangGraph
Simple LLM calls are limited by the knowledge the model was trained on. To overcome this, developers use Chains or Agentic Systems to give LLMs more control over application workflows.

Chains vs. Agents
Chains – Define fixed steps before and after an LLM call, ensuring reliable execution.

Agents – Allow the LLM to decide the flow of execution dynamically.

Why LangGraph?
Giving more control to an LLM reduces reliability--but LangGraph helps maintain reliability while enabling agentic behavior.

More flexibility in designing workflows.
Clear visibility into control flow (no hidden complex prompts).
Supports cycles and persistence, making it suitable for iterative AI workflows.
Graphs in LangGraph
LangGraph structures workflows as graphs with nodes and edges:

Nodes – Python functions that define agent logic.

Edges – Python functions that decide which node runs next based on state.

Graph-Based AI Workflows
Graphs are widely used in AI and data-driven applications:

Social Networks – Users (nodes) connected by relationships (edges).
E-Commerce – Items and customers as nodes, with purchasing behavior forming edges.
In LangGraph, this concept is applied to AI workflows, where decision-making paths are dynamically determined.

Integration with LangChain
LangGraph works independently, but it integrates seamlessly with LangChain, allowing developers to:

Use LangChain components to build nodes and edges.
Leverage LangGraph for workflow orchestration.
Final Thoughts
LangGraph enables structured, agent-driven AI applications while keeping control and reliability in the hands of developers. By combining LangChain and LangGraph, it’s possible to build dynamic, intelligent applications that adapt to user inputs and external data.

Quiz Question
Which of the following is an important feature of LangGraph that makes it powerful for agentic designs?









## Agentic Workflows
Lesson
Cloud Resources

Agentic Workflows with LangGraph
Agentic workflows allow LLMs to control execution flow, adapting to user input, conditions, and tools. Unlike fixed Chains, agentic workflows make real-time decisions, improving flexibility and automation.

Setting Up the Workflow
Instantiate the Model – Define an LLM and optionally bind tools to expand its capabilities.
llm_with_tools = llm.bind_tools([tool_a, tool_b, tool_c], tool_choice="auto")
Initialize the Graph – Create a StateGraph to track input, output, and intermediate data.
workflow = StateGraph(MessagesState)
Define Nodes – Each node represents a step in the workflow, processing input and modifying the state.
def first_node(state):
    return {"results": f"Hello, {state['input']}!"}
workflow.add_node(first_node)
Create Edges – Define execution paths between nodes.
workflow.add_edge("node_a", "node_b")
Specify Start and End – Ensure the workflow has a defined entry and exit.
workflow.add_edge(START, "node_a")
workflow.add_edge("node_b", END)
Compile the Workflow – Validate structure before execution.
graph = workflow.compile()
Executing and Visualizing
Invoke the workflow with input and configuration.

graph.invoke({"input": "Some input"})
Use Mermaid diagrams to visualize the process for debugging and documentation.

Final Thoughts
LangGraph enables dynamic, AI-driven workflows by combining state tracking, flexible decision-making, and structured execution. By integrating nodes, edges, and visualization, developers can create scalable, intelligent automation.

Quiz Question
Which of the following are key components involved in setting up an agentic workflow using LangGraph?











## Demo: Building a Workflow with LangGraph
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Simple Workflows with LangGraph
Overview
This demo introduces the basics of creating sequential workflows using LangGraph. It starts with simple data processing examples, then moves to a more realistic use case involving LLMs for question answering.

Key Steps Covered
1. Basic Data Processing Workflow
a. State Definition
A State class is created by extending TypedDict.
State holds:
input: integer
output: integer
class State(TypedDict):
  input: int
  output: int
b. Node A
Processes the input value.
Adds a random offset (1–10) to the input.
Updates the output field.
def node_a(state):
  offset = random.randint(1, 10)
  output = state["input"] + offset
  return {"output": output}
c. Node B
Takes the output of Node A as its input.
Adds another random offset.
Updates the output field again.
def node_b(state):
  offset = random.randint(1, 10)
  output = state["output"] + offset
  return {"output": output}
d. Workflow Construction
A StateGraph is created.
Nodes are added.
Edges are set:
start → node_a → node_b → end
workflow = StateGraph(State)
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)
workflow.add_edge("start", "node_a")
workflow.add_edge("node_a", "node_b")
workflow.add_edge("node_b", "end")
e. Execution Example
Input: 1
Example run:
Node A: 1 + offset 1 → output 2
Node B: 2 + offset 6 → output 8
Each run may vary due to random offsets.
2. LLM-Based Workflow
a. State Definition
A second State class is created for the LLM use case:
question: string
response: string
class State(TypedDict):
  question: str
  response: str
b. LLM Node
A node uses a chat LLM to answer Pokémon-related questions.
Composes messages:
SystemMessage: "You are a Pokémon specialist."
HumanMessage: User-provided question.
The model generates a response which is stored in the state.
def model_node(state):
  messages = [
      SystemMessage(content="You are a Pokémon specialist."),
      HumanMessage(content=state["question"])
  ]
  response = llm.invoke(messages)
  return {"response": response.content}
c. Workflow Construction
Only one node (model) is added.
Edges:
start → model → end
workflow = StateGraph(State)
workflow.add_node("model", model_node)
workflow.add_edge("start", "model")
workflow.add_edge("model", "end")
d. Execution Example
Question: "What is the name of Ash's first Pokémon?"
Correct output: "Ash's first Pokémon is Pikachu."
3. Key Concepts Highlighted
Sequential flow: Data passes from one node to the next.
TypedDict states: Enforce predictable data structure across nodes.
Node outputs feed node inputs: Node A’s output becomes Node B’s input.
Graphs vs. Chains: Unlike LangChain chains, LangGraph explicitly defines nodes and edges for modular flow control.
Random vs. Deterministic processing: Shows use of randomness in basic workflows and structured, reproducible behavior in LLM flows.
4. Conclusion
LangGraph enables building modular, sequential workflows for both simple data tasks and complex AI-driven applications.
It sets a strong foundation for more advanced multi-node and multi-agent workflows.

## Exercise: Create a Router with LangGraph
Lesson
Cloud Resources
Welcome to your Prompt Routing Challenge! In this exercise, you'll build a system that can intelligently route user inputs to different tasks based on an input. This technique is widely used in real-world applications where a single interface must handle multiple tasks -- such as summarization, translation, or answering questions.

Scenario
Imagine you're building a smart assistant that can handle various types of requests through a single conversation interface. Your assistant should understand the user's intent and respond accordingly -- but each task may require a different prompt structure or strategy.

To manage this complexity, you'll build a node router. This router will evaluate the user input and choose the most appropriate node to use. For example, it should be able to decide whether the user is asking for a summary, a translation, or a general question -- and route the request to the correct prompt logic.

Challenge
You're building a text processing application that can:

Reverse a string (e.g., "hello" → "olleh")
Convert a string to uppercase (e.g., "hello" → "HELLO")
Your application should:

Accept user input and an action type.
Route to the appropriate node (reverse or upper) based on the action.
Handle invalid actions gracefully.
This will be achieved by routing the input through LangGraph nodes using a conditional edge.

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.


## Exercise Solution: Create a Router with LangGraph
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Router with LangGraph
Overview
This exercise focuses on building a simple router workflow using LangGraph. Learners create a branching logic where inputs are routed dynamically to different nodes based on specified actions ("reverse" or "upper"), illustrating how control flow and routing work within LangGraph.

Key Steps Covered
1. Setup and Imports
All necessary libraries are imported.
Environment is prepared to use LangGraph components.
2. State Schema Definition
A State class is created using TypedDict to define the schema for the workflow's input and output.
The State includes:
input (string)
action (string constrained by a Literal type to either "reverse" or "upper")
output (string)
class State(TypedDict):
  input: str
  action: Literal["reverse", "upper"]
  output: str
3. Node Functions
Two nodes are defined:
Node A: Reverses the input string.
Node B: Converts the input string to uppercase.
def node_a(state):
  return {"output": state["input"][::-1]}

def node_b(state):
  return {"output": state["input"].upper()}
4. Workflow Creation
A workflow object is created.
Nodes A and B are added to the workflow using add_node().
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)
5. Routing Function
A routing function directs execution to the appropriate node based on the action specified in the input.
def router(state):
  if state["action"] == "reverse":
      return "node_a"
  elif state["action"] == "upper":
      return "node_b"
6. Defining Edges
Edges are defined in the workflow:
From start to either node_a or node_b, based on the router function.
From both node_a and node_b to end.
workflow.add_edge("start", router)
workflow.add_edge("node_a", "end")
workflow.add_edge("node_b", "end")
7. Compilation and Visualization
The workflow graph is compiled and visualized, showing:
Start → Router → Node A or Node B → End
8. Testing the Router
Inputs are tested:
With action "upper": Input is converted to uppercase.
With action "reverse": Input is reversed.
graph.invoke({"input": "some input", "action": "upper"})
--Output: "SOME INPUT"

graph.invoke({"input": "some input", "action": "reverse"})
 --Output: "tupni emos"
An error initially occurred because the State class was missing its base class (TypedDict), but it was corrected, and the workflow executed as expected.
9. Encouraged Exploration
Learners are invited to:
Add more actions (e.g., "lower", "capitalize").
Improve error handling for unsupported actions.
Make the router more flexible and robust.

## Exercise Solution: Create a Router with LangGraph
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Router with LangGraph
Overview
This exercise focuses on building a simple router workflow using LangGraph. Learners create a branching logic where inputs are routed dynamically to different nodes based on specified actions ("reverse" or "upper"), illustrating how control flow and routing work within LangGraph.

Key Steps Covered
1. Setup and Imports
All necessary libraries are imported.
Environment is prepared to use LangGraph components.
2. State Schema Definition
A State class is created using TypedDict to define the schema for the workflow's input and output.
The State includes:
input (string)
action (string constrained by a Literal type to either "reverse" or "upper")
output (string)
class State(TypedDict):
  input: str
  action: Literal["reverse", "upper"]
  output: str
3. Node Functions
Two nodes are defined:
Node A: Reverses the input string.
Node B: Converts the input string to uppercase.
def node_a(state):
  return {"output": state["input"][::-1]}

def node_b(state):
  return {"output": state["input"].upper()}
4. Workflow Creation
A workflow object is created.
Nodes A and B are added to the workflow using add_node().
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)
5. Routing Function
A routing function directs execution to the appropriate node based on the action specified in the input.
def router(state):
  if state["action"] == "reverse":
      return "node_a"
  elif state["action"] == "upper":
      return "node_b"
6. Defining Edges
Edges are defined in the workflow:
From start to either node_a or node_b, based on the router function.
From both node_a and node_b to end.
workflow.add_edge("start", router)
workflow.add_edge("node_a", "end")
workflow.add_edge("node_b", "end")
7. Compilation and Visualization
The workflow graph is compiled and visualized, showing:
Start → Router → Node A or Node B → End
8. Testing the Router
Inputs are tested:
With action "upper": Input is converted to uppercase.
With action "reverse": Input is reversed.
graph.invoke({"input": "some input", "action": "upper"})
--Output: "SOME INPUT"

graph.invoke({"input": "some input", "action": "reverse"})
--Output: "tupni emos"
An error initially occurred because the State class was missing its base class (TypedDict), but it was corrected, and the workflow executed as expected.
9. Encouraged Exploration
Learners are invited to:
Add more actions (e.g., "lower", "capitalize").
Improve error handling for unsupported actions.
Make the router more flexible and robust.

## State Management
Lesson
Cloud Resources

Managing State in LangGraph
State management is essential in LangGraph workflows, where a StateGraph tracks inputs, outputs, and intermediate data. Understanding how to define and manage state properly improves reliability and control in AI-driven workflows.

State Machines and LangGraph
State-based systems are not new. State Machines--like traffic light controllers--transition between predefined states based on logic and conditions. In LangGraph, workflows follow a similar approach, where nodes represent states and edges define transitions.

Defining State Schemas
State schemas define what data is stored and updated as the workflow runs. Two common methods exist:

TypedDict – A lightweight approach for defining structured key-value pairs.

Pydantic – A more robust option with built-in validation for production use.

Using TypedDict (Simple, No Validation)
TypedDict works well for small states but does not enforce validation.

from typing_extensions import TypedDict

class State(TypedDict):
      color: str
If incorrect data is passed, LangGraph won’t raise an error, which can lead to unintended behavior:

graph.invoke({"color": 2})  # No error, but incorrect state handling
Using Pydantic (Validated, More Reliable)
Pydantic ensures type safety and prevents incorrect inputs.

from pydantic import BaseModel

class State(BaseModel):
      color: str
Now, if an invalid value is passed, LangGraph raises an error:

graph.invoke({"color": 2})
--ValidationError: Input should be a valid string
Final Thoughts
When designing LangGraph workflows, take the time to define a structured state that aligns with your application’s needs.

Use TypedDict for lightweight, simple state management.
Use Pydantic for complex, validated workflows to prevent data inconsistencies.
Proper state design improves reliability, ensuring your workflow behaves predictably while handling data dynamically.

Quiz Question
Which of the following describes the difference between using TypedDict and Pydantic for state management in LangGraph workflows?









## Demo: State Schemas
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: State Schemas and State Machines in LangGraph
Overview
This demo explores how to define state schemas for workflows using both TypedDict and Pydantic, and how to implement state machines in LangGraph, including basic workflows and conditional branching with repeatable flows.

Key Steps Covered
1. TypedDict vs. Pydantic for State Definition
a. Using TypedDict
A simple State is defined using TypedDict with:
input_color: Literal["green", "yellow", "red"]
output_color: Literal["green", "yellow", "red"]
class State(TypedDict):
  input_color: Literal["green", "yellow", "red"]
  output_color: Literal["green", "yellow", "red"]
A color_node randomly selects an output color based on the input.
def color_node(state):
  output_color = random.choice(["green", "yellow", "red"])
  return {"output_color": output_color}
Problem: TypedDict does not enforce type validation at runtime.
Even invalid inputs like "black" pass silently.
b. Using Pydantic
Same state but now using BaseModel from Pydantic for strict validation.
class State(BaseModel):
  input_color: Literal["green", "yellow", "red"]
  output_color: Literal["green", "yellow", "red"]
Benefits:
Validation errors are raised if an invalid color is passed.
Errors show exactly which field failed validation.
State(input_color="black", output_color="green")  # Raises validation error
Note:
Pydantic uses dot notation (state.input_color), not dictionary subscripting (state["input_color"]).
2. Simple Color Workflow
A basic StateGraph is created.
Nodes:
One color_node operating on state.
Edges:
start → color_node → end
workflow.add_node("color_node", color_node)
workflow.add_edge("start", "color_node")
workflow.add_edge("color_node", "end")
Invocations generate random color transitions based on input.
3. Traffic Light State Machine
a. Extended State Definition
A more complex State is defined with:
color: str
repeat_mode: bool
messages: list
counter: int
class State(BaseModel):
  color: str
  repeat_mode: bool
  messages: List[str]
  counter: int
b. Node Definitions
green_light_node: Waits 60 seconds (simulated), sets color to green.
yellow_light_node: Waits 3 seconds, sets color to yellow.
red_light_node: Waits 15 seconds, sets color to red.
Each node updates the state and logs its action to the messages list.

def green_light_node(state):
  --Simulate green light action
  return {"color": "green", "counter": state.counter + 1}
c. Conditional Router
After red_light_node, a conditional router (should_repeat) decides:
If repeat_mode is True and counter <= 3, loop back to green_light_node.
Else, terminate the workflow.
def should_repeat(state):
  if state["repeat_mode"] and state["counter"] <= 3:
      return "green_light"
  return "end"
d. Workflow Construction
Nodes added: green, yellow, red.
Edges:
start → green_light
green_light → yellow_light
yellow_light → red_light
red_light → (conditional router) → green_light or end
workflow.add_edge("red_light", should_repeat)
workflow.add_conditional_edges(should_repeat, path_map={"green_light": "green_light", "end": "end"})
e. Execution Example
If repeat_mode=True, the lights cycle through green → yellow → red up to 3 times.
If repeat_mode=False, the lights complete only one full cycle.
state = {"color": "green", "repeat_mode": True, "messages": [], "counter": 0}
Outputs trace each light transition and counter increment.
4. Key Concepts Highlighted
TypedDict is flexible but weak on validation; Pydantic enforces strong runtime validation.
State graphs allow for sequential and conditional flows.
Conditional branching enables looping behaviors like state machines.
LangGraph easily supports both simple workflows and complex event-driven state transitions.
5. Conclusion
TypedDict is useful for simple, lenient workflows.
Pydantic is essential for robust, validated workflows.
LangGraph provides the control and flexibility needed to build real-world, multi-path workflows with clear state management.

## Demo: Understanding Reducers
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Using Reducers in LangGraph
Overview
This demo explains reducers in LangGraph--mechanisms that allow safe merging of parallel updates to the same field in a workflow’s state. It walks through basic examples with integers, lists, and LangChain messages, highlighting how reducers prevent conflicts when nodes operate in parallel.

Key Steps Covered
1. Recap: Sequential Data Processing
A basic state was created with:

input: integer
output: integer
Two nodes:

node_a: Adds a random offset to input.
node_b: Adds another random offset to the result from node_a.
class State(TypedDict):
  input: int
  output: int
Sequential flow: start → node_a → node_b → end.
Example:
Input: 1
Offset node_a: +13 → 14
Offset node_b: +3 → 17
2. Problem with Parallel Execution
Changing the workflow so start sends the state to both node_a and node_b in parallel causes a problem:
Both nodes try to update the output field at the same time.
Results in an InvalidUpdateError because the output field was designed to store only a single integer.
workflow.add_edge("start", "node_a")
workflow.add_edge("start", "node_b")
The system cannot automatically merge two integer outputs.
3. Solution: Reducers
Reducers resolve conflicts by defining how to combine multiple updates to the same field.
Example:
Using operator.add to concatenate two lists.
Now output becomes a list instead of an integer.
class State(TypedDict):
  input: int
  output: List[int]  # Note: output is now a list
Example run:

node_a produces 9
node_b produces 4
Final output: [9, 4]
The reducer ensures both results are preserved.

4. Reducers with LangChain Messages
In workflows involving messages, a simple operator.add doesn’t work well when merging structured messages.
Instead, LangGraph provides the add_messages reducer.
from langgraph.reducers import add_messages
This handles merging messages (e.g., SystemMessage, HumanMessage, AIMessage) properly into a list.
5. Creating a Workflow with MessageState
A MessageState is used instead of custom schema:
It automatically sets up messages with the add_messages reducer.
from langgraph.graph.message import MessageState
Node:

Receives the user’s question.
Passes it to the LLM.
Captures the AI's answer.
Example:

Input: "What is the name of Ash’s first Pokémon?"
Output: "Ash’s first Pokémon is Pikachu."
6. Key Concepts Highlighted
Sequential workflows are simple because each node modifies the state one after another.
Parallel workflows require reducers to avoid update conflicts.
Reducers define how to merge concurrent updates:
Adding numbers → Sum
Adding lists → Concatenation
Adding messages → Message aggregation
MessageState simplifies using LangChain messages in workflows without needing custom schemas.
7. Conclusion
Reducers are critical for safe and correct parallel execution in LangGraph.
They allow multiple nodes to contribute to the same field without data loss or collisions.
Properly designing state and reducers enables scalable, modular graph workflows.

## Demo: Exploring Configurable Parameters
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Using Config Objects in LangGraph Workflows
Overview
This demo explains how to use the config object in LangGraph workflows. Configs allow you to pass external, dynamic parameters into your workflow execution, enabling behaviors like customized offsets in calculations or personalized LLM responses.

Key Steps Covered
1. Configurable Data Processing Example
a. State Definition
A State is created with:
input: integer
partial: integer (intermediate result)
results: integer (final result)
Both partial and results use operator.add as a reducer.
class State(TypedDict):
  input: int
  partial: int
  results: int
b. Node Definitions
node_a:
Adds an offset (retrieved from config) to input.
Stores the result in partial.
node_b:
Adds a new offset (also from config) to partial.
Stores the result in results.
def node_a(state, config):
  offset = config.get("offset", 0)
  return {"partial": state["input"] + offset}

def node_b(state, config):
  offset = config.get("offset", 0)
  return {"results": state["partial"] + offset}
c. Workflow Construction
Nodes added: node_a, node_b.
Edges:
start → node_a → node_b → end
workflow = StateGraph(State)
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)
workflow.add_edge("start", "node_a")
workflow.add_edge("node_a", "node_b")
workflow.add_edge("node_b", "end")
d. Execution Example
Input: 1
Config offset: 10
node_a: 1 + 10 → 11
node_b: 11 + 10 → 21
workflow.invoke({"input": 1}, config={"offset": 10})
Changing the offset to 20 results in different outputs accordingly.
2. Configurable LLM Example
a. State Definition
A State is created by extending MessageState and adding a question field.
class State(MessageState):
  question: str
MessageState automatically includes a messages list with a reducer.
b. Model Node
A node that:
Checks if a user's name is present in the config.
If so, injects a SystemMessage to personalize the greeting.
def model_node(state, config):
  name = config.get("name")
  if name and not state["messages"]:
      state["messages"].append(SystemMessage(content=f"Help the following user: {name}. Give initial greeting before responding."))
  response = llm.invoke(state["messages"])
  return {"messages": [response]}
c. Workflow Construction
Single node (model) is added.
Edges:
start → model → end
workflow = StateGraph(State)
workflow.add_node("model", model_node)
workflow.add_edge("start", "model")
workflow.add_edge("model", "end")
d. Execution Example
Input question: "What is the name of Ash’s first Pokémon?"
Config name: "Henrique"
workflow.invoke({"question": "What is the name of Ash’s first Pokémon?"}, config={"name": "Henrique"})
Output: "Hello Henrique, Ash's first Pokémon is Pikachu."

Changing the name to "James" dynamically changes the greeting.

3. Key Concepts Highlighted
RunnableConfig is used to inject external parameters during workflow execution.
Config values can:
Customize numeric processing (offsets).
Dynamically modify prompt instructions (personalized greetings).
Configs enhance flexibility by making workflows adaptable to different contexts without rewriting code.
4. Conclusion
Config objects provide a powerful mechanism to parameterize workflows.
They allow external information--such as API results, database fields, or user session data--to influence the workflow's behavior dynamically.
Configurations greatly improve reusability and modularity of LangGraph applications.

## Agent Implementation
Lesson
Cloud Resources

Designing AI Agents with LangGraph
AI agents can be structured using design patterns that improve their reliability and adaptability. Two important patterns in agentic workflows are:

• Tool Use – Enables the agent to interact with external systems like APIs, databases, or function calls.

• Reflection – Allows the agent to evaluate its own responses and refine them before finalizing an output.

These patterns are combined in cyclic workflows, where an agent continuously assesses, takes action, and reassesses until an optimal response is reached.

Steps for Implementing an Agent in LangGraph
Define Tools

Tools extend the agent’s capabilities by allowing it to interact with external functions.
Each tool is implemented as a Python function and is registered within the workflow.
Tools are added to the workflow as a dedicated node.
Create the Agent

The LLM is initialized and tools are bound to it.
The agent takes user input, evaluates it, and decides whether a tool is needed.
The agent’s decision-making process is guided by system prompts that clearly define its role and responsibilities.
Connect Nodes with Conditional Routing

The agent node is the first step after the start node.
The agent then chooses between two paths:
If tool execution is needed, the workflow moves to the tools node.
If no tool is needed, the workflow terminates.
This decision is handled by a conditional routing function that inspects the latest LLM message.
Introduce a Cycle for Reflection

After tool execution, the result loops back to the agent for further evaluation.
The agent determines whether more steps are needed or if the task is complete.
This cycle allows for iterative refinement of responses.
LangGraph enables structured, flexible agent behavior by supporting these patterns, making it a strong choice for AI-driven workflows.

Quiz Question
Which of the following are steps involved in implementing an AI agent using LangGraph? Select all that apply.











## Demo: Creating a Database Toolkit
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Creating a Database Toolkit for Text-to-SQL Agents
Overview
This demo shows how to build a database interaction toolkit that an LLM can use, laying the groundwork for a text-to-SQL agent. It covers setting up database access, programmatically querying metadata, and building structured tools that expose these capabilities.

Key Steps Covered
1. Setting up the Database Engine
A SQLite database file named sales.db is used.
SQLAlchemy is used to create the database engine.
from sqlalchemy import create_engine

db_engine = create_engine("sqlite:///sales.db")
Sales table structure:
ID
Transaction Date
Model
Price
Quantity
Customer ID
There are 100 rows in the table.
2. Using the Inspector
An Inspector object is created to programmatically retrieve schema information.
from sqlalchemy import inspect

inspector = inspect(db_engine)
With the inspector, you can:
List table names.
tables = inspector.get_table_names()  # ['sales']
List columns in a specific table.
columns = inspector.get_columns('sales')
column_names = [col['name'] for col in columns]
Query the database directly:
result = db_engine.execute("SELECT * FROM sales LIMIT 10")
Results can be loaded into a Pandas DataFrame for easier handling.
import pandas as pd

df = pd.DataFrame(result.fetchall(), columns=result.keys())
3. Building Database Tools
Three tools are developed:

a. List Tables Tool
Lists all tables in the database.
Receives the db_engine from the config parameter.
@tool
def list_tables(config):
  inspector = inspect(config["db_engine"])
  return inspector.get_table_names()
b. Get Table Schema Tool
Returns the column names for a specific table.
@tool
def get_table_schema(table_name: str, config):
  inspector = inspect(config["db_engine"])
  columns = inspector.get_columns(table_name)
  return [{"name": col["name"], "type": col["type"]} for col in columns]
c. Execute SQL Tool
Runs a SQL query against the database and returns results.
@tool
def execute_sql(query: str, config):
  result = config["db_engine"].execute(query)
  return [dict(row) for row in result]
All tools are built to expect a config dictionary containing the database engine.
4. Tool Testing
A config object is created:
config = {"db_engine": db_engine}
list_tables is called:
Returns: ['sales']
get_table_schema is called with "sales":
Returns all columns and their types.
execute_sql is called:
Runs SELECT * FROM sales LIMIT 10
Returns the first 10 rows of the sales table.
5. Key Concepts Highlighted
Dynamic config passing:
Tools are environment-independent and can be re-used across databases by passing a different db_engine through the config.
Separation of concerns:
Tools do not hardcode database connection logic.
Retrieval, schema exploration, and querying are decoupled.
Foundation for Text-to-SQL agents:
LLMs can now list tables, retrieve schema information, and execute custom SQL queries through tool calling.
6. Conclusion
A structured toolkit like this enables powerful text-to-SQL workflows.
It abstracts database operations into callable tools that an agent can use safely.
This pattern is essential for building scalable, database-driven AI systems.

## Exercise: Create a Text2SQL ReAct Agent
Lesson
Cloud Resources
Welcome to your Text-to-SQL Challenge!

In this exercise, you’ll create a ReAct-based agent capable of interpreting natural language questions and converting them into SQL queries to extract data from a database. This kind of agent bridges the gap between human language and structured data -- a valuable capability in many enterprise applications.

Scenario
You're working on a conversational analytics assistant that allows users to query business data in plain English. Users might say things like "What was the total sales last month?" or "List the top 5 products by revenue." -- and expect instant answers from your system.

However, the underlying data is stored in a relational database. To access this data, your assistant must convert the user's query into a valid SQL command. Not only that, it needs to reason about the best way to get the answer and execute the query safely.

To accomplish this, you'll use the ReAct pattern, where your agent can both think (reason step-by-step about the query) and act (run tools like a SQL engine) to solve the task.

This enables non-technical users to ask questions in plain English and get data insights without writing SQL.

Challenge
You’re building a Text2SQL assistant for a Sales Dashboard. The agent should:

Parse user questions.
Identify the relevant tables and columns. -
Generate the corresponding SQL query. -
Execute the query and return the result.
This enables non-technical users to ask questions in plain English and get data insights without writing SQL.

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.


## Exercise Solution: Create a Text2SQL ReAct Agent
Lesson
Cloud Resources
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Text2SQL Workflow with LangGraph
Overview
This exercise guides learners through building a Text2SQL workflow using LangGraph. The workflow interprets natural language questions, generates corresponding SQL queries, and executes them against a sample sales database using a combination of LangGraph nodes, tools, and agent logic.

Key Steps Covered
1. Tooling and Environment Setup
Several database interaction tools are pre-defined and available:
list_tables_tool
get_table_schema_tool
execute_sql_tool
A sales database (with 100 rows) is preloaded for use in queries.
The OpenAI LLM is initialized with load_dotenv to securely handle the API key.
2. State Definition
A custom State class is created by extending MessageGraphState, adding a single field:
user_query: str
This state holds the user’s question and message history throughout the graph execution.
class State(MessageGraphState):
  user_query: str
3. LLM Tool Binding
The three SQL tools are bound to the LLM using LangChain's tool abstraction.
A new node (dba_tools) is added to the graph for tool invocation.
dba_llm_with_tools = llm.bind_tools([list_tables_tool, get_table_schema_tool, execute_sql_tool])
workflow.add_node("dba_tools", dba_llm_with_tools)
4. Agent Node Construction
A message-building node initializes the system prompt and injects the user query as a message.
The dba_agent node uses this message history and invokes the LLM to generate the next response.
def messages_builder(state):
  return {"messages": [SystemMessage(...), HumanMessage(content=state.user_query)]}
These two nodes (messages_builder, dba_agent) are added to the workflow.
5. Routing Logic
A routing function examines the most recent message:
If the message includes a tool_call, the workflow routes to dba_tools.
Otherwise, it terminates.
Tool execution results are looped back to the agent for further reasoning if needed.
def router(state):
  last_msg = state["messages"][-1]
  return "dba_tools" if last_msg.tool_calls else "end"
Edges are defined to form a loop: start → messages_builder → dba_agent → dba_tools → dba_agent, until no tools are called.
6. Execution and Testing
The workflow is compiled and visualized.

A test query is provided: "How many Dell XPS 15 were sold?"

The system processes the query in the following steps:

Lists available tables.
Retrieves the schema for the relevant table (sales).
Generates and executes the SQL: SELECT SUM(quantity) FROM sales WHERE model = 'Dell XPS 15';
Returns the result via an AI message.
Logs confirm the tool usage and intermediate steps, ensuring the flow works as expected.

7. Encouraged Exploration
Learners are encouraged to:
Add more tools or extend tool functionality.
Modify prompts for improved SQL accuracy.
Test the workflow with a wider variety of user queries.

## Demo: Limiting Messages
Lesson
Cloud Resources


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Techniques for Limiting Messages to Save Tokens
Overview
This demo explores multiple techniques for limiting messages in LangGraph workflows. Reducing message history is important for saving tokens and optimizing performance in agentic applications that use LLMs over multi-turn conversations.

Key Steps Covered
1. Initial Setup
A single-node workflow is created with:
A system message ("You are a FinTech specialist").
Few-shot examples of human and AI messages (e.g., "What is Pokémon?" → refusal to answer).
messages = [
  SystemMessage(...),
  HumanMessage(...),
  AIMessage(...),
  HumanMessage(...),
]
Each message is assigned a unique ID for easier filtering later.
2. Token Usage Without Trimming
When invoking with the full message history:
Prompt tokens and completion tokens are relatively high (e.g., ~239 total tokens).
response = llm.invoke(messages)
3. Simple Manual Filtering
Manually invoking the LLM with only a subset of the messages (e.g., first and last message).
This substantially reduces token usage (e.g., ~96 total tokens).
response = llm.invoke([messages[0], messages[-1]])
4. Filtering Inside the Node
A custom state is created by extending MessageState, including:
messages
filtered_messages
Inside the node, only the last three messages are passed to the LLM.
state = {"messages": [...], "filtered_messages": state["messages"][-3:]}
This avoids needing to manually slice messages each time.
5. Using Remove Messages Strategy
The remove_message reducer from LangGraph is used to delete unwanted messages based on IDs.
A deletion list is created to filter out irrelevant few-shot examples while preserving essential context.
from langgraph.reducers import remove_messages

delete_messages = ["id_of_old_message", "id_of_another_old_message"]
messages = remove_messages(existing_messages, delete_messages=delete_messages)
This helps refine conversation history efficiently.
6. Using Trim Messages for Token Limits
Trim strategy is introduced to limit messages by token budget:
Keeps only the latest messages that fit within a specified token limit.
The trim_messages() method is used with different max token thresholds.
trimmed = trim_messages(messages, max_tokens=250, strategy="last")
Behavior:

Higher token limits keep more conversation history.
Lower token limits progressively discard older messages.
Examples:

250 tokens → retains last two messages.
30 tokens → retains only system message.
7. Summarization to Compress Messages
Messages between the initial system message and the latest user query are summarized.
Summarization is prompted by inserting a special HumanMessage: "Summarize the above conversation."
This produces a concise summary that replaces multiple older turns.
summarized_message = llm.invoke(summary_prompt)
The resulting list:

SystemMessage
Summary AIMessage
Most recent HumanMessage
Token usage drops significantly after summarization.

8. Key Concepts Highlighted
Manual slicing reduces input size but needs management.
Automatic filtering inside nodes allows persistent behavior.
Reducers (remove_messages, add_messages) provide fine-grained control.
Trimming by token count ensures fitting into LLM token limits dynamically.
Summarization reduces message volume while retaining conversation context.
9. Conclusion
Efficient management of conversation history is essential for scalable LLM applications.
LangGraph offers flexible techniques to balance memory retention with token usage constraints.
Combining filtering, trimming, and summarization enables smooth long-running agentic workflows.

## Demo: Creating Multiple Schemas
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Using Multiple State Schemas in LangGraph
Overview
This demo demonstrates how to use multiple state schemas within a LangGraph workflow. This approach allows separating "visible" state from "hidden" internal state, and supports modular processing pipelines with distinct input, process, and output stages.

Key Steps Covered
1. First Approach: Hidden Layer State
a. State Definitions
Two distinct TypedDict classes are created:

ProcessState:
input: string
output: string
HiddenState:
thought: string
class ProcessState(TypedDict):
  input: str
  output: str

class HiddenState(TypedDict):
  thought: str
b. Node Definitions
Node A:

Accesses ProcessState (specifically input).
Updates HiddenState by predicting a hidden "thought."
Example thought: "I don't know what to do with this message."
Node B:

Accesses HiddenState.
Updates ProcessState with a safe output.
Example output: "Thank you for your message. We are processing it."
def node_a(state):
  return {"thought": "I don't know what to do with this message."}

def node_b(state):
  return {"output": "Thank you for your message. We are processing it."}
c. Workflow Construction
Nodes added: node_a, node_b.
Edges:
start → node_a → node_b → end
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)
workflow.add_edge("start", "node_a")
workflow.add_edge("node_a", "node_b")
workflow.add_edge("node_b", "end")
d. Execution Example
Input: "The product doesn't work. I want my money back."
Internal "thought" (hidden): "I don't know what to do with this message."
External response (output): "Thank you for your message. We're processing it and will get back to you soon."
2. Second Approach: Input-Process-Output State Separation
a. Extended State Definitions
Three states are now defined:

InputState: for initial user input.
ProcessState: for internal intermediate reasoning.
OutputState: for the final user-facing response.
class InputState(TypedDict):
  input: str

class ProcessState(TypedDict):
  thought: str

class OutputState(TypedDict):
  output: str
b. Node Definitions
L1 Agent:

Receives InputState.
Outputs ProcessState with a "thought."
L2 Agent:

Receives ProcessState.
Outputs OutputState with a public response.
c. Workflow Construction
StateGraph is now configured with multiple states:
It manages input, processing, and output separately.
Nodes and edges are set similarly, but different nodes operate on different parts of the state.
workflow = StateGraph(
  input_schema=InputState,
  output_schema=OutputState,
  process_state_schema=ProcessState
)
d. Execution Example
Input: "The product doesn't work. I want my money back."

Final Output: "Thank you for your message."

Only the OutputState (i.e., the safe external response) is returned to the user.

3. Key Concepts Highlighted
Hidden state allows reasoning to be separated from user-facing outputs.
Input-process-output separation makes workflows modular and easier to debug.
Multiple schemas support complex workflows with clean transitions between stages.
Avoids accidentally exposing internal thoughts (like uncertainty) directly to users.
4. Conclusion
LangGraph’s support for multiple state schemas enables building structured, multi-phase workflows.
Using hidden or separated states improves system safety, transparency, and modularity.
This pattern is particularly useful for agent design where reasoning must be separated from final user communication.

## State vs. Short-Term Memory
Lesson
Cloud Resources

State Management and Persistence in LangGraph
State in LangGraph acts as a data package that flows through nodes, carrying relevant information within a single execution. However, state does not persist between invocations, meaning each new execution starts from scratch.

State Limitations
When a workflow runs, it processes state only for that instance. Once execution finishes, the state is discarded. If re-invoked, the previous state is lost, which breaks continuity for applications like chatbots that need memory.

Adding Short-Term Memory with Checkpoints
To persist state across multiple runs, checkpoints store snapshots of state at each step. LangGraph provides MemorySaver(), an in-memory checkpoint system, to retain state temporarily.

from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
graph = workflow.compile(checkpointer=checkpointer)
Using Threads for Persistent State
Checkpoints are organized into threads, similar to conversation histories in ChatGPT. Each execution must include a thread ID to retrieve past interactions.

config = {"configurable": {"thread_id": "1"}}
graph.invoke({"node_name": ""}, config)
If the same thread ID is used again, the state continues from where it left off.

Output:
{'node_name': 'b', 'value': ['a', 'b', 'a', 'b']}
Accessing State History
LangGraph allows retrieval of state history for debugging and analysis.

list(graph.get_state_history(config))
Returns a chronological list of state snapshots, showing how the workflow evolved.

Final Thoughts
State is ephemeral--without checkpoints, it resets after each execution.
MemorySaver() is useful for debugging, but production systems should use PostgresSaver() for reliability.
Threads track execution history, enabling persistent AI-driven interactions.
By combining state tracking, checkpoints, and threads, LangGraph enables intelligent, memory-aware applications that evolve dynamically.

Quiz Question
What is the purpose of checkpoints in managing state within LangGraph?










## Demo: Add Checkpoints to Your Workflow
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Threads and Checkpoints in LangGraph
Overview
This demo explains how to use threads and checkpoints in LangGraph workflows. These features enable persistent conversation tracking and state snapshotting, which are critical for building multi-turn, stateful workflows and agents.

Key Steps Covered
1. Basic Workflow Setup
a. State Definition
A State is defined with a value field as a list of strings.
A reducer (operator.add) is applied to value, allowing safe merging of updates from different nodes.
class State(TypedDict):
  value: List[str]
b. Node Definitions
node_a: Appends "a" to the value list.
node_b: Appends "b" to the value list.
def node_a(state):
  return {"value": ["a"]}

def node_b(state):
  return {"value": ["b"]}
c. Workflow Construction
Nodes: node_a and node_b.
Edges:
start → node_a → node_b → end
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)
workflow.add_edge("start", "node_a")
workflow.add_edge("node_a", "node_b")
workflow.add_edge("node_b", "end")
d. Basic Execution
Invoking the workflow with an empty list as input produces:
["a", "b"]
Re-running without any checkpointing does not retain any additional memory or history.
2. Adding Checkpoints
a. Memory Checkpointer Setup
A MemorySaver checkpointer is created.
When building the workflow, the checkpointer is passed into the graph.
from langgraph.checkpoints import MemorySaver

checkpointer = MemorySaver()
workflow = StateGraph(State, checkpointer=checkpointer)
b. Using Config and Thread IDs
Each invocation now accepts a RunnableConfig with a thread_id specified.
Same thread_id → state snapshots accumulate.
Different thread_id → separate histories.
workflow.invoke({"value": []}, config={"thread_id": "1"})
c. Behavior Differences
Without checkpointing: Every run is stateless.
With checkpointing:
Running twice with thread_id="1" appends twice → ["a", "b", "a", "b"]
New thread_id values (e.g., "2", "3") start fresh each time.
3. Viewing State History
The state history for a thread can be retrieved using:
workflow.get_state_history(thread_id="1")
State snapshots include:

Node transitions (e.g., from start to node_a to node_b to end).
The evolving value list at each step.
Example:

After two invocations under thread ID "1":
First run: ["a", "b"]
Second run: ["a", "b", "a", "b"]
Thread ID "2" or "3" will show only one cycle of ["a", "b"].

4. Key Concepts Highlighted
Threads allow partitioning workflow runs by conversation ID or user session.
Checkpoints automatically snapshot state after each node.
State history retrieval enables:
Debugging workflows
Resuming from intermediate steps
Auditing or replaying execution
5. Conclusion
Threads and checkpoints are foundational for building persistent, multi-turn, and recoverable workflows.
LangGraph’s checkpointer mechanism enables lightweight memory without needing external databases.
This system is scalable to more complex workflows involving LLMs, agents, and external data integrations.

## Exercise: Loan Agent
Lesson
Cloud Resources
Welcome to your Loan Agent challenge. In this exercise, you’ll build a Loan Agent Workflow using LangGraph, designed to negotiate loan amounts with customers.

Scenario
You're building an AI-powered loan recommendation agent for a fintech company. Based on customer profile data (such as name, income, credit history, etc.), your agent should return a structured recommendation.

This agent will be integrated into a larger pipeline of automated decision-making. To ensure everything works smoothly, it’s essential that the agent’s output strictly follows a predefined schema -- no extra fields, no format deviations.

Challenge
The workflow should:

Interpret user queries intelligently.
Dynamically call tools for loan calculation
Track negotiation status and terminates gracefully.
Route the workflow using intelligent conditional edges.
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. 

## Exercise Solution: Loan Agent
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Loan Agent Workflow
Overview
This exercise walks through building a multi-turn agentic workflow in LangGraph that simulates a loan negotiation process. The system uses conversation history, tool-based logic, summarization, and routing to respond to user loan queries and determine approval status. It introduces session state management, message reduction, tool use, and state-based routing.

Key Steps Covered
1. Session State Definition
A custom SessionState is created by extending MessageGraphState.
It includes:
customer_query: the user’s initial loan request.
negotiation_status: tracks if the conversation is "in_progress" or "lost".
class SessionState(MessageGraphState):
  customer_query: str
  negotiation_status: Literal["in_progress", "lost"]
2. Summarization Logic
A summarization function is created to summarize message history when it exceeds a certain length.
The summary is injected as a new message with a unique ID.
All prior non-system messages are removed to reduce token usage.
def summarized_conversation(messages):
  # Prompt LLM to summarize and return summary message
  ...
If the total message count reaches 7 or more, summarization is triggered.
3. Loan Tools
Two tools are implemented:

calculate_max_loan: Calculates maximum loan based on:
income × 10, credit score, and age-based rules.
Max cap enforced at \$50,000.
update_negotiation_status: Updates the negotiation_status in state and logs the update.
tools = [calculate_max_loan, update_negotiation_status]
llm_with_tools = llm.bind_tools(tools)
4. Loan Agent Node
This node invokes the LLM with the provided state and tools.
It processes user input, responds accordingly, and outputs a new message.
def loan_agent(state):
  return {"messages": messages + [llm_with_tools.invoke(...)], "negotiation_status": state["negotiation_status"]}
The agent and its message ID are clearly labeled for traceability.
5. Routing Function
Determines whether to:
Continue to the tools node (if tool calls are found),
Or terminate (if no tool is needed or negotiation status has changed).
def negotiation_router(state):
  if state["negotiation_status"] != "in_progress":
  return "end"
  elif state["messages"][-1].tool_calls:
  return "tools"
  return "end"
6. Workflow and Edges
A StateGraph is built using the defined nodes:

entry_point → prepares initial messages
loan_agent → processes queries with LLM
tools → handles tool calls
Edges:

start → entry_point
entry_point → loan_agent
loan_agent → tools (if tools are required)
loan_agent → end (if not)
tools → loan_agent (loop)
7. Checkpointing and Execution
A checkpointer is added to store graph state between turns.
The graph is compiled and visualized to show the flow.
8. Invocation and Testing
A sample input is passed:
Query: “I want to have a million dollars”
Details: name, age, income, credit score
The agent calculates that the max loan is \$10,000 (due to user’s profile).
The status is updated to "lost" and the user is notified.
inputs = {
  "thread_id": "t1",
  "customer_query": "I want to have a million dollars",
  "name": "User",
  "age": 30,
  "income": 1000,
  "credit_score": 650
}
State history and snapshots confirm correct routing and updates.
9. Encouraged Exploration
Learners are encouraged to:
Reuse thread IDs to simulate ongoing conversations.
Enhance the summarizer or negotiation strategy.
Add interest calculation tools or more complex logic.
