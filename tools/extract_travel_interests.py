from settings.config import get_llm_global
from langchain_core.prompts import ChatPromptTemplate

from schemas.llm_parsers import FindUserInterestsParser


def generate_travel_interests_prompt() -> str:
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
                **["beaches", "mountains", "cultural experiences"]**

                If you cannot identify any travel interests, return an empty list:
                **[]**

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


def extract_user_travel_interests(question: str) -> list[str]:
    """
    Extract travel interests from the user's question using the LLM.
    Args:
        question (str): The user's question containing travel interests.
    Returns:
        List[str]: A list of identified travel interests.
    """
    # Use the LLM to generate travel interests based on the question
    prompt = generate_travel_interests_prompt()
    llm = get_llm_global()
    structured_llm = llm.with_structured_output(FindUserInterestsParser)
    chain = prompt | structured_llm
    travel_interests = chain.invoke({"question": question})
    return travel_interests.interests
