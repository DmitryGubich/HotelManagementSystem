import shutil

from app.hotels.router import get_hotels
from fastapi import APIRouter, Depends, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

image_router = APIRouter(prefix="/images", tags=["Upload image"])
template_router = APIRouter(prefix="/pages", tags=["Templates"])


@image_router.post("/hotels")
async def add_hotel_image(image_id: int, file: UploadFile) -> None:
    with open(f"static/images/{image_id}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)


@template_router.get("/hotels", response_class=HTMLResponse)
async def get_hotels_page(request: Request, hotels=Depends(get_hotels)):
    return templates.TemplateResponse(
        "hotels.html",
        {
            "request": request,
            "hotels": hotels,
        },
    )
