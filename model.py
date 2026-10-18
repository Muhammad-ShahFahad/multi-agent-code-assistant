import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv(override=True)

# Initialize LLM using Groq
model = init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq",
    temperature=0
)

# Initialize Tavily search
tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)
