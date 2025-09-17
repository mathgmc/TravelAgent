from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field


class FindUserInterestsParser(BaseModel):
    """
    Parser for user interests in travel destinations.
    """

    interests: List[Optional[str]] = Field(
        description="List of travel interests extracted from the user's input."
    )


class RequiredTripDetailsParser(BaseModel):
    """Parser for required trip planning fields present in the latest user message."""

    address: Optional[str] = Field(
        default=None,
        description="City, region, or address the user will depart from.",
    )
    trip_maximum_cost_usd: Optional[float] = Field(
        default=None,
        description="Maximum budget the user wants to spend in USD.",
    )
    amount_of_days: Optional[int] = Field(
        default=None,
        description="How many days the user plans to travel.",
    )
