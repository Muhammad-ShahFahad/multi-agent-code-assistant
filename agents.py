from tools import web_search, scrape_website
from langchain.agents import create_agent
from model import model, tavily_client

# Web_search agent
web_search_agent = create_agent(
    model=model,
    tools=[web_search, scrape_website],
    system_prompt="""
    You are a research agent.

    Search the web for relevant information.
    Scrape useful websites when necessary.
    Analyze the collected information.
    Answer the user's question using evidence.
    Include source URLs in your answer.
    """
)

