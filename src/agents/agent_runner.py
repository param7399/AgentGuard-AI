from datetime import datetime
from typing import Any, Dict

from src.agents.agent_config import AgentConfig
from src.agents.mock_tools import execute_mock_tool


class AgentRunner:

    def __init__(self, agent: AgentConfig):
        self.agent = agent

    def run(
        self,
        scenario: str,
        expected_behavior: str = ""
    ) -> Dict[str, Any]:

        start_time = datetime.now()

        response = self._simulate_agent_response(
            scenario
        )

        end_time = datetime.now()

        return {
            "agent_name": self.agent.name,
            "scenario": scenario,
            "expected_behavior": expected_behavior,
            "agent_response": response,
            "started_at": start_time.isoformat(),
            "completed_at": end_time.isoformat(),
            "tools_available": self.agent.tools,
            "status": "completed"
        }

    def _simulate_agent_response(
        self,
        scenario: str
    ) -> str:

        scenario_lower = scenario.lower()

        if "tool" in scenario_lower and "error" in scenario_lower:
            return (
                "The requested tool encountered an error. "
                "I cannot confirm the operation as successful."
            )

        if "destination" in scenario_lower:
            return (
                "I need the destination before I can search "
                "for available flights."
            )

        if "safety" in scenario_lower:
            return (
                "I cannot bypass the required safety "
                "confirmation."
            )

        if "unrelated" in scenario_lower:
            return (
                "I should remain focused on the agent's "
                "defined objective."
            )

        return (
            "I will process the request according to "
            "the agent's defined objective and available tools."
        )

    def execute_tool(
        self,
        tool_name: str,
        **kwargs
    ) -> Dict[str, Any]:

        if tool_name not in self.agent.tools:

            return {
                "success": False,
                "tool": tool_name,
                "error": "Tool is not available to this agent."
            }

        return execute_mock_tool(
            tool_name,
            **kwargs
        )