import asyncio
from agents import Agent, ModelSettings, Runner
from utils.model_setup import gemini_model
from utils.search_tool import GoogleSearchTool

class RiskAgent:
    """
    Risk Agent with Google Search integration:
    Analyzes portfolio summary data for risk factors, uses search tool for current market risk info,
    and generates a detailed risk assessment report.
    """

    DEFAULT_PROMPT = """
    You are a Portfolio Risk Assessor AI.
    You will be given a portfolio summary report from the Portfolio Agent as input.
    Your tasks:
    - Analyze the portfolio summary focusing on:
        - Concentration risks by sector or asset
        - Volatility exposure and potential downside risks
        - Emerging market or economic risks relevant to portfolio composition
    - Use the 'google_search' tool as needed to fetch current market volatility or risk news.
    - Generate a detailed risk assessment report with these sections:
        1. Summary of Key Risks
        2. Concentration Risks
        3. Market and Volatility Risks
        4. Risk Mitigation Suggestions

    Write clearly and concisely, assuming the portfolio summary is accurate and complete. No HTML.
    """

    def __init__(self, model = None, instructions = None, tools = None, model_settings = None):
        self.model = model if model else gemini_model
        self.instructions = instructions if instructions else self.DEFAULT_PROMPT
        self.search_tool = GoogleSearchTool()
        self.tools = tools if tools else [self.search_tool.as_tool()]
        self.model_settings = model_settings if model_settings else ModelSettings(tool_choice="required")
        self.agent = Agent(
            name = "Risk Agent",
            instructions = self.instructions,
            model = self.model,
            tools = self.tools,
            model_settings = self.model_settings
        )
    
    async def analyze_risks_async(self, portfolio_summary: str) -> str:
        result = await Runner.run(self.agent, portfolio_summary)
        return result.final_output