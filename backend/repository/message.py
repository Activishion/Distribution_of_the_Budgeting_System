from datetime import datetime, timedelta
from typing import List

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Message
from ..schemas import MessageRead


class MessageRepository:
    def __init__(self, session: AsyncSession, limit: int = 10, skip: int = 0):
        self.__session = session,
        self.limit = limit,
        self.skip = skip

    async def get_all_message_in_year(self) -> List[MessageRead]:
        query = (
            select(Message)
            .where(Message.date > self.sample_per_year(365))
            .order_by(desc(Message.date))
            .limit(self.limit)
            .offset(self.skip)
        )
        result = await self.__session.execute(query)
        return result.scalars().all()
    
    async def get_message_by_id(self, message_id: int) -> MessageRead:
        query = select(Message).where(Message.id == message_id)
        message = await self.__session.execute(query)
        return message.scalar()
    
    async def get_message_by_user(self, username: str) -> List[MessageRead]:
        query = (
            select(Message)
            .where(Message.author == username)
            .limit(self.limit)
            .offset(self.skip)
        )
        result = await self.__session.execute(query)
        return result.scalars().all()

    @staticmethod
    def sample_per_year(days: int = 365):
        return datetime.today() - timedelta(days=days)
