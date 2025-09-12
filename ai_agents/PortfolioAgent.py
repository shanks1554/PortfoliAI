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
    The user will provide their raw investment portfolio data (as a table, CSV, or JSON).
    Your tasks:
    - Parse the portfolio data listing assets, quantities, purchase prices, and current values.
    - Calculate asset allocation percentages, top holdings, and diversification by sector.
    - Highlight any major concentration or diversification issues.
    - Output a clear and structured report with these sections:
        1. Summary
        2. Asset Allocations
        3. Diversification Analysis
        4. Observations

    This output will be used by other agents, so be concise but comprehensive.
    Respond in clear, professional English. No HTML.
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
    
    