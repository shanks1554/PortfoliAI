import os
import requests
from dotenv import load_dotenv
from agents import function_tool

load_dotenv(override=True)

class GoogleSearchTool:
    """Reusable Google Search Tool for agents."""
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cse_id = os.getenv("GOOGLE_CSE_ID")
        self.num_results = 5
        if not self.api_key:
            raise ValueError("Google API Key not found")
        if not self.cse_id:
            raise ValueError("Google CSE ID not found.")

    def _search_impl(self, query: str) -> str:
        f"""Internal implementation of Google Search API Call."""
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.cse_id,
            "q": query,
            "num": self.num_results
        }

        try:
            resp = requests.get(url, params = params)
            resp.raise_for_status()
            data = resp.json()

            results = []
            for item in data.get("items", []):
                title = item.get("title", "No Title")
                snippet = item.get("snippet", "No Description")
                link = item.get("link", "")
                results.append(f"{title}: {snippet} ({link})")
            
            return "\n".join(results) if results else "No result found."
        except Exception as e:
            return f"Google search failed: {e}"
    
    def as_tool(self):
        """Return a decorator function_tool for use in agents."""
        @function_tool
        def google_search(query: str) -> str:
            """Search the web using Google Custom Search and return top results."""
            return self._search_impl(query)
        
        return google_search    