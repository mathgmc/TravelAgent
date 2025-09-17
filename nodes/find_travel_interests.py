from models.agent_state import AgentState
from tools.extract_travel_interests import extract_user_travel_interests


def find_travel_interests(agent_state: AgentState):
    """Update the state with any new interests mentioned in the latest message."""

    question = agent_state.get("question", "")
    if not question:
        return {}

    new_interests = extract_user_travel_interests(question)

    existing_interests = agent_state.get("travel_interests", [])
    combined_interests = [
        interest
        for interest in existing_interests + new_interests
        if interest
    ]

    # Preserve insertion order while removing duplicates.
    deduped_interests = list(dict.fromkeys(combined_interests))

    updates = {
        "travel_interests": deduped_interests,
    }

    if deduped_interests:
        missing_fields = agent_state.get("missing_fields", [])
        updated_missing = [
            field for field in missing_fields if field != "travel_interests"
        ]
        if updated_missing != missing_fields:
            updates["missing_fields"] = updated_missing

    return updates
