---
title: "Extract Function Details and Create JSON Schema"
date: 2026-05-19
tags: [note]
publish_external: true
---

## Introduction to Agentic Frameworks
Lesson
Cloud Resources

Introduction to Understanding Agentic Systems
AI is evolving from reactive tools to autonomous systems capable of anticipating needs, executing tasks, and even collaborating with other AI agents. These agentic systems extend generative AI capabilities by making decisions, using tools, and refining their outputs.

Why Agentic AI?
Traditional AI provides static responses--it’s like a GPS giving directions.

Agentic AI, on the other hand, executes tasks autonomously--it’s like a self-driving car handling the journey for you.

Example
A marketing team wants insights on potential customers but only has an earnings call transcript.

An agentic system listens, analyzes, and summarizes key insights before generating an actionable report for sales reps.

This automates complex workflows, making AI not just a tool but an active participant in decision-making.

What to Expect in This Lesson
This lesson focuses on how to build AI Agents that go beyond single LLM calls.

Learn how to assign tools to AI models for executing external functions.
Explore how agents can create execution plans instead of just responding to queries.
Understand how self-reflection mechanisms improve agent accuracy.
Gain hands-on experience designing AI-driven workflows.
Learn how to choose the right agentic approach for different applications.
By the end, you’ll have a strong foundation in AI agent design and will be able to apply agentic workflows effectively across various domains.

Quiz Question
A marketing team wants insights on potential customers but only has an earnings call transcript. What’s the best approach to leverage this data for Marketing & Sales?










## AI Agents Landscape and Real World Applications
Lesson
Cloud Resources

The global AI agents market is experiencing explosive growth. By 2030, it is projected to reach \$47.1 billion, driven by major players like Salesforce, Google, and Oracle. Meanwhile, no-code SaaS platforms such as Retool and Zapier are integrating agentic AI into their offerings.

This shift signals a major transformation--AI is moving beyond traditional Robotic Process Automation (RPA) and rule-based systems into a world where agents can autonomously execute tasks and interact with other AI systems.

To keep up, businesses must recognize that LLMs alone are not enough--the future belongs to intelligent, proactive AI agents.

Quiz Question
What does this market growth indicate?









AI has evolved through three major waves, each shaping the way businesses leverage technology

Free Response
Describe the most recent shift in the Third Wave of AI

Enter your response here, there's no right or wrong answer

## OpenAI SDK
Lesson
Cloud Resources
For this lesson, we'll be creating everything from scratch using just Python and openai sdk.

Installation
Your workspace already has openai installed, but it can be easily installed in any other Python environment:


```
$ pip install "openai==1.55.3" 
```
API keys
OpenAI API keys provide access to paid OpenAI services. Vocareum is a provider that Udacity uses to grant learners access to these keys as part of enrolling in a Udacity program.

Unlike API keys that come directly from OpenAI, Vocareum OpenAI API keys must be routed through Vocareum servers, allowing Udacity to manage API usage budgets.

You will find this on the “Cloud Resources” button on the navigation pane. By clicking into the “Cloud Resources” button, you will be provided with a OpenAI API key along with the budget assigned to that key.

Using the SDK
You first need to instantiate your openai client with your API key:


from openai import OpenAI
client = OpenAI(
      base_url = "https://openai.vocareum.com/v1",
      api_key = "voc-00000000000000000000000000000000abcd.12345678"
)
Many times you'll see the instructor not passing the OpenAI key directly. This happens because he uses a local environment variable. That way he doesn't disclose his own key.


from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
You could create your own .env file and load in API keys using code like the block above. Then you can start using the client.

We recommend reading the OpenAI documentation(opens in a new tab) when trying to remember a specific method.



## Exercise Solution: Simple LLM Calls
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Simple LLM Calls
Overview
This exercise demonstrates how to make simple calls to a Large Language Model (LLM) using the OpenAI SDK. It focuses on setting up a basic environment for LLM interaction, creating prompts, and packaging the interaction logic into a reusable function.

Key Steps Covered
1. Environment Setup
Import OpenAI: The notebook begins by importing the openai library.
Authentication: It uses an API key for authentication, loaded from environment variables to keep credentials secure.
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
2. Parameter Definition
Model and Temperature: Defines the LLM model (e.g., gpt-3.5-turbo) and the generation temperature to control output creativity.
model = "gpt-3.5-turbo"
temperature = 0.7
3. System Prompt Creation
Behavior Instructions: A system prompt is created to guide the LLM's behavior, e.g., acting as a B2B content creator for CultPass.
system_prompt = "Act as a B2B content creator, create marketing campaign text, to reach the audience of the company CultPass."
4. Reusable Function Development
Function to Create Content: A function create_content(query) is developed to send user queries along with the system prompt to the model.
def create_content(query):
  messages = [
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": query}
  ]
  response = client.chat.completions.create(
      model=model,
      temperature=temperature,
      messages=messages
  )
  return response.choices[0].message.content
5. Testing the Function
A sample user query is tested: "Create an Instagram post for clients in the automotive industry."
The function runs successfully and generates a marketing post targeted at that industry.
query = "Create an Instagram post for clients in the automotive industry."
result = create_content(query)
print(result)
Final Notes
The walkthrough ends by encouraging learners to experiment further with different queries and modify parameters to deepen their understanding of LLM interactions.
## From LLM Calls to Agents
Lesson
Cloud Resources

Understanding AI Agents and Their Levels of Autonomy
AI agents interact with their environment, process information, and take action. Traditional AI agents, like vacuum robots, use sensors to perceive their surroundings and actuators to perform tasks. More recent AI agents, such as LLM-based systems, process text input and generate responses.

Levels of Agentic AI
Different AI systems require different levels of autonomy. The more control given to an AI system, the more “agentic” it becomes.

Code: Full control over decisions by explicitly coding every step. Best for critical tasks like deleting user records.
LLM Call: Single-step responses using an LLM. Works well for FAQ chatbots.
Chain: Multi-step processes in a fixed sequence. Ideal for structured workflows like text cleaning and summarization.
Router: Multi-step tasks with branching decisions but no loops. Useful for customer support systems that classify queries.
State Machines: Workflows with loops and decision-making based on prior steps. Suitable for iterative tasks like content refinement.
Autonomous: Fully independent systems that act without user input. Best for safe, automated tasks like supply tracking and reordering.
Choosing the Right Approach
More autonomy increases complexity in deployment and maintenance. Selecting the right agentic level ensures efficiency while balancing control and automation.

Question 1 of 2
Which of these AI systems is considered the most agentic?













Question 2 of 2
True or False: An AI system using state machines is more agentic than a system utilizing only LLM calls.

## Exercise Solution: Create AI Agents from Scratch
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Agents from Scratch
Overview
This exercise introduces the concept of building a simple abstraction over LLMs--custom agents. These agents are tailored LLM wrappers with specific roles, instructions, and configurations. The goal is to understand how to structure and reuse LLM interactions by encapsulating them in a class.

Key Steps Covered
1. Setup and Prompting Recap
The OpenAI client is initialized, with environment variables loaded via load_dotenv to securely access the API key.
A system prompt is crafted to instruct the LLM to behave as a senior Python developer, and an example user prompt is issued: "What is the Java virtual machine?" This highlights how context affects the model's behavior.
import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_message = "Act as a senior Python programmer."
user_prompt = "What is the Java virtual machine?"
2. Agent Class Definition
A new Agent class is created to encapsulate behavior.
The constructor stores the agent’s name, role, instructions, model, and temperature.
The invoke() method sends a prompt to the model, combining the system message (role and instructions) with the user’s message.
class Agent:
  def __init__(self, name, role, instructions, model="gpt-3.5-turbo", temperature=0.7):
    self.name = name
    self.role = role
    self.instructions = instructions
    self.model = model
    self.temperature = temperature

  def invoke(self, message: str) -> str:
    messages = [
        {"role": "system", "content": f"{self.role}. {self.instructions}"},
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(
        model=self.model,
        temperature=self.temperature,
        messages=messages
    )
    return response.choices[0].message.content
3. Agent Examples
Default Agent (Personal Assistant)
Prompt: "What is the capital of France?"
Response: "The capital of France is Paris."
default_agent = Agent(name="default", role="You are a personal assistant", instructions="Answer as helpfully as possible.")
print(default_agent.invoke("What is the capital of France?"))
Travel Agent
Prompt: "Where should I go for vacation in December?"
Temperature: Increased for more variety.
Response: Suggested warm places, winter activities, and cultural destinations.
travel_agent = Agent(name="travel", role="You are a travel assistant", instructions="Offer travel recommendations.", temperature=0.9)
print(travel_agent.invoke("Where should I go for vacation in December?"))
Math Tutor Agent
Prompt: "How do I solve a quadratic equation?"
Response: Detailed explanation of the quadratic formula and alternative methods.
math_tutor_agent = Agent(name="math", role="You are a math tutor", instructions="Explain math concepts clearly.")
print(math_tutor_agent.invoke("How do I solve a quadratic equation?"))
Storyteller Agent
Prompt: "Tell me a story about a dragon and a wizard."
Temperature: Raised to increase creativity.
Response: A short fantasy tale involving the requested elements.
storyteller_agent = Agent(name="story", role="You are a creative storyteller", instructions="Invent engaging and imaginative stories.", temperature=1.0)
print(storyteller_agent.invoke("Tell me a story about a dragon and a wizard."))
Final Notes
This exercise provides a practical introduction to constructing lightweight agents by embedding system instructions and reusing model calls. The walkthrough ends by encouraging learners to tweak parameters and invent new agents for different use cases.

## Demo: Add a Memory Layer to Your Agent
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Memory Layer for Stateless LLMs
Overview
This demo shows how to solve the inherent statelessness of Large Language Models (LLMs) by implementing a memory layer. By managing a conversation history, the agent can simulate remembering past interactions and provide coherent multi-turn conversations.

Key Steps Covered
1. Problem: Statelessness
LLMs do not retain context between calls.
Example:
First message: "Hi" → Response: "Hello! How can I assist you today?"
Follow-up: "What have I asked before?" → Response: "I don't have the ability to recall past interactions."
2. Initial Setup
OpenAI library and environment variables are loaded to securely manage API keys.
import openai
from dotenv import load_dotenv
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
3. Simple Memory List
A basic messages list is used to maintain conversation history.
Each interaction is appended to this list:
system message to set behavior,
user messages,
assistant responses.
memory = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "What is an API?"}
]

response = client.chat.completions.create(model="...", messages=memory)
memory.append({"role": "assistant", "content": response.choices[0].message.content})
After this, asking "What have I asked before?" yields the correct recall: "You asked what an API is..."
4. Creating a Memory Abstraction
A Memory class is created to manage messages more cleanly.
The class provides:
add_message(role, content): Adds a message.
get_messages(): Retrieves the full memory list.
class Memory:
  def __init__(self):
      self.messages = []

  def add_message(self, role, content):
      self.messages.append({"role": role, "content": content})

  def get_messages(self):
      return self.messages
5. Enhanced Chat Function
A chat function is built to interact with the LLM using the Memory instance.
It:
Adds the user message to memory,
Calls the LLM with the full message history,
Appends the LLM response back to memory,
Returns the new assistant message.
def chat(user_message, memory):
  memory.add_message("user", user_message)
  response = client.chat.completions.create(
      model="...",
      messages=memory.get_messages()
  )
  ai_message = response.choices[0].message.content
  memory.add_message("assistant", ai_message)
  return ai_message
6. Testing the Memory Layer
Initial system message is set manually.
Example conversation:
User: "The capital of Brazil is Brasília."
Follow-up: "What have I asked?"
The agent correctly recalls the previous question using the built memory.
memory = Memory()
memory.add_message("system", "You are a geography expert.")

chat("The capital of Brazil is Brasília.", memory)
chat("What have I asked?", memory)
The memory structure includes all system, user, and assistant messages in the right sequence.
7. Conclusion
By managing the conversation history externally, the agent can emulate memory.
The abstraction via a Memory class makes the approach scalable for more complex workflows.

## Exercise: Adding Self-Reflection Capability to Your Agent
Lesson
Cloud Resources
Welcome to your next step in building more advanced AI Agents! In this exercise, you’ll enhance your AI agent by adding self-reflection and memory. These features allow the agent to critique its responses iteratively, improving over time while maintaining a log of all interactions.

This mimics how human learning and feedback loops work, helping your agent refine its answers and avoid mistakes. By implementing this, you’ll push your agent towards more accurate and thoughtful outputs.

Scenario
Imagine you’re working on an AI-powered chatbot that needs to provide high-quality, refined responses to users in a customer support system. Sometimes, AI-generated responses might miss context or lack clarity.

Your task is to upgrade your agent by:

Enabling it to reflect on its responses before delivering them.

Allowing iterative refinement to improve response quality.

Keeping track of conversations for better context awareness.

By the end of this exercise, you’ll have an AI agent that learns from itself, identifies errors, and iteratively enhances its replies.

Challenge
In this exercise, you are tasked with upgrading the existing Agent class by adding:

A memory layer to track previous interactions.

A self-reflection mechanism that critiques and refines responses.

Your agent should:

Store conversation history for better decision-making.

Critique its own responses using a structured feedback prompt.

Refine its outputs iteratively, following predefined rules.

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Exercise Solution: Adding Self-Reflection Capability to Your Agent
Lesson
Cloud Resources
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Self-Reflection and Memory
Overview
This exercise extends the agent abstraction by introducing memory and self-reflection, enabling the agent to learn from previous interactions and revise its outputs. Learners implement a memory mechanism to preserve dialogue context and a self-critique loop to iteratively improve responses.

Key Steps Covered
1. Initial Setup
The OpenAI client is initialized with environment variables for secure authentication.
A recap illustrates the limitation of stateless LLMs: when asked "What have I asked?", the model cannot recall prior input without an explicit memory mechanism.
2. Basic Memory Implementation
A simple memory is implemented using a Python list to store messages.
After sending a question and appending the assistant's response, the model can now reference previous turns (e.g., recalling a prior question about APIs).
memory = [
  {"role": "system", "content": "Answer all user questions."},
  {"role": "user", "content": "What is an API?"},
  {"role": "assistant", "content": "An API is..."}
]
Asking "What have I asked?" now yields a relevant response because the full conversation history is sent with the query.
3. Memory Class
A Memory class is created with three methods:
add_message(role, content)
get_messages()
last_message()
class Memory:
  def __init__(self):
      self.messages = []

  def add_message(self, role, content):
      self.messages.append({"role": role, "content": content})

  def get_messages(self):
      return self.messages

  def last_message(self):
      return self.messages[-1] if self.messages else None
4. Agent with Self-Reflection
The Agent class is enhanced with memory and self-reflection:
Stores instructions, memory, and a special self-critique prompt, which asks the model to review its previous output.
The invoke() method can now perform multiple iterations with self-reflection and improvement.
self_critique_prompt = (
  "Reflect on previous response. Identify any mistakes, areas for improvement, "
  "and return a JSON structure with suggestions and a revised response."
)
The invoke() method:
Adds the user message to memory.
Optionally logs responses if verbose=True.
Iteratively asks the model to critique and revise its own output if self_reflection=True.
5. Example: Favorite Character
User prompt: "Pick only one, who is the best character in Game of Thrones?"
Initial response: A subjective answer citing Tyrion Lannister.
Self-reflection critique: The response is good but could be more concise.
Revised response: "Many fans consider Tyrion Lannister the best character in Game of Thrones, due to his wit and complexity."
6. Encouraged Exploration
The walkthrough concludes by encouraging learners to:
Customize the self-critique prompt.
Experiment with different agent personalities and critique styles.
Extend memory structure and logic for more complex use cases.

## Function Calling
Lesson
Cloud Resources

Extending AI Capabilities with Function Calling
Modern AI models can enhance their abilities by calling functions, allowing them to interact with external data and systems. Most chat models today are designed to accept function calls, making them more versatile and effective.

For example, in a sports application, an AI model can use a function like “get_latest_score” to fetch real-time football match results. If a user asks, “How did Manchester United do in their match?”, the model recognizes the need for external data, calls the function, and retrieves accurate match details.

Use Cases for Function Calling
Function calling makes AI applications more powerful and adaptable. Some key uses include:

Retrieving external data from APIs or databases (e.g., fetching weather reports or stock prices).
Triggering actions like scheduling meetings or processing orders.
Executing multi-step processes, such as extracting data or personalizing content.
Updating interfaces dynamically based on user input.
How It Works
LLMs do not execute functions directly. Instead, they suggest function calls and generate the necessary parameters. The application then executes the function and returns the result to the model.

When an OpenAI model suggests a function call, it returns a “tool_calls” field with:

The function name
The arguments to use
If the model does not require a function call, it simply generates a response based on its knowledge.

Function Calling Lifecycle
Define functions – List the functions the model can use.

Send a request – The user prompt and function definitions are included in the request.

Model processing – The model decides whether to respond directly or call a function.

LLM response – If needed, the model suggests a function call with the required arguments.

Execute function – The application runs the function and retrieves data or performs an action.

Send results back – The application sends the function output to the model, which incorporates it into its final response.

Why It Matters
Function calling allows AI models to interact with real-world systems, making them more dynamic and responsive. Whether fetching data, automating tasks, or handling complex workflows, this approach expands what AI can do beyond simple text generation.

Quiz Question
Which of the following statements correctly describe the role of function calling in enhancing AI model capabilities? Select all that apply.









## Demo: Defining and Calling Functions with OpenAI
Lesson
Cloud Resources


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Function Calling with OpenAI and a Memory Layer
Overview
This demo explores how to use function calling with OpenAI’s chat models while maintaining a memory layer. The system identifies when to use a tool (function), extracts arguments, executes the tool, and feeds the result back into the conversation, enabling a full loop of reasoning and tool use.

Key Steps Covered
1. Memory Class Recap and Enhancement
A custom Memory class is used to:
Add new messages.
Fetch all messages.
Fetch the last message.
Reset the memory.
class Memory:
  def __init__(self):
      self.messages = []

  def add_message(self, role, content, tool_calls=None, tool_call_id=None):
      message = {"role": role, "content": content}
      if tool_calls:
          message["tool_calls"] = tool_calls
      if tool_call_id:
          message["tool_call_id"] = tool_call_id
      self.messages.append(message)

  def get_messages(self):
      return self.messages

  def last_message(self):
      return self.messages[-1] if self.messages else None

  def reset(self):
      self.messages = []
2. Function Calling Preparation
A custom function power(base, exponent) is defined for exponentiation.
This function is wrapped in a JSON schema tool description so the model can learn about its existence and parameters.
def power(base: float, exponent: float) -> float:
  """Raise base to the power of exponent."""
  return base ** exponent

tools = [{
  "type": "function",
  "function": {
      "name": "power",
      "description": "Raise base to the power of exponent.",
      "parameters": {
          "type": "object",
          "properties": {
              "base": {"type": "number"},
              "exponent": {"type": "number"}
          },
          "required": ["base", "exponent"]
      }
  }
}]
3. Enhanced Chat Function
chat_with_tools is created to:
Accept user input and available tools.
Pass the tools and memory to the model.
Handle tool call outputs.
def chat_with_tools(user_message, tools, memory):
  memory.add_message("user", user_message)
  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=memory.get_messages(),
      tools=tools
  )
  ai_message = response.choices[0].message
  memory.add_message("assistant", ai_message.content, tool_calls=ai_message.tool_calls)
  return ai_message
4. Flow of Execution
The model receives a query like "2^-5".
Instead of responding directly, it outputs a tool call:
Function name: power
Arguments: base=2, exponent=-5
Developer extracts these arguments, executes the power function manually, and stores the result.
A new tool role message is added to the memory, linking it to the original tool call ID.
args = json.loads(tool_call.function.arguments)
result = power(**args)
memory.add_message("tool", str(result), tool_call_id=tool_call.id)
5. Final AI Response
After feeding back the tool’s result, the model is invoked again.
Now, the assistant produces a natural language response incorporating the tool’s output (e.g., "2 to the power of -5 is approximately 0.031").
6. Key Concepts Highlighted
The difference between standard responses and tool call behavior.
How function calling allows LLMs to extend their capabilities.
Importance of linking tool responses back via tool_call_id.
How memory tracks both user interactions and intermediate tool operations.
7. Conclusion
Function calling enables a much more structured and powerful interaction loop.
The memory structure supports complex multi-turn conversations that involve external tool use.
Proper handling of tool call and tool response messages is crucial for building advanced AI agents.

## Exercise: Tool Calling
Lesson
Cloud Resources
Welcome to the next evolution of AI Agents! In this exercise, you'll enhance your AI agent by adding tool-calling capabilities, allowing it to interact with external functions dynamically.

By equipping your agent with the ability to invoke external tools when needed, you unlock a new level of interactivity. Your AI can now fetch real-time data, run calculations, and interact with the outside world, making it much more powerful.

Scenario
Imagine you're building an AI-powered assistant that helps users with various tasks such as:

Fetching real-time stock prices

Performing complex calculations

Querying a weather API

Searching a database

Instead of manually deciding when to call which function, your AI agent will automatically detect when a tool is needed and invoke it.

Challenge
Your task is to:

Create a Tool class that acts as an abstraction for external functions.

Modify the Agent class to support dynamic tool calling.

Enable the AI agent to decide when it needs to use a tool.

At the end of this exercise, you'll have a working AI agent that can use external tools on its own!

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

## Exercise Solution: Tool Calling
Lesson
Cloud Resources


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Tool Calling with Agents
Overview
This exercise introduces the idea of equipping agents with the ability to call external tools (functions) based on user inputs. Learners build a system where an agent can detect when a tool should be used, invoke the tool, and incorporate the tool’s output into the final response.

Key Steps Covered
1. Setup and Recap
The OpenAI client is instantiated with environment variables.
A quick review of memory functionality is provided.
Chat-based interaction with tools is introduced.
2. First Tool: Power Function
A simple power(base, exponent) function is defined to calculate powers.
A corresponding tool schema in JSON format is manually created to describe the function's usage, input types, and required parameters.
def power(base: float, exponent: float) -> float:
  return base ** exponent

power_tool_schema = {
  "name": "power",
  "description": "Calculate base raised to the exponent.",
  "parameters": {
      "type": "object",
      "properties": {
          "base": {"type": "number"},
          "exponent": {"type": "number"}
      },
      "required": ["base", "exponent"]
  }
}
Memory is updated after tool use, storing both the tool call and the model’s final response.
3. Tool Abstraction Class
A new class is built to automatically generate a tool's JSON schema based on a function’s type hints and signature.
Key tasks included:
Extracting function name and description from dunder (__name__ and __doc__) properties.
Parsing type hints and parameter signatures.
Inferring JSON schema types (e.g., float → number, int → integer).
class Tool:
  def __init__(self, func):
      # Extract function details and create JSON schema
      pass

  def infer_json_schema_type(self, arg_type):
      # Map Python types to JSON schema types
      pass

  def call(self, **kwargs):
      return self.func(**kwargs)
The abstraction automatically outputs a full schema ready for OpenAI tool usage.
4. Updating the Agent Class
The Agent class is updated to accept a list of tools.
A tool map is built to quickly find and execute tools by name.
A call_tools() method is created to:
Detect if the model issued a tool call.
Execute the appropriate tool with the provided arguments.
Store the result back into the conversation memory.
def call_tools(self, tool_calls):
  for tool_call in tool_calls:
      tool_name = tool_call.function.name
      tool = self.tool_map.get(tool_name)
      if tool:
          args = json.loads(tool_call.function.arguments)
          result = tool.call(**args)
          self.memory.add_message(role="tool", content=str(result), name=tool_name)
5. Testing Tool Use
Non-tool query example: "What is 10 + 5?" → No tool used, answered directly by the model.

Tool query example: "What is two to the power three?" → Tool power is called, and the result (8) is inserted into the conversation.

Complex Query: "What is three to the power of two to the power of two?"

Model correctly sequences the operations and uses the tool.
Final result: 81.
6. Encouraged Exploration
Learners are challenged to create additional tools.
Suggestions include trying more complex mathematical operations or integrating external APIs.

## The ReAct Agent
Lesson
Cloud Resources

Planning with the ReAct Agent
Calling tools is useful, but some tasks require more than a single function call. When solving complex, multi-step tasks, an AI model must plan a sequence of actions. The ReAct paradigm (named for Reasoning + Acting) helps by combining reasoning and acting into a structured process.

How the ReAct Agent Works
The ReAct Agent enables AI models to both analyze a task and execute the necessary steps. This is useful for tasks requiring multiple decisions, such as booking a flight or troubleshooting an issue.

Components of ReAct
Reasoning
The model breaks the problem into smaller steps and determines the best approach.

Example: Understanding travel preferences, such as destination, dates, and budget.

Acting
The model performs actions using external tools or APIs.

Example: Searching for flights, comparing prices, and making a reservation.

How to Build a ReAct Agent
Run a loop of Thought → Action → Pause → Observation to guide the AI’s decision-making.
Provide tools the agent can use to complete actions (e.g., APIs for retrieving information).
Accept user queries as input to initialize the process.
Process each step by generating thoughts and actions in sequence.
Execute actions by calling the appropriate tool with generated parameters.
Observe results and continue looping until the task is completed or a condition is met.
Advantages
Improves reasoning and decision-making
Integrates well with external tools
Provides transparency in execution steps
Challenges
Depends heavily on well-structured input prompts and tools
Can be slow, requiring multiple steps and higher token usage
Final Thoughts
The ReAct Agent is a strong first approach for AI systems that require complex planning and execution. By combining reasoning and action, it allows models to solve tasks step-by-step while integrating with external tools. However, ensuring well-designed prompts and tools is essential for optimal performance.

References
ReAct: Synergizing Reasoning and Acting in Language Models(opens in a new tab)

Quiz Question
Which of the following best describes the primary function of the ReAct Agent in AI systems?









## Demo: Adding Planning Capabilities to Your Agent
Lesson
Cloud Resources


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: ReAct Agent with Planning and Tool Use
Overview
This demo introduces the construction of a ReAct-style agent using OpenAI models. The agent uses a planning loop where it reasons about the problem, chooses a tool (function) to act, and continues iterating until the task is complete. This method combines both thought and action steps.

Key Steps Covered
1. Environment and Base Classes
Required libraries are imported, environment variables are loaded, and the OpenAI client is instantiated.
Helper classes are prepared:
Memory class for tracking conversation history.
Tool class abstraction for wrapping Python functions with a JSON schema for tool calling.
2. Controlling the ReAct Loop
A custom exception StopReactLoopException is defined to gracefully exit the reasoning loop when a task is complete.
A special termination function and corresponding message are created so the LLM can explicitly choose to stop.
class StopReactLoopException(Exception):
  pass

def call_termination():
  raise StopReactLoopException("Terminating the ReAct loop.")
3. Agent Class Design
The Agent class manages the reasoning and tool execution steps:

Constructor parameters:
name
role
instructions
model
temperature
tools
Core components initialized:
Memory
Tool map and OpenAI tools
Termination handling
System message guiding the thought-action structure
class Agent:
  def __init__(self, name="agent", role="personal assistant", instructions=..., model=..., temperature=0.7, tools=[]):
      ...
Key methods:
invoke(): Entry point for user questions, starting the planning loop.
react_loop(): Main loop that alternates reasoning (plan generation) and action (tool use).
reason(): Creates a thought and selects an action without tools initially.
call_tools(): Executes a tool when the model specifies a tool call.
get_completion(): Wraps a standard call to the OpenAI chat model.
register_tool(): Adds user-defined tools into the agent’s toolkit.
4. Tool Creation
Two tools are created:
power(base, exponent): Calculates exponentiation.
sum_numbers(a, b): Sums two numbers.
These tools are wrapped with JSON schema metadata so the LLM understands their parameters.
def power(base: float, exponent: float) -> float:
  return base ** exponent

def sum_numbers(a: float, b: float) -> float:
  return a + b
5. Execution and Testing
An agent is instantiated with the created tools.

A user query is submitted:

"What’s 2^3 then add 10 to the result."
The agent follows this ReAct sequence:

Thought: Calculate 2^3.
Action: Calls the power tool (receives 8).
Thought: Add 10 to 8.
Action: Calls the sum tool (receives 18).
Thought: Task completed.
Action: Calls the termination function.
The final output: "The final result of 2^3 + 10 is 18."

Inspection of memory shows the detailed flow:

User question.
Agent's thought processes.
Tool calls and results.
Termination message.
6. Key Concepts Highlighted
Planning: The agent plans intermediate steps before acting.
Tool usage: Model identifies and executes tools based on task needs.
Iteration control: Loop safely terminates when a task is complete.
Memory maintenance: Each reasoning and action step is stored for full conversation traceability.
7. Conclusion
ReAct agents combine the model’s reasoning abilities with function execution.
The structure allows solving multi-step problems in a dynamic, interpretable way.
Proper use of memory, tool mapping, and controlled termination is crucial for building reliable ReAct systems.

## Multi-Agent Interaction
Lesson
Cloud Resources

Multi-Agent Collaboration in AI
AI agents can work together like a team of specialists, each with unique expertise and tools. By communicating, sharing information, and solving problems collaboratively, they enhance their collective capabilities. This approach allows agents to handle complex tasks more efficiently than a single agent could.

Key Components of a Multi-Agent System
Define Roles and Specializations – Assign each agent a role based on its expertise.

Communication and Information Sharing – Agents exchange data, results, and context to improve collaboration.

Collaborative Problem-Solving – Agents work together to achieve a goal.

Feedback and Iteration – Agents refine their approach over multiple interactions, improving the final outcome.

Workflow of a Multi-Agent System
Initiation – The process starts with a user request or event trigger.

Processing – Agents coordinate to solve the problem, either following a fixed flow or adapting dynamically.

Completion – The system compiles the final response and delivers results.

Applications of Multi-Agent Collaboration
Healthcare – One agent analyzes symptoms, another reviews medical history to suggest diagnoses.

Finance – Agents assess market trends, evaluate investments, and provide risk assessments.

Customer Support – A chatbot answers common questions, while another agent retrieves past interactions for personalized responses.

Challenges to Consider
Ensuring effective communication between agents.

Managing dependencies and maintaining consistency.

Designing complementary agent roles that align with overall goals.

Final Thoughts
Multi-agent collaboration enables AI systems to combine diverse expertise and tackle complex challenges efficiently. As AI evolves, this approach will be crucial for creating intelligent, adaptable systems across industries.

Quiz Question
Which of the following statements accurately describe components or characteristics of multi-agent collaboration in AI? Select all that apply.









## Demo: Making Agents to Interact with Each Other
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Multi-Agent Collaboration
Overview
This demo demonstrates how to set up and coordinate multiple agents within a single process using OpenAI's function calling and memory structures. Each agent specializes in a task (e.g., exponentiation, addition), and a supervising agent delegates subtasks by calling its peer agents through tool calls.

Key Steps Covered
1. Setup and Imports
Required libraries are imported, environment variables loaded, and the OpenAI client instantiated.
Supporting classes and components are reused:
Memory for conversation tracking
Tool abstraction to define functions
StopReactLoopException and call_termination() for stopping loops
2. New Tool: call_peer_agent
This tool enables one agent to invoke another.
Function is defined and wrapped with the required metadata for function calling.
def call_peer_agent(agent_name: str, message: str) -> str:
  # Allows one agent to delegate a task to another agent
3. Agent Class Enhancements
The Agent class is modified to support a list of peer agents.
When a peer agent is provided, the call_peer_agent function is automatically registered.
Peer agents are stored in a dictionary for easy access by name.
The call_tools() method is updated to:
Detect tool calls to call_peer_agent
Forward the delegated message to the appropriate agent
Capture and return the peer agent's response
if function_name == "call_peer_agent":
  peer_agent = self.peer_agents[tool_call.function.arguments["agent_name"]]
  response = peer_agent.invoke(tool_call.function.arguments["message"])
4. Defining Specialized Agents
Three agents are created:

exponentiation_agent:
Role: Handles exponentiation.
Tool: power(base, exponent)
summing_agent:
Role: Performs addition.
Tool: sum_numbers(a, b)
supervisor_agent:
Role: Delegates tasks.
Tools: Only call_peer_agent.
Peer agents: exponentiation_agent and summing_agent
5. Execution Flow
The supervisor agent receives the query: "What’s 2^3 then add 10 to the result?"

Execution trace:

Thought: I need to calculate 2^3.
Action: Call exponentiation_agent → result is 8.
Thought: I now need to add 10 to 8.
Action: Call summing_agent → result is 18.
Thought: Task complete.
Action: Call termination function.
Final response: "The final result of 2^3 + 10 is 18."

6. Inspecting Agent Memories
Each agent maintains its own memory.
supervisor_agent memory includes:
User question
Thoughts
Tool calls (to peer agents)
exponentiation_agent memory:
Instruction to compute 2^3
Result of 8
summing_agent memory:
Instruction to compute 8 + 10
Result of 18
peer_agent_map["exponentiation_agent"].memory.get_messages()
peer_agent_map["summing_agent"].memory.get_messages()
7. Conclusion
This demo showcases a simple but powerful pattern for multi-agent collaboration.
Agents can be modularized, with each handling a specific type of task.
Communication is enabled through a generic peer-calling mechanism.
The design is scalable and could support more complex task delegation in the future.

## The Role of Frameworks
Lesson
Cloud Resources

Accelerating AI Development with Frameworks
Building AI-driven applications from scratch is possible, but when working under tight deadlines with evolving requirements, frameworks help streamline development. They provide pre-built components, tools, and best practices, allowing developers to focus on innovation rather than repetitive setup.

Why Use Frameworks?
• Speeds up development by reducing boilerplate work.

• Provides structured components like memory, tools, and agents.

• Enhances scalability for building complex applications.

• Ensures best practices for integrating LLMs effectively.

Popular Agentic AI Frameworks
LangChain

Simplifies integrating LLMs into applications.
Supports memory, tools, and agent chaining for complex workflows.
Helps build sophisticated AI systems efficiently.
AutoGen (by Microsoft)

Treats workflows as conversations between agents.
Includes tools for code execution and function calling.
Highly customizable for defining custom workflows.
CrewAI

Designed for role-based multi-agent collaboration.
Supports autonomous task delegation between agents.
Ideal for research teams, collaborative AI, and team-based automation.
LangGraph

Graph-based approach for building stateful, multi-actor applications.
Provides fine-grained control over workflows with nodes representing specific tasks.
Useful for error recovery, advanced memory, and human-in-the-loop interactions.
PydanticAI

Built by the creators of Pydantic, widely used for data validation.
Enables type-safe AI agent composition using standard Python development practices.
Allows developers to build AI agents without relying on custom DSLs.
Final Thoughts
Frameworks accelerate AI development, making it easier to build scalable, maintainable applications. By leveraging these tools, developers can focus on solving real-world problems rather than handling low-level implementation details. Choosing the right framework ensures efficient, high-quality AI solutions in an ever-evolving landscape.

Quiz Question
What is one of the main benefits of using frameworks in AI development?









## Navigating Concerns with AI Agents
Lesson
Cloud Resources

Building Responsible AI Agents
Creating AI agents is exciting, but with great power comes important considerations. To build trustworthy and efficient AI solutions, it’s essential to focus on safety, cost, permissions, evaluation, and traceability.

Key Considerations
Safety and Reliability – AI agents must behave predictably and safely, just like a self-driving car must obey traffic rules. Regular testing and monitoring help prevent unexpected behavior.

Cost Management – Every AI request uses tokens, which can add up quickly. Optimizing prompts, caching frequent queries, and monitoring usage help control costs.

Permissions – AI agents need the right access to tools and data. Restricting permissions prevents unauthorized actions and enhances security.

Evaluation vs. Testing –

Evaluation measures overall performance and effectiveness.
Testing focuses on catching specific bugs and errors.
Both are necessary for ensuring high-quality AI behavior.
Traceability and Observability – Keeping logs of AI decisions and actions helps track what happened if something goes wrong. Observability tools provide insights for fine-tuning and debugging.

Final Thoughts
Beyond these technical aspects, ethical considerations, user privacy, and data security are just as important. By addressing these concerns, AI agents can be powerful, reliable, and responsible, ensuring they are both effective and safe to use.

Quiz Question
Which of the following considerations are essential for building responsible AI agents?











## 
