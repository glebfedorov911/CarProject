from pydantic import BaseModel, ConfigDict

from typing import TYPE_CHECKING


class OwnerBase(BaseModel):
    name: str
    surname: str
    phone: str

class OwnerCreate(OwnerBase):
    pass

class OwnerUpdate(OwnerCreate):
    pass