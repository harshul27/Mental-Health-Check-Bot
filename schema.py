from pydantic import BaseModel, Field

class MoodResponse(BaseModel):
    """
    Represents a response containing mood information.
    """
    mood_summary: str = Field(..., description="Reflection on the mood of the user, e.g., happy, sad, etc.")
    suggestions: str = Field(..., description="Suggestions for helpful activities based on the user's mood.")
    log_status = str = Field(..., description="Status of the mood log entry")