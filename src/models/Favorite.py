from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from database.db import db
from .User import User
from .Character import Character
from .Planet import Planet



class Favorite(db.Model):
    User_username: Mapped[str] = mapped_column(ForeignKey("user.username"), nullable= False)
    user: Mapped["User"] = relationship(back_populates="favorite")
    character_favorite: Mapped[str] = mapped_column(ForeignKey("character.name"), nullable=True)
    character: Mapped["Character"] = relationship(back_populates="favorite")
    planet_favorite: Mapped[str] = mapped_column(ForeignKey("planet.name"), nullable=True )
    planet: Mapped["Planet"] = relationship(back_populates="favorite")

    def serialize(self):
        return {
            "User_username": self.User_username,
            "character_favorite": self.character_favorite,
            "planet_favorite": self.planet_favorite
            # do not serialize the password, its a security breach
        }
