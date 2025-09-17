from models.agent_state import AgentState
from tools.extract_travel_interests import extract_user_travel_interests


def find_travel_interests(agent_state: AgentState):
    """Update the state with any new interests mentioned in the latest message."""

    question = agent_state.get("question")
    if not question:
        return {}

    existing_interests = agent_state.get("travel_interests", [])
    new_interests = extract_user_travel_interests(question)
    deduped_interests = list(set(existing_interests + new_interests))

    return {"travel_interests": deduped_interests}
