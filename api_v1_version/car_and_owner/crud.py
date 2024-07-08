from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import Owner, Car

async def get_car_by_owner(session: AsyncSession, owner_id: int) -> list[Car]:
    stmt = select(Car).where(Car.owner_id == owner_id)
    result: Result = await session.execute(stmt)
    cars = result.scalars().all()

    return list(cars)