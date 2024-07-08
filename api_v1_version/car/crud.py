from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import Car
from .schemas import CarBase, CarCreate, CarUpdate

async def create_car(car_in: CarCreate, session: AsyncSession) -> Car:
    car = Car(**car_in.model_dump())
    session.add(car)
    await session.commit()

    return car

async def get_cars(session: AsyncSession) -> list[Car]:
    stmt = select(Car)
    result: Result = await session.execute(stmt)
    car = result.scalars().all()

    return list(car)

async def get_car_by_id(car_id: int, session: AsyncSession) -> Car:
    stmt = select(Car).where(Car.id == car_id)
    result: Result = await session.execute(stmt)
    car = result.scalar()

    return car

async def edit_car(car_in: CarUpdate, car: Car, session: AsyncSession) -> Car:
    for name, value in car_in.model_dump().items():
        setattr(car, name, value)

    await session.commit()
    return car

async def delete_car(car: Car, session: AsyncSession) -> None:
    await session.delete(car)
    await session.commit()