import asyncio
from agents import Agent, ModelSettings, Runner
from utils.model_setup import gemini_model
from utils.search_tool import GoogleSearchTool

class PortfolioAgent:
    """
    Portfolio Agent with Google Search integration:
    Analyzes user investment portfolios, uses search tool to ensure up-to-date asset prices,
    calculates key metrics, and generates detailed portfolio insights.
    """

    DEFAULT_PROMPT = """
    You are a Portfolio Analyzer AI.
    The user will provide their investment portfolio data (as table, CSV, or JSON).
    Use the 'google_search' tool to fetch the latest accurate asset prices when needed.
    Your tasks:
    - Parse the portfolio, listing assets, units, purchase and current value.
    - Validate and update asset prices using search results.
    - Calculate asset allocations (%), top holdings, and diversification (sector/type).
    - Highlight over-concentration/diversification issues.
    - Output 4 sections: Summary, Asset Allocations, Diversification Analysis, Observations.
    Respond in clear, concise, professional English. No HTML.
    """

    def __init__(self, model = None, instructions = None, tools = None, model_settings = None) -> None:
        self.model = model if model else gemini_model
        self.instructions = instructions if instructions else self.DEFAULT_PROMPT
        self.search_tools = GoogleSearchTool()
        self.tools = tools if tools else [self.search_tools.as_tool()]
        self.model_settings = model_settings if model_settings else ModelSettings(tool_choice="required")
        self.agent = Agent(
            name = "Portfolio Agent with Search",
            instructions = self.instructions,
            model = self.model,
            tools = self.tools,
            model_settings = self.model_settings
        )
    
    async def analyze_portfolio_async(self, portfolio_data: str) -> str:
        result = await Runner.run(self.agent, portfolio_data)
        return result.final_output
    
    def run(self, portfolio_data: str) -> str:
        """
        Synchronous method to run the agent and get output.
        Wraps async analyze_portfolio_async in event loop.
        """
        return asyncio.run(self.analyze_portfolio_async(portfolio_data))