from agents import Agent, Runner, ModelSettings
from utils.model_setup import gemini_model
from utils.search_tool import GoogleSearchTool

class ResearchAgent:
    """
    Research Agent with Google Search integration:
    Uses the search tool to gather recent financial data,
    synthesizes market outlook, company insights, risks, and opportunities,
    and generates a structures research report.
    """

    DEFAULT_PROMPT = """
    You are a Financial Research Assistant AI.
    You will receive a user query or portfolio context describing the assets of interest.
    Your tasks:
    - Use the 'google_search' tool to gather recent, authoritative financial data related to the portfolio’s assets or relevant market sectors.
    - Summarize your findings in these sections:
        1. Market Overview
        2. Company Insights
        3. Risks
        4. Opportunities
        5. References

    Maintain a professional tone and base your report solely on the search results. No HTML.
    """

    def __init__(self, model = None, instructions = None, tools = None, model_settings = None) -> None:
        self.model = model if model else gemini_model
        self.instructions = instructions if instructions else self.DEFAULT_PROMPT
        self.search_tools = GoogleSearchTool()
        self.tools = tools if tools else [self.search_tools.as_tool()]
        self.model_settings = model_settings if model_settings else ModelSettings(tool_choice="required")
        self.agent = Agent(
            name = "Research Agent with Search",
            instructions = self.instructions,
            model = self.model,
            tools = self.tools,
            model_settings = self.model_settings
        )
    
    async def research_async(self, input: str) -> str:
        result = await Runner.run(self.agent, input)
        return result.final_output
    