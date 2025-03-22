"""Define response model for the endpoint version."""
from pydantic import BaseModel, Field  # type: ignore


class VersionResponse(BaseModel):
    """Response for version endpoint."""
    version: str = Field(..., example="1.0.0")


class RecognitionResponse(BaseModel):
    """Response for recognition endpoint."""
    prediction: list


class ErrorResponse(BaseModel):
    """Response for incorrect request."""
    message: str
