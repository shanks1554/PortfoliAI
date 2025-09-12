from agents import Agent, Runner, ModelSettings
from utils.model_setup import gemini_model
from utils.search_tool import GoogleSearchTool

class RecommendationAgent:
    """
    Recommendation Agent:
    Synthesizes portfolio summary, risk assessment, and research inputs
    to generate peronalized investment recommendations with rationales and next steps.
    """

    DEFAULT_PROMPT = """
    You are an Investment Recommendation AI.
    You will receive the following:

    Portfolio Summary: {portfolio_summary}

    Risk Assessment: {risk_assessment}

    Portfolio-related Research: {portfolio_research}

    Risks-related Research: {risk_research}

    Your task:
    - Analyze and synthesize all of the above information.
    - Provide clear, personalized investment recommendations.
    - Include rationales and actionable next steps.
    - Structure output into:
        1. Personalized Suggestions
        2. Rationales
        3. Next Steps

    Use the 'google search' tool if required.
    Write in professional, concise language. No HTML.
    """

    def __init__(self, model = None, instructions = None, tools = None, model_settings = None) -> None:
        self.model = model if model else gemini_model
        self.instructions = instructions if instructions else self.DEFAULT_PROMPT
        self.search_tools = GoogleSearchTool()
        self.tools = tools if tools else [self.search_tools.as_tool()]
        self.model_settings = model_settings if model_settings else ModelSettings(tool_choice="required")
        self.agent = Agent(
            name = "Recommendation Agent with Search",
            instructions = self.instructions,
            model = self.model,
            tools = self.tools,
            model_settings = self.model_settings
        )
    
    async def analyze_recommendation_async(
        self,
        portfolio_summary: str,
        risk_assessment: str,
        portfolio_research: str,
        risks_research: str
    ) -> str:
        full_prompt = self.instructions.format(
            portfolio_summary = portfolio_summary,
            risk_assessment = risk_assessment,
            portfolio_research = portfolio_research,
            risk_research = risks_research
        )
        result = await Runner.run(self.agent, full_prompt)
        return result.final_output