from langgraph.graph import END, START, StateGraph

from nodes.find_travel_interests import find_travel_interests
from models.agent_state import AgentState

def add_nodes(workflow):
    """Add nodes to the workflow graph."""
    workflow.add_node("find_travel_interests", find_travel_interests)

def add_edges(workflow):
    """Add edges to the workflow graph."""
    workflow.add_edge(START, "find_travel_interests")
    workflow.add_edge("find_travel_interests", END)

def create_workflow():
    """Create the travel agent workflow graph."""
    workflow = StateGraph(AgentState)

    add_nodes(workflow)
    add_edges(workflow)

    return workflow

AGENT = create_workflow().compile()

def agent_run():
    question = input("Hello! I'm your travel agent. What are your travel interests? ")

    while question.lower() != "exit":
        agent_state = AGENT.invoke(
            {
                "question": question,
                "travel_interests": [],
                "selected_destinations": [],
            }
        )
        print(f"Identified travel interests: {agent_state['travel_interests']}")
        question = input("What else would you like to know? (type 'exit' to quit) ")

if __name__ == "__main__":
    agent_run()
