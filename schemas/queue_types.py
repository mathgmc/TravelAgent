from pydantic import BaseModel, Field


class QuestionMessage(BaseModel):
    """
    Represents a question message in the queue.
    """
    question: str = Field(
        description="The question to be processed by the LLM."
    )
    user_id: str = Field(
        description="The ID of the user who asked the question."
    )
