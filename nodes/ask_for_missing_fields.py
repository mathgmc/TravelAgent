from models.agent_state import AgentState


def ask_for_missing_fields(agent_state: AgentState):
    """Ask the user for any required fields that are still missing."""
    missing_fields = agent_state.get("missing_fields", [])

    if not missing_fields:
        question = "Could you share any other trip details so I can help further?"
    else:
        readable_fields = [_field_to_prompt(field) for field in missing_fields]

        if len(readable_fields) == 1:
            question = (
                f"Could you share {readable_fields[0]} so I can tailor your travel ideas?"
            )
        else:
            joined_fields = ", ".join(readable_fields[:-1])
            question = (
                "Could you share "
                f"{joined_fields} and {readable_fields[-1]} so I can tailor your travel ideas?"
            )

    return {"answer": question}


def _field_to_prompt(field_name: str) -> str:
    prompts = {
        "address": "the city or address you will be travelling from",
        "trip_maximum_cost_usd": "your maximum budget in USD",
        "amount_of_days": "how many days you plan to travel",
    }

    return prompts.get(field_name, field_name.replace("_", " "))
