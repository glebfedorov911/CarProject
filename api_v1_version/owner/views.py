from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Owner
from .schemas import OwnerCreate, OwnerUpdate
from . import crud

router = APIRouter(tags=['Owners'], prefix='/owner')

@router.post('/create_owner/', status_code=status.HTTP_201_CREATED)
async def create_owner(owner_in: OwnerCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_owner(session=session, owner_in=owner_in)

@router.get('/')
async def get_owners(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_owners(session=session)

@router.get('/{owner_id}/')
async def get_owner(owner_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_owner_by_id(session=session, owner_id=owner_id)

@router.put('/edit/{owner_id}/')
async def get_owner(update_owner: OwnerUpdate, owner_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    owner = await session.get(Owner, owner_id)
    return await crud.edit_owner(
        session=session,
        owner=owner,
        owner_update=update_owner
    )

@router.delete('/delete/{owner_id}/')
async def get_owner(owner_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    owner = await session.get(Owner, owner_id)
    return await crud.delete_owner(session=session, owner=owner)
