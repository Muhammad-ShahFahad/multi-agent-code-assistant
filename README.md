🤖 LLM-Based Multi-Agent Code Assistant

A **multi-agent AI code assistant** built with **Python, LangChain, and Groq**. The system dynamically decides which specialized agents should handle a user's coding request and then combines their outputs into a final response.

🚀 Overview

Instead of using a single LLM for every task, this project uses multiple specialized agents:

- **Writer Agent** — Generates the requested code.
- **Reviewer Agent** — Reviews the generated code for errors, edge cases, and improvements.
- **Explainer Agent** — Explains the code in a clear and understandable way.
- **Supervisor Agent** — Decides which agents are needed and determines their execution order.
- **Final Response Agent** — Combines the relevant outputs into the final answer.

The important part is that the system is **dynamic**. For example:

```text
User Request
     ↓
Supervisor Agent
     ↓
Selects required agents
     ↓
Writer → Reviewer → Explainer
     ↓
Final Response Agent
     ↓
Final Answer
```

🧠 Architecture

```text
                    ┌──────────────────┐
                    │   User Request   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Supervisor Agent │
                    └────────┬─────────┘
                             ↓
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
          Writer         Reviewer       Explainer
              │              │              │
              └──────────────┼──────────────┘
                             ↓
                  ┌─────────────────────┐
                  │ Final Response Agent│
                  └──────────┬──────────┘
                             ↓
                       Final Answer
```

✨ Key Features

- Multi-agent architecture
- Dynamic agent selection
- Specialized coding, reviewing, and explaining agents
- Structured output from the supervisor using **Pydantic**
- LangChain LCEL chains
- Sequential agent execution
- Agents can pass outputs to other agents
- Final response synthesis
- No external tools required
- Environment variables for API key management

📁 Project Structure

```text
multi-agent-code-assistant/
│
├── agents.py
├── chains.py
├── model.py
├── prompts.py
├── supervisor.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── README.md
└── .env
```

`model.py`

Contains the LLM configuration.

The project uses a Groq-hosted OpenAI GPT OSS model through LangChain.

`prompts.py`

Contains the prompts for:

- Writer
- Reviewer
- Explainer
- Supervisor
- Final response

Keeping prompts separate makes the agents easier to modify and maintain.

`chains.py`

Creates the individual LangChain chains:

```text
Prompt → Model → Output Parser
```

`supervisor.py`

The supervisor decides which agents should execute.

It uses **Pydantic structured output** to return a predictable structure such as:

```python
{
    "agents": ["writer", "reviewer", "explainer"],
    "reason": "The user requested code, a review, and an explanation."
}
```

`pipeline.py`

Controls the complete workflow:

1. Receives the user request.
2. Calls the supervisor.
3. Executes the selected agents.
4. Passes generated code to reviewer/explainer when required.
5. Sends the outputs to the final response agent.
6. Returns the final answer.

`tools.py`

Reserved for future tool integrations. The current version intentionally uses **LLM-only agents**.

---

🔄 Example Workflow

User Request

```text
Write a Python function to check whether a number is prime.
Review the code and explain it.
```

Supervisor

The supervisor may decide:

```text
writer → reviewer → explainer
```

Writer

Generates the Python implementation.

Reviewer

Receives the writer's code and checks:

- Logical correctness
- Edge cases
- Code quality
- Efficiency

Explainer

Receives the code and explains how it works.

Final Response Agent

Combines the relevant outputs into one clean response for the user.

---

🛠️ Technologies

- **Python**
- **LangChain**
- **LangChain Core**
- **Groq**
- **Pydantic**
- **python-dotenv**

⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

Add it to `.gitignore`:

```text
.env
.venv/
__pycache__/
```
▶️ Running the Project

Run:

```bash
python pipeline.py
```

Then enter a coding request:

```text
Enter a topic you want to write code about:
```

Example:

```text
Write a Python function to reverse a string and review the code.
```

🎯 Project Goal

The goal of this project is to understand how **multi-agent LLM systems** can be designed using LangChain.

Instead of treating an LLM as one general-purpose assistant, the project separates responsibilities between specialized agents and uses a supervisor to coordinate them.

This project focuses particularly on:

- Agent orchestration
- Dynamic routing
- Structured LLM output
- LCEL
- State management
- Agent-to-agent communication
- Multi-step LLM workflows

🔮 Future Improvements

Possible future additions include:

- Streaming responses
- Better error handling
- Parallel agent execution where appropriate
- Conversation memory
- More specialized coding agents
- Unit-test generation
- Code execution and testing
- GitHub integration
- Web/documentation research agents
- LangGraph-based orchestration

👨‍💻 Author

**Muhammad Shah Fahad**

BS Computer Science | Machine Learning & Generative AI Learner

This project is part of my learning journey into **Generative AI, LangChain, and multi-agent systems**.