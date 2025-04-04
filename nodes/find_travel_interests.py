from config import LLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser

from models.agent_state import AgentState
from models.llm_parsers import FindUserInterestsParser




def get_travel_interests_prompt() -> str:
    """
    Generate a prompt for the travel interests question.
    """
    return ChatPromptTemplate(
        [
            (
                "system",
                """
                You are a travel agent. Based on the user's question, identify their travel interests.
                Your response should be a list of travel interests.
                
                For example, if the user asks about beaches, mountains, or cultural experiences,
                you should identify those as their travel interests and return them in a list format:
                ["beaches", "mountains", "cultural experiences"]

                If you cannot identify any travel interests, return an empty list:
                []

                If the user say that he like a specific destination, you should identify the categories 
                that the destination belongs to and return them in a list format, for example:
                Question: "I like Paris"
                Answer: ["cultural experiences", "historical sites", "romantic getaways"]

                You can provide as many travel interests as you can identify, but make sure to keep them relevant to the user's question.
                """,
            ),
            (
                "user",
                "What are the user's travel interests based on the following question: {question}",
            ),


        ]
    )
    

def find_travel_interests(agent_state: AgentState) -> str:
    """
    Find travel interests based on the user's input.
    Args:
        agent_state (AgentState): The current state of the agent.
    Returns:
        str: A string containing the travel interests.
    """
    # Extract the question from the agent state
    question = agent_state["question"]

    # Use the LLM to generate travel interests based on the question
    prompt = get_travel_interests_prompt()
    chain = prompt | LLM | JsonOutputParser(pydantic_object=FindUserInterestsParser)
    travel_interests = chain.invoke({"question": question})

    return {"travel_interests": travel_interests}

    # # Check if the travel interests are empty
    # if not travel_interests:
    #     return {"found_travel_interests": False}
    
    # # If travel interests are found, update the agent state
    # agent_state["travel_interests"] = travel_interests
    # return {"found_travel_interests": True}