## Introduction to Knowledge Base Agents and Reliability


Knowledge Base Agents and Reliability
Building effective AI agents requires expanding their knowledge sources and ensuring they function reliably in real-world applications. Whether developing a customer support bot or a complex AI assistant, agents need access to accurate data and well-structured workflows to improve their performance.

Expanding an Agent’s Knowledge
Agents can go beyond simple LLM-powered responses by integrating external data sources.

APIs – Provide real-time data, allowing agents to access updated information.
Long-Term Memory – Enables agents to store and recall past interactions by saving data in a database.
Retrieval-Augmented Generation (RAG) – Enhances agents by retrieving relevant knowledge before generating a response.
Designing for Reliability
Reliability means ensuring an agent performs its intended function efficiently and safely. Several factors must be considered:

Defining the Agent’s Role – Should an agent handle multiple tasks, or should there be specialized agents with clear objectives?
Measuring Performance – Is the agent efficient? If a task takes 10 minutes and thousands of tokens, it may need optimization.
Assessing Success Probability – Establish evaluation criteria before deploying an agent.
Understanding the Operational Environment – A banking agent assisting investors may require a different workflow than one advising loan applicants.
Preventing Harm – Restrict agent permissions to avoid critical failures, such as deleting an entire database table.
Techniques for Improving Reliability
Human-in-the-Loop – In critical cases, human oversight ensures correctness.
Observability – Tracking response time, accuracy, and user interactions helps in optimizing agent behavior.
Evaluation – Unlike traditional ML models, agentic systems require continuous, iterative evaluation to maintain quality.
Final Thoughts
AI applications must be designed for reliability by carefully structuring workflows, integrating external knowledge sources, and implementing best practices. In the next lesson, these concepts will be applied using LangGraph.

Quiz Question
When designing a knowledge base agent, which techniques and considerations are essential for ensuring its reliability? Select all that apply.












## Knowledge


Enhancing an Agent’s Knowledge
An agent’s knowledge can be improved by optimizing its internal components. These can be grouped into three categories:

Understanding – How well the underlying model interprets and reasons about user inputs.
Context – Additional instructions or external data provided to shape the agent’s responses.
Memory – Storage and retrieval of past interactions to ensure continuity across conversations.
Understanding
An LLM processes language by predicting the most probable next token, enabling it to interpret inputs and adapt to different situations.

Ways to improve understanding:

Use a larger model with more training data and better reasoning capabilities.
Fine-tune a model with high-quality, domain-specific data to enhance performance in a particular field.
A strong underlying model ensures the agent can handle diverse queries and make informed decisions.

Context
Context enhances an agent’s decision-making by providing background information and external tools.

Ways of adding context:

System Prompts – Provide procedural guidelines.
Few-Shot Prompting – Supplies examples of how to respond to specific inputs, improving behavior.
Tool Use – Allows the model to select and call external functions when needed.
Knowledge Bases (RAG) – Uses Retrieval-Augmented Generation to fetch relevant documents, reducing the need for complex prompts.
Memory
Since LLMs are stateless, they do not remember past interactions unless memory is explicitly managed.

Types of memory storage:

Short-Term Memory – Maintains conversation continuity within a single interaction loop but resets once the loop ends.

In-Session Memory – Stores conversation history for the duration of a session, allowing multi-turn interactions.

Across-Session Memory – Retains long-term knowledge of past user interactions, preferences, or previous agent actions across multiple sessions.

Balancing Knowledge and Cost
While adding context and memory improves agent performance, it comes with trade-offs:

Stateless models require full context for every invocation.
Token limits restrict how much information can be included in a prompt.
Larger models and longer prompts increase computational costs.
Effective AI workflow design requires balancing context, memory, and efficiency to create knowledgeable and scalable agents.

Quiz Question
Which of the following can be effects of adding context and memory to an agent? (Select all that apply)











## Demo: Calling APIs


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Calling External APIs with Tools in LangGraph Workflows
Overview
This demo explains how to integrate external API calls into LangGraph workflows by building custom tools. It highlights the use of real-time data retrieval (quotes and web search) and shows how agents interact with external information sources.

Key Steps Covered
1. Setting up External API Tools
a. Random Game of Thrones Quote Tool
A tool is created to fetch a random Game of Thrones quote.

Uses a public API endpoint (https://api.gameofthronesquotes.xyz/v1/random).


@tool

def random_got_quote():

  response = requests.get("https://api.gameofthronesquotes.xyz/v1/random")

  return response.json()
Sample outputs include:

"sentence": "The things I do for love."

"character": "Jaime Lannister"

b. Tavily Web Search Tool
A second tool is built for live web search using the Tavily API.

Allows answering follow-up questions based on current information.


@tool

def web_search(question: str):

  response = tavily_client.search(query=question)

  return response
Example use:

Question: "Who performs Cersei Lannister in Game of Thrones?"

Top result: "Lena Headey" from Wikipedia.

2. Binding Tools to the LLM
The tools are bound to the LLM using bind_tools.

This creates an LLM with Tools object.


llm_with_tools = llm.bind_tools([random_got_quote, web_search])
An agent abstraction is built around the LLM with tools.
3. Router Logic
A router determines if tool usage is necessary:

If the last message includes a tool call, the workflow routes to the tools node.

Otherwise, it terminates.


def router(state):

  last_message = state.messages[-1]

  if last_message.tool_calls:

      return "tools"

  return "end"
4. Workflow Construction
A LangGraph StateGraph is set up using MessageState to manage conversation history.

Nodes:

agent node: Handles standard LLM interaction.

tools node: Executes the external API tool calls.

Edges:

start → agent

agent → tools (conditionally, if needed)

tools → agent (loop)

Terminate when no tool calls are made.


workflow.add_node("agent", agent_node)

workflow.add_node("tools", tools_node)

workflow.add_edge("start", "agent")

workflow.add_conditional_edges("agent", router)

workflow.add_edge("tools", "agent")
5. Execution Example
System sets the agent’s personality: "You are a web researcher focused on Game of Thrones."

Human asks: "Give me a random Game of Thrones quote."

Flow:

Agent calls random_got_quote.

Receives a quote (e.g., by Jaime Lannister).

Agent decides it needs to find the actor.

Calls web_search for "Jaime Lannister actor."

Receives result: "Nikolaj Coster-Waldau."

Outputs:

Sentence

Character

Actor

Associated URLs for more information.

6. Key Concepts Highlighted
Tool integration enables real-time, dynamic retrieval of external data.

Routers allow conditional control flow inside the workflow.

MessageState tracks conversation memory between user, LLM, and tool outputs.

Multiple tools can be chained flexibly based on LLM reasoning.

7. Conclusion
External APIs extend an agent's knowledge and capability far beyond static LLM training.

Combining API tools, LLM reasoning, and structured workflows creates powerful, responsive systems.

LangGraph provides a clean, modular architecture to manage this complexity.

## Demo: Persisting Memory with a Database


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Persisting Memory with a Database in LangGraph
Overview
This demo explains how to persist memory across sessions by saving conversation history into a SQLite database instead of keeping it only in RAM. This makes it possible to resume conversations later and builds the foundation for session-based systems.

Key Steps Covered
1. Helper Function for Running Graphs
A run_graph helper function is created to simplify invoking the graph repeatedly:

Takes a query, the graph object, and a thread_id.

def run_graph(query, graph, thread_id):

  ...
2. In-Memory Workflow Setup
a. Workflow Definition
A simple workflow with a single chatbot node.

State: Based on MessageState.


workflow = StateGraph(MessageState)

workflow.add_node("chatbot", chatbot_node)

workflow.add_edge("start", "chatbot")

workflow.add_edge("chatbot", "end")
b. MemorySaver Checkpointer
A MemorySaver is used to checkpoint states in RAM only.

from langgraph.checkpoints import MemorySaver

memory = MemorySaver()

workflow = StateGraph(MessageState, checkpointer=memory)
c. Execution
Queries like "What is memory?" are sent to the chatbot.

Metadata about each step (node traversed, messages) is collected internally in memory.

3. SQLite-Persisted Workflow Setup
a. SqliteSaver Checkpointer
A SqliteSaver is used to persist workflow state to a SQLite database file (memory.db).

from langgraph.checkpoints import SqliteSaver

memory = SqliteSaver(db_path="memory.db")

workflow = StateGraph(MessageState, checkpointer=memory)
The database file can be accessed and queried independently.
b. Execution
The same queries are sent, but this time, metadata and snapshots are saved into the SQLite database.
4. Inspecting the SQLite Database
a. Schema Inspection
A cursor is created to query the database.

Two tables are found:

checkpoints

writes


SELECT name FROM sqlite_master WHERE type='table'
b. Metadata Retrieval
Metadata columns contain serialized snapshots of:

Node transitions

Message exchanges (e.g., HumanMessage, AIMessage)

Model configurations


SELECT metadata FROM checkpoints
Example metadata entries:

Step -1: HumanMessage ("What is memory?")

Step 0: System setup

Step 1: AIMessage ("Memory can refer to several concepts...")

c. Advantages
Full history of each thread is preserved.

Metadata includes model names, message types, and conversation content.

Conversations can be resumed at any point by using the same thread_id.

5. Key Concepts Highlighted
MemorySaver is temporary; disappears when the session ends.

SqliteSaver creates persistent, resumable sessions.

Thread IDs differentiate multiple parallel conversations.

Session management becomes trivial with database persistence:

Can resume, search, or audit conversations.
6. Conclusion
Persisting memory with a database turns ephemeral conversations into durable sessions.

LangGraph's checkpoint system allows flexible storage backends.

This pattern is crucial for production-grade chatbot and agent applications that require history continuity across sessions.

## RAG Pipelines


RAG Pipelines: Enhancing AI Agents with Retrieval and Generation
Retrieval-Augmented Generation (RAG) enhances AI agents by retrieving relevant data from external sources and generating informed responses based on that data. This technique improves accuracy, ensures up-to-date information, and provides contextually relevant answers that go beyond an LLM’s training data.

How a RAG Pipeline Works
Retrieval
The user submits a query.
The query is converted into a vector representation using an embedding model.
A vector database searches for similar stored content based on semantic similarity.
Augmentation
The retrieved information is added to the model’s context window.
This enriches the input so the model has both the query and relevant background knowledge.
Generation
The LLM processes the augmented input and generates a response.
The final output combines the model’s internal knowledge with retrieved external information.
Use Case: E-Commerce Customer Support
A user asks: “What is the return policy for electronics?”

Without RAG – The agent gives a generic response based on its training data, which may be outdated or inaccurate.

With RAG – The agent retrieves the actual return policy document, finds the relevant section, and generates a response based on company guidelines.

Preparing Data for RAG Pipelines
Before retrieval and generation can occur, documents must be collected, processed, and stored efficiently.

Data Collection
Sources include PDFs, websites, internal databases, and FAQs.
Preprocessing
Cleaning: Remove unnecessary text like HTML tags or special characters.
Chunking: Break large documents into smaller sections (e.g., paragraphs or sentences).
Embedding Generation: Convert text chunks into vector representations using models like OpenAI embeddings or bge-m3.
Storage
Store embeddings in a vector database (e.g., ChromaDB).
Include metadata (e.g., source, date) to enable efficient filtering.
RAG vs. Fine-Tuning
Both RAG and fine-tuning enhance an agent’s performance but in different ways:

Aspect	RAG	Fine-Tuning
How it works	Retrieves external data at runtime	Adjusts model weights using new data
Best for	Dynamic, frequently updated data	Domain-specific, long-term improvements
Data needs	Large document corpus for retrieval	Small, high-quality training dataset
Cost	Requires vector storage, minimal compute	Requires computational resources
Risk	Retrieval quality impacts accuracy	Catastrophic forgetting is possible
Choosing Between RAG and Fine-Tuning
The best approach is combining both:

Start with an LLM and strategic prompting – Quickly test feasibility.

Integrate RAG – Improve accuracy with external data retrieval.

Fine-tune a smaller model – Optimize performance once stable, reducing cost and latency.

A fine-tuned customer support agent using RAG for live knowledge retrieval creates a personalized, real-time experience that is accurate and cost-efficient.

Both techniques are powerful in agent design, and the right balance depends on the use case, cost, and update frequency of the required knowledge.

Quiz Question
What is the primary advantage of a RAG (Retrieval-Augmented Generation) pipeline in the context of AI agents?









## Demo: Understanding Embeddings


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Understanding Embeddings in LangGraph Workflows
Overview
This demo develops intuition about embeddings—dense vector representations of text—and how to use them for similarity search and visualization. It introduces building embeddings with Hugging Face or OpenAI, comparing semantic similarity, and visualizing embeddings in 2D space.

Key Steps Covered
1. Embeddings Factory Setup
A simple EmbeddingsFactory class is built to support two providers:

Hugging Face models (e.g., all-MiniLM-L6-v2)

OpenAI Embeddings (via API key)


class EmbeddingsFactory:

  def __init__(self, provider):

      ...
Hugging Face models are freely available and downloaded automatically.

OpenAI models require an API key and internet access.

2. Sentence List Creation
Six sample sentences are prepared:

Grouped into three pairs of similar sentences.

Example:

"The cat sat on the mat." and "A cat was resting on a mat."


sentences = [

  "The cat sat on the mat.",

  "A cat was resting on a mat.",

  "The sun is bright today.",

  "It’s sunny and warm outside.",

  "I love reading books at night.",

  "Reading at bedtime is my favorite."

]
3. Generating Embeddings
Hugging Face embeddings are generated for each sentence.

Each embedding is a 384-dimensional vector.


embeddings = [embeds.embed_query(sentence) for sentence in sentences]
These vectors encode semantic meaning: similar sentences yield similar vectors.
4. Computing Similarities
Using dot product from NumPy, semantic similarity between embeddings is calculated.

Pairs of similar sentences have higher similarity scores (e.g., 0.62, 0.58, 0.56).

Non-related sentences yield lower similarity scores.


similarity_score = np.dot(embedding1, embedding2)
Results demonstrate that embeddings capture semantic (not just lexical) similarity.
5. Dimensionality Reduction
Embeddings (384 dimensions) are too large to visualize easily.

Dimensionality reduction is performed (e.g., via PCA) to map embeddings into 2D space.


from sklearn.decomposition import PCA

pca = PCA(n_components=2)

embeddings_2d = pca.fit_transform(embeddings)
Although some information is lost, this allows easier visualization.
6. Visualization
A scatterplot is created showing embeddings in 2D space.

Sentences with similar meaning are plotted close together.


plt.scatter(...)

for i, sentence in enumerate(sentences):

  plt.annotate(sentence, ...)
Visualization confirms:

Similar sentences cluster together.

Dissimilar sentences are further apart.

7. Switching Providers
Switching from Hugging Face to OpenAI:

OpenAI embeddings are larger (e.g., 1536 dimensions).

Higher-dimensional embeddings may better capture subtle semantic differences.

Procedure is the same; only provider changes.


embeds = EmbeddingsFactory(provider="openai")
8. Key Concepts Highlighted
Embeddings represent the meaning of text numerically.

Similarity between embeddings reflects semantic closeness.

Dimensionality reduction sacrifices precision but increases explainability.

Provider choice affects embedding quality, size, and performance.

9. Conclusion
Embeddings are the backbone of RAG, retrieval, recommendation systems, and clustering tasks.

Understanding how to create, compare, and visualize embeddings is fundamental to building AI systems that understand natural language at a deeper level.

## Demo: Using ChromaDB


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Using ChromaDB for Embedding Storage and Retrieval
Overview
This demo shows how to apply embeddings in practice using ChromaDB, a vector database. It walks through inserting documents, querying with semantic similarity, switching embedding models, and eventually integrating ChromaDB with LangChain.

Key Steps Covered
1. Initial Setup
Five sentences (mini news articles) are created.

Topics include Meta, Nvidia, Google, Intel, and more.


sentences = [

  "Meta drops multimodal Llama model.",

  "Chip giant Nvidia acquires OctoAI.",

  "Google brings Gemini to older Pixel Buds.",

  "Intel Battlemage GPU benchmarks leaked.",

  "Nvidia CEO reveals new AI chip roadmap."

]
2. Creating a Chroma Collection
A Chroma client is created.

A collection named "Udacity" is initialized.


import chromadb

client = chromadb.Client()

collection = client.create_collection(name="Udacity")
Documents and IDs are added.

Default embedding model: all-MiniLM-L6-v2 (via Sentence Transformers).


collection.add(documents=sentences, ids=[...])
Validation:

Number of documents = 5.

Peeking into the collection shows embedded vectors.

3. Querying the Vector Database
Queries are performed using keywords like:

"GPU"

"CPU"

"memory"

"gadget"

Chroma searches based on semantic similarity, returning:

Closest matching documents

Metadata

Distances (similarity scores)


results = collection.query(query_texts=["GPU"], n_results=2)
Example result:

Top results for "GPU" are articles about Intel GPUs and Nvidia acquisitions.
4. Changing Embedding Models
A new embedding model all-mpnet-base-v2 is introduced to improve semantic search quality.

OpenAI embeddings (text-embedding-ada-002) can also be used.

After changing the embedding model:

The Udacity collection is deleted and recreated.

New embeddings are added.


from sentence_transformers import SentenceTransformer

embedding_function = SentenceTransformer('all-mpnet-base-v2')
Comparisons using dot products show that articles about Nvidia are highly similar.
5. Switching to LangChain Chroma Integration
Instead of using raw Chroma, the demo switches to using Chroma vector stores through LangChain.

from langchain.vectorstores import Chroma
Documents are created with metadata (e.g., company, topic).

Example metadata:

Company: Meta, Topic: Llama

Company: Nvidia, Topic: OctoAI


docs = [

  Document(page_content="...", metadata={"company": "Meta", "topic": "Llama"}),

  ...

]
Vector store created with:

Documents

Embeddings

Persistence to Chroma backend

Semantic search with score:

Top results are returned with both their text content and similarity scores.

vectorstore.similarity_search_with_score(query="GPU", k=3)
6. Key Concepts Highlighted
Vector databases like Chroma are essential for fast semantic search.

Embeddings encode meaning; better models yield better search quality.

Metadata enhances retrieval by enabling filtered or faceted searches.

LangChain integration makes it easy to manage vector stores for downstream tasks.

7. Conclusion
Using ChromaDB (standalone or with LangChain) enables powerful semantic search capabilities.

Combining embeddings, persistent storage, and flexible search methods is crucial for real-world RAG (Retrieval-Augmented Generation) and AI systems.

## Exercise: Create a Knowledge Base Agent

Welcome to your Knowledge Base Agent Challenge!

In this exercise, you'll create an agent that can answer user questions by consulting a collection of documents. Instead of relying solely on the model’s internal knowledge, the agent will ground its responses in an external source of truth.

Scenario
You’re building a support assistant for a company that maintains a large set of internal documentation, such as FAQs, policy guides, and how-to manuals. The assistant should be able to:

Search through the documentation
Retrieve the most relevant sections
Provide helpful answers grounded in the retrieved information
This approach, aka Retrieval-Augmented Generation (RAG) — is a powerful technique for building agents that are accurate, verifiable, and up-to-date.

Challenge
Your task is to create a LangGraph Workflow that includes:

A document loading and vectorization process for a knowledge base.
An Agent Node capable of:
Retrieving relevant knowledge.
Augmenting responses with contextual documents.
Generating accurate answers.
Conditional routing to control query resolution.
Optimization techniques such as text chunking and embedding search.
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.


## Exercise Solution: Create a Knowledge Base Agent


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Knowledge Base Agent with RAG
Overview
This exercise demonstrates how to create a knowledge base (KB) agent using Retrieval-Augmented Generation (RAG) techniques in LangGraph. The agent uses vector embeddings to retrieve relevant context from a document and answers user questions by augmenting the prompt with that context.

Key Steps Covered
1. Environment Setup
OpenAI's chat model (ChatOpenAI) and embedding model (OpenAIEmbeddings) are initialized.
A vector store is created using Chroma, with a custom collection name and the embedding function.
vectorstore = Chroma(collection_name="udacity", embedding_function=embedding)
2. Document Preparation
A PDF file (provided in the environment) is loaded using PyPDFLoader (async).
The text is split using a RecursiveCharacterTextSplitter with:
chunk_size=1000
chunk_overlap=200
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(pages)
vectorstore.add_documents(documents)
3. Session State Definition
A custom state class is defined, extending MessageGraphState, and includes:
question: user input string
documents: list of retrieved documents
answer: model-generated answer
class State(MessageGraphState):
  question: str
  documents: List[Document]
  answer: str
4. RAG Workflow Nodes
a. Retrieve Node
Performs a similarity search using the vector store.
Retrieves documents related to the input question and stores them in state.
def retrieve(state):
  docs = vectorstore.similarity_search(state["question"])
  return {"documents": docs}
b. Augment Node
Uses a ChatPromptTemplate with placeholders for question and context.
Constructs a system message with relevant document excerpts and user input.
prompt = ChatPromptTemplate.from_messages([
  ("system", "Answer using the following context:\n\n{context}"),
  ("human", "{question}")
])
c. Generate Node
Calls the LLM with the constructed prompt to produce an answer.
def generate(state):
  return {"answer": llm.invoke(state["messages"]).content}
5. Workflow Construction
A LangGraph StateGraph is created with four nodes:
retrieve, augment, generate, end
Sequential edges connect the nodes to form the RAG pipeline:
start → retrieve → augment → generate → end
workflow = StateGraph(State)
workflow.add_node("retrieve", retrieve)
workflow.add_node("augment", augment)
workflow.add_node("generate", generate)
workflow.set_entry_point("retrieve")
workflow.set_finish_point("generate")
6. Execution and Testing
The workflow is compiled and visualized.

Sample query: "What are open source models?"

Output:

Relevant context is retrieved from Section 3 of the document.
LLM response is correctly augmented: "Open source models are language models developed and shared by the community..."
The state history confirms that:

The user's question was processed,
The appropriate context was retrieved,
A complete answer was generated using RAG.
7. Encouraged Exploration
Learners are encouraged to:
Ask new questions of the document.
Adjust chunk sizes and overlaps.
Swap out the embedding model or vector store.

## Demo: Agentic RAG


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Introducing Agentic Decisions into RAG Pipelines
Overview
This demo expands a basic RAG (Retrieval-Augmented Generation) pipeline to include agentic decision-making. The system dynamically decides whether to rely on retrieved documents or perform live web research depending on the quality of retrieved information.

Key Steps Covered
1. Setting up the Vector Store
Documents (from a previously used PDF) are loaded into a Chroma vector database.

Embeddings are generated and stored.

This is the standard offline preprocessing step for RAG.


vectorstore = Chroma(...)

vectorstore.add_documents(...)
2. Defining the State Schema
A custom state is defined including:

search_required: a yes/no flag determining whether a web search is necessary.

Other standard RAG fields (messages, question, etc.).


class State(MessageState):

  search_required: Optional[str]
3. Creating Nodes
a. Retrieve Node
Performs similarity search on the vector store to find relevant documents.

retrieved_docs = retriever.invoke(state.question)
b. Evaluator Node
Uses an LLM chain with a prompt asking:

"Based on retrieved documents, is a web search required? Answer 'yes' or 'no'."
The LLM's response sets the search_required field.


prompt = ChatPromptTemplate.from_messages([...])

evaluator = prompt | llm | StrOutputParser()
c. Researcher Node
If web search is needed, the researcher node uses Tavily’s web search tool.

Searches the web and updates messages with search results.


web_search_tool = tavily_client.search
d. Augment Node
If web search is not required, retrieved documents are passed to the LLM for direct answering.

augment_prompt = ChatPromptTemplate.from_messages([...])

augment = augment_prompt | llm | StrOutputParser()
e. Generate Node
Final output generation based on the selected source of context.
4. Defining Router Functions
Two routers manage control flow:

First router:

If search_required == "yes", route to the researcher.

If no, route to augment.


def should_search_router(state):

  return "researcher" if state.search_required == "yes" else "augment"
Second router:

After tool use, if more tool calls are needed, loop.

Otherwise, terminate.


def tool_router(state):

  ...
5. Building the Workflow
Nodes: retrieve, evaluator, researcher, augment, web_search_tool

Edges:

start → retrieve → evaluator

Conditional edge based on search decision.

If web search is needed, the researcher loops until termination.

Otherwise, augment proceeds directly to answer generation.


workflow.add_conditional_edges("evaluator", should_search_router)
Workflow is visualized and compiled.
6. Execution Examples
a. Question: "What is Pokémon?"
Retrieval fails (no relevant documents).

Evaluator responds "yes" to search_required.

Researcher performs web search.

Returns correct answer: "Pokemon, short for Pocket Monsters..."

b. Question: "What is open source model?"
Retrieval succeeds.

Evaluator responds "no" to search_required.

Context is used directly from the document without web search.

Answer successfully pulled from offline documents.

7. Key Concepts Highlighted
Dynamic decision-making inside a RAG workflow.

Fallback to web search when knowledge gaps are detected.

Agentic behavior: LLM assesses context sufficiency and adapts.

Efficient resource use: Web search is only triggered when necessary.

8. Conclusion
Adding agentic decisions to RAG pipelines increases reliability and adaptability.

Blending offline retrieval with online search creates more robust AI systems.

This modular, decision-driven design is foundational for advanced AI agents.

## Demo: LangMem (Bonus)


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Building Long-Term Memory with LangMem
Overview
This demo explains how to combine vector database storage with an agent framework to create long-term memory using LangMem, a library built by the LangChain team. The goal is to enable agents to remember facts across multiple interactions.

Key Steps Covered
1. Setting up LangMem
LangMem handles the memory store behind the scenes, using vector embeddings to save and retrieve information.

Memory storage is backed by OpenAI embeddings in this example.


from langmem import OpenAIMemoryStore

store = OpenAIMemoryStore()
2. Creating the Workflow
A ReAct agent is created using a prebuilt LangMem utility:

create_react_agent(model, tools, store)
No custom StateSchema is needed.

Two tools are defined:

manage_memory_tool: Saves information into the store.

search_memory_tool: Retrieves information from the store.


tools = [manage_memory_tool, search_memory_tool]

agent = create_react_agent(model=llm, tools=tools, store=store)
The agent workflow:

Agent node → Tools node → Agent node → End
3. Inspecting the Input Schema
The input schema for the agent expects a field called messages.

messages should include:

SystemMessage

HumanMessage

AIMessage

ToolMessages (after tool calls)


{

  "messages": [...]

}
4. Example Interaction: Setting and Retrieving Preferences
a. Initial Question
User asks:

"What are my lighting preferences?"
The agent:

Calls the search_memory tool.

Tool responds: No memory found.

Agent replies: "I don't have any information about your lighting preferences."

b. Saving New Information
User follows up:

"Remember that I prefer dark mode."
The agent:

Calls the manage_memory tool.

Saves the new preference into the store.

Replies: "I've noted that you prefer dark mode."

c. New Session Retrieval
A new thread is started with a fresh message:

"What are my lighting preferences?"
Only this question is provided (no prior conversation).

The agent:

Calls the search_memory tool.

Finds the saved memory from the previous interaction.

Replies correctly: "You prefer dark mode."

5. Key Concepts Highlighted
Persistent memory across different sessions and thread IDs.

Memory search and management handled with tools abstracted from the agent's reasoning.

Vector-based retrieval ensures memory is stored in a scalable, semantically searchable format.

The user does not need to manually maintain history; it's offloaded to LangMem.

6. Conclusion
LangMem makes it easy to extend ReAct agents with long-term memory.

Agents can now recall user preferences or facts across completely different conversations.

This memory-enhanced design is a key step toward building more lifelike, persistent AI agents.

## Reliability


Ensuring Reliability in AI Agents
AI agents are everywhere, but many lack reliability. Creating agents is easy—making them predictable, consistent, and trustworthy is the real challenge.

Reliability means the likelihood that an agent will perform as expected in its environment without causing harm. Building reliable agents requires clear success metrics, proper evaluation, and ongoing monitoring.

Defining Success with Metrics
To improve reliability, agents need measurable success criteria:

Accuracy – Are responses correct and relevant? How often do errors occur?
Efficiency – Does the agent complete tasks quickly and with minimal resource usage?
Cost Optimization – Is performance optimized without excessive API calls, tokens, or compute costs?
By defining these metrics, agents can be continuously refined and optimized.

Evaluation vs. Testing
Testing identifies defects and functional errors, ensuring the agent works under different conditions.

Evaluation assesses overall quality, determining how well the agent performs its intended task.

Both are essential, but evaluation plays a strategic role in improving AI agents over time. For example, different embedding models may be evaluated to maximize accuracy.

Observability: Monitoring Agents in Production
Reliability requires ongoing monitoring to detect failures and improve performance.

Key observability techniques include:

Tracking KPIs – Continuously measure accuracy, efficiency, and error rates.
Logging & Tracing – Record both failures and successes to refine workflows.
Decision Transparency – Monitor how the agent makes choices and selects actions.
Observability enables proactive issue detection and allows dynamic fine-tuning of agents.

Other Considerations for Reliable Agents
Scalability – AI agents must integrate smoothly into complex systems without causing bottlenecks.
Human-in-the-Loop – Human oversight improves decision-making in high-stakes scenarios.
Multi-Agent Collaboration – Agents should communicate effectively in multi-agent workflows.
Self-Healing Mechanisms – Agents should recover from errors and refine their responses over time.
Practical Use Cases – Instead of replacing humans, focus on workflow automation, research assistance, and large-scale data analysis.
Final Thoughts
Reliability is what separates AI enthusiasts from real AI engineers. Reliable agents are designed with clear metrics, evaluation processes, and continuous observability.

By focusing on measurable success, proactive monitoring, and real-world application, AI agents can become trustworthy problem solvers that enhance human capabilities.

Quiz Question










## Human-in-the-Loop and Observability


Human-in-the-Loop & Observability in AI Agents
AI agents are becoming more complex and autonomous, making transparency and control essential. Observability helps monitor, interpret, and optimize agent workflows, while human-in-the-loop (HITL) ensures oversight and error correction in critical scenarios.

Gaining Initial Visibility
Basic debugging starts with printing outputs in Jupyter Notebooks, allowing developers to:
Observe agent responses to different inputs.
Identify errors or inconsistencies.
Iterate and refine logic quickly.
This method is useful for early-stage development, but it does not scale well for production environments.
Introducing Human-in-the-Loop
As AI agents handle more complex decisions, human intervention becomes crucial for reliability.

HITL mechanisms allow humans to:

Interrupt and approve an action before execution.
Validate outputs to prevent errors.
Modify agent state in real-time to correct misinterpretations.
Review checkpoints can be built into workflows, enabling human reviewers to approve or reject key decisions before the agent proceeds.

Advanced Observability for Production Systems
For large-scale deployments, fine-grained observability ensures agents remain efficient and trustworthy.

Observability relies on three core techniques:

Metrics – Monitor performance indicators like response time, accuracy, and token usage.

Logs – Capture detailed records of agent actions, errors, and interactions.

Tracing – Tracks the sequence of actions taken by the agent.

Final Thoughts
Observability and HITL are essential for building reliable AI agents.

Early-stage debugging in Jupyter is useful but limited.
Human-in-the-loop ensures oversight in high-stakes scenarios.
Advanced observability techniques (metrics, logs, tracing) enable proactive monitoring and optimization.
AI deployment is not just about monitoring—it’s about continuous learning and improvement. Organizations that implement robust observability tools and human oversight mechanisms can scale AI safely while maintaining control and performance.

Quiz Question
Which of the following do Human-in-the-Loop (HITL) mechanisms allow humans to do in AI agent workflows?









## Demo: Human-in-the-Loop


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Human-in-the-Loop Approvals and Edits in LangGraph Workflows
Overview
This demo introduces human-in-the-loop (HITL) techniques for LangGraph workflows, allowing users to approve, reject, or edit the state before certain actions (like tool calls) proceed. This control mechanism is vital for building safe and supervised AI systems.

Key Steps Covered
1. Basic Workflow Structure
a. State Definition
The custom state includes:

question: str

answer: str

MessagesState is inherited for managing message history.


class State(MessagesState):

  question: str

  answer: str
b. Nodes
Entry Point:

Receives the user question and builds system and human messages.
Agent Node:

Binds the web search tool to the LLM.

Invokes the LLM with the current messages.

Updates the answer field.


def entry_point(state):

  ...

  

def agent(state):

  ...
c. Router
If the latest message contains tool_calls, the workflow proceeds to tools.

Otherwise, it terminates.


def router(state):

  last_message = state["messages"][-1]

  return "tools" if last_message.tool_calls else END
2. Introducing Breakpoints
During graph compilation, interrupt_before=["tools"] is specified.

This pauses the workflow execution before tools are called.

Workflow visualization:

start → entry_point → agent → [breakpoint] tools → agent → end

graph = workflow.compile(interrupt_before=["tools"], checkpointer=memory)
Initial example:

Question: "What's the capital of Brazil?"

Workflow pauses after agent identifies a web search is needed.

3. Human Approval Flow
a. Basic Approval
A function human_in_the_loop_run streams the workflow.

After seeing the agent’s intent (e.g., to call a tool), the human is prompted:

YES: Continue execution.

NO: Abort workflow.


human_input = input("Do you approve the tool calling? (YES or NO): ")
Example:

Approving → Continues and retrieves the correct answer.

Rejecting → Prints "Workflow aborted by a human."

b. More Interactive Control (Human Revision)
Workflow is modified to interrupt before the agent instead of tools.

If the user says NO to the initial question:

They are prompted to edit the question.

A system message ("Workflow edited by a human") and a new human message are inserted.


human_input = input("So what should be the question? ")
The graph state is updated with the revised input.

Execution then resumes from the updated state.

Example:

Original: "What’s the capital of Brazil?"

Edit to: "What’s the capital of Canada?"

Output: "The capital of Canada is Ottawa."

4. Second Human Step After Tool Messages
After a tool call, the human again can:

Review.

Continue execution.

Potentially enhance logic to approve post-tool actions.

5. Key Concepts Highlighted
Breakpoints allow controlled interruptions during workflows.

Human approvals ensure critical actions (like external API calls) can be supervised.

Human edits allow correction of user input before significant processing happens.

Thread IDs manage session persistence, enabling inspection and modification across sessions.

6. Conclusion
Human-in-the-loop mechanisms enhance AI system transparency and safety.

LangGraph’s breakpoint and checkpoint features make integrating HITL workflows straightforward.

A next enhancement would be extending approval loops after tool messages, enabling full-cycle human supervision.

## Demo: Observability


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Observability with MLflow and LangGraph
Overview
This demo introduces MLflow observability into LangGraph workflows. By tracing and logging each step of a workflow—including LLM invocations and tool usage—developers can monitor, debug, and analyze their pipelines directly from the MLflow UI.

Key Steps Covered
1. MLflow Setup
a. Tracking Configuration
A local MLflow server is assumed to be running at http://127.0.0.1:5000.

This address is set as the MLflow tracking URI.


mlflow.set_tracking_uri("http://127.0.0.1:5000")
The experiment is named "udacity".

mlflow.set_experiment("udacity")
b. Manual Trace Example
A simple add() function is traced with @mlflow.trace.

Inputs and outputs are automatically logged to the MLflow UI.


@mlflow.trace

def add(a, b):

  return a + b

add(1, 2)
2. Workflow Overview
The workflow uses a similar structure to previous demos:

A question is passed to an entry_point.

The agent determines whether a tool (web search) is needed.

If required, the tool is called and results are returned.

The workflow interrupts at a breakpoint before tools, enabling streaming inspection.


graph = workflow.compile(interrupt_before=["tools"], checkpointer=MemorySaver())
3. LangChain Autologging Integration
mlflow.langchain.autolog() is called to enable automatic logging of LangChain events:

LLM inputs and outputs

Tool call traces

Message sequences

Token usage and performance metrics


mlflow.langchain.autolog()
4. Execution Example
Input question: "What is the capital of Brazil?"

Initial invocation:

System and human messages are appended.

The agent node recognizes the need for a tool call (no direct answer yet).

MLflow logs the trace up to the tool call breakpoint.

a. Tool Node Execution
The tool node (Tavily web search) is executed.

Output: Top results related to the question are logged.

b. Final Agent Node Execution
With the web search response in memory, the agent generates a complete answer:

"The capital of Brazil is Brasília..."

Includes citations or source links when available.

5. Reviewing the Trace in MLflow UI
Each node’s inputs and outputs are logged:

Entry point: initial user input and message formatting.

Agent: LLM messages and tool call info.

Tool: external API invocation and response data.

Final agent call: formatted answer to the user.

MLflow panels show:

Run timeline

Artifact logs

Token counts

Inputs/outputs per node

6. Key Concepts Highlighted
Breakpoints provide pause-and-inspect control.

Traces log the full context of decision-making and tool use.

MLflow + LangChain combination brings transparency and observability to LLM-based workflows.

Easy to debug issues, understand performance, and trace final outputs to original prompts or tool responses.

7. Conclusion
Integrating MLflow with LangGraph and LangChain gives developers critical insight into how AI workflows behave.

Each component’s behavior becomes traceable, auditable, and optimizable.

This observability is crucial for safe, production-grade LLM applications.

## Demo: Evaluating Agents


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Evaluating RAG and Agent Performance with RAGAS
Overview
This demo walks through building a simple Retrieval-Augmented Generation (RAG) pipeline, converting it into a LangGraph workflow with tool use, and evaluating both using RAGAS, a framework for measuring the quality and correctness of RAG systems and agent responses.

Key Steps Covered
1. Building a Simple RAG Pipeline
a. Document Setup
A list of five documents is created, covering topics like Meta, Nvidia, Google, Intel, and Dell.

Each Document object includes metadata such as company and topic.


documents = [

  Document(page_content="Meta drops multimodal Llama 3.2...", metadata={"company": "Meta", "topic": "llama"}),

  ...

]
b. Chroma Vector Store
A Chroma vector store is created using OpenAI embeddings and documents are added to it.

vector_store = Chroma(collection_name="udacity", embedding_function=OpenAIEmbeddings())

vector_store.add_documents(documents, ids=...)
c. RAG Chain
A simple prompt-based chain is constructed:

Prompt: "Answer the question based only on the following context: {context}"

Chain: Prompt → LLM → Output parser


chain = prompt | llm | StrOutputParser()
d. Invocation Example
Query: "Who is partnering with Nvidia?"

Answer returned: "Dell" — correctly retrieved from the document set.

2. Evaluating the RAG Pipeline with RAGAS
a. Evaluation Dataset Creation
Five example queries and expected responses are prepared.

For each, relevant documents are retrieved and responses generated.

A EvaluationDataset is created using these entries.


evaluation_dataset = EvaluationDataset.from_list(dataset)
b. Metrics Used
RAGAS metrics include:

LLMContextRecall

Faithfulness

FactualCorrectness

c. Execution
evaluate() is called with the evaluation dataset and the wrapped LLM.

Result:

100% context recall

100% faithfulness

~54% factual correctness


result = evaluate(

  dataset=evaluation_dataset,

  metrics=[LLMContextRecall(), Faithfulness(), FactualCorrectness()],

  llm=evaluator_llm,

)
3. Creating an Agent Workflow in LangGraph
a. Tool Definition
A custom get_pokemon_type tool is defined to return Pokémon types by name.

@tool

def get_pokemon_type(pokemon_name: str) -> str:

  ...
b. LangGraph Construction
A simple agent workflow is created:

Agent node → Conditional tool call → Tool node → Back to agent or end
Standard ReAct-style flow.


workflow = StateGraph(MessagesState)

workflow.add_node("agent", agent)

workflow.add_node("tools", ToolNode(tools))
c. Invocation Example
Input: "What is the Gengar's type?"

The agent correctly calls the tool and responds: "ghost/poison"

4. Evaluating the Agent with RAGAS
a. Conversion to RAGAS Format
LangGraph message trace is converted to RAGAS-compatible format using convert_to_ragas_messages().

ragas_trace = convert_to_ragas_messages(result["messages"])
b. Tool Call Accuracy
Measured using ToolCallAccuracy metric.

Reference includes expected tool call and arguments.

Result: 100%

c. Agent Goal Accuracy
Measures whether the agent achieved the intended result.

Uses AgentGoalAccuracyWithReference.

Result: 100%

5. Key Concepts Highlighted
RAG pipelines can be evaluated objectively for performance and correctness using RAGAS.

LangGraph workflows with tool calls can be tested just like standard RAG flows.

Metrics such as faithfulness, factual correctness, and tool call accuracy enable deep insights into agent behavior.

Agent performance can be reliably benchmarked and improved iteratively.

6. Conclusion
RAGAS is a powerful toolkit for evaluating the effectiveness of both retrieval-based systems and agent workflows.

This demo shows how to apply evaluation metrics in both traditional and tool-augmented pipelines to ensure system quality and correctness.

## Exercise: Evaluate Your Agent

Welcome to your Agent Evaluation Challenge!

In this exercise, you’ll implement a framework for evaluating the responses of your AI agent. Whether you're building a chatbot, a knowledge assistant, or a task-specific agent, evaluation is key to ensuring trust, relevance, and continuous improvement.

Scenario
You’ve deployed a knowledge-based agent that answers user questions using company documentation. Now, stakeholders want to know:

How accurate are the responses?
Are the answers grounded in the context provided?
Do they follow the expected format?
To answer these questions, you need to implement a response evaluation pipeline that scores or classifies agent outputs based on defined criteria — either using another LLM (automatic evaluation) or a manual review process.

Challenge
Your task is to create a LangGraph Workflow that includes:

A RAG pipeline for information retrieval.
An LLM-based judge for evaluation.
RAGAS metrics for quality assessment.
MLflow logging for observability.
The workflow should:

Retrieve, augment, and generate answers.
Evaluate the answers using RAGAS.
Log performance metrics in MLflow.
Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.


## Exercise Solution: Evaluate Your Agent


Start Workspace

Workspaces will shut down after 30 minutes of inactivity. Any running processes will be stopped.

Workspaces may take up to 5 minutes to start.

Summary: Evaluation of RAG Pipeline with RAGAS and MLflow
Overview
This exercise demonstrates how to evaluate a Retrieval-Augmented Generation (RAG) pipeline using RAGAS for scoring and MLflow for tracking. Learners set up a full RAG pipeline (retrieve, augment, generate, evaluate) and log evaluation metrics like faithfulness, context precision, and answer relevancy.

Key Steps Covered
1. Multiple Model Setup
Three models are initialized:

llm: a standard OpenAI model used for generating answers.
llm_judge: a more powerful model used to evaluate the generated answers.
embedding: OpenAI embeddings used for vector search.
2. MLflow Experiment Configuration
An MLflow experiment is created and a run is started with a custom name.
Run metadata, such as model names and embedding models, are logged as parameters.
mlflow.set_experiment("udacity")
with mlflow.start_run(run_name="L4_exercise_02") as run:
  mlflow_run_id = run.info.run_id
  mlflow.log_params({
      "llm_model": llm.model_name,
      "llm_judge_model": llm_judge.model_name,
      "embedding_model": embedding.model
  })
3. Document Processing
A previously used PDF document is reloaded.
Text is chunked and embedded into a vector store using Chroma.
4. State Schema Definition
A new session state class is defined, extending MessageGraphState.
It includes fields for:
run_id
question
ground_truth
documents (retrieved context)
answer (LLM response)
evaluation (dictionary of evaluation metrics)
class State(MessageGraphState):
  run_id: str
  question: str
  ground_truth: str
  documents: List[Document]
  answer: str
  evaluation: dict
5. RAG Node Pipeline
Four functional nodes are reused from previous exercises:

retrieve: Similarity search on the vector store.
augment: Uses a chat prompt with question and context.
generate: Uses the standard LLM to produce the response.
6. Evaluation Node
A new evaluate_rag node is created.
It constructs a dataset of:
question, answer, context, and ground_truth.
Uses llm_judge and evaluate() from RAGAS to score:
faithfulness
context_precision
context_recall
answer_relevancy
Each metric is logged to MLflow.
mlflow.log_metric("faithfulness", eval_result["faithfulness"])
mlflow.log_metric("context_precision", eval_result["context_precision"])
mlflow.log_metric("context_recall", eval_result["context_recall"])
mlflow.log_metric("answer_relevancy", eval_result["answer_relevancy"])
7. Workflow Construction
A StateGraph is created with the following nodes and edges:
start → retrieve → augment → generate → evaluate_rag → end
workflow.add_node("retrieve", retrieve)
workflow.add_node("augment", augment)
workflow.add_node("generate", generate)
workflow.add_node("evaluate_rag", evaluate_rag)
8. Execution and Evaluation
A test query is submitted:
"What are open source models?"
A ground truth reference answer is provided.
The pipeline completes and produces evaluation metrics, e.g.:
answer_relevancy: 0.9
faithfulness: 0.85, etc.
MLflow logs both the parameters and evaluation metrics for inspection.
9. Encouraged Exploration
Learners are encouraged to:

Run multiple experiments with different RAG parameters.
Use different reference answers or documents.
Tune and compare performance over time using MLflow tracking.

## Security Concerns


Security Concerns in AI Agent Deployments
AI agents are automating workflows and making decisions at scale, but security risks must be taken seriously. Protecting AI agents from threats like data leakage, manipulation, and unauthorized access is essential for building trustworthy and resilient systems.

Common Security Threats
Data Leakage – Sensitive data, such as financial records or healthcare information, may be exposed if AI agents are not properly secured.

Prompt Injection Attacks – Attackers manipulate inputs to alter agent behavior, extract confidential data, or generate misleading outputs.

Unauthorized Access – Weak authentication and poor access controls allow attackers to hijack AI capabilities.

Bias Exploitation – Malicious actors can manipulate biased models to generate harmful or misleading content.

Understanding these threats is the first step toward designing secure AI agents.

Best Practices for AI Security
Access Control
Role-Based Access Control (RBAC) ensures only authorized users can interact with AI systems.
Multi-Factor Authentication (MFA) adds an extra layer of protection.
Data Encryption secures information both in transit and at rest.
Input Validation & Sanitization
Filtering and sanitizing user inputs helps prevent prompt injection attacks.
Using predefined templates and allowlists reduces the risk of input manipulation.
Continuous monitoring detects unusual or harmful input patterns.
Explainability & Transparency
AI decisions must be auditable to maintain trust and accountability.
Logging all interactions ensures transparency.
Human-in-the-loop mechanisms allow oversight of critical decisions.
Real-Time Monitoring
Anomaly detection systems track unusual behavior.
Alerts for suspicious activity enable a quick response to security breaches.
A clear incident response plan ensures AI-related security issues are handled efficiently.
Challenges in AI Security
Evolving Threats – Attackers continuously develop new ways to exploit AI vulnerabilities.
Lack of Standardization – AI security guidelines vary across industries, making enforcement difficult.
Balancing Security and Performance – Overly strict security can slow down AI performance.
Human Error – Insider threats and unintentional user mistakes pose security risks.
Final Thoughts
AI security is an ongoing effort, not a one-time fix. Protecting data, models, and users requires continuous monitoring, adaptation, and best practice implementation.

Staying informed about emerging threats and proactively improving security measures is essential for ensuring safe AI deployments.

Quiz Question










## 