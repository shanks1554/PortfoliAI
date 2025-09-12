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
    You will receive portfolio summary data including assets, allocations, and valuations.
    Your Tasks:
    - Identify and explain portfolio risk factors such as over-concentration, volatility exposure, sector or geographic risks.
    - Fetch recent market volatility indices or news using the 'google_search' tool when necessary.
    - Provide a clear risk assessment report with sections:
        1. Summary of key risks
        2. Concentration risks
        3. Market risks and volatility
        4. Risk mitigation suggestions
    Write the report in professional, clear language without HTML.
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