from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Car
from . import crud


router = APIRouter(tags=['Car And Owner'], prefix='/car_and_owner')

@router.get('/cars/')
async def get_car_by_owner(owner_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_car_by_owner(session=session, owner_id=owner_id) 