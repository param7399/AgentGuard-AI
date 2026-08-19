from dataclasses import dataclass, field
from typing import List


@dataclass
class AgentConfig:
    name: str
    objective: str
    system_prompt: str
    tools: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "objective": self.objective,
            "system_prompt": self.system_prompt,
            "tools": self.tools,
        }


def create_agent_config(
    name: str,
    objective: str,
    system_prompt: str,
    tools
) -> AgentConfig:

    if isinstance(tools, str):
        tools = [
            tool.strip()
            for tool in tools.splitlines()
            if tool.strip()
        ]

    return AgentConfig(
        name=name.strip(),
        objective=objective.strip(),
        system_prompt=system_prompt.strip(),
        tools=tools,
    )