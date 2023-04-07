from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import UserCreate, UserRead
from core.database import get_async_session
from repository.user import UserRepository


router = APIRouter()


@router.get("/")
async def get_all_active_users(
        limit: int = 10,
        skip: int = 0,
        session: AsyncSession = Depends(get_async_session)
) -> List[UserRead]:
    async with session.begin():
        async_session = UserRepository(session, limit, skip)
        users: list = await async_session.get_all_active_users()
        if users is None:
            return {
                'status': status.HTTP_404_NOT_FOUND,
                'data': None,
                'description': "Active users is not defined."
            }
        return users
