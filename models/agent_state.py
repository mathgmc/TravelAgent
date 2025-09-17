from typing import List

from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict


class AgentState(TypedDict, total=False):
    """Mutable state shared between workflow nodes."""

    messages: List[BaseMessage]
    question: str
    travel_interests: List[str]
    selected_destinations: List[str]
    address: str
    trip_maximum_cost_usd: float
    amount_of_days: int
    answer: str
    missing_fields: List[str]
