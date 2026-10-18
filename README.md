# 🤖 Multi-Agent Code Assistant

A Python-based multi-agent AI system built with **LangChain, LCEL, and Groq**. It uses a supervisor to dynamically route user requests to specialized agents for code generation, code review, and code explanation, then combines their outputs into a final response.

The project explores how specialized LLM agents can collaborate through structured routing, sequential execution, and reusable processing chains.

## 🚀 Key Features

- **Supervisor-based orchestration** — selects the agents required for each request.
- **Code generation** — generates code according to the user's requirements.
- **Code review** — identifies potential bugs, logical errors, edge cases, and improvements.
- **Code explanation** — explains programming concepts and code in understandable language.
- **Structured output** — uses Pydantic to define the supervisor's routing decisions.
- **LCEL pipelines** — composes prompts, models, and output parsers into reusable chains.
- **Web research tools** — integrates Tavily Search and Beautiful Soup for searching and extracting webpage content.
- **Final response synthesis** — combines relevant agent outputs into a single response.
- **Environment-based configuration** — manages API keys through environment variables.

## 🏗️ Architecture

The supervisor determines which agents should execute and in what order. The selected agents run sequentially, and their outputs are passed to the final response agent.

```text
                 ┌────────────────────┐
                 │    User Request    │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │  Supervisor Agent  │
                 │  Pydantic Routing  │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │  Selected Agents   │
                 └─────────┬──────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Writer        Reviewer      Explainer
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Final Response     │
                 │ Agent              │
                 └─────────┬──────────┘
                           │
                           ▼
                    Final Answer
```

The agents are not all required for every request. For example, a conceptual question may only need the explainer, while a request to generate, review, and explain code may require all three specialized agents.

### Agent Responsibilities

| Agent | Responsibility |
|---|---|
| **Supervisor** | Analyzes the request and selects agents in execution order. |
| **Writer** | Generates code based on the user's requirements. |
| **Reviewer** | Reviews code for correctness, edge cases, and potential improvements. |
| **Explainer** | Explains code or programming concepts. |
| **Final Response** | Produces the final answer from the relevant agent outputs. |
| **Research Agent** | Uses web-search and scraping tools when research is required by the writer workflow. |

## 🧠 How It Works

1. **Receive request:** The user submits a coding or programming-related question.
2. **Determine workflow:** The supervisor produces a structured routing decision.
3. **Execute selected agents:** The pipeline invokes the selected agents in the specified order.
4. **Gather research when needed:** The writer workflow can invoke the research agent, which has access to Tavily Search and website-scraping tools.
5. **Share outputs:** Relevant agent results are stored in the pipeline state and passed to downstream agents.
6. **Generate final response:** The final response agent combines the available outputs into an answer suited to the original request.

## 🔍 Web Research

The project includes two research tools:

- **Tavily Search:** Finds relevant webpages for a given query.
- **Beautiful Soup:** Extracts readable text from webpage HTML fetched using Requests.

The research agent can use these tools to gather information and return findings to the writer workflow.

The current scraping implementation extracts text from HTML and limits the returned content to 12,000 characters per page. Some websites may block requests or require JavaScript rendering.

## 📁 Project Structure

```text
multi-agent-code-assistant/
│
├── agents.py          # Research agent and tool registration
├── chains.py          # LCEL chains for agent workflows
├── model.py           # Groq model and Tavily configuration
├── prompts.py         # Prompts for supervisor and specialized agents
├── supervisor.py      # Structured supervisor routing
├── pipeline.py        # Main orchestration and state management
├── tools.py           # Web search and website scraping tools
├── requirements.txt   # Python dependencies
├── .env               # Local API keys (not committed)
├── .gitignore         # Files excluded from version control
└── README.md
```

### Core Components

**`model.py`**

Initializes the Groq-hosted model using LangChain's `init_chat_model` and configures the Tavily client.

**`prompts.py`**

Contains the instructions for the supervisor, writer, reviewer, explainer, final response agent, and web-content processing.

**`chains.py`**

Defines reusable LCEL workflows by composing prompts, the language model, runnable components, and output parsers.

**`supervisor.py`**

Defines the supervisor's structured output using Pydantic and creates the chain responsible for agent selection.

**`pipeline.py`**

Coordinates the complete workflow, maintains the execution state, invokes selected agents, and generates the final response.

**`agents.py`**

Creates the research agent and makes the search and scraping tools available to it.

**`tools.py`**

Implements the Tavily web-search tool and the webpage text-extraction tool.

## 🛠️ Technology Stack

- **Python** — application logic and orchestration
- **LangChain** — agent creation and model integration
- **LangChain Core / LCEL** — reusable processing pipelines
- **Groq** — language-model inference
- **OpenAI GPT-OSS 20B** — model configured through Groq
- **Pydantic** — structured supervisor output
- **Tavily** — web search
- **Requests** — webpage fetching
- **Beautiful Soup 4** — HTML parsing
- **python-dotenv** — environment-variable loading

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd multi-agent-code-assistant
```

Replace `<YOUR_REPOSITORY_URL>` with your GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Obtain the required API keys from the relevant service providers. Ensure your configured model is available through Groq.

**Security:** Never commit your actual API keys or `.env` file to GitHub. Add the following entries to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
```

### 5. Run the application

```bash
python pipeline.py
```

Enter your request when prompted.

## 💻 Example Requests

**Code generation**

```text
Write a Python function that checks whether a number is prime.
```

**Concept explanation**

```text
Explain how Retrieval-Augmented Generation (RAG) works.
```

**Code review**

```text
Review this Python list comprehension for syntax errors:
[num for num in numbers}
```

**Multi-agent workflow**

```text
Write a Python function to calculate factorial, review the code,
and explain how it works.
```

The supervisor determines the appropriate agent sequence based on the request.

## 🧩 Example Workflow

For the request:

> Write a Python function to check whether a number is prime, review it, and explain how it works.

The supervisor may select:

```text
Writer → Reviewer → Explainer → Final Response
```

- The **Writer** generates the implementation.
- The **Reviewer** checks the generated code and suggests corrections if needed.
- The **Explainer** describes how the implementation works.
- The **Final Response Agent** combines the relevant results into one answer.

The actual sequence depends on the supervisor's routing decision.

## 🔧 Current Limitations

- Agent routing depends on LLM-generated decisions and may require validation.
- Code review is based on model reasoning; code is not automatically executed or tested.
- Web research quality depends on search results and webpage accessibility.
- Some websites block scraping or require JavaScript rendering.
- Research context may be incomplete or contain irrelevant information.
- Reviewing user-provided code requires that the code be passed correctly through the pipeline.
- Model availability, rate limits, and API usage depend on the configured providers.

## 🗺️ Future Improvements

Potential enhancements include:

- Automated code execution in a secure sandbox
- Unit-test generation and execution with `pytest`
- More robust input validation and error handling
- Improved state management and agent-routing validation
- Source attribution and research verification
- Conversation memory for follow-up requests
- Streaming responses
- Parallel execution for independent tasks
- GitHub integration
- A Streamlit user interface
- LangGraph-based orchestration for more advanced stateful workflows

## 🎯 Learning Objectives

This project explores practical concepts in Generative AI engineering:

- Multi-agent system design
- Supervisor-based routing
- Agent tool calling
- LangChain LCEL composition
- Structured output with Pydantic
- State management and sequential execution
- Prompt engineering
- Web research and content extraction
- Multi-step LLM orchestration

## 👨‍💻 Author

**Muhammad Shah Fahad**

BS Computer Science | Machine Learning & Generative AI Learner

This project is part of my journey toward building practical Generative AI applications and developing skills in agent orchestration, LLM workflows, and AI engineering.

---

*Built with Python, LangChain, and Groq.*
