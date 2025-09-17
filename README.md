# TravelAgent

TravelAgent is a lightweight LangGraph agent built to experiment with LangChain and LangGraph concepts for conversational trip planning.

![Travel Agent Workflow](travel_agent_workflow.png)

## Overview
- Maintains an `AgentState` that collects key trip details and the running conversation.
- Relies on LangChain prompt templates and structured output parsers to normalize user inputs.
- Uses LangGraph to orchestrate nodes that extract missing information and generate tailored travel ideas.
- Ships with a Mermaid-based graph render so you can inspect how information moves through the workflow.

## How It Works
1. `check_required_fields` extracts core trip requirements (origin, budget, trip length, interests).
2. `find_travel_interests` expands the list of interests mentioned across the chat.
3. `ask_for_missing_fields` prompts the traveler for any remaining gaps.
4. `generate_travel_ideas` calls the LLM for recommendations once the state is complete.

## Project Structure
- `travel_agent.py` assembles the workflow graph and provides a simple CLI runner.
- `nodes/` contains the LangGraph node functions responsible for state transitions.
- `tools/` wraps LangChain prompt/LLM helpers used by the nodes.
- `models/` defines the shared `AgentState` and Pydantic parsers for structured outputs.
- `visualize_graph.py` regenerates `travel_agent_workflow.png` from the compiled graph.

## Getting Started
1. Create a virtual environment and install dependencies: `pip install -r requirements.txt`.
2. Export an OpenAI-compatible API key (e.g. `export OPENAI_API_KEY=...`).
3. Run the CLI: `python travel_agent.py`.
4. Type `exit` to close the session.

To update the workflow diagram run `python visualize_graph.py`; the image will be saved as `travel_agent_workflow.png`.
