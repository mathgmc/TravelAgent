from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field


class FindUserInterestsParser(BaseModel):
    """
    Parser for user interests in travel destinations.
    """

    interests: List[str] = Field(
        description="List of travel interests extracted from the user's input."
    )
