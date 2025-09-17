from travel_agent import create_workflow

def visualize_workflow():
    """Generate and save a visualization of the travel agent workflow."""
    # Get the graph visualization
    workflow = create_workflow()
    compiled_workflow = workflow.compile()
    graph = compiled_workflow.get_graph()
    
    # Generate and save the Mermaid PNG
    png_bytes = graph.draw_mermaid_png()
    with open("travel_agent_workflow.png", "wb") as png_file:
        png_file.write(png_bytes)
    print("Graph visualization saved as 'travel_agent_workflow.png'")

if __name__ == "__main__":
    visualize_workflow() 
