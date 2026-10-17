# A supervsior agent responsible for calling agents as per-requirement
from typing import Literal
from pydantic import BaseModel, Field
from model import model
from prompts import supervisor_prompt
from chains import output_parser
from rich import print



# Agents
AgentName = Literal[
    "writer",
    "explainer",
    "reviewer"
]

# Supervisor's decision structure
class supervisor_decision(BaseModel):
    agents: list[AgentName] = Field(
        description = "The agent that should be executed in order."
    )

    reason: str = Field(
        description= "why these agents were selected."
    )

# Supervisor chain
supervisor_agent_chain = supervisor_prompt | model.with_structured_output(supervisor_decision)