from pydantic import BaseModel, ConfigDict


class CarBase(BaseModel):
    model: str
    number: str
    owner_id: int

class CarCreate(CarBase):
    pass

class CarUpdate(CarCreate):
    pass