import asyncio
import nest_asyncio
from typing import Any, Annotated

from langgraph.graph import StateGraph, START
from pydantic import BaseModel, Field

# Import your agents
from ai_agents.PortfolioAgent import PortfolioAgent
from ai_agents.ResearchAgent import ResearchAgent
from ai_agents.RiskAgent import RiskAgent
from ai_agents.RecommendationAgent import RecommendationAgent

# Apply nest_asyncio for environments like Jupyter/Colab
nest_asyncio.apply()


# === Reducer function ===
def keep_first_value(current_value, new_value):
    return current_value if current_value is not None else new_value


# === Portfolio State ===
class PortfolioState(BaseModel):
    portfolio_data: Annotated[Any, keep_first_value] = Field(..., frozen=True)
    portfolio_summary: str | None = None
    risk_assessment: str | None = None
    portfolio_research: str | None = None
    risk_research: str | None = None
    recommendation: str | None = None


# === Main Workflow Class ===
class PortfolioWorkflow:
    def __init__(self):
        self.workflow = self._build_workflow()

    # --- Node Functions ---
    async def run_portfolio_agent(self, state: PortfolioState) -> dict:
        agent = PortfolioAgent()
        summary = await agent.analyze_portfolio_async(state.portfolio_data)
        return {"portfolio_summary": summary}

    async def run_risk_agent(self, state: PortfolioState) -> dict:
        agent = RiskAgent()
        risks = await agent.analyze_risks_async(state.portfolio_summary)
        return {"risk_assessment": risks}

    async def run_portfolio_research_agent(self, state: PortfolioState) -> dict:
        agent = ResearchAgent()
        research = await agent.research_async(state.portfolio_summary)
        return {"portfolio_research": research}

    async def run_risk_research_agent(self, state: PortfolioState) -> dict:
        agent = ResearchAgent()
        research = await agent.research_async(state.risk_assessment)
        return {"risk_research": research}

    async def run_recommendation_agent(self, state: PortfolioState) -> dict:
        agent = RecommendationAgent()
        recommendation = await agent.analyze_recommendation_async(
            portfolio_summary=state.portfolio_summary,
            portfolio_research=state.portfolio_research,
            risk_assessment=state.risk_assessment,
            risks_research=state.risk_research,
        )
        return {"recommendation": recommendation}

    # --- Workflow Builder ---
    def _build_workflow(self):
        workflow = StateGraph(PortfolioState)

        workflow.add_node("portfolio_agent", self.run_portfolio_agent)
        workflow.add_node("risk_agent", self.run_risk_agent)
        workflow.add_node("portfolio_research_agent", self.run_portfolio_research_agent)
        workflow.add_node("risk_research_agent", self.run_risk_research_agent)
        workflow.add_node("recommendation_agent", self.run_recommendation_agent)

        workflow.add_edge(START, "portfolio_agent")
        workflow.add_edge("portfolio_agent", "risk_agent")
        workflow.add_edge("portfolio_agent", "portfolio_research_agent")
        workflow.add_edge("risk_agent", "risk_research_agent")
        workflow.add_edge("portfolio_research_agent", "recommendation_agent")
        workflow.add_edge("risk_research_agent", "recommendation_agent")

        return workflow.compile()

    # --- Runner ---
    async def run(self, portfolio_data: str):
        initial_state = PortfolioState(portfolio_data=portfolio_data)
        final_state = await self.workflow.ainvoke(initial_state)

        results = {
            "Portfolio Analysis": final_state.get("portfolio_summary"),
            "Portfolio Risk": final_state.get("risk_assessment"),
            "Portfolio Research": final_state.get("portfolio_research"),
            "Risk Research": final_state.get("risk_research"),
            "Recommendation": final_state.get("recommendation"),
        }
        return results

    # ✅ Sync wrapper for Streamlit or normal Python
    def run_sync(self, portfolio_data: str):
        return asyncio.run(self.run(portfolio_data))


# === CLI Entry Point ===
async def main():
    workflow = PortfolioWorkflow()

    # Get portfolio data manually from the user
    print("Enter your portfolio data (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    portfolio_data = "\n".join(lines)

    results = await workflow.run(portfolio_data)

    for k, v in results.items():
        print(f"\n=== {k} ===\n{v}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
