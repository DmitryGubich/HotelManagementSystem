from app.hotels.models import Hotels
from sqladmin import ModelView


class HotelsAdmin(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.c] + [Hotels.rooms]
    name_plural = "Hotels"
