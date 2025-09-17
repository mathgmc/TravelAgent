from config import get_llm_global
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from models.agent_state import AgentState


def generate_travel_ideas_prompt() -> ChatPromptTemplate:
    """Create a prompt that grounds travel ideas in user interests and trip constraints."""
    return ChatPromptTemplate(
        [
            (
                "system",
                """
                You are a travel agent planning an itinerary. Combine the user's stated interests with
                their practical constraints like departure location, budget, and trip length. When you
                suggest activities or destinations, prefer options that fit within the provided budget
                and can be completed in the available days starting from the departure location.

                Answer with a conversational yet concise description of recommended destinations,
                activities, and tips that align with the interests and constraints.
                """,
            ),
            (
                "user",
                """
                Interests: {travel_interests}
                Departure location: {address}
                Budget (USD): {trip_maximum_cost_usd}
                Available days: {amount_of_days}

                Provide tailored travel ideas.
                """,
            ),
        ]
    )


def llm_generate_travel_ideas(agent_state: AgentState) -> str:
    """
    Generate travel ideas using the LLM based on the user's travel interests and constraints.

    Args:
        agent_state (AgentState): Current state containing interests and constraints.

    Returns:
        str: A string containing generated travel ideas.
    """
    prompt = generate_travel_ideas_prompt()
    llm = get_llm_global()
    parser = StrOutputParser()
    chain = prompt | llm | parser
    travel_interests = agent_state.get("travel_interests", [])
    response = chain.invoke(
        {
            "travel_interests": travel_interests,
            "address": agent_state.get("address") or "unknown",
            "trip_maximum_cost_usd": agent_state.get("trip_maximum_cost_usd") or "unknown",
            "amount_of_days": agent_state.get("amount_of_days") or "unknown",
        }
    )
    return response
