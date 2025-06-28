## Introduction to LangChain
Lesson
Cloud Resources

Introduction to LangChain
LangChain is a framework for building applications powered by large language models (LLMs). It simplifies LLM integration, making it easier to develop AI-driven solutions like chatbots, retrieval-augmented generation (RAG) systems, document summarization tools, and autonomous agents.

Why Use LangChain?
LangChain provides abstractions that connect LLMs with various tools, including:

Cloud storage services for managing data.
Web scraping tools for fetching real-time information.
Vector databases for efficient search and retrieval.
This flexibility allows developers to focus on building AI solutions rather than handling complex integrations.

Core Components
LangChain supports multiple programming languages, including Python, JavaScript, and TypeScript. This lesson focuses on the Python libraries.

Models
LangChain supports multiple LLM providers, such as OpenAI and Anthropic.
Uses lightweight integration packages like langchain-openai or langchain-anthropic.
Simplifies model interaction with the invoke() method, handling messages efficiently.
Messages
LangChain standardizes communication with models through message objects:

HumanMessage – Represents user input.
AIMessage – Represents model responses.
SystemMessage – Provides additional instructions.
ToolMessage – Used for function calling.
Example:

llm.invoke([HumanMessage(content="What’s the capital of Brazil?")])
For convenience, LangChain automatically converts text inputs into the correct format.

Final Thoughts
LangChain provides a powerful and flexible foundation for LLM-based applications. Its structured approach simplifies model interactions, message handling, and system integration, allowing developers to build AI solutions efficiently. Understanding LLMs, messages, and workflows is key to making the most of LangChain’s capabilities.

Quiz Question
What is the primary purpose of LangChain as a framework in the development of AI-driven applications?









## # Chat History and Prompt Templates

LessonCloud Resources


## Building Stateful Interactions with LLMs

LLMs are **stateless**, meaning they **do not remember previous interactions** unless past messages are explicitly provided. To build **cohesive conversations**, applications must manage **chat history** and supply relevant context with each request.

### Structure of a Conversation

A conversation typically consists of three key message types:

**SystemMessage** – Sets the context for the interaction.

`SystemMessage("You are a geography tutor")`

**HumanMessage** – Represents user input.

`HumanMessage("What's the capital of Brazil?")`

**AIMessage** – Represents the model’s response.

**ToolMessage** – Requests a tool invocation (for agent-based workflows).

A conversation is structured as a **list of messages**, which is then passed to the model.

`messages = [          SystemMessage("You are a geography tutor"),         HumanMessage("What's the capital of Brazil?") ]   llm.invoke(messages)`

### Few-Shot Prompting for Better Responses

By **programmatically structuring chat history**, developers can create **examples of ideal interactions**, guiding the model toward better responses.

This technique, called **few-shot prompting**, improves performance by providing **examples of desired behavior**.

- More examples **enhance response quality**.
- Larger prompts **increase costs and latency**.

To manage these trade-offs, **LangChain provides the FewShotPromptTemplate**, but first, understanding **prompt templates** is essential.

### Prompt Templates

`prompt_template = PromptTemplate(template="Tell me a joke about {topic}") llm.invoke(prompt_template.format(topic="Java"))`

**ChatPromptTemplates** – Define prompts for structured conversations.

`template = ChatPromptTemplate([         ("system", "You are a helpful AI bot. Your name is {name}."),         ("human", "Hello, how are you doing?"),         ("ai", "I'm doing well, thanks!"),         ("human", "{user_input}"), ])`

**Few-Shot Prompt Templates** – Provide examples for better guidance.

`template = FewShotPromptTemplate(         examples=examples,         example_prompt=example_prompt,         suffix="Question: {input}",         input_variables=["input"], )`

**Final Thoughts**

By managing **chat history, structuring prompts, and leveraging few-shot learning**, developers can build **ChatGPT-like applications** with **better responses and task-specific optimizations**. These tools provide the foundation for **more powerful and interactive AI applications**.

### Quiz Question

What is one key advantage of using Few-Shot Prompt Templates in LangChain when building LLM-based applications?

They significantly reduce the cost and latency of model responses.

They allow the model to remember previous interactions without providing past messages.

They provide examples of ideal interactions, guiding the model toward better responses.

They automatically generate a list of all possible questions a user might ask.

Submit

## Demo: LangChain 101
Lesson
Cloud Resources


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: LangChain 101 – Basic Concepts and Prompting
Overview
This demo introduces fundamental concepts in LangChain, focusing on how to interact with chat models, structure messages, and use prompt templates for zero-shot and few-shot prompting. It’s a beginner-friendly overview of key abstractions used throughout LangChain workflows.

Key Steps Covered
1. Chat Model Initialization
The OpenAI chat model (ChatOpenAI) is instantiated.
Environment variables are loaded to securely pass the API key.
Temperature settings can be configured to adjust response creativity.
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
response = llm.invoke("Hello there.")
2. Message Structuring
LangChain supports structured message inputs including:
SystemMessage: Sets the assistant’s behavior.
HumanMessage: Represents user input.
AIMessage: Includes prior assistant responses.
messages = [
  SystemMessage(content="You are a helpful assistant."),
  HumanMessage(content="What's the capital of Brazil?"),
  AIMessage(content="The capital of Brazil is Brasília."),
  HumanMessage(content="What's the capital of Canada?")
]

response = llm.invoke(messages)
Including previous assistant responses helps with few-shot learning, as it teaches the LLM how to respond in context.
3. Prompt Templates
LangChain offers two styles of templated prompting:

a. Basic PromptTemplate
Defines a single-variable input prompt with a placeholder.
prompt = PromptTemplate(
  input_variables=["topic"],
  template="Tell me a joke about {topic}"
)
The prompt can be formatted using .format() or .invoke():
formatted_prompt = prompt.format(topic="Python")
llm.invoke(prompt.invoke({"topic": "Python"}))
b. Few-Shot PromptTemplate
Combines multiple structured examples to guide the LLM’s reasoning.
Components:
examples: List of example dictionaries (input → thought → output).
example_prompt: A PromptTemplate defining the format for each example.
suffix: The actual question for the current prompt.
examples = [
  {"input": "A train leaves City A...", "thought": "...", "output": "2 hours"},
  {"input": "A store applies a 20% discount...", "thought": "...", "output": "..."},
  ...
]

example_prompt = PromptTemplate(
  input_variables=["input", "thought", "output"],
  template="Question: {input}\nThought: {thought}\nResponse: {output}"
)

few_shot_prompt = FewShotPromptTemplate(
  examples=examples,
  example_prompt=example_prompt,
  suffix="Question: {input}",
  input_variables=["input"]
)

llm.invoke(few_shot_prompt.invoke({"input": "If today is Wednesday, what day will it be in 10 days?"}))
The result shows the model following the reasoning steps provided in the examples and outputting: "Saturday."
4. Takeaways
Prompt engineering in LangChain is modular and powerful.
Structured messages and few-shot examples significantly improve LLM response quality.
PromptTemplates enable consistent formatting and reusability.

## Exercise: Create a Chatbot Application
Lesson
Cloud Resources
Welcome to your Chatbot Building Exercise! In this challenge, you’ll create a chatbot that remembers past interactions, follows a structured conversation flow, and provides more human-like responses using Few-Shot Prompting.

By leveraging memory, structured prompts, and few-shot examples, your chatbot will behave in a consistent and engaging manner.

Scenario
You're developing a virtual assistant for a company. Your chatbot needs to:

Maintain conversation history.

Respond consistently using predefined few-shot examples.

Be customizable for different roles, such as:

A robotic assistant with a sci-fi tone.

A casual chatbot for fun interactions.

A professional AI assistant for business tasks.

At the end of this exercise, you’ll have a fully functional chatbot that can chat dynamically while following a predefined personality.

Challenge
Your chatbot must:

Track conversation history.

Use a structured Few-Shot Prompting approach.

Allow customization of tone and personality.

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.


## Exercise Solution: Create a Chatbot Application
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Chatbot Application with LangChain
Overview
This exercise walks through the creation of a simple chatbot using LangChain. The focus is on structuring the chatbot class to support memory, managing message formatting via LangChain message objects, and using prompt templates to enable contextual, character-driven interactions.

Key Steps Covered
1. Setup and Imports
Required libraries are imported, including LangChain modules.
Environment variables are loaded to securely manage the OpenAI API key.
2. Chatbot Class Construction
A chatbot class is created with an internal memory (self.messages), which stores a list of messages exchanged during the conversation.
The OpenAI chat model is instantiated using LangChain's ChatOpenAI, without explicitly passing the API key thanks to environment configuration.
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage

self.llm = ChatOpenAI()
self.messages = []
3. Implementing the invoke Method
The method accepts user input, wraps it in a HumanMessage, appends it to the message list, and invokes the model with the full conversation history.
The model's response is wrapped in an AIMessage and also appended to memory.
The AI response is returned at the end.
def invoke(self, user_input):
  human_msg = HumanMessage(content=user_input)
  self.messages.append(human_msg)

  ai_msg = self.llm(self.messages)
  self.messages.append(ai_msg)

  return ai_msg.content
4. Prompt Template and Message Formatting
The prompt uses LangChain’s PromptTemplate with a structure that includes system instructions, human input, and AI output. This template manages consistent formatting for few-shot examples.

Sample message flow includes:

System message defining personality and role.
Human messages as input.
AI messages as example responses.
5. Creating and Interacting with the Chatbot
A bot named BEEP-42 is created, initialized with humorous and thematic system instructions.

A series of example interactions are seeded, such as:

"Hello, what is 2+2?"
"Can you dream?"
"Why did the robot go to therapy?"
Memory is inspected to confirm the full conversation history is stored correctly with role-based message types.

6. Sample Invocation
The bot is queried with a playful sequence of questions:
"HAL, is that you?" → Responds it's not HAL.
"RedQueen from The Terminator?" → Clarifies different protocols.
"Wall-E?" → Confirms it's not Wall-E.
"What's the answer for every question?" → Replies: "Answer 42."
7. Next Steps
Learners are encouraged to experiment further by:
Adjusting the temperature to influence creativity.
Modifying the bot’s personality.
Expanding the set of few-shot examples for better grounding.

## Streaming
Lesson
Cloud Resources

Streaming in Generative AI Applications
Streaming enables faster and smoother user experiences in entertainment platforms like Spotify and Netflix, where content plays immediately while additional data is loaded in the background. The same concept applies to Generative AI applications, ensuring low-latency, real-time interactions.

Why Streaming Matters in AI Applications
• Without streaming, users must wait for the full response to generate, causing delays.

• With streaming, output is displayed progressively, reducing perceived latency and improving responsiveness.

• Example: ChatGPT streams text word by word, making interactions feel fluid and natural.

Streaming in LangChain
LangChain provides built-in streaming support through the Runnable Interface, allowing developers to process responses as they are generated.

• stream() – Synchronous streaming, suitable for real-time processing.

• astream() – Asynchronous streaming, designed for non-blocking workflows.

Using stream() for Real-Time Processing
for chunk in component.stream(some_input):
        print(chunk)  # Processes each chunk as it's produced
• Enhances chat applications by displaying responses progressively.

• Allows interruption if the user no longer needs the full response.

• Requires efficient processing to avoid delays between chunks.

Using astream() for Asynchronous Streaming
Works similarly but is optimized for async applications, ensuring smooth, non-blocking execution.

Final Thoughts
Streaming significantly improves user experience by making LLM applications more responsive. Whether building chatbots, virtual assistants, or interactive AI tools, streaming ensures seamless real-time interactions.

Quiz Question
What is a key benefit of using streaming in Generative AI applications?









## Demo: Streaming
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Streaming Responses in LangChain
Overview
This demo introduces streaming capabilities in LangChain. Instead of waiting for the full response from the model, the output is streamed token-by-token or chunk-by-chunk. This approach enables real-time feedback, partial result handling, and dynamic response processing.

Key Steps Covered
1. Initial Setup
Necessary libraries are imported and environment variables loaded.
The OpenAI chat model (ChatOpenAI) is instantiated as the LLM.
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
Standard use with .invoke() is demonstrated:
Sends the full prompt and waits for the complete response.
2. Streaming Basics
Streaming is enabled by using .stream() instead of .invoke().
Responses are received incrementally as chunks.
chunks = []
for chunk in llm.stream("What does FIFA stand for?"):
  chunks.append(chunk)
  print(chunk.content, end="")
Output begins immediately instead of waiting for full completion.
Each chunk is an AIMessageChunk with content and additional metadata.
3. Working with Chunks
Chunks can be processed individually:
Slicing chunks (e.g., first 5 chunks) to form partial outputs.
Concatenating chunks to recreate the full final output.
complete_output = "".join(chunk.content for chunk in chunks)
4. Handling Interruptions
It is possible to interrupt a streaming response.
A KeyboardInterrupt is caught to gracefully stop streaming.
If interruption handling is disabled, the raw exception is displayed.
try:
  for chunk in llm.stream("Question..."):
      print(chunk.content, end="")
except KeyboardInterrupt:
  print("Interrupted!")
5. Resuming After Interruptions
A simple play() and resume() mechanism is demonstrated:
play() appends streamed chunks to memory.
resume() prompts the model to complete a previously interrupted response.
```
def play():
  # Streams response and stores in memory

def resume():
  # Resumes based on memory if output seems incomplete
If the model believes the prior output is unfinished, it continues the answer.
6. On-the-Fly Processing
Words are counted dynamically during streaming.
Each new word token can trigger updates or calculations.
word_count = 0
for chunk in llm.stream("Prompt..."):
  word_count += len(chunk.content.split())
```

This shows how streaming enables real-time processing and metric calculation.
7. Event Handling
Events are emitted during streaming:
on_chat_model_start
on_chat_model_stream
on_chat_model_end
Listeners can be attached to these events to trigger additional actions.
Example:
After on_chat_model_end, a different process could be initiated.
8. Using Streaming in a Chatbot
The BEEP-42 chatbot is re-created with streaming enabled.
It now outputs text progressively during a conversation, creating a more interactive user experience.
bot = Chatbot(name="BEEP-42", instructions="...", examples=[...])
response = bot.ask("Tell me a joke.")
9. Conclusion
Streaming offers faster, more interactive, and more flexible user experiences.
Processing data as it arrives enables more sophisticated applications like real-time dashboards, live feedback systems, or conversational agents.

## Demo: Schemas and Output Parsers
Lesson
Cloud Resources


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Structured Output Parsing with LangChain
Overview
This demo focuses on how to parse and structure outputs from LLMs using LangChain's output parsers, including strategies for handling structured text like dictionaries, booleans, datetimes, and using Pydantic models for robustness. It also covers how to fix parsing errors automatically when the LLM output is misformatted.

Key Steps Covered
1. Basic String Parsing
By default, calling .invoke() on an LLM returns an AIMessage object.
To extract the raw text, access ai_message.content.
response = llm.invoke("Hello there.")
raw_text = response.content
Alternatively, a StrOutputParser can be used to transform the output cleanly.
parser = StrOutputParser()
text = parser.invoke(response)
2. Datetime Parsing
A DatetimeOutputParser is used when you need to convert LLM output into a Python datetime object.
The LLM is prompted to produce a date in a specific format.
parser = DatetimeOutputParser()
datetime_obj = parser.invoke(response)
3. Boolean Parsing
A BooleanOutputParser converts "yes" or "no" responses into Python True or False.
Example:
Content: "yes" → True
Content: "no" → False
parser = BooleanOutputParser()
result = parser.invoke(AIMessage(content="yes"))
4. TypedDict Parsing
LangChain supports using TypedDict to define the structure of expected output.
class UserInfo(TypedDict):
  name: str
  country: str
Using with_structured_output(UserInfo), the model is guided to format its response accordingly.
Examples:
Input: "My name is Henrique and I am from Brazil." → { "name": "Henrique", "country": "Brazil" }
If no relevant info is found, defaults are used.
5. Pydantic Parsing
For more robust parsing and validation, Pydantic models are used.
class UserInfo(BaseModel):
  name: str
  country: str
Pydantic models provide automatic type checking and better error handling.
parsed = llm.with_structured_output(UserInfo).invoke("My name is Washington and I am from Australia.")
If the LLM output is properly structured, parsing succeeds.
If missing information, fields default to empty strings or None, based on model configuration.
6. Parsing Complex Structures
A more complex example is parsing a list of films (filmography) for an actor using a Pydantic model.
class Performer(BaseModel):
  name: str
  film_names: List[str]
Asking for "Scarlett Johansson filmography" returns the correct structured object with movie names.
7. Handling Parsing Errors
Sometimes the LLM outputs poorly formatted JSON or semi-structured text.
If parsing fails (e.g., bad quotes, wrong format), an OutputParserException is raised.
try:
  parser.invoke(bad_output)
except OutputParserException as e:
  print("Parsing error caught!")
8. Fixing Misformatted Outputs Automatically
LangChain provides an OutputFixingParser.
This parser:
Detects format errors.
Attempts to reformat the output using the LLM itself.
fixing_parser = OutputFixingParser.from_llm(parser, llm)
corrected_output = fixing_parser.invoke(misformatted_output)
This enables parsing even from imperfect LLM outputs, making workflows much more reliable.
9. Conclusion
Structured output parsing transforms unstructured LLM responses into reliable Python objects.
TypedDicts and Pydantic models improve structure and validation.
Parsers combined with automatic fixing allow workflows to handle imperfect LLM behavior gracefully.

## Multi-Step Workflows
Lesson
Cloud Resources

The Evolution from Chains to Runnables in LangChain
LangChain originally introduced Chains, which allowed developers to build sequential workflows by passing outputs from one step as inputs to the next. Over time, these legacy Chain classes have been deprecated in favor of more flexible and powerful approaches:

LCEL (LangChain Expression Language) – A declarative way to compose AI workflows.
LangGraph – A framework for agentic workflows with complex state management.
Runnables: The New Standard
The Runnable interface is now the core building block of LangChain. It standardizes how components—such as LLMs, output parsers, retrievers, and agent workflows—are executed and composed.

What Can Runnables Do?

Invoke – Process a single input into an output.
Batch – Handle multiple inputs at once.
Stream – Output data in chunks for real-time processing.
Inspect – Access input, output, and configuration details.
Compose – Chain multiple Runnables together for complex workflows.
Example of invoking a Runnable with custom configuration:

some_runnable.invoke(
        some_input, 
        config={
            'run_name': 'my_run', 
            'tags': ['tag1', 'tag2'], 
            'metadata': {'key': 'value'}   
        }
)
LCEL: The Declarative Approach to Chains
LCEL (LangChain Expression Language) enables composing Runnables efficiently using a syntax similar to Linux pipes:

chain = prompt | llm | output_parser
Instead of manually managing execution, LCEL automatically optimizes the workflow, making it easier to build scalable AI applications.

Final Thoughts
The shift from legacy Chains to Runnables and LCEL provides greater flexibility, efficiency, and composability. Developers can now build complex AI pipelines with less boilerplate code, focusing on defining workflows rather than managing execution.

Quiz Question
What is the primary benefit of using LCEL (LangChain Expression Language) in LangChain workflows?









## Demo: LCEL
Lesson
Cloud Resources


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Chaining Executions and LCEL (LangChain Expression Language)
Overview
This demo explores chaining multiple LangChain components into structured workflows, culminating in the use of LCEL (LangChain Expression Language) for more concise and flexible chain creation. Learners see how to manually connect prompt templates, LLMs, and parsers into execution sequences and how to inspect and customize these executions.

Key Steps Covered
1. Foundations: Recap of Key Objects
Core components revisited:
PromptTemplate: Formats input.
ChatOpenAI (LLM): Generates AI messages.
StrOutputParser: Converts AI messages into strings.
Manual chaining:
Prompt is filled with input (e.g., topic: Python).
LLM generates a joke about the topic.
Parser extracts the response as a string.
prompt.invoke({"topic": "Python"})
llm.invoke(prompt_output)
parser.invoke(llm_output)
2. Understanding Runnables
Each component is a runnable, meaning it supports:
invoke()
batch()
stream()
Runnables also provide introspection:
input_schema, output_schema, and config_schema for validation and structure understanding.
print(runnable.input_schema)
print(runnable.output_schema)
Configuration (config) can be passed during invocation to set metadata like run names and tags.
llm.invoke(input, config={"run_name": "demo_run", "tags": ["demo", "lcel"]})
3. Building Chains Manually
A RunnableSequence is introduced to combine multiple runnables.
Outputs are automatically passed to the next runnable.
Example:
Prompt → LLM → Parser, wrapped as a single chain.
chain = RunnableSequence(first=prompt, middle=llm, last=parser)
result = chain.invoke({"topic": "Python"})
Batch execution is supported: multiple topics can be processed at once.
results = chain.batch([{"topic": "Python"}, {"topic": "Football"}])
Diagrams show the step-by-step data flow inside chains.
4. Advanced Chain Construction
Custom Functions as Runnables:
Simple Python functions (like doubling or tripling numbers) are wrapped in runnable form.
double = RunnableLambda(lambda x: x * 2)
triple = RunnableLambda(lambda x: x * 3)
Parallel Execution:
RunnableParallel runs multiple runnables simultaneously on the same input.
parallel_chain = RunnableParallel(double=double, triple=triple)
result = parallel_chain.invoke(3)

Output: {"double": 6, "triple": 9}
5. Introduction to LCEL (LangChain Expression Language)
LCEL introduces a pipe (|) syntax to build chains more concisely.
Same chain as before, but constructed with just:
chain = prompt | llm | parser
This is functionally identical to manually creating a RunnableSequence.
LCEL enhances readability and composability of chains.
6. Summary of Features
Single and batched invocation.
Streaming support built into runnables.
Chain visualization through diagrams.
Parallel execution for more complex workflows.
LCEL for clean, expressive pipeline construction.
7. Conclusion
LangChain’s chaining system is flexible and composable.
LCEL simplifies construction and visualization of multi-step pipelines.
Streaming, parallelism, and structured outputs open the door for building robust AI-driven systems.

## Exercise: Multi-Step Workflows
Lesson
Cloud Resources
Welcome to your next challenge in mastering LangChain’s Language Chain Expression Language (LCEL)! 🎯

In this exercise, you’ll build a multi-step workflow using LCEL to solve a more complex task than simply generating a joke. We’ll walk through the entire process, from planning a task, to using multiple prompts and chaining steps together.

By the end of this exercise, you’ll have built a workflow that generates a business idea, analyzes it, and presents the results in a structured, easy-to-understand format.

Scenario
You’ve been hired by a startup incubator to build an AI-powered assistant that helps aspiring entrepreneurs brainstorm business ideas, evaluate their potential, and summarize key insights.

Challenge
Create an AI Business Advisor that:

Accepts an industry as input.

Generates a business idea.

Analyzes the strengths and weaknesses.

Formats the results as a final report.

Use LangChain LCEL to chain prompts, LLMs, and output parsers.

## Exercise Solution: Multi-Step Workflows
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Multi-Step Workflow with LCEL
Overview
This exercise demonstrates how to build a more complex, multi-step workflow using the LangChain Expression Language (LCEL). The project involves generating business ideas, analyzing them for strengths and weaknesses, and producing a structured business report, all through interconnected chains.

Key Steps Covered
1. Initial Setup
All necessary imports and environment configurations are completed.
LCEL components such as RunnableParallel, pipe, and message parsing utilities are ready for use.
2. Idea Generation Chain
A prompt template is created to generate a business idea based on a given industry.
The chain uses:
The idea prompt
A language model (llm)
An output parser to structure the result
idea_chain = idea_prompt | llm | parse
Invoking the chain with an example input like "agro" produces an innovative business idea and a brief description.
3. Business Idea Analysis Chain
A second prompt template is created to analyze the generated business idea.

The analysis prompt asks for:

Three key strengths
Three potential weaknesses
This chain follows the same structure: prompt → model → parser.

analysis_chain = analysis_prompt | llm | parse
The output lists the strengths and weaknesses of the business idea clearly.
4. Business Report Generation Chain
A structured prompt and Pydantic model are used to create a business report from the analysis.
The report uses function calling to ensure structured output:
A Report class is defined with strengths and weaknesses fields.
class Report(BaseModel):
  strengths: List[str]
  weaknesses: List[str]
The report chain builds a structured final report from the analysis results.
report_chain = report_prompt | llm.with_structured_output(Report)
5. Building the End-to-End Workflow
An overall end-to-end chain combines:

idea_chain
analysis_chain
report_chain
This composite chain takes an industry input and produces a complete, structured business report in one invocation.

end_to_end_chain = idea_chain | analysis_chain | report_chain
Testing the full chain with "agro" yields:
An innovative idea
An analysis
A final structured report
6. Encouraged Exploration
Learners are encouraged to:
Add memory modules to track multiple interactions.
Explore additional runnables to expand the workflow.
Integrate even more complex processing steps or refine output formatting.

## RAG Pipelines
Lesson
Cloud Resources

Introduction to Retrieval-Augmented Generation (RAG)
Retrieval-Augmented Generation (RAG) enhances language models by providing external context from a retrieval system before generating responses. This approach improves accuracy and reduces hallucinations by grounding responses in relevant information.

How RAG Works
RAG pipelines consist of three main components:

Retrieval – Searches a database or document corpus to find relevant information. Uses vector search or keyword matching.

Augmentation – Combines retrieved documents with the user’s query in a structured prompt.

Generation – The LLM generates a response using both the query and retrieved context.

Building a RAG Pipeline
A RAG system requires both an offline indexing phase and an online retrieval phase.

Indexing (Offline Phase)
Before retrieval can happen, documents must be processed and stored efficiently:

Document Loaders – Extract raw data from files, APIs, or databases.
Text Splitters – Divide large documents into smaller, searchable chunks.
VectorStore & Embeddings – Convert text into vector representations and store them for fast retrieval.
Retrieval & Augmented Generation (Online Phase)
When a user submits a query, the system:

Searches the VectorStore for relevant document chunks.

Incorporates retrieved text into a structured prompt.

Generates an informed response using the LLM.

Applications of RAG
Customer Support – AI chatbots retrieve relevant FAQ responses.
Content Creation – AI-assisted writing tools generate fact-based content.
Research & Knowledge Management – Quickly synthesize insights from large datasets.
Design Considerations
Ensure retrieval quality – Poorly selected documents lead to irrelevant outputs.
Optimize text chunking – Too small, and key details get lost; too large, and retrieval suffers.
Manage LLM context limits – Retrieved text must fit within the model’s processing window.
Final Thoughts
RAG significantly improves the accuracy, efficiency, and trustworthiness of AI-generated content. By combining retrieval systems with generative models, applications can deliver more precise and context-aware responses.

Quiz Question
Which of the following activities takes place during the online phase of a RAG pipeline?









## Demo: RAG Pipelines
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Retrieval-Augmented Generation (RAG) Pipeline in LangChain
Overview
This demo introduces the fundamentals of building a RAG (Retrieval-Augmented Generation) pipeline using LangChain. The approach enriches an LLM’s knowledge by retrieving external documents relevant to the user's question and passing that context along with the query to the model.

Key Steps Covered
1. Setting the Stage: Defining the Data Source
Wikipedia is used as the external knowledge source.
A search query retrieves a document about Anthony Hopkins.
Only one document is retrieved initially, containing a significant amount of text.
docs = wikipedia_search("Anthony Hopkins")
2. Splitting Documents into Chunks
Large documents are split into smaller segments using a text splitter.
Smaller chunks improve retrieval accuracy by narrowing the search space.
split_docs = text_splitter.split_documents(docs)
Example: One document is split into 182 sub-documents.
3. Embedding and Storing Chunks
Each document chunk is converted into a vector embedding using OpenAI Embeddings.
All embeddings are stored in an in-memory vector store.
vectorstore.add_documents(split_docs)
This allows for fast similarity searches when a user query arrives.
4. Retriever Setup
A retriever is created from the vector store.
The retriever fetches the top k=3 most relevant documents based on similarity to the user query.
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
5. Prompt Template Creation
A chat prompt template is defined to guide the LLM:
It receives both the context (retrieved documents) and the question.
The model is instructed to reason based only on provided context.
prompt = ChatPromptTemplate.from_messages([
  ("system", "You are an assistant for question answering."),
  ("human", "Use the following context: {context}\nQuestion: {question}\nAnswer:")
])
The template is a runnable object, so it can be invoked directly.
6. Generation Pipeline
The complete flow:
Format the retrieved documents into a single string for the context.
Fill the prompt template with the question and context.
Pass the resulting messages to the LLM.
Retrieve the final answer.
context = format_docs(docs)
messages = prompt.invoke({"context": context, "question": "When was The Silence of the Lambs released?"})
answer = llm.invoke(messages)
Example output: "The Silence of the Lambs was released in 1991."
7. Alternative: LCEL Version
The RAG flow is also implemented using LCEL (LangChain Expression Language) for a more concise pipeline:
Parallel retrieval of context and question.
Formatting the final prompt.
LLM invocation.
rag_chain = (
  {"context": retriever | format_docs, "question": RunnablePassthrough()}
  | prompt
  | llm
)
Example question: "When was Anthony Hopkins born?"
Correct answer: "December 31, 1937."
8. Key Concepts Reinforced
Augmenting LLMs with external knowledge improves factual accuracy.
Chaining retrieval, prompt construction, and generation creates flexible, reusable workflows.
LCEL simplifies the construction of complex pipelines with minimal code.
9. Conclusion
RAG pipelines enhance LLM outputs by grounding them in verified external documents.
Document splitting, retrieval tuning, and structured prompting are critical for high-quality RAG systems.

## Functions and Tools
Lesson
Cloud Resources

Encapsulating Functions as Tools in LangChain
LangChain tools allow developers to encapsulate Python functions with a schema, making them available for AI-driven function calls. This enables models to extend their capabilities by invoking external functions when needed.

Creating Tools with the @tool Decorator
LangChain simplifies tool creation with the @tool decorator, which automatically infers function names, descriptions, and expected arguments from the function’s definition.

@tool
def power(base: int, exponent: int) -> int:
    """Exponentiation: base a to the power e"""
    return base ** exponent
Using and Inspecting Tools
Once defined, a tool can be invoked using the invoke() method.

power.invoke({"base": 3, "exponent": 2})  # Returns: 9
Tools can also be inspected to retrieve their description and argument schema.

Binding Tools to Models
Tools can be attached to chat models, allowing AI systems to dynamically decide when to use them.

model_with_tools = model.bind_tools([power])
How AI Decides When to Use Tools
The model does not always use tools—it decides based on input relevance.

If a question is general, the model responds directly:

model_with_tools.invoke("What is Udacity?")
If the model knows the answer from training, it may respond without tool invocation:

model_with_tools.invoke("What is 2 multiplied by 3?")
If the model requires external computation, it calls the appropriate tool:

ai_message = model_with_tools.invoke("What is 2 to the power 3?")
Executing Tool Calls
If the model chooses to call a tool, the response will include a tool_calls attribute:

print(ai_message.tool_calls)
[{'name': 'power', 'args': {'base': 2, 'exponent': 3}, 'id': 'call_abc123', 'type': 'tool_call'}]
The function must still be executed manually:

tool_message = power.invoke(ai_message.tool_calls[0])
If multiple tools are bound, iterate over tool_calls to execute each one.

Passing Tool Outputs Back to the Model
After execution, the ToolMessage object must be added to the conversation history:

messages.append(tool_message)
Then, invoke the model again with the updated messages list to generate a final response:

llm_with_tools.invoke(messages)
Final Thoughts
Encapsulating functions as tools allows LLMs to interact with external systems, enabling more complex and dynamic AI applications. By binding, invoking, and passing tool outputs, AI models can perform real-time computations and external API interactions, greatly expanding their usefulness.

Quiz Question
In LangChain, what is the purpose of encapsulating functions as tools using the @tool decorator?









## Demo: Functions and Tools
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Using Tools with LangChain
Overview
This demo shows how to create and integrate tools into LangChain workflows. Tools allow the LLM to delegate specific tasks to external functions by invoking them during the conversation, enabling a powerful method for function calling within AI applications.

Key Steps Covered
1. Tool Creation
Tools are simple Python functions decorated with @tool.
A good description must be provided so the LLM can understand when to call it.
@tool("multiply")
def multiply(x: int, y: int) -> int:
  """Multiply two numbers together."""
  return x * y
The tool is registered into a tools list and a tool map for easy lookup by name.
tools = [multiply]
tool_map = {tool.name: tool for tool in tools}
2. Binding Tools to an LLM
Tools are bound to the LLM using bind_tools().
llm_with_tools = llm.bind_tools(tools)
This makes the LLM aware that it can call tools during a conversation if needed.
3. Invoking with Tools
A typical message list includes:
A SystemMessage setting the assistant's behavior.
A HumanMessage containing the user query (e.g., "What is 3 multiplied by 2?").
messages = [
  SystemMessage(content="You are a helpful assistant."),
  HumanMessage(content="What is 3 multiplied by 2?")
]
Invoking the LLM:
If the LLM identifies a tool to call, it produces tool_calls instead of a direct text response.
Otherwise, it produces regular content.
response = llm_with_tools.invoke(messages)
Example:
"How are you?" → Direct response, no tool_calls.
"What is 3 multiplied by 2?" → Empty content + tool_calls for the multiply function.
4. Handling Tool Calls Programmatically
Tool calls must be handled by the developer:
Parse tool_calls from the LLM response using LangChain utilities.
Extract the function name, arguments, and call ID.
Execute the corresponding tool using the arguments.
parsed_calls = parse_tool_calls(response.additional_kwargs["tool_calls"])
tool_call = parsed_calls[0]
function_name = tool_call["name"]
args = tool_call["args"]

tool = tool_map[function_name]
result = tool.invoke(**args)
After executing the tool:
A ToolMessage is created with the result, linking it back to the original tool_call ID.
tool_message = ToolMessage(content=str(result), tool_call_id=tool_call["id"])
messages.append(tool_message)
5. Sending the Result Back to the LLM
After the tool result is appended to the messages list:
A second invocation sends the updated conversation to the LLM.
The LLM then generates a final, natural language response incorporating the tool result.
final_response = llm_with_tools.invoke(messages)
Example final output: "3 multiplied by 2 is 6."
6. Summary of the Flow
Human asks a question.
LLM identifies if a tool is needed.
Tool is called manually by the application.
Tool output is fed back to the LLM.
LLM produces a complete answer.
7. Conclusion
Tools in LangChain enable structured, reliable, and expandable interaction patterns.
Developers must manage tool execution and message flow carefully.
This method paves the way for building powerful agentic systems that combine LLM reasoning with external capabilities.

## Demo: Simple Agentic Workflows
Lesson
Cloud Resources

Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Building a Basic Agent Abstraction in LangChain
Overview
This demo shows how to create a lightweight agent abstraction that layers together LLMs, memory, and tool use. The goal is to allow seamless handling of user inputs, tool calls, and model responses without having to manually orchestrate every piece at each step.

Key Steps Covered
1. Initial Setup
Standard imports and environment loading.
OpenAI chat model is instantiated as the LLM.
Tools are defined and organized:
A simple multiply tool is created.
A tool map is built for easy lookup by tool name.
@tool("multiply")
def multiply(x: int, y: int) -> int:
  """Multiply two numbers together."""
  return x * y

tools = [multiply]
tool_map = {tool.name: tool for tool in tools}
2. Memory Initialization
A Memory object is created to track the conversation history.
The memory is seeded with a SystemMessage to instruct the model on its role and behavior.
memory.add_message("system", "You are a helpful assistant specialized in math operations.")
3. Agent Class Design
An Agent class is implemented with the following key features:

Constructor
Takes parameters like:
name, role, instructions
model, temperature
tools (optional)
Sets up the LLM, tools, tool map, and initializes memory.
invoke() Method
Accepts a user_message input.
Appends the user's message to memory.
Invokes the LLM with the current memory.
Detects if the LLM produced a tool call:
If yes, it delegates the action to the call_tool() method.
Otherwise, it records the assistant's reply.
Returns the final assistant response from the latest memory entry.
def invoke(self, user_message):
  memory.add_message("user", user_message)
  ai_response = llm.invoke(memory.get_messages())
  if ai_response.tool_calls:
      self.call_tool(ai_response.tool_calls)
  else:
      memory.add_message("assistant", ai_response.content)
  return memory.last_message().content
call_tool() Method
Handles the parsing of tool calls.
Executes the appropriate tool based on the call and appends the result back into memory as a ToolMessage.
def call_tool(self, tool_calls):
  tool_call = tool_calls[0]
  function_name = tool_call.function.name
  args = json.loads(tool_call.function.arguments)
  tool = self.tool_map[function_name]
  result = tool.invoke(**args)
  memory.add_message("tool", str(result), tool_call_id=tool_call.id)
4. Execution Example
An agent is created using default parameters and the multiply tool.

User input: "What is 2 multiplied by 2?"

The agent flow:

User input is added to memory.
LLM recognizes the need to call the multiply tool.
Tool is called and the result (4) is captured.
Result is sent back to the LLM.
LLM responds naturally: "2 multiplied by 2 is 4."
Memory inspection shows:

System message
Human message
AI tool call
Tool message with result
Final AI message
5. Conclusion
This basic agent design creates a clean abstraction for:
Managing conversation history
Handling tool execution
Producing coherent LLM responses
It's a strong starting point for building more sophisticated, autonomous agent systems.

