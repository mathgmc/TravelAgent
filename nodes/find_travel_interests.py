from schemas.agent_state import AgentState
from tools.extract_travel_interests import extract_user_travel_interests


def find_travel_interests(agent_state: AgentState):
    """
    Extract travel interests from the agent state.
    
    Args:
        agent_state (AgentState): The current state of the agent.
    
    Returns:
        AgentState: Updated agent state with identified travel interests.
    """
    
    travel_interests = extract_user_travel_interests(agent_state)

    return {
        "travel_interests": travel_interests,
    }