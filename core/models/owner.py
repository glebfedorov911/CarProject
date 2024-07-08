from .base import Base

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .car import Car

class Owner(Base):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(100), nullable=False) 
    phone: Mapped[str] = mapped_column(unique=True)
    car: Mapped[list["Car"]] = relationship("Car", back_populates="owner")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id} name={self.name})"

    def __repr__(self):
        return str(self)