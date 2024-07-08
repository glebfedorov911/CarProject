from pydantic import BaseModel, ConfigDict


class OwnerBase(BaseModel):
    name: str
    surname: str
    phone: str

class OwnerCreate(OwnerBase):
    pass

class OwnerUpdate(OwnerCreate):
    pass