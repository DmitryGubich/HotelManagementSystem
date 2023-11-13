import shutil

from fastapi import APIRouter, UploadFile

router = APIRouter(prefix="/images", tags=["Upload image"])


@router.post("/hotels")
async def add_hotel_image(image_id: int, file: UploadFile) -> None:
    with open(f"static/images/{image_id}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
