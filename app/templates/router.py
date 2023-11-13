from datetime import datetime, timedelta

from app.hotels.router import get_hotels
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/pages", tags=["Templates"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/hotels", response_class=HTMLResponse)
async def get_hotels_page(request: Request, hotels=Depends(get_hotels)):
    return templates.TemplateResponse(
        "hotels.html",
        {
            "request": request,
            "hotels": hotels,
        },
    )
