from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from core.models import Owner
from .schemas import OwnerCreate, OwnerUpdate


async def create_owner(session: AsyncSession, owner_in: OwnerCreate) -> Owner:
    owner = Owner(**owner_in.model_dump())
    session.add(owner)
    await session.commit()

    return owner

async def get_owners(session: AsyncSession) -> list[Owner]:
    stmt = select(Owner)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()

    return list(users)

async def get_owner_by_id(session: AsyncSession, owner_id: int) -> Owner:
    stmt = select(Owner).where(Owner.id == owner_id)
    result: Result = await session.execute(stmt)
    users = result.scalar()

    return users

async def edit_owner(session: AsyncSession, owner: Owner, owner_update: OwnerUpdate) -> Owner:
    for name, value in owner_update.model_dump().items():
        setattr(owner, name, value)

    await session.commit()
    return owner

async def delete_owner(session: AsyncSession, owner: Owner) -> None:
    await session.delete(owner)
    await session.commit()