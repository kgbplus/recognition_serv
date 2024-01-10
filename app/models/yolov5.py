from typing import AnyStr
import torch
from PIL import Image
import io

model = torch.hub.load("ultralytics/yolov5", "yolov5n", trust_repo=True)


async def predict(image_str: AnyStr) -> dict:
    image = Image.open(io.BytesIO(image_str))
    return model(image, size=640)
