from typing import List

from sqlalchemy import select, insert, update, and_
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User
from schemas.user import UserCreate, UserRead


class UserRepository:
    def __init__(self, session: AsyncSession, limit: int = 10, skip: int = 0):
        self.__session = session,
        self.limit = limit,
        self.skip = skip

    async def create_user(self, new_user: UserCreate, user: UserRead) -> User:
        user = self.get_user_by_email(UserCreate.email)
        # сделать проверку, что если такой есть, то вернуть ошибку
        stmt = insert(User).values(**new_user.dict(), user_id=user.id)
        await self.__session.execute(stmt)
        await self.__session.commit()
        return {**user.dict()}

    async def get_all_users(self) -> List[User]:
        query = select(User).limit(self.limit).offset(self.skip)
        result = await self.__session.execute(query)
        return result.scalars().all()
    
    async def get_all_active_users(self) -> List[User]:
        query = (
            select(User)
            .where(User.is_active_subscription == True)
            .limit(self.limit)
            .offset(self.skip)
        )
        result = await self.__session.execute(query)
        return result.scalars().all()
    
    async def get_user_by_email(self, email: str) -> User:
        query = select(User).where(User.email == email)
        result = await self.__session.execute(query)
        return result.scalars()
    
    async def delete_user(self, user_id: int) -> User:
        statement = (
            update(User)
            .where(and_(User.id == user_id, User.is_active_subscription == True))
            .values(is_active_subscription = False)
            .returning(User.id)
        )
        result = await self.__session.execute(statement)
        return result
