from typing import List

from langchain_core.messages import BaseMessage
from typing_extensions import NotRequired, TypedDict


class AgentState(TypedDict):
    """
    AgentState is a TypedDict that represents the state of an agent.

    Attributes:
        messages (List[BaseMessage]): A list of messages exchanged with the agent.
        tools (List[str]): A list of tools available to the agent.
        tool_index (int): The index of the tool currently in use by the agent.
    """

    messages: List[BaseMessage]
    question: str
    travel_interests: List[str]
    selected_destinations: List[str]
    address: str
    trip_maximum_cost_usd: float
    amount_of_days: int
    answer: str
    missing_fields: NotRequired[List[str]]
