from typing import Any, Dict, List

from models.agent_state import AgentState
from tools.extract_required_trip_details import extract_required_trip_details


REQUIRED_FIELDS = (
    "address",
    "trip_maximum_cost_usd",
    "amount_of_days",
    "travel_interests",
)


def check_required_fields(agent_state: AgentState):
    """Capture the list of required fields that are still missing."""
    message = agent_state.get("question", "")
    extracted_details = _extract_details(message)

    updates: Dict[str, Any] = {}

    for field in REQUIRED_FIELDS:
        current_value = agent_state.get(field)
        extracted_value = extracted_details.get(field)

        if _value_is_missing(current_value) and not _value_is_missing(extracted_value):
            updates[field] = extracted_value

    missing_fields: List[str] = []
    for field in REQUIRED_FIELDS:
        candidate_value = updates.get(field, agent_state.get(field))
        if _value_is_missing(candidate_value):
            missing_fields.append(field)

    updates["missing_fields"] = missing_fields
    return updates


def _value_is_missing(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False


def _extract_details(message: str) -> Dict[str, Any]:
    if not message:
        return {}

    parsed = extract_required_trip_details(message)
    return parsed.model_dump(exclude_none=True)
