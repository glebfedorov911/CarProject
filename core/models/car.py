from .base import Base

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .owner import Owner


class Car(Base):
    model: Mapped[str] = mapped_column(nullable=False)
    number: Mapped[str] = mapped_column(unique=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("owners.id"))
    owner: Mapped["Owner"] = relationship("Owner", back_populates="car")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id} model={self.model})"

    def __repr__(self):
        return str(self)