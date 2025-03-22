"""Endpoints for getting version information."""
from typing import Any
from fastapi import APIRouter, File, UploadFile, Security
from ..schemas.base import VersionResponse, RecognitionResponse, ErrorResponse
from ..version import __version__
from ..models.yolov5 import predict
from .api_key import get_api_key

base_router = APIRouter()


@base_router.get("/version", response_model=VersionResponse)
async def version() -> Any:
    """Provide version information about the web service.

    \f
    Returns:
        VersionResponse: A json response containing the version number.
    """
    return VersionResponse(version=__version__)


@base_router.post('/recognize')
async def recognize(pic: UploadFile = File(...), api_key: str = Security(get_api_key)) -> Any:
    try:
        contents = pic.file.read()
    except Exception:
        return ErrorResponse(message="There was an error uploading the file")
    finally:
        pic.file.close()

    try:
        results = await predict(contents)
    except:
        return ErrorResponse(message="Input file is incorrect")
    else:
        return RecognitionResponse(
            prediction=results.pandas().xyxy[0].to_dict(orient="records")
        )
