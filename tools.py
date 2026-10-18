from model import tavily_client
from rich import print
from langchain_core.tools import tool
from bs4 import BeautifulSoup
import requests

# Tool for web_search
@tool
def web_search(query: str):
    """Search the web for information relevant to the user's query."""

    response = tavily_client.search(
        query=query,
        max_results=5
    )

    return response

# Tool for web_scrapping
@tool
def scrape_website(url: str) -> str:
    """Fetch a webpage and extract its reabable text content."""

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={"User-Agent":"Mozilla/5.0"}
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unnecessary HTML elements
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        # Extract readable text
        text = soup.get_text(separator=" ", strip=True)
        return text[:12000]
    except requests.RequestException as e:
        return f"Error fetching webpage: {e}"
