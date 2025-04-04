from travel_agent import workflow

def visualize_workflow():
    """Generate and save a visualization of the travel agent workflow."""
    # Get the graph visualization
    graph = workflow.get_graph()
    
    # Generate and save the Mermaid PNG
    graph.draw_mermaid_png("travel_agent_workflow.png")
    print("Graph visualization saved as 'travel_agent_workflow.png'")

if __name__ == "__main__":
    visualize_workflow() 