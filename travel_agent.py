from langgraph.graph import END, START, StateGraph

from nodes.ask_for_missing_fields import ask_for_missing_fields
from nodes.check_required_fields import check_required_fields
from nodes.find_travel_interests import find_travel_interests
from nodes.generate_ideas import generate_travel_ideas
from models.agent_state import AgentState


def add_nodes(workflow):
    """Add nodes to the workflow graph."""
    workflow.add_node("check_required_fields", check_required_fields)
    workflow.add_node("ask_for_missing_fields", ask_for_missing_fields)
    workflow.add_node("find_travel_interests", find_travel_interests)
    workflow.add_node("generate_travel_ideas", generate_travel_ideas)


def route_after_checks(agent_state: AgentState):
    missing_fields = agent_state.get("missing_fields", [])
    if missing_fields:
        return "missing"
    return "complete"


def add_edges(workflow):
    """Add edges to the workflow graph."""
    workflow.add_edge(START, "find_travel_interests")
    workflow.add_edge("find_travel_interests", "check_required_fields")
    workflow.add_conditional_edges(
        "check_required_fields",
        route_after_checks,
        {
            "missing": "ask_for_missing_fields",
            "complete": "generate_travel_ideas",
        },
    )
    workflow.add_edge("ask_for_missing_fields", END)
    workflow.add_edge("generate_travel_ideas", END)


def create_workflow():
    """Create the travel agent workflow graph."""
    workflow = StateGraph(AgentState)

    add_nodes(workflow)
    add_edges(workflow)

    return workflow


AGENT = create_workflow().compile()


def agent_run():
    question = input(
        "Hello! I'm your travel agent. Please, to start, tell me: "
        "\n- Where you are?"
        "\n- How much you want to spent in USD?"
        "\n- How many days you wish to travel?"
        "\n- What kinds of travel experiences you enjoy?\n"
    )
    agent_state = AgentState()
    while question.lower() != "exit":
        agent_state["question"] = question
        agent_state = AGENT.invoke(agent_state)
        #print(f"Identified travel interests: {agent_state['travel_interests']}")
        print(f"Answer: {agent_state['answer']}")
        question = input("Write you message (type 'exit' to quit): ")


if __name__ == "__main__":
    agent_run()
