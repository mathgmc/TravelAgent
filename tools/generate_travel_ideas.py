from settings.config import get_llm_global
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def generate_travel_ideas_prompt() -> str:
    """
    Generate a prompt for generating travel ideas based on user interests.
    """
    return ChatPromptTemplate(
        [
            (
                "system",
                """
                You are a travel agent. Based on the user's travel interests, generate a list of travel ideas.
                
                For example, if the user has interests in beaches, mountains, or cultural experiences,
                you should generate travel ideas that align with those interests.

                Your response should be a list of travel ideas relevant to the user's interests.
                """,
            ),
            (
                "user",
                """
                Generate travel ideas based on the following extracted travel interests: {travel_interests}
                And the user's question: {question}
                Please provide a list of travel ideas that match the user's interests.
                """,
            ),
        ]
    )

def llm_generate_travel_ideas(travel_interests: list[str], question: str) -> str:
    """
    Generate travel ideas using the LLM based on the user's travel interests.
    
    Args:
        travel_interests (list[str]): A list of travel interests.
        question (str): The user's question to provide context for the travel ideas.
    
    Returns:
        str: A string containing generated travel ideas.
    """
    prompt = generate_travel_ideas_prompt()
    llm = get_llm_global()
    parser = StrOutputParser()
    chain = prompt | llm | parser
    response = chain.invoke(
        {
            "travel_interests": travel_interests,
            "question": question,
        }
    )
    return response
