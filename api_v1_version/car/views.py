from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Car
from .schemas import CarCreate, CarUpdate
from . import crud


router = APIRouter(tags=['Cars'], prefix='/car')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_car(car_in: CarCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_car(session=session, car_in=car_in)

@router.get('/')
async def get_cars(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_cars(session=session)

@router.get('/{car_id}/')
async def get_car(car_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_car_by_id(car_id=car_id, session=session)

@router.put('/edit/{car_id}/')
async def edit_car(car_id: int, car_in: CarUpdate, session: AsyncSession = Depends(db_helper.session_dependency)):
    car = await session.get(Car, car_id)
    return await crud.edit_car(car_in=car_in, car=car, session=session)

@router.delete('/delete/{car_id}/')
async def get_car(car_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    car = await session.get(Car, car_id)
    return await crud.delete_car(car=car, session=session)