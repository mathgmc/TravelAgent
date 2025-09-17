from config import get_llm_global
from langchain_core.prompts import ChatPromptTemplate

from models.llm_parsers import RequiredTripDetailsParser


def _build_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate(
        [
            (
                "system",
                """
                You are helping a travel agent collect required trip planning details from the user.
                Analyze the user's latest message and extract the following fields when possible:
                - address: the city, region, or address the user will depart from.
                - trip_maximum_cost_usd: the maximum travel budget in USD as a number.
                - amount_of_days: the number of days the user plans to travel as an integer.

                Respond using JSON that matches the provided schema. Use null when information is
                not explicitly provided. Do not guess.
                """,
            ),
            (
                "user",
                "User message: {question}",
            ),
        ]
    )


def extract_required_trip_details(question: str) -> RequiredTripDetailsParser:
    """Extract required trip planning fields from the user's latest message."""
    if not question:
        return RequiredTripDetailsParser()

    prompt = _build_prompt()
    llm = get_llm_global()
    structured_llm = llm.with_structured_output(RequiredTripDetailsParser)
    chain = prompt | structured_llm
    return chain.invoke({"question": question})
