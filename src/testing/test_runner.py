from typing import Any, Dict, List

from src.agents.agent_config import AgentConfig
from src.agents.agent_runner import AgentRunner
from src.core.evaluator import Evaluator
from src.core.failure_classifier import classify_failure


class TestRunner:

    def __init__(
        self,
        agent: AgentConfig,
        evaluator: Evaluator
    ):

        self.agent = agent
        self.agent_runner = AgentRunner(agent)
        self.evaluator = evaluator

    def run_test(
        self,
        scenario: Dict[str, Any]
    ) -> Dict[str, Any]:

        execution = self.agent_runner.run(
            scenario=scenario.get(
                "scenario",
                ""
            ),
            expected_behavior=scenario.get(
                "expected_behavior",
                ""
            )
        )

        evaluation = self.evaluator.evaluate(
            scenario=scenario,
            agent_response=execution.get(
                "agent_response",
                ""
            )
        )

        result = {
            "test_id": scenario.get(
                "id"
            ),
            "category": scenario.get(
                "category",
                "Unknown"
            ),
            "scenario": scenario.get(
                "scenario",
                ""
            ),
            "expected_behavior": scenario.get(
                "expected_behavior",
                ""
            ),
            **evaluation,
        }

        return classify_failure(result)

    def run_suite(
        self,
        scenarios: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:

        results = []

        for scenario in scenarios:

            result = self.run_test(
                scenario
            )

            results.append(result)

        return results