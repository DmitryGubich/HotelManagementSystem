from datetime import datetime, timedelta

from app.hotels.service import HotelService
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/pages", tags=["Templates"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/hotels", response_class=HTMLResponse)
async def get_hotels_page(request: Request):
    date_from = datetime.today().date()
    date_to = (datetime.today() + timedelta(days=180)).date()
    return templates.TemplateResponse(
        "hotels.html",
        {
            "request": request,
            "hotels": await HotelService.find_all(),
            "location": "",
            "date_to": date_to,
            "date_from": date_from,
        },
    )
