from models.agent_state import AgentState
from tools.generate_travel_ideas import llm_generate_travel_ideas


def generate_travel_ideas(agent_state: AgentState):
    """
    Generate travel ideas based on the agent state.
    
    Args:
        agent_state (AgentState): The current state of the agent.
    
    Returns:
        AgentState: Updated agent state with generated travel ideas.
    """
    
    # Extract travel interests from the agent state
    travel_interests = agent_state.get("travel_interests", [])


    answer = llm_generate_travel_ideas(travel_interests)
    
    return {
        "answer": answer,
    }