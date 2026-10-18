# 🤖 Multi-Agent Code Assistant

A Python-based multi-agent AI application built with **LangChain, LCEL, and Groq**. The system uses a supervisor to dynamically select specialized agents, coordinate their execution, and synthesize their outputs into a final response.

It also integrates web research capabilities through **Tavily Search** and **Beautiful Soup**, enabling the research agent to retrieve relevant information from the web when needed.

## 🚀 Key Features

- **Dynamic Agent Routing** — Selects the appropriate agents based on the user's request.
- **Code Generation** — Generates code according to user requirements.
- **Code Review** — Analyzes code for potential bugs, logical errors, edge cases, and improvements.
- **Code Explanation** — Explains code and programming concepts clearly.
- **Web Research** — Uses Tavily to search for relevant information and identify useful webpages.
- **Website Scraping** — Extracts readable text from webpages using Requests and Beautiful Soup.
- **Structured Output** — Uses Pydantic to define the supervisor's routing decisions.
- **LCEL Pipelines** — Composes prompts, models, and output parsers into reusable workflows.
- **Agent Coordination** — Passes relevant outputs between selected agents.
- **Final Response Synthesis** — Combines relevant results into a unified answer.
- **Environment Configuration** — Loads API credentials through environment variables.

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │    User Request     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Supervisor Agent   │
                    │  Structured Routing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Selected Agents    │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
              Writer        Reviewer      Explainer
                 │             │             │
                 └─────────────┼─────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Final Response Agent│
                    └──────────┬──────────┘
                               │
                               ▼
                         Final Answer


              Research Agent (when invoked)
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
                Tavily Search      Website Scraper
                                   Requests + Beautiful Soup
```

The supervisor determines which specialist agents should execute and in what order. The research agent provides access to web search and webpage extraction tools when the workflow requires external information.

## 🧠 Agents and Responsibilities

| Agent | Responsibility |
|---|---|
| **Supervisor Agent** | Analyzes the request and selects agents in execution order. |
| **Writer Agent** | Generates code based on the user's requirements. |
| **Reviewer Agent** | Reviews code for potential errors, edge cases, and improvements. |
| **Explainer Agent** | Explains code or programming concepts. |
| **Research Agent** | Searches for relevant information and retrieves webpage content using its available tools. |
| **Final Response Agent** | Combines relevant agent outputs into the final response. |

## 🔍 Research Tools

### 1. Tavily Search

Searches the web for information relevant to a query and returns search results that can help the research agent identify useful sources.

### 2. Website Scraper

Uses **Requests** to fetch webpage HTML and **Beautiful Soup** to extract readable text. The current implementation removes common non-content elements, such as scripts, styles, navigation, headers, and footers.

The scraper limits the returned text to 12,000 characters per page. Websites that block automated requests or require JavaScript rendering may not be accessible.

## ⚙️ How It Works

1. **User Request:** The user submits a coding task or programming question.
2. **Supervisor Routing:** The supervisor produces a structured decision identifying the agents required for the task.
3. **Agent Execution:** The pipeline executes the selected agents in the specified order.
4. **Web Research:** When invoked, the research agent uses Tavily Search and website scraping to gather relevant information.
5. **State Management:** The pipeline stores agent outputs and passes relevant information to subsequent agents.
6. **Response Synthesis:** The final response agent combines the available outputs into a single response.

## 📁 Project Structure

```text
multi-agent-code-assistant/
│
├── agents.py          # Research agent and tool registration
├── chains.py          # LCEL chains and processing workflows
├── model.py           # Groq model and Tavily configuration
├── prompts.py         # Prompts for agents and supervisor
├── supervisor.py      # Structured supervisor routing
├── pipeline.py        # Main workflow and state management
├── tools.py           # Web search and webpage scraping tools
├── requirements.txt   # Project dependencies
├── .env               # Local API credentials (not committed)
├── .gitignore         # Files excluded from version control
└── README.md
```

### Core Modules

- **`model.py`** — Configures the language model and Tavily client.
- **`prompts.py`** — Stores the prompts used by the supervisor, specialist agents, and final response workflow.
- **`chains.py`** — Defines reusable LCEL chains by composing prompts, models, runnable components, and output parsers.
- **`supervisor.py`** — Defines the Pydantic schema and structured routing chain.
- **`pipeline.py`** — Coordinates agent execution, manages state, and produces the final response.
- **`agents.py`** — Defines the research agent and its available tools.
- **`tools.py`** — Implements web search and webpage text extraction.

## 🛠️ Technology Stack

- **Python** — Application logic
- **LangChain** — Agent creation and model integration
- **LangChain Core / LCEL** — Workflow composition
- **Groq** — Language-model inference
- **OpenAI GPT-OSS 20B** — Model configured through Groq
- **Pydantic** — Structured output validation
- **Tavily** — Web search
- **Requests** — HTTP requests
- **Beautiful Soup 4** — HTML parsing
- **python-dotenv** — Environment-variable management

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Muhammad-ShahFahad/multi-agent-code-assistant.git
cd multi-agent-code-assistant
```

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

Replace the placeholder values with your API keys. Ensure that the configured model is available through Groq.

**Security:** Never commit API keys or your `.env` file to GitHub.

Ensure your `.gitignore` includes:

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

## 📝 Example Requests

### Code Generation

```text
Write a Python function that checks whether a number is prime.
```

### Concept Explanation

```text
Explain how Retrieval-Augmented Generation (RAG) works.
```

### Code Review

```text
Review this Python list comprehension for syntax errors:
[num for num in numbers}
```

### Multi-Agent Task

```text
Write a Python function to calculate factorial,
review the implementation, and explain how it works.
```

The supervisor determines which agents are appropriate for each request. The selected workflow may vary depending on the task.

## 🔧 Current Limitations

- Agent selection depends on LLM-generated routing decisions.
- Code review relies on model reasoning and does not automatically execute or test code.
- Research quality depends on search results and webpage accessibility.
- Some websites may block scraping or require JavaScript rendering.
- User-provided code must be passed correctly to the reviewer.
- Model availability, API quotas, and rate limits depend on the configured providers.

## 🔮 Future Improvements

- Secure code execution and automated testing.
- Unit-test generation with `pytest`.
- Improved error handling, retries, and input validation.
- Stronger validation of supervisor routing decisions.
- Better source attribution and research verification.
- Conversation memory and streaming responses.
- Parallel execution for independent tasks.
- GitHub integration.
- A Streamlit user interface.
- LangGraph-based orchestration for more advanced stateful workflows.

## 🎯 Learning Objectives

This project explores practical Generative AI engineering concepts:

- Multi-agent architecture and orchestration.
- Supervisor-based routing.
- Tool calling and web research.
- LangChain Expression Language (LCEL).
- Structured output with Pydantic.
- State management and sequential execution.
- Prompt engineering.
- External API integration.
- Multi-step LLM workflows.

## 👨‍💻 Author

**Muhammad Shah Fahad**

BS Computer Science | Machine Learning & Generative AI Learner

This project is part of my journey toward building practical Generative AI applications and developing expertise in agent orchestration, LLM workflows, and AI engineering.


*Built with Python, LangChain, and Groq.*
