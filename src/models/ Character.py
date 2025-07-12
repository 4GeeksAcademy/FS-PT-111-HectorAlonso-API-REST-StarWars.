from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database.db import db

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False) 
    planet_origin: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    is_favorite: Mapped[bool] = mapped_column(Boolean())

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "planet": self.planet_origin,
            "is_active": self.is_active,
            "is_favorite": self.is_favorite
            
            # do not serialize the password, its a security breach
        }
