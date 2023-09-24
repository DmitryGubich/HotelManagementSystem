from app.database import Base
from sqlalchemy import JSON, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[dict] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    def __str__(self):
        return f"Hotel {self.name} ({self.id})"
